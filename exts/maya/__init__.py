import os
import sys
from ... import util
from ... import cropImage

from maya import OpenMayaUI
from maya import OpenMaya

IS_PYTHON2 = (sys.version_info[0] == 2)


def _saveBuffer(savePath, tmpImgExtension="bmp"):
    img = OpenMaya.MImage()
    view = OpenMayaUI.M3dView.active3dView()
    view.readColorBuffer(img, True)
    img.writeToFile(savePath, tmpImgExtension)


def SaveScreenShot(outPath, tmpImgExtension="bmp"):
    util.CheckDirectory(outPath)
    tmp_file = util.GetTempImgPath(extension=tmpImgExtension)

    _saveBuffer(tmp_file)

    result = cropImage.CropImage.RunCropImage(tmp_file,
                                              outPath,
                                              parent=GetMayaMainWindow())

    os.remove(tmp_file)

    return (result is 1)


def _get_main_window_pointer():
    if hasattr(OpenMayaUI, "MQtUtil_mainWindow"):
        pointer = OpenMayaUI.MQtUtil_mainWindow()
    elif hasattr(OpenMayaUI, "MQtUtil"):
        pointer = OpenMayaUI.MQtUtil.mainWindow()

    if IS_PYTHON2:
        return long(pointer)
    return int(pointer)


def GetMayaMainWindow():
    from ... import Qt
    from ...Qt import QtWidgets

    if Qt.IsPySide2:
        import shiboken2 as shiboken
    else:
        import shiboken

    return shiboken.wrapInstance(_get_main_window_pointer(),
                                 QtWidgets.QMainWindow)
