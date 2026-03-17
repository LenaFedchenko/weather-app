import PyQt6.QtWidgets as widgets
from .card import Card
import PyQt6.QtCore as core
from .info_from_api import info_for_card
from datetime import datetime, timedelta, timezone
import json, os

class Scroll_frame(widgets.QScrollArea):
    def __init__(self, parent, right_layout_frame, content_frame):
        widgets.QScrollArea.__init__(self, parent = parent)
        self.right_layout_frame = right_layout_frame
        self.content_frame = content_frame
        self.path_json = os.path.abspath(os.path.join(__file__, "..", "..", "static", "json", "countries.json"))
        with open(self.path_json, "r", encoding="utf-8") as file:
            # список всех городов с джсона
            data = json.load(file)
        self.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFixedSize(370, 727)
        self.setStyleSheet("border: none; background-color: transparent")
        self.setWidgetResizable(True)
        self.SCROLL_FRAME = widgets.QFrame(parent = self)
        
        self.SCROLL_FRAME_LAYOUT = widgets.QVBoxLayout()
        self.SCROLL_FRAME_LAYOUT.setSpacing(0)
        self.SCROLL_FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.SCROLL_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.SCROLL_FRAME.setLayout(self.SCROLL_FRAME_LAYOUT)
        if data:
            for city in data:
                self.setWidget(self.SCROLL_FRAME)
                try:
                    card = Card(
                        city_name_from_list= city,
                        right_layout_frame= self.right_layout_frame,
                        content_frame = self.content_frame
                        )
                    self.SCROLL_FRAME_LAYOUT.addWidget(card)
                except:
                    print("error")
    def city_list(self, city):
        self.LIST_CITY = city
        try:
            with open(self.path_json, "r", encoding="utf-8") as file:
                data = json.load(file)
        # если чтото не так с джсоном
        except (FileNotFoundError, json.JSONDecodeError):
            data = []  
        if self.LIST_CITY not in data:
            data.append(self.LIST_CITY)

            with open(self.path_json, "w") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            self.setWidget(self.SCROLL_FRAME)
            try:
                card = Card(
                    city_name_from_list= self.LIST_CITY,
                    right_layout_frame= self.right_layout_frame,
                    content_frame = self.content_frame
                    )
                self.SCROLL_FRAME_LAYOUT.addWidget(card)
            except:
                print("error")




