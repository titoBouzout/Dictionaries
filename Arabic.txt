#AyaSpell Arabic Dictionary for Spellchecking 
AyaSpell Arabic Dictionary for Hunspell Spellchecker

[![downloads]( https://img.shields.io/sourceforge/dt/ayaspell.svg)](http://sourceforge.org/projects/ayaspell)
[![downloads]( https://img.shields.io/sourceforge/dm/ayaspell.svg)](http://sourceforge.org/projects/ayaspell)
  
  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com
  Collect data manually Mohamed Kebdani, Morroco < med.kebdani gmail.com>
  
Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/linuxscout/ayaspell/master/AUTHORS.md)
Release  | 3.7
License  |[GPL](https://github.com/linuxscout/ayaspell/master/LICENSE)
Tracker  |[linuxscout/ayaspell/Issues](https://github.com/linuxscout/ayaspell/issues)
Website  |[http://ayaspell.sourceforge.net](http://ayaspell.sourceforge.net)
Source  |[Github](http://github.com/linuxscout/ayaspell)
Download  |[sourceforge](http://ayaspell.sourceforge.net)
Feedbacks  |[Comments](https://github.com/linuxscout/ayaspell/)
Accounts  |[@Twitter](https://twitter.com/linuxscout)  [@Sourceforge](http://sourceforge.net/projects/ayaspell/)

#Description
Ayaspell project aims to provide Arabic dictionaries for free office applications like OpenOffice.org, Firefox, Thunderbird, abiword, gedit ...etc. This project is under GPL/LGPL/MPL tri-license. For the lexicon part of Ayaspell project, we are working to provide:

- An Arabic spellchecker dictionary: hunspell-ar (doc:arabic/pdf). The hunspell-ar dictionary is based on Hunspell the spellchecker's OpenOffice.org project ;
- An Arabic thesaurus dictionary: thesaurus-ar , based on MyThes, (from OpenOffice.org project) ; on web (using sinonimi )
- An Arabic morphological lexicon: grammar-ar , for the grammar-checker ;
- A Light Arabic spellchecker dictionary for embedded systems , like PDA, mobile phone, etc.



##Thanks for their encouragement and support.

- [King Abdulaziz City For Science And Technology](http://www.kacst.edu.sa/eng/index.php") (Saudi Arabia)
- [Cheikh Ali Jabir Al-ali Assalim Assabah](http://raihur.com/?page_id=2) (Kuwait)
- [Osmium Work](http://www.osmium-work.com) (Morocco)
- [ArabTechies](http://www.arabtechies.net) Team
- [ArabEyes](http://www.arabeyes.org) Team


## وثائق ومقالات

### وثائق

*   تقديم الإصدار الأول من القاموس العربي للتدقيق الإملائي [hunspell-ar](doc/hunspell-ar.pdf) (توثيق عربية/pdf)

### مقالات

*   طه زروقي، محمد كبداني،[ **"مشروع أية –سبل، القاموس العربي للتدقيق الإملائي مفتوح المصدر،تجربة وآفاق".** ](doc/ayaspell_alecso_damascus2009.pdf)اجتماع الخبراء، مشروع المعجم العربي التفاعلي، المنظمة العربية للتربية والثقافة والعلوم ، دمشق 26-28 مايو 2009
*   Taha Zerrouki*،, Amar Balla, [**"Implementation of infixes and circumfixes in the spellcheckers"**](doc/infixes_medar_2009.pdf), 2nd International Conference on Arabic Language Resources and Tools, Cairo (Egypt), 22 - 23 April 2009.
*   طه زروقي، [**" المــــدقق الإمـلائي العـربي الحـر، لمشروع آيسبل"،**](doc/ayaspell_tlemcen2008.pdf) الندوة الدولية حول الأداة المعلوماتية في خدمة اللغة العربية في مواجهة تحديات العولمة، جامعة أبوبكر بلقايد، تلمسان، الجزائر 15-16 نوفمبر 2008.
*   طه زروقي، [**"الجوانب البرمجية لدعم اللغة العربية في المدقّق الإملائي مفتوح المصدر هانسبال"،** ](doc/jetic-bechar2007.pdf)الأيام الدراسية حول المعالجة الآلية للغة العربية، المركز الجامعي بشار، ماي 2007.
*   طه زروقي، [**"أهمية المصادر المفتوحة في المعالجة الآلية للغة العربية"،** ](doc/crstdla-2007.pdf)يوم دراسي حول المعالجة الآلية للغة العربية، مركز البحوث العلمية والتقنية لترقية اللغة العربية، الجزائر، جوان 2007.
*   طه زروقي،[ **"الزوائد المتوسّطة والمزدوجة في المدققات الآلية مفتوحة المصدر"،** ](doc/Aspell-barmadjiat2007.pdf)ندوة "البرمجيات الحرة التطبيقية باللغة العربية: خطوات نحو الإدارة الإلكترونية"، المجلس الأعلى للغة العربية، الجزائر، 9-10 ديسمبر 2007.

### مذكرة ماجستير

*   اسماعيل حجير، "[ من أجل مدقق إملائي عربي مفتوح المصدر](doc/Ismail_hadjir_these.pdf)"، مركز البحث العلمي وترقية اللغة العربية، الجزائر 2009، [ihadjir@](http://yahoo.fr/)

##BUILD Dictionary in multiple format

The source files are data folder as text files in Hunspell format, then we can build dictionary in format as OpenOffice/LibreOffice and Mozilla Firefox/Thunderbird
```
make
```
To build a specific format you can 
* zip:
```
make zip
```
* LibreOffice/OpenOffice:
```
make libreoffice
```
* Mozilla Firefox/Thunderbird:
```
make mozilla
```

The resulted files can be found in releases folder.

To modify the version, you can update $VERSION variable in Makefile file.

To clean  releases use:
```
make clean
```

