# saveSnapShot


<IMAGEPATH> export image path
<MODULEPATH> module path

# max run

imgpath = @"<IMAGEPATH>"
pythoncode = stringStream ""
format "import sys;sys.path.append(r'<MODULEPATH>');from saveScreenShot.exts import max as ssmax;ssmax.SaveScreenShot(r'%')" imgpath to:pythoncode
python.Execute pythoncode


# maya run

from saveScreenShot.exts import maya as ssmaya
ssmaya.SaveScreenShot(r"<IMAGEPATH>")


# motionbuilder run

```
	output image must be in
    ".bmp", ".pbm", ".pgm", ".png", ".ppm", ".xbm", ".xpm" 
```

from saveScreenShot.exts import mobu as ssmobu
ssmobu.SaveScreenShot(r"<IMAGEPATH>")

# License

This software is released under the MIT License
