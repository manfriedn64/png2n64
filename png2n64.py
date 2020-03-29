#!/usr/bin/python3

import sys, math, os
import numpy as np
from PIL import Image

def cvt5_round(val):
#	return int(val) / 8
	return max(0, min(31, round(val / 8)))

def getRGBA16(RGBA):
	transparency = 1
	if len(RGBA) > 3:
		if RGBA[3] < 1:
			transparency = 0
	out_rgb = (
		cvt5_round(float(RGBA[0])),
		cvt5_round(float(RGBA[1])),
		cvt5_round(float(RGBA[2])),
		transparency
	)
	return (out_rgb[0] * 2048 + out_rgb[1] *   64 + out_rgb[2] *    2 + out_rgb[3])

assert(len(sys.argv) > 1)

filesplit = os.path.split(sys.argv[1])
folder = filesplit[0]
filename = os.path.splitext(filesplit[1])[0]
fileout = os.path.join(folder, filename)

print("output files: "+fileout+"_*x*.551")

img = Image.open(sys.argv[1])
datas = img.getdata()
if img.mode == "RGBA" or img.mode == "RGB":
	RGB = img.getdata()
else:
	print ("image format needs to be RGB or RGBA (current: ",img.mode,")")
	sys.exit()

if len(sys.argv) > 2:
	if sys.argv[2] == '32x32':
		split_x = 32
		split_y = 32
	elif sys.argv[2] == '32x64':
		split_x = 32
		split_y = 64
	elif sys.argv[2] == '64x32':
		split_x = 64
		split_y = 32
	else:
		print('possibles split values: 32x32 64x32 32x64')
		sys.exit()
else:
	split_x = img.size[0]
	split_y = img.size[1]

print("processing...")
if img.size[0] % split_x != 0 or img.size[1] % split_y != 0:
	print("image width must be multiple of "+str(split_x)+" and height must multiples of "+str(split_y))
	sys.exit()
splits = {}
for i in range(0,len(RGB)):
	x = i % img.size[0]
	y = i // img.size[0]
	split = str(x // split_x) + 'x' + str(y // split_y)
	if not split in splits:
		splits[split] = np.ones(split_x * split_y, dtype=np.uint16)
	position = (y % split_y) * split_x + (x % split_x)
	splits[split][position] = getRGBA16(RGB[i])
print("saving converted files...")

segments = []
waves = []
for split in splits:
	split_out = fileout+'_'+split+'.551'
	splits[split].byteswap().tofile(split_out)
	segments.append("beginseg\n  name    \""+(filename+'_'+split)+"\"\n  flags   RAW\n  include \""+split_out+"\"\nendseg")
	waves.append("  include \""+(filename+'_'+split)+"\"")

print("add the following in your spec file: \n\n")
for segment in segments:
	print(segment)
print("\nbeginwave\n  name  \""+filename+"\"")
for wave in waves:
	print(wave)
print("endwave")
#else:
#	out = np.ones(len(RGB), dtype=np.uint16)
#	for i in range(0,len(RGB)):
#		transparency = 1
#		if len(RGB[i]) > 3:
#			if RGB[i][3] < 1:
#				transparency = 0
#		out_rgb = (
#			cvt5_round(float(RGB[i][0])),
#			cvt5_round(float(RGB[i][1])),
#			cvt5_round(float(RGB[i][2])),
#			transparency
#		)
#		out[i] = (
#			out_rgb[0] * 2048 +
#			out_rgb[1] *   64 +
#			out_rgb[2] *    2 +
#			out_rgb[3]
#		)
#	out.byteswap().tofile(fileout+'.551')

