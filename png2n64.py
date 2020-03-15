#!/usr/bin/python3

import sys
import math
import numpy as np
from PIL import Image

def cvt5_round(val):
#	return int(val) / 8
	return max(0, min(31, round(val / 8)))

assert(len(sys.argv) > 2)

img = Image.open(sys.argv[1])
datas = img.getdata()
if img.mode == "RGBA" or img.mode == "RGB":
	RGB = img.getdata()
else:
	print ("image format needs to be RGB or RGBA (current: ",img.mode,")")
	sys.exit()

out = np.ones(len(RGB), dtype=np.uint16)
for i in range(0,len(RGB)):
	transparency = 1
	if len(RGB[i]) > 3:
		if RGB[i][3] < 1:
			transparency = 0
	out_rgb = (
		cvt5_round(float(RGB[i][0])),
		cvt5_round(float(RGB[i][1])),
		cvt5_round(float(RGB[i][2])),
		transparency
	)
	out[i] = (
		out_rgb[0] * 2048 +
		out_rgb[1] *   64 +
		out_rgb[2] *    2 +
		out_rgb[3]
	)

out.byteswap().tofile(sys.argv[2])

