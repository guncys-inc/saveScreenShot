# What's it?

このツールは、ビューポート上のスクリーンショット画像の取得を目的とした汎用ツールです。
使用用途としては、アーティストが作業の成果物を出荷する際に、サムネイル画像を残したい時などに使用します。
GUIの取得や画像の切り取りには、mottosso氏が開発した[Qt.py](https://github.com/mottosso/Qt.py)を使用しています。
Qtを採用しているDCCツールでPythonのAPIがあるものであれば更にサポートツールを広げることが出来ると思います。
開発にご協力して頂ける方を募集中です。
現在は、Autodesk Maya® 3ds Max® MotionBuilder®をサポートしています。


# saveSnapShotの使い方


<IMAGEPATH> export image path
<MODULEPATH> module path

# 3dsmax run

```
imgpath = @"<IMAGEPATH>"
pythoncode = stringStream ""
format "import sys;sys.path.append(r'<MODULEPATH>');from saveScreenShot.exts import max as ssmax;ssmax.SaveScreenShot(r'%')" imgpath to:pythoncode
python.Execute pythoncode
```

# maya run

```
from saveScreenShot.exts import maya as ssmaya
ssmaya.SaveScreenShot(r"<IMAGEPATH>")
```

# motionbuilder run

```
    output image must be in
    ".bmp", ".pbm", ".pgm", ".png", ".ppm", ".xbm", ".xpm" 
```

```
from saveScreenShot.exts import mobu as ssmobu
ssmobu.SaveScreenShot(r"<IMAGEPATH>")
```
# License

This software is released under the MIT License
