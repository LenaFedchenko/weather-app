import PyQt6.QtWidgets as widgets
from .card import Card
import PyQt6.QtCore as core

class Scroll_frame(widgets.QScrollArea):
    def __init__(self, parent):
        widgets.QScrollArea.__init__(self, parent = parent)
        self.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFixedSize(370, 707)
        self.setStyleSheet("border: none; background-color: transparent")
        self.setWidgetResizable(True)
        self.SCROLL_FRAME = widgets.QFrame(parent = self)
        self.SCROLL_FRAME_LAYOUT = widgets.QVBoxLayout()
        self.SCROLL_FRAME.setLayout(self.SCROLL_FRAME_LAYOUT)
        self.setWidget(self.SCROLL_FRAME)
        
        for i in range(10):
            card = Card()
            self.SCROLL_FRAME_LAYOUT.addWidget(card)


