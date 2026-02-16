import PyQt6.QtWidgets as widgets
from .card import Card
import PyQt6.QtCore as core
from .info_from_api import info_for_card
from datetime import datetime, timedelta, timezone

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
        city_name, temp, descr, max_t, min_t, timezone_offset= info_for_card("Miami")
        self.setWidget(self.SCROLL_FRAME)
        # текущее UTC время
        utc_now = datetime.now(timezone.utc)
        # прибавляем к времени сейчас, время которое отстает в секундах, что бы получить разницу
        city_time = utc_now + timedelta(seconds=timezone_offset)
        # только часы и минуты
        time_final = city_time.strftime("%H:%M")


        for i in range(10):
            card = Card(
                time= time_final,
                city_name= city_name, 
                temp = temp, 
                description_weather = descr, 
                max_temp = max_t,
                min_temp = min_t
                )
            self.SCROLL_FRAME_LAYOUT.addWidget(card)


