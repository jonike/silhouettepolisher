
from PySide2 import QtWidgets
import shiboken2
import maya.OpenMayaUI as omui
from silhouettepolisher.ui import SilhouettePolisherWindow


_silhouette_polisher_window = None


def launch():
    if _silhouette_polisher_window is None:
        global _silhouette_polisher_window
        main_window = omui.MQtUtil.mainWindow()
        parent = shiboken2.wrapInstance(long(main_window), QtWidgets.QWidget)
        _silhouette_polisher_window = SilhouettePolisherWindow(parent)
    _silhouette_polisher_window.show()