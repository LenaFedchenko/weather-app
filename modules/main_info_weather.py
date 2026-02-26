from .frame import Frame_create
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
import os
from .load_img import ImageLoad

class MainInfoWeather():
    def __init__(self, content_frame):
        self.FRAME_LAYOUT = widgets.QHBoxLayout()
        self.FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0)

        frame_all = Frame_create(layout=self.FRAME_LAYOUT, width=788, height=303)
        content_frame.addWidget(frame_all)

        WEATHER_LAYOUT = widgets.QVBoxLayout()
        WEATHER_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)

        WEATHER = Frame_create(WEATHER_LAYOUT, 390, 303)
        WEATHER.setStyleSheet("""
            background-color: rgba(0, 0, 0, 51);
            border-radius: 20px;
        """)

        self.FRAME_LAYOUT.addWidget(WEATHER)

        POSITION_LAYOUT = widgets.QVBoxLayout()
        POSITION_LAYOUT.setContentsMargins(0, 0, 0, 0)
        POSITION_LAYOUT.setSpacing(5)

        POSITION = Frame_create(POSITION_LAYOUT, 358, 50, "transparent")

        group_layout = widgets.QHBoxLayout()
        group_layout.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        group_layout.setSpacing(5)

        group = Frame_create(group_layout, 358, 40, "transparent")

        self.LABEL_ICON = ImageLoad(16, 16, group, 'location.png')

        self.LABEL = widgets.QLabel("Поточна позиція")
        self.LABEL.setStyleSheet("font-size: 16px; background-color: transparent")

        group_layout.addWidget(self.LABEL_ICON)
        group_layout.addWidget(self.LABEL)

        line = widgets.QFrame()
        line.setFixedHeight(1)
        line.setStyleSheet("background-color: white; border-radius: 1px;")

        POSITION_LAYOUT.addWidget(group)
        POSITION_LAYOUT.addWidget(line)
        self.LABEL_1 = widgets.QLabel("Дніпро")
        self.LABEL_1.setStyleSheet("font-size: 44px; background-color: transparent")
        self.LABEL_1.setAlignment(core.Qt.AlignmentFlag.AlignCenter)

        degree_layout = widgets.QHBoxLayout()
        degree_layout.setAlignment(core.Qt.AlignmentFlag.AlignCenter)

        degree_frame = Frame_create(degree_layout, 300, 100, color="transparent")

        img_weather = ImageLoad(96, 96, degree_frame, 'example.png')
        self.LABEL_2 = widgets.QLabel("11°")
        self.LABEL_2.setStyleSheet("font-size: 74px; background-color: transparent")
        self.LABEL_2.setAlignment(core.Qt.AlignmentFlag.AlignCenter)

        degree_layout.addWidget(img_weather)
        degree_layout.addWidget(self.LABEL_2)

        self.LABEL_3 = widgets.QLabel("Хмарно")
        self.LABEL_3.setStyleSheet("font-size: 24px; background-color: transparent")
        self.LABEL_3.setAlignment(core.Qt.AlignmentFlag.AlignCenter)

        self.LABEL_4 = widgets.QLabel("Макс.:11°, мін.:0°")
        self.LABEL_4.setStyleSheet("font-size: 16px; background-color: transparent")
        self.LABEL_4.setAlignment(core.Qt.AlignmentFlag.AlignCenter)

        WEATHER_LAYOUT.addWidget(POSITION)
        WEATHER_LAYOUT.addWidget(self.LABEL_1)
        WEATHER_LAYOUT.addWidget(degree_frame)
        WEATHER_LAYOUT.addWidget(self.LABEL_3)
        WEATHER_LAYOUT.addWidget(self.LABEL_4)
        

        FRAME_LAYUOT1 = widgets.QVBoxLayout()
        frame_date = Frame_create(layout=FRAME_LAYUOT1, width=390, height=303) 
        
        frame_date.setStyleSheet('background-color: rgba(0, 0, 0, 56); border-radius: 20px')
        self.FRAME_LAYOUT.addWidget(frame_date)

        group2_layout = widgets.QVBoxLayout()
        group2 = Frame_create(group2_layout, 358, 45, color= "transparent")

        self.TODAY = widgets.QLabel("Сьогодні")
        self.TODAY.setStyleSheet("font-size: 16px")
        line2 = widgets.QFrame()
        line2.setFixedHeight(1)
        line2.setStyleSheet("background-color: white;")

        group2_layout.addWidget(self.TODAY)
        group2_layout.addWidget(line2)

        group3_layout = widgets.QHBoxLayout()
        group3 = Frame_create(group3_layout, 358, 44, color= "transparent")

        day = widgets.QLabel("Понеділок")
        date = widgets.QLabel("24.03.2025")
        day.setStyleSheet("font-size: 24px")
        date.setStyleSheet("font-size: 24px")
        group3_layout.addWidget(day)
        group3_layout.addStretch()
        group3_layout.addWidget(date)

        clock_layout = widgets.QVBoxLayout()
        clock = Frame_create(clock_layout, width=168, height= 168)
        clock_layout.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        clock.setStyleSheet(f"""
                            border-radius: 80px; 
                            background-image: url({os.path.abspath(os.path.join(__file__, "..", "..", "media", "Ticks.png"))});
                            """)

        FRAME_LAYUOT1.addWidget(group2)
        FRAME_LAYUOT1.addWidget(group3)
        FRAME_LAYUOT1.addWidget(clock, alignment=core.Qt.AlignmentFlag.AlignCenter)
