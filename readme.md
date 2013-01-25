# Dictionaries for Sublime Text 2

The following repository contains some dictionaries for the sepll checker feature of Sublime Text.

Each language was downloaded from the Open Office list. Credits to the people working on that languages! Read every LANG.txt for details.

	http://extensions.services.openoffice.org/en/dictionaries

## Language List

 * Català
 * Dansk
 * Deutsch
 * Deutsch (AT)
 * Deutsch (CH)
 * Deutsch (DE)
 * Czech
 * Ελληνικά
 * English (Canadian)
 * Español
 * Français
 * Italiano
 * Lietuvių
 * Magyar
 * Nederlands
 * Norwegian (Bokmål)
 * Norwegian (Nynorsk)
 * Română
 * Polski
 * Português (do Brasil)
 * Português (Europeu)
 * Русский
 * Slovensky
 * Svenska
 * Tiếng Việt

## Idea

Since installing a new language requires some non easy procedures. The idea is to collect here the dictionaries ready for use.

Today this contains a list of some languages, the idea is to extends the list with help from the community.

## Adding a new language

My primary language is Spanish, then I'm not sure of the state and quality of the different languages added here.

Please if you found a better dictionary or something to improve, your change will be welcome.

To add a new language:

 * Download the language file from link above.
 * Rename the "some.oxt" file to "some.zip"
 * Unzip the file
 * Look for three files: "lang.aff", "lang.dic" and "readme_lang.txt"(or something similar)
 * Open the "lang.aff" to check the encoding used. Such the line: "SET ISO-8859-1"
 * Convert that file to UTF-8 from the used encoding
 * Convert "lang.dic" to UTF-8 from the used encoding.
 * Convert "readme_lang.txt" to UTF-8 from the used encoding.
 * Change "SET ISO-8859-1" to "SET UTF-8"
 * Copy "readme_lang.txt" to "lang.txt"
 * Copy these three files to this repository
 * Open a pull request to help improve this package! Thank you.

## Iconv and Encodings

[Iconv](http://en.wikipedia.org/wiki/Iconv) may be used to convert a file to UTF-8 from another encoding. For example:

    iconv -f iso-8859-1 -t utf-8 en_CA.aff > en_CA_utf8.aff

You can use the file command to check an encoding:

    file -bi en_CA_utf8.aff

Example output:

    text/plain; charset=utf-8

Note that `us-ascii` might be reported if there are no unicode (utf-8) characters present in the file.


## Contributors

	* Adam St. John
	* Andrej Kvasnica
	* Jonas Follesø
	* Kalman Kemenczy
	* MrTux
	* Petr Dvořák
	* Roland Richter
	* Thomas Feldmann
	* Valery Kocubinsky
	* Maksim Norkin
	* Alexandr Zhevedenko

## Docs

Sublime Text uses Hunspell for its spell checking support.

http://www.sublimetext.com/docs/2/spell_checking.html
