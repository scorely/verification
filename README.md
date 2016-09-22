# verification

This code is all of the components of how we plan on doing verification. 
There are two main checks we want in our verification process.

1. Is the PLAID linkage a 'Business Account' if YES == OK, if NO ==FAIL
Reference here: https://plaid.com/docs/api/#connect

"meta": {
      "name": "Plaid Credit Card",
      "number": "3002"
    },
    "type": "depository",
    "subtype": "checking"
  }
  
We will be looking for "Business" in the "Name" or the "Type"

2. We want to run a fuzzy matching between our data and the plaid response.

A simple logic such as matches between Owner Name, Business Name, Address, and Phone Number should be PASS.

#In This Repo You Will Find:

Sample of the Plaid Response JSON
Sample of our Data
Modules for Owner Name, Business Name, Address, and Phone Number
Dictionaries to Use for Preprocessing
