# png2n64

## description
simple python script to convert a png file (32 or 24 bits) to a 16 RGBA file usable (for example) in a n64 project.
a converted file with .551 extension will be created in the same folder

## usage
./png2n64.py _\<file to convert>_ _\<split option>_ _\<transparency threshold>_

**file to convert:** 
Absolute or relative path to the png file to convert

**split option:** 
Optional.

possible values are 32x32, 32x64 and 64x32. If enabled, it will split the output file in as many as needed in order to get parts of the choosen width and height.
If you don't want to split the file, leave empty of set to 0x0

**transparency threshold:**
Optional.

Value (integer) of the 32 bits png transparency value below which the pixel will be converted to a fully transparent one. Default value is 1 (while for PNG 32 bits it goes from 0 to 255)
In 16 RGBA, Red Green Blue and Transparent values are coded respectively with 5 bits, 5 bits, 5 bits and 1 one. Only one bit for transparent means it can only be not transparent at all of fully transparent. 

