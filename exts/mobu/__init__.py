from ... import util
from ... import cropImage
from ... import tiff2bitmap


import pyfbsdk as fb

import os


def _saveBuffer(savePath, tmpImgExtension="tif"):

    app = fb.FBApplication()
    take = fb.FBSystem().CurrentTake
    current = fb.FBTime(fb.FBPlayerControl().GetEditCurrentTime())
    next = fb.FBTime(fb.FBPlayerControl().GetEditCurrentTime() + 1)

    opts = fb.FBVideoGrabber().GetOptions()
    videoManager = fb.FBVideoCodecManager()
    videoManager.VideoCodecMode = fb.FBVideoCodecMode.FBVideoCodecUncompressed

    opts.OutputFileName = savePath
    opts.RenderAudio = False
    opts.BitsPerPixel = fb.FBVideoRenderDepth.FBVideoRender32Bits
    opts.TimeSpan = fb.FBTimeSpan(current, next)
    opts.TimeStep = fb.FBTime(0, 0, 0, 1, 0)

    app.FileRender( opts )


def SaveScreenShot(outPath, tmpImgExtension="tif"):
    util.CheckDirectory(outPath)
    tmp_file = util.GetTempImgPath(extension=tmpImgExtension)

    _saveBuffer(tmp_file)
    current = fb.FBTime(fb.FBPlayerControl().GetEditCurrentTime())
    tmp_file = "{0}{1:04d}.tif".format(tmp_file.split(".")[0], current.GetFrame())
    tmp_bmp = tmp_file.replace(".tif", ".bmp")
    tiff2bitmap.execute(tmp_file, tmp_bmp)


    result = cropImage.CropImage.RunCropImage(tmp_bmp, outPath, parent=None)

    os.remove(tmp_file)
    os.remove(tmp_bmp)

    return (result == 1)


def GetMayaMainWindow():
    from ...Qt import QtWidgets

    parent = next(
        o for o in QtWidgets.QApplication.instance().topLevelWidgets()
        if "MotionBuilder " in o.windowTitle()
    )
    return parent
