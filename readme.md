# Dictionaries for Sublime Text

The following repository contains some UTF8-ready dictionaries for the spell checker feature of Sublime Text.

Most of them were downloaded from the [Open Office list](http://extensions.services.openoffice.org/en/dictionaries). Credits to the people working on these! Read every LANG.txt for details.

## Language List

 * Armenian (Eastern)
 * Armenian (Western)
 * Català -- Catalan
 * Dansk -- Danish
 * Deutsch (AT) -- German
 * Deutsch (CH) -- German
 * Deutsch (DE) -- German
 * Deutsch -- German
 * Eesti -- Estonian
 * English (American)
 * English (Australian)
 * English (British)
 * English (Canadian)
 * English (South African)
 * Español -- Spanish
 * Euskara -- Basque
 * Français -- French (There is a special package for this language you may want to check [here](https://github.com/superbob/SublimeTextLanguageFrench))
 * Galego -- Galician
 * Hrvatski -- Croatian
 * Italiano -- Italian
 * Lietuvių -- Lithuanian
 * Lëtzebuergesch -- Luxembourgish
 * Magyar -- Hungarian
 * Nederlands -- Dutch
 * Norsk (Bokmål) -- Norwegian
 * Norsk (Nynorsk) -- Norwegian
 * Polski -- Polish
 * Português (Brasileiro) -- Portuguese (Brazilian)
 * Português (Europeu - Antes do Acordo Ortográfico de 1990) -- Portuguese (European - Before the Ortographic Agreement of 1990)
 * Português (Europeu) -- Portuguese (European)
 * Română -- Romanian
 * Slovensky -- Slovenian
 * Slovenčina -- Slovak
 * Srpski (Latinica) -- Serbian (Latin)
 * Srpski (Ćirilica) -- Serbian (Cyrillic)
 * Svenska -- Swedish
 * Tiếng Việt -- Vietnamese
 * Türkçe -- Turkish
 * Čeština -- Czech
 * Ελληνικά -- Greek
 * български -- Bulgarian
 * Монгол -- Mongolian
 * Русский -- Russian
 * Українська -- Ukrainian

## Idea

Since installing a new language requires some non easy procedures. The idea is to collect here the dictionaries ready for use.

Today this contains a list of some languages, the idea is to extends the list with help from the community.

## Adding a new language

My primary language is Spanish, then I'm not sure of the state and quality of the different languages added here.

Please if you found a better dictionary or something to improve, your change will be welcome.

To add a new language:

 * Download the language file from [here](http://extensions.services.openoffice.org/en/dictionaries).
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
 * Update the [language list](#language-list) above in this file,
   add yourself to the [credits](#contributors) section (keep alphabetical
   order!)
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

 * @SteveClement
 * Adam Retter
 * Adam St. John
 * Aitor Carlos Urrutia Aranburu
 * Aksel Meola
 * Alexandr Zhevedenko
 * Andrej Kvasnica
 * Chris---
 * Domingues
 * Florian Morgan
 * gw0
 * Haoliang Yu
 * Hayk Karapetyan
 * Jack Cuthbert
 * Jacob Bundgaard
 * Jonas Follesø
 * Kalman Kemenczy
 * Lyubomir Vezev
 * Maksim Norkin
 * Marcos Chavarría Teijeiro
 * Max @ulidtko
 * Mehmet Ali Gozaydin @kubudik
 * Mladen Mihajlović @mika76
 * MrTux
 * Nick Wilde
 * Pedro Chambino
 * Petr Dvořák
 * Roland Richter
 * Thomas Feldmann
 * Valery Kocubinsky
 * Zeljko Babic


## Installation

Download or clone the contents of this repository to a folder named exactly as the package name into the Packages/ folder of ST.


## Docs

Sublime Text uses Hunspell for its [spell checking support](http://www.sublimetext.com/docs/3/spell_checking.html).
