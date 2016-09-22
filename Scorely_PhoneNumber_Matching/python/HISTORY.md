
What's new in 7.7.0
-------------------

Merge to
[upstream commit 1ec4d341c3cd](https://github.com/googlei18n/libphonenumber/commit/1ec4d341c3cd);
no code changes that affect the Python version so this is just a version bump to
stay in sync with upstream.


What's new in 7.6.1
-------------------

Merge to [upstream commit 7cc500f588db](https://github.com/googlei18n/libphonenumber/commit/7cc500f588db); code changes:

 - `phonemetadata.py` has two more fields to represent possible lengths of phone
   numbers. Changed `buildmetadatafromxml.py` to alter the way
   that metadata about possible-lengths information is consumed when constructing
   metadata to populate these.
   [Discussion list email](https://groups.google.com/forum/#!topic/libphonenumber-discuss/75TOpTFVi08)


What's new in 7.6.0
-------------------

Merge to [upstream commit ddf60b1c175e](https://github.com/googlei18n/libphonenumber/commit/ddf60b1c175e); code changes:

 - Made `is_number_geographical()` public and added `is_number_type_geographical()`,
   and changed the geocoder to use this when checking whether to give a detailed
   answer or country-level only.


What's new in 7.5.0
-------------------

Merge to [upstream commit 3f83454ed62b](https://github.com/googlei18n/libphonenumber/commit/3f83454ed62b); no code changes that affect the Python
version so this is just a version bump to stay in sync with upstream.


What's new in 7.4.0
-------------------

Merge to [upstream commit 598b9a4f89d6](https://github.com/googlei18n/libphonenumber/commit/598b9a4f89d6); no code changes that affect the Python
version so this is just a version bump to stay in sync with upstream.


What's new in 7.3.0
-------------------

Merge to [upstream commit d933631fbf15](https://github.com/googlei18n/libphonenumber/commit/d933631fbf15); code changes:

 - Added support for `region_code of None in example_number_for_type()`
 - Added `invalid_example_number()`
 - Improvements to docstring for parse method
 - Update `is_number_geographical` to return true for geographical mobile numbers.


What's new in 7.2.0
-------------------

Merge to [upstream commit ab5e61acc087ec9f5](https://github.com/googlei18n/libphonenumber/commit/ab5e61acc087ec9f5), which is 7.2.1 (7.2.0 had an immediate
problem on release); upstream changelog mentions no code changes, but the Java
implementation includes a change to use nano protobufs.


What's new in 7.1.0
-------------------

Merge to [upstream commit 903ac5de5b6e1112](https://github.com/googlei18n/libphonenumber/commit/903ac5de5b6e1112); upstream code changelog:

 - Only upstream code change doesn't affect python version
   (New `MetadataSource` implementation that reads from a single metadata file with
   all regions' phone number metadata.)


What's new in 7.0.0
-------------------

Merge to upstream Subversion revision 715; upstream code changelog:

 - New APIs for ShortNumberInfo. The old APIs have been deprecated and will be
   removed in an upcoming release.


What's new in 6.3.0
-------------------

Merge to upstream Subversion revision 703; upstream code changelog:

 - Changing the offline geocoder to not return any country at all if the number
   could belong to multiple countries
 - Removing obsolete code that treated countries with no metadata as valid.


What's new in 6.2.0
-------------------

Merge to upstream Subversion revision 674; upstream code changelog:

 - Better exclusion of dates when matching phone numbers from text.
 - Handle phone input in RFC3966 with missing tel: prefix


What's new in 6.1.0
-------------------

Merge to upstream Subversion revision 656; upstream code changelog:

 - Adding MetadataLoader support to allow custom metadata loading from
   alternative sources (should have no visible impact to users).
 - Fixing bug where digits could be lost in as-you-type formatting and
   formatting patterns incorrectly applied.


What's new in 6.0.0a
--------------------

Split geographic metadata into chunks.
Generate separate `phonenumbers-lite` package.
(No upstream changes.)


What's new in 6.0.0
-------------------

Removed beta status.
Merge up to upstream Subversion revision 650; upstream code changelog:

 - Better support for detecting phone numbers in text that are beside each
   other
 - Change to how Japanese numbers beginning with "00" are modelled, with the
   side-effect that the maximum possible number length has been extended by
   1.
 - Handle `StringIndexOutOfBoundsException` in the `AsYouTypeFormatter` when the
   national prefix that was extracted was not found in the prefix. This
   affected countries with very long carrier codes, such as Korea.
 - Removal of some of the author attributions - contributions to be tracked
   in CONTRIBUTORS file.


What's new in 5.9b1
-------------------

The codebase now supports Python 2.5-2.7 and Python 3.x out of the box, without
needing 2to3 conversion.

The top-level module no longer exports the following functions:

 - `country_name_for_number`
 - `description_for_number`
 - `description_for_valid_number`

These functions now need to be imported via the `phonenumbers.geocoder` submodule.

The short number functions have been renamed:

 - `is_possible_short_number_object` becomes `is_possible_short_number`
 - `is_possible_short_number` becomes `is_possible_short_number_for_object`
 - `is_valid_short_number_object` becomes `is_valid_short_number`
 - `is_valid_short_number` becomes `is_valid_short_number_for_object`
 - `expected_cost` becomes `expected_cost_for_region`, and there's a new `expected_cost`
   function that takes a `PhoneNumber` object.

Merge up to upstream Subversion revision 622; upstream code changelog:

  - Adding support for numbers with multiple Italian leading zeros, by
    adding a field to the phone number proto to allow an arbitrary number of
    leading zeros, and supporting this when parsing, validating and
    formatting.
  - Adding more functionality to `ShortNumberInfo` -> such as
    `GetExpectedCostForRegion`.
  - Fix for parsing short numbers that start with the national prefix.
  - Updating `FormatNumberForMobileDialing` to work with short numbers.
  - Stop finding Israeli 4-digit "star" numbers in text when no star is in
    fact present.
  - Bug fix for finding phone numbers where the area code was also part of
    the country calling code.


What's new in 5.8b1
-------------------

Rename `shortnumberutil.py` to `shortnumberinfo.py`.
Merge up to upstream Subversion revision 603; upstream code changelog:

 - Renamed `ShortNumberUtil` to `ShortNumberInfo` -> the former class is now
   deprecated and will be deleted in a later release. At the moment it just
   delegates to `ShortNumberInfo`.
 - New methods in the `ShortNumberInfo` API - `isCarrierSpecific`, singleton interface,
   `isPossibleShortNumber`, `isValidShortNumber`, `getShortNumberCost`. Note this
   is an experimental API at the moment and subject to change.
 - Bug fixes:
    - AsYouTypeFormatting: 3-digit numbers can be formatted as a group
      where appropriate
    - AsYouTypeFormatting: Countries with an optional national prefix were
      considered before to have always entered it, resulting in bugs where
      numbers without the national prefix were not properly formatted.
    - Numbers in Chile that overlap with emergency numbers are no longer
      marked as connecting to them
    - Not requiring the NDC to be alone for countries where there is no
      national prefix in strict grouping when extracting phone numbers


What's new in 5.7b2
-------------------

Fix `setup.py` to include new `.shortdata` sub-package.


What's new in 5.7b1
-------------------

Merge up to upstream Subversion revision 594; upstream code changelog:

  - Improve phone number extraction recall.
  - Add support for loading short number metadata.


What's new in 5.6b1
-------------------

Merge up to upstream Subversion revision 579; upstream code changelog:

 - Fix for as-you-type-formatting bug affecting countries with no national prefix
   formatting rule, such as China.


What's new in 5.5b1
-------------------

Merge up to upstream Subversion revision 574; upstream code changelog:

 - Changed internal initialization code and made more fields final.
   Note that we now throw an exception if an attempt is made to set the
   metadata more than once (which should only happen during testing).
 - Fix problem with `formatNumberForMobileDialing` for HU and CL.


What's new in 5.4b1
-------------------

Load metadata on demand rather than all at start of day.
Merge up to upstream Subversion revision 557; upstream code changelog:

 - Switch `formatNumberForMobileDialing` to prefer national format to international format when the
   number is dialed from the same region the phone number is from.


What's new in 5.3b1
-------------------

Merge up to upstream Subversion revision 550; upstream code changelog:

 - Handling UAN numbers in Argentina better when dialling them locally from a
   mobile


What's new in 5.2b1
-------------------

Merge up to upstream Subversion revision 532.


What's new in 5.1b1
-------------------

Merge up to upstream Subversion revision 516.


What's new in 5.0b2
-------------------

Merge up to upstream Subversion revision 500.
The upstream metadata at r489 didn't match the
generated Java code in 5.0; this upstream revision
fixed the mismatch.


What's new in 5.0b1
-------------------

Merge up to upstream Subversion revision 492.


What's new in 4.9b1
-------------------

Merge up to upstream Subversion revision 469.


What's new in 4.8b1
-------------------

Merge up to upstream Subversion revision 441.


What's new in 4.7b1
-------------------

Merge up to upstream Subversion revision 431.


What's new in 4.6b1
-------------------

Merge up to upstream Subversion revision 426.
Reinstated Python 2.5 support, accidentally broken since 4.3.


What's new in 4.5b1
-------------------

Merge up to upstream Subversion revision 419.


What's new in 4.4b1
-------------------

Merge up to upstream Subversion revision 411.


What's new in 4.3b1
-------------------

Merge up to upstream Subversion revision 396.
Adjust codebase to allow 2to3 generation of Python 3.x version.


What's new in 4.2b1
-------------------

Merge up to upstream Subversion revision 383.


What's new in 4.1b1
-------------------

Merge up to upstream Subversion revision 374.


What's new in 4.0b1
-------------------

Merge up to upstream Subversion revision 362.


What's new in 3.9b1
-------------------

Merge up to upstream Subversion revision 353.


What's new in 3.8b1
-------------------

Merge up to upstream Subversion revision 325.
Includes initial simplistic implementation of geocoding functionality.


What's new in 3.7b1
-------------------

Merge up to upstream Subversion revision 289 (but
geocoding functionality not yet ported).


What's new in 3.6b1
-------------------

Merge up to upstream Subversion revision 277 (but
geocoding functionality not yet ported).
Require Python 2.5, to allow import unicodedata.


What's new in 3.5b2
-------------------

Fix GH-3: crash in `parse()` for number with blank metadata


What's new in 3.5b1
-------------------

Merge up to upstream Subversion revision 213.


What's new in 3.4b1
-------------------

Merge up to upstream Subversion revision 205.
Changed version marker from a to b.
More unit test coverage


What's new in 3.3a1
-------------------

Merge up to upstream Subversion revision 190.


What's new in 3.2a1
-------------------

Merge up to upstream version 3.3, Subversion revision 171.


What's new in 3.1a1
-------------------

Initial port of libphonenumber, from http://code.google.com/p/libphonenumber/

This version based on upstream version 3.2, Subversion revision 166 of:
http://libphonenumber.googlecode.com/svn/trunk/java
