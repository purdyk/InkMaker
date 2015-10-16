InkMaker
========

Inkmaker is a tool to generate Android assets from an svg using inkscape.

Usage:

Create an ink.js file in the directory containing the svgs you wish to render out.

```javascript
[
  {
    "file": "directions.svg",
    "ids": ["ic_dir"],
    "base": [18,18],
    "resize": [22,22]
  }
]
```

This file would render out a drawing with id 'ic_dir' from a file called 'directions.svg'

It would use a base (mdpi) resolution of 18 by 18 pixels, and scale this to all sizes by the 
recommended scale factor.

All scaled sizes would then have their canvas extended to a scaled 22x22 pixels. This is useful when your drawing is not the correct aspect ratio to your desired image.

The script outputs commands to run inkscape, imagemagic, and create the required directories.

The "resize" parameter is optional.

```bash
InkMaker.py > ./make_it.sh
sh make_it.sh
```

This would produce outputs in folders named drawable-RES/ for mdpi, hdpi, xhdpi, xxhdpi, and xxxhdpi, as well as an ic_dir.imageset with a 1x, 2x, and 3x scaled image.