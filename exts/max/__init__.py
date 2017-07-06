from ... import util
from ... import cropImage

import os
import MaxPlus


CaptureCmd = '''imagepath = @"%s"
view_size = getViewSize()
anim_bmp = bitmap view_size.x view_size.y filename:imagepath

dib = gw.getViewportDib()
copy dib anim_bmp
save anim_bmp

bmpGrab = undefined
freescenebitmaps()'''


def _saveBuffer(tmp_file):
    MaxPlus.Core.EvalMAXScript(CaptureCmd % tmp_file)


def SaveScreenShot(outPath, tmpImgExtension="bmp"):
    util.CheckDirectory(outPath)

    tmp_file = util.GetTempImgPath(extension=tmpImgExtension)

    _saveBuffer(tmp_file)

    # crop window
    result = cropImage.CropImage.RunCropImage(tmp_file, outPath)

    # remove temp file
    os.remove(tmp_file)

    return (result is 1)

