#!/usr/bin/env python

import json

resolutions = [('mdpi', 1), ('hdpi', 1.5), ('xhdpi', 2), ('xxhdpi', 3), ('xxxhdpi',4)]

outputs = []

base_file = "transparent_map_buttons.svg"
base = (48, 41)
ids = ['btn_top_on', 'btn_top_off', 'btn_bottom_on', 'btn_bottom_off']

ink = "/Applications/Inkscape.app/Contents/Resources/bin/inkscape"

fh = open('./ink.js','r')
data = json.load(fh)
fh.close()

for each in data:
    for id in each['ids']:
        for res in resolutions:
            fname = 'drawable-{0}/{1}.png'.format(res[0],id)
            width = each['base'][0] * res[1]
            height = each['base'][1] * res[1]
        
            outputs.append([id, fname, width, height, each['file']])

for each in resolutions:
  print "mkdir drawable-{0}".format(each[0])

for each in outputs:
  print "{0} -e {1} -w {2} -h {3} -i {5} {4}".format(ink, each[1], each[2], each[3], each[4], each[0])
