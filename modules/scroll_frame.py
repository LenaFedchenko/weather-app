import PyQt6.QtWidgets as widgets
import PyQt6.QtCore as core

from .load_img import ImageLoad

class Scroll_frame(widgets.QScrollArea):
    def __init__(self, parent):
        widgets.QScrollArea.__init__(self, parent = parent)
        self.setFixedSize(370, 707)
        self.setStyleSheet("border: none;")
        self.setWidgetResizable(True)
        self.setStyleSheet("background-color: transparent")
        self.SCROLL_FRAME = widgets.QFrame(parent = self)
        self.SCROLL_FRAME_LAYOUT = widgets.QVBoxLayout()
        self.SCROLL_FRAME.setLayout(self.SCROLL_FRAME_LAYOUT)
        self.setWidget(self.SCROLL_FRAME)
        
        for i in range(10):
            card = widgets.QFrame(parent = self.SCROLL_FRAME)
            card.setFixedSize(core.QSize(330, 90))
            card.setStyleSheet("background-color: red; ")
            
            self.SCROLL_FRAME_LAYOUT.addWidget(card)

        