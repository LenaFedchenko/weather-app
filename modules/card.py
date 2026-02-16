from PyQt6 import QtWidgets as widgets
import PyQt6.QtCore as core
from .frame import Frame_create

class Card(widgets.QFrame):
    def __init__(self, city_name, time, temp, max_temp, min_temp, description_weather):
        super().__init__()
        self.setFixedSize(core.QSize(330, 98))
        self.setStyleSheet("""
                            background-color: rgba(0, 0, 0, 51); 
                            border-radius: 8px;
                            """)
        self.LAYOUT = widgets.QVBoxLayout()
        self.LAYOUT.setContentsMargins(8, 8, 8, 8)
        self.setLayout(self.LAYOUT)

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
        

        self.LAYOUT_FRAME3 = widgets.QVBoxLayout()
        frame3 = Frame_create(layout=self.LAYOUT_FRAME3, width=247, height=58)
        frame3.setStyleSheet("background-color: transparent;")
        self.LAYOUT_FRAME3.setContentsMargins(2, 0, 0, 7)
        self.LAYOUT_DEGREE = widgets.QHBoxLayout()
        frame_degree = Frame_create(layout=self.LAYOUT_DEGREE, width=67, height=52)
        self.DEGREE = widgets.QLabel(parent= frame_degree, text= f"{temp}°") 
        self.DEGREE.setStyleSheet("font-size: 44px; background-color: transparent") 

        self.CITY_NAME = widgets.QLabel(parent= frame3, text= city_name)
        self.TIME = widgets.QLabel(parent= frame3, text=time)
        self.CITY_NAME.setStyleSheet("font-size: 24px; background-color: transparent")
        self.TIME.setStyleSheet("font-size: 12px; background-color: transparent")

        self.WEATER_FEELING = widgets.QLabel(parent=frame2, text= description_weather)
        self.TEMP = widgets.QLabel(parent=frame2, text=f"Макс.:{max_temp}°, мін.:{min_temp}°s")
        self.WEATER_FEELING.setStyleSheet("font-size: 12px; background-color: transparent")
        self.TEMP.setStyleSheet("font-size: 12px; background-color: transparent")
        self.TEMP.setAlignment(core.Qt.AlignmentFlag.AlignRight)
        self.WEATER_FEELING.setAlignment(core.Qt.AlignmentFlag.AlignLeft)

        self.FRAME2_LAYOUT.addWidget(self.WEATER_FEELING)
        self.FRAME2_LAYOUT.addWidget(self.TEMP)
        self.LAYOUT_FRAME3.addWidget(self.CITY_NAME)
        self.LAYOUT_FRAME3.addWidget(self.TIME)
        self.FRAME_LAYOUT.addWidget(frame3)
        self.FRAME_LAYOUT.addWidget(frame_degree)