rom __future__ import print_function
from future.builtins import next

import os
import csv
import re
import collections
import logging
import optparse
import numpy

import dedupe
from unidecode import unidecode

optp = optparse.OptionParser()
optp.add_option('-v', '--verbose', dest='verbose', action='count',
                help='Increase verbosity (specify multiple times for more)'
                )
(opts, args) = optp.parse_args()
log_level = logging.WARNING 
if opts.verbose :
    if opts.verbose == 1:
        log_level = logging.INFO
    elif opts.verbose >= 2:
        log_level = logging.DEBUG
logging.getLogger().setLevel(log_level)

output_file = 'data_matching_output.csv'
settings_file = 'data_matching_learned_settings'
training_file = 'data_matching_training.json'

def preProcess(column):
    column = unidecode(column)
    column = re.sub('\n', ' ', column)
    column = re.sub('-', '', column)
    column = re.sub('/', ' ', column)
    column = re.sub("'", '', column)
    column = re.sub(",", '', column)
    column = re.sub(":", ' ', column)
    column = re.sub('  +', ' ', column)
    column = column.strip().strip('"').strip("'").lower().strip()
    if not column :
        column = None
    return column
    
def readData(filename):
    data_d = {}

    with open(filename) as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            clean_row = dict([(k, preProcess(v)) for (k, v) in row.items()])
            if clean_row['price'] :
                clean_row['price'] = float(clean_row['price'][1:])
            data_d[filename + str(i)] = dict(clean_row)

    return data_d

    
print('importing data ...')
data_1 = readData('AbtBuy_Abt.csv')
data_2 = readData('AbtBuy_Buy.csv')
#
def descriptions() :
    for dataset in (data_1, data_2) :
        for record in dataset.values() :
            yield record['description']
            
if os.path.exists(settings_file):
    print('reading from', settings_file)
    with open(settings_file, 'rb') as sf :
        linker = dedupe.StaticRecordLink(sf)

else:
    
fields = [
        {'field' : 'title', 'type': 'String'},
        {'field' : 'title', 'type': 'Text', 'corpus' : descriptions()},
        {'field' : 'description', 'type': 'Text',
         'has missing' : True, 'corpus' : descriptions()},
        {'field' : 'price', 'type' : 'Price', 'has missing' : True}]
        
linker = dedupe.RecordLink(fields)

    linker.sample(data_1, data_2, 15000)

    if os.path.exists(training_file):
        print('reading labeled examples from ', training_file)
        with open(training_file) as tf :
            linker.readTraining(tf)


Dedupe will find the next pair of records it is least certain about and ask you to label them as matches or not. use 'y', 'n' and 'u' keys to flag duplicates press 'f' when you are finished

    print('starting active labeling...')

    dedupe.consoleLabel(linker)

    linker.train()

    with open(training_file, 'w') as tf :
        linker.writeTraining(tf)
   with open(settings_file, 'wb') as sf :
        linker.writeSettings(sf)

print('clustering...')
linked_records = linker.match(data_1, data_2, 0)

print('# duplicate sets', len(linked_records))

cluster_membership = {}
cluster_id = None
for cluster_id, (cluster, score) in enumerate(linked_records):
    for record_id in cluster:
        cluster_membership[record_id] = (cluster_id, score)

if cluster_id :
    unique_id = cluster_id + 1
else :
    unique_id =0
    

with open(output_file, 'w') as f:
    writer = csv.writer(f)
    
    header_unwritten = True

    for fileno, filename in enumerate(('AbtBuy_Abt.csv', 'AbtBuy_Buy.csv')) :
        with open(filename) as f_input :
            reader = csv.reader(f_input)

            if header_unwritten :
                heading_row = next(reader)
                heading_row.insert(0, 'source file')
                heading_row.insert(0, 'Link Score')
                heading_row.insert(0, 'Cluster ID')
                writer.writerow(heading_row)
                header_unwritten = False
            else :
                next(reader)

            for row_id, row in enumerate(reader):
                cluster_details = cluster_membership.get(filename + str(row_id))
                if cluster_details is None :
                    cluster_id = unique_id
                    unique_id += 1
                    score = None
                else :
                    cluster_id, score = cluster_details
                row.insert(0, fileno)
                row.insert(0, score)
                row.insert(0, cluster_id)
                writer.writerow(row)