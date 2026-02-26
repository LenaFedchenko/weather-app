import PyQt6.QtWidgets as widgets
from .card import Card
import PyQt6.QtCore as core
from .info_from_api import info_for_card
from datetime import datetime, timedelta, timezone

class Scroll_frame(widgets.QScrollArea):
    def __init__(self, parent, right_layout_frame, content_frame):
        widgets.QScrollArea.__init__(self, parent = parent)
        list_cities = [
            "Tokyo",
            "Sydney",
            "Berlin",
            "Toronto",
            "Barcelona",
            "Dubai",
            "Cape Town",
            "Dnipro"
        ]
        self.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFixedSize(370, 727)
        self.setStyleSheet("border: none; background-color: transparent")
        self.setWidgetResizable(True)
        self.SCROLL_FRAME = widgets.QFrame(parent = self)
        self.SCROLL_FRAME_LAYOUT = widgets.QVBoxLayout()
        self.SCROLL_FRAME_LAYOUT.setSpacing(0)
        self.SCROLL_FRAME.setLayout(self.SCROLL_FRAME_LAYOUT)
            
        for city in list_cities:
            self.setWidget(self.SCROLL_FRAME)
            card = Card(
                city_name_from_list= city,
                right_layout_frame= right_layout_frame,
                content_frame = content_frame 
                )


            self.SCROLL_FRAME_LAYOUT.addWidget(card)



