#!/usr/bin/env python

import json


class InkMaker:
    def __init__(self, fname):
        self.filename = fname
        self.resolutions_and = [('mdpi', 1), ('hdpi', 1.5), ('xhdpi', 2), ('xxhdpi', 3), ('xxxhdpi', 4)]
        self.resolutions_ios = [('@1x', 1), ('@2x', 2), ('@3x', 3)]
        self.outputs = []
        self.resizes = []
        self.data = []
        self.ink = "/Applications/Inkscape.app/Contents/Resources/bin/inkscape"
        self.convert = "/usr/local/bin/convert"

    def load_data(self):
        fh = open(self.filename, 'r')
        self.data = json.load(fh)
        fh.close()

    def make_directories(self):
        for res in self.resolutions_and:
            print "mkdir drawable-{0}".format(res[0])

    def build_inks(self):
        for file_spec in self.data:
            for drawing_id in file_spec['ids']:
                print "mkdir {0}.imageset".format(drawing_id)
                for res in self.resolutions_and:
                    fname = 'drawable-{0}/{1}.png'.format(res[0], drawing_id)
                    self.out_add(drawing_id, fname, res, file_spec)

                for res in self.resolutions_ios:
                    fname = '{0}.imageset/{0}{1}.png'.format(drawing_id, res[0], file_spec)
                    self.out_add(drawing_id, fname, res, file_spec)

    def out_add(self, drawing_id, fname, res, fspec):
        width = fspec['base'][0] * res[1]
        height = fspec['base'][1] * res[1]

        if 'resize' in fspec:
            r_width = fspec['resize'][0] * res[1]
            r_height = fspec['resize'][1] * res[1]
            self.resizes.append([fname, r_width, r_height])

        self.outputs.append([drawing_id, fname, width, height, fspec['file']])

    def do_ink_output(self):
        for out in self.outputs:
            print "{0} -e {1} -w {2} -h {3} -i {5} -j {4}".format(self.ink, out[1], out[2], out[3], out[4], out[0])

    def do_resize_output(self):
        for res in self.resizes:
            print "{0} {1} -gravity center -background transparent -extent {2}x{3} {1}"\
                .format(self.convert, res[0], res[1], res[2])

    def handle(self):
        self.load_data()
        self.make_directories()
        self.build_inks()
        self.do_ink_output()
        self.do_resize_output()

if __name__ == "__main__":
    im = InkMaker('./ink.js')
    im.handle()
