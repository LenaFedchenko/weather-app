import PyQt6.QtWidgets as widgets
import PyQt6.QtCore as core
import PyQt6.QtGui as gui
from .frame import Frame_create
from .load_img import ImageLoad
import os

class Weather_per_hour:
    def __init__(self, frame):
        self.LAYOUT_MAIN = widgets.QVBoxLayout()
        self.LAYOUT_MAIN.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        self.FRAME_MAIN = Frame_create(self.LAYOUT_MAIN, width = 788, height = 157)
        self.FRAME_MAIN.setStyleSheet("border-radius: 8px; background-color:rgba(0, 0, 0, 51)")

        frame.addWidget(self.FRAME_MAIN)

        self.FRAME_TEXT_LAYOUT = widgets.QVBoxLayout()
        self.FRAME_TEXT = Frame_create(self.FRAME_TEXT_LAYOUT, width = 756, height = 45, color = "transparent")
        self.LAYOUT_MAIN.addWidget(self.FRAME_TEXT)


        self.FRAME_PEAGTIJ_LAYOUT = widgets.QHBoxLayout()
        self.FRAME_PEAGTIJ_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.FRAME_PAERT = Frame_create(self.FRAME_PEAGTIJ_LAYOUT, width = 765, height = 90, color="transparent")
        self.FRAME_PEAGTIJ_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.LAYOUT_MAIN.addWidget(self.FRAME_PAERT)
        
        self.LABEL = widgets.QLabel("Хмарна погода до кінця дня")
        line = Frame_create(widgets.QVBoxLayout(), 756, 1, "white")

        self.FRAME_TEXT_LAYOUT.addWidget(self.LABEL)
        self.FRAME_TEXT_LAYOUT.addWidget(line)


        self.BUTTON = widgets.QPushButton(parent= self.FRAME_PAERT)
        self.BUTTON.setFixedSize(40, 82)
        self.path_img = os.path.abspath(os.path.join(__file__, "..", "..", "media", "btn_scroll.png"))
        self.ICON_BUTTON = gui.QIcon(self.path_img)
        self.BUTTON.setIcon(self.ICON_BUTTON)
        # self.BUTTON.setIconSize(core.QSize(40, 82))
        self.FRAME_PEAGTIJ_LAYOUT.addWidget(self.BUTTON)

        
        self.SCROLL_WEATHER = widgets.QScrollArea(parent= self.FRAME_PAERT)
        self.SCROLL_WEATHER.setHorizontalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.SCROLL_WEATHER.setFixedSize(676, 102)
        self.SCROLL_WEATHER.setStyleSheet("border: none; background-color: transparent")
        self.SCROLL_WEATHER.setWidgetResizable(True)
        self.SCROLL_FRAME_WEATHER = widgets.QFrame(parent = self.SCROLL_WEATHER)
        self.SCROLL_FRAME_WEATHER_LAYOUT = widgets.QHBoxLayout()
        self.SCROLL_FRAME_WEATHER_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.SCROLL_FRAME_WEATHER_LAYOUT.setSpacing(0)
        self.SCROLL_FRAME_WEATHER.setLayout(self.SCROLL_FRAME_WEATHER_LAYOUT)
        for i in range(25):
            self.SCROLL_WEATHER.setWidget(self.SCROLL_FRAME_WEATHER)
            self.HORIZONTAL_LAYOUT = widgets.QVBoxLayout()
            self.FRAME_MAIN2 = Frame_create(self.HORIZONTAL_LAYOUT, width = 50, height = 92, color= "transparent")
            self.LABEL_TIME = widgets.QLabel("22")
            self.LABEL_MIN_TEMP = widgets.QLabel("0°")
            self.HORIZONTAL_LAYOUT.addWidget(self.LABEL_TIME)
            self.IMAGE = ImageLoad(25, 25, self.FRAME_MAIN2, 'example.png')
            self.HORIZONTAL_LAYOUT.addWidget(self.IMAGE)
            self.HORIZONTAL_LAYOUT.addWidget(self.LABEL_MIN_TEMP)

            self.SCROLL_FRAME_WEATHER_LAYOUT.addWidget(self.FRAME_MAIN2)
        
        self.FRAME_PEAGTIJ_LAYOUT.addWidget(self.SCROLL_WEATHER)
        self.BUTTON2 = widgets.QPushButton(parent= self.FRAME_PAERT)
        self.BUTTON2.setFixedSize(40, 82)
        self.path_img2 = os.path.abspath(os.path.join(__file__, "..", "..", "media", "btn_next.png"))
        self.ICON_BUTTON2 = gui.QIcon(self.path_img2)
        self.BUTTON2.setIcon(self.ICON_BUTTON2)
        # self.BUTTON2.setIconSize(core.QSize(40, 82))
        self.FRAME_PEAGTIJ_LAYOUT.addWidget(self.BUTTON2)

    def weather_per_hour(self):
        self.FRAME_MAIN.setParent(None)