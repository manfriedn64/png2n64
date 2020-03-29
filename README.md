# png2n64
simple python script to convert a png file (32 or 24 bits) to a 16 RGBA file usable (for example) in a n64 project.
a converted file with .551 extension will be created in the same folder

usage:
./png2n64.py <file_to_convert> <split_option*>

split_option: optional, possible values are 32x32, 32x64 and 64x32. If enabled, it will split the output file in as many as needed in order to get parts of the choosen width and height
