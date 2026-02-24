import os
import PyQt6.QtWidgets as widgets
from PIL import Image
from PIL.ImageQt import ImageQt
import PyQt6.QtGui as gui


class ImageLoad(widgets.QLabel):
    def __init__(self, width, height, frame, img):
        super().__init__(parent=frame)
        image_logo = Image.open(
            os.path.abspath(
                os.path.join(__file__, "..", "..", "media", img)
            )
        )
        qt_image = ImageQt(image_logo)
        pixmap = gui.QPixmap(gui.QImage(qt_image))
        pixmap = pixmap.scaled(width, height)
        self.setPixmap(pixmap)