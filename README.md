FBReader (Android) OPDS plugin prototype
============

This code represents a prototype of a simple OPDS plugin that implements 2 actions:
* adds new OPDS catalog to the [FBReader](http://fbreader.org/FBReaderJ/) network library
* creates new launcher item that opens your catalog for browsing

License
------------
This code is in public domain

How to start
------------
1. Clone this code to your computer
2. Run script `generate_project.py` script to create your project tree

  Script **required** parameters:
  *  `-d DIR      ` directory where to create the project
  *  `-p PACKAGE  ` java package prefix, e.g.: com.mycatalog
  *  `-n NAME     ` name for android launcher, e.g.: My Catalog
  *  `-u URL      ` OPDS catalog URL, e.g.: http://mycatalog.com/opds.xml

  Script **optional** parameter:
  *  `-i ICON     ` PNG icon file for android launcher

3. Create build.xml file for your project using `android update project` command, then build it using `ant release`
*OR* use your preferred IDE to build the project
4. The plugin is now ready. Enjoy!
