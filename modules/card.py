from PyQt6 import QtWidgets as widgets
import PyQt6.QtCore as core
from .frame import Frame_create
from .load_img import ImageLoad
from .info_from_api import info_for_card
from datetime import datetime, timedelta, timezone
from .main_info_weather import MainInfoWeather
from .graphic import Graphic

class Card(widgets.QFrame):
    active_card = None
    active_info_weather = None
    active_grafic = None
    def __init__(self, city_name_from_list, right_layout_frame, content_frame ):
        super().__init__()
        self.setFixedSize(core.QSize(330, 98))
        self.setStyleSheet("""
                            background-color: transparent; 
                            border-radius: 8px;
                            """)
        self.LAYOUT = widgets.QVBoxLayout()
        self.LAYOUT.setContentsMargins(8, 8, 8, 8)
        self.setLayout(self.LAYOUT)
        self.RIGHT_LAYOUT_FRAME = right_layout_frame
        self.CONTENT_FRAME = content_frame
        self.FRAME_LAYOUT = widgets.QHBoxLayout()
        self.FRAME_LAYOUT.setContentsMargins(0, 0, 0, 8)
        self.FRAME2_LAYOUT = widgets.QHBoxLayout()
        frame = Frame_create(layout=self.FRAME_LAYOUT, width=314, height=52)
        frame.setStyleSheet("background-color: transparent")
        frame2 = Frame_create(layout=self.FRAME2_LAYOUT, width=314)
        self.FRAME2_LAYOUT.setContentsMargins(0, 0, 0, 0)
        frame2.setStyleSheet("background-color: transparent")
        self.LAYOUT.addWidget(frame)
        self.LAYOUT.addWidget(frame2)
        self.city_name_from_list = city_name_from_list
        city_name, temp, info_weather, max_temp, min_temp, timezone_offset, img = info_for_card(self.city_name_from_list)
        self.CITY_NAME2 = city_name
        # self.TIME2 = time
        self.TEMP2 = temp
        self.MAX_TEMP = max_temp
        self.MIN_TEMP = min_temp
        self.TIME_ZONE = timezone_offset
        self.DECS_WEATH = info_weather

        # текущее UTC время
        self.utc_now = datetime.now(timezone.utc)
        # прибавляем к времени сейчас, время которое отстает в секундах, что бы получить разницу
        self.city_time = self.utc_now + timedelta(seconds=self.TIME_ZONE)
        # только часы и минуты
        self.time_final = self.city_time.strftime("%H:%M")

        self.LAYOUT_FRAME3 = widgets.QVBoxLayout()
        frame3 = Frame_create(layout=self.LAYOUT_FRAME3, width=247, height=58)
        frame3.setStyleSheet("background-color: transparent;")
        self.LOCATION_LAYOUT = widgets.QHBoxLayout() 
        self.LOCATION_LAYOUT.setContentsMargins(0, 0, 10, 0)
        self.LOCATION = Frame_create(self.LOCATION_LAYOUT, 125, 48)
        self.LAYOUT_FRAME3.addWidget(self.LOCATION)
        self.location_icon = ImageLoad(16, 16, self.LOCATION, "location.png")
        self.LOCATION_LAYOUT.addWidget(self.location_icon)
        self.location_icon.hide()
        self.LAYOUT_FRAME3.setContentsMargins(2, 0, 0, 7)
        self.LAYOUT_DEGREE = widgets.QHBoxLayout()
        frame_degree = Frame_create(layout=self.LAYOUT_DEGREE, width=67, height=52)
        self.DEGREE = widgets.QLabel(parent= frame_degree, text= f"{self.TEMP2}°") 
        self.DEGREE.setStyleSheet("font-size: 40px; background-color: transparent; font-weight: 700") 

        self.CITY_NAME = widgets.QLabel(parent= frame3, text= self.CITY_NAME2)
        self.TIME = widgets.QLabel(parent= frame3, text=self.time_final)
        self.CITY_NAME.setStyleSheet("font-size: 24px; background-color: transparent; font-weight: 700")
        self.TIME.setStyleSheet("font-size: 12px; background-color: transparent; font-weight: 700")

        self.WEATER_FEELING = widgets.QLabel(parent=frame2, text= self.DECS_WEATH)
        self.TEMP = widgets.QLabel(parent=frame2, text=f"Макс.:{self.MAX_TEMP}°, мін.:{self.MIN_TEMP}°s")
        self.WEATER_FEELING.setStyleSheet("font-size: 12px; background-color: transparent; font-weight: 700")
        self.TEMP.setStyleSheet("font-size: 12px; background-color: transparent; font-weight: 700")
        self.TEMP.setAlignment(core.Qt.AlignmentFlag.AlignRight)
        self.WEATER_FEELING.setAlignment(core.Qt.AlignmentFlag.AlignLeft)

        self.layoutLine = widgets.QVBoxLayout()
        self.frame_line = Frame_create(layout=self.layoutLine, width=314, height=1, color= "rgba(255, 255, 255, 0.5)")
        self.FRAME2_LAYOUT.addWidget(self.WEATER_FEELING)
        self.FRAME2_LAYOUT.addWidget(self.TEMP)
        self.LOCATION_LAYOUT.addWidget(self.CITY_NAME)
        self.LAYOUT_FRAME3.addWidget(self.TIME)
        self.FRAME_LAYOUT.addWidget(frame3)
        self.LAYOUT.addWidget(self.frame_line)
        self.FRAME_LAYOUT.addWidget(frame_degree)

        btn_card = widgets.QPushButton(parent= self)
        btn_card.setStyleSheet("background-color: transparent")
        btn_card.setFixedSize(330, 98)
        btn_card.clicked.connect(self.select_card)
    
        
    def select_card(self):
        city_name, temp, info_weather, max_temp, min_temp, timezone_offset, img = info_for_card(self.city_name_from_list)
        self.CITY_NAME2 = city_name
        self.TEMP2 = temp
        self.MAX_TEMP = max_temp
        self.MIN_TEMP = min_temp
        self.DECS_WEATH = info_weather
        self.TIME_ZONE = timezone_offset

        # текущее UTC время
        self.utc_now = datetime.now(timezone.utc)
        self.city_time = self.utc_now + timedelta(seconds=self.TIME_ZONE)
        self.time_final = self.city_time.strftime("%H:%M")
        date = self.city_time.strftime("%d/%m/%Y")
        date = date.split("/")
        new_date = ""
        for num in date:
            new_date += str(num) + "."
        new_date = new_date[:-1]
        days_ua = {
            "Monday": "Понеділок",
            "Tuesday": "Вівторок",
            "Wednesday": "Середа",
            "Thursday": "Четвер",
            "Friday": "Пʼятниця",
            "Saturday": "Субота",
            "Sunday": "Неділя",
        }

        day_en = self.city_time.strftime("%A")
        day = days_ua.get(day_en, day_en)
        
        # Сброс предыдущей активной карточки
        if Card.active_card:
            if Card.active_card is not self:
                Card.active_card.reset_style()
        # Удаляем предыдущий MainInfoWeather
        if Card.active_info_weather:
            Card.active_info_weather.delete()
            Card.active_info_weather = None
        if Card.active_grafic:
            Card.active_grafic.delete_graphic()
            Card.active_grafic = None
        # Создаём новый
        Card.active_card = self
        Card.active_info_weather = MainInfoWeather(
            self.RIGHT_LAYOUT_FRAME,
            self.DECS_WEATH,
            self.TEMP2,
            self.CITY_NAME2,
            self.MAX_TEMP,
            self.MIN_TEMP,
            day,
            new_date,
            self.time_final,
            img
        )
        Card.active_grafic = Graphic(
            self.CONTENT_FRAME
        )
        # Обновляем визуальные элементы после новых запросов в апи
        self.CITY_NAME.setText(self.CITY_NAME2)
        self.DEGREE.setText(f"{self.TEMP2}°")
        self.TEMP.setText(f"Макс.:{self.MAX_TEMP}°, мін.:{self.MIN_TEMP}°")
        self.WEATER_FEELING.setText(self.DECS_WEATH)
        self.TIME.setText(self.time_final)

        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 51); 
            border-radius: 8px;
        """)
        self.frame_line.setStyleSheet("background-color: transparent")
        self.location_icon.show()
        self.LOCATION_LAYOUT.addWidget(self.CITY_NAME)
    def reset_style(self):
        self.setStyleSheet("""
            background-color: transparent; 
            border-radius: 8px;
        """)
        self.frame_line.setStyleSheet("background-color: rgba(255, 255, 255, 0.5)")
        self.location_icon.hide()