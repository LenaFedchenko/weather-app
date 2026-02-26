import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import os
import PyQt6.QtGui as gui

from .app import app_obj
from .title_bar import Title_bar
from utils import api_request
from .scroll_frame import Scroll_frame
from .load_img import ImageLoad
from .graphic import Graphic
from .frame import Frame_create
# from .main_info_weather import MainInfoWeather

class MainWindow(widgets.QMainWindow):
    def __init__(self, window_width: int, window_height: int):
        widgets.QMainWindow.__init__(self)
        
        self.setWindowFlags(core.Qt.WindowType.FramelessWindowHint)
        
        self.WINDOW_WIDTH = window_width
        self.WINDOW_HEIGHT = window_height
        self.SCREEN = app_obj.primaryScreen()
        self.SCREEN_SIZE = self.SCREEN.size()
        self.SCREEN_WIDTH = self.SCREEN_SIZE.width()
        self.SCREEN_HEIGHT = self.SCREEN_SIZE.height()
        self.CENTER_X = (self.SCREEN_WIDTH // 2) - (self.WINDOW_WIDTH // 2)
        self.CENTER_Y = (self.SCREEN_HEIGHT // 2) - (self.WINDOW_HEIGHT // 2)
        self.setGeometry(self.CENTER_X, self.CENTER_Y, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        
        self.CENTRAL_WIDGET = widgets.QWidget(parent = self)
        self.CENTRAL_WIDGET.setFixedSize(core.QSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.CENTRAL_WIDGET_LAYOUT = widgets.QVBoxLayout()
        self.CENTRAL_WIDGET_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.CENTRAL_WIDGET_LAYOUT.setSpacing(0)
        self.CENTRAL_WIDGET.setLayout(self.CENTRAL_WIDGET_LAYOUT)
        self.TITLE_BAR = Title_bar(self.CENTRAL_WIDGET, width = self.WINDOW_WIDTH)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.TITLE_BAR)
        

        self.CONTENT_FRAME_LAYOUT = widgets.QHBoxLayout()
        self.CONTENT_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        self.CONTENT_FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.content_frame = Frame_create(layout= self.CONTENT_FRAME_LAYOUT)
        # для того, что бы фон применялся не глобально
        self.content_frame.setObjectName("CONTENT_FRAME")
        self.content_frame.setLayout(self.CONTENT_FRAME_LAYOUT)
        path = os.path.abspath(os.path.join(__file__, "..", "..", "media", "light_mode.png"))
        self.content_frame.setStyleSheet(f"""
                                        #CONTENT_FRAME {{
                                        background-image: url({path});
                                        }}""")
        
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.content_frame)
        
        self.LEFT_FRAME_LAYOUT = widgets.QVBoxLayout()
        left_frame = Frame_create(layout= self.LEFT_FRAME_LAYOUT, width=370, height= 800)
        self.LAYOUT_RIGHT_FRAME = widgets.QVBoxLayout()
        self.RIGHT_FRAME = Frame_create(self.LAYOUT_RIGHT_FRAME, 828, 800)
        self.CONTENT_FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0)
        left_frame.setLayout(self.LEFT_FRAME_LAYOUT)
        left_frame.setStyleSheet("background-color: rgba(0, 0, 0, 51)")
        self.CONTENT_FRAME_LAYOUT.addWidget(left_frame)
        self.CONTENT_FRAME_LAYOUT.addWidget(self.RIGHT_FRAME)
        self.LEFT_FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0)

        self.FRAME_BUTTON_LAYOUT = widgets.QVBoxLayout()
        self.FRAME_BUTTON_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignRight)
        frame_for_button = Frame_create(layout= self.FRAME_BUTTON_LAYOUT, width=330, height=44)
        frame_for_button.setStyleSheet("background-color: transparent")
        self.DARK_MODE_BUTTON = widgets.QPushButton(parent=frame_for_button)
        self.DARK_MODE_BUTTON.setFixedSize(52, 24)
        self.DARK_MODE_BUTTON.setObjectName("BUTTON")
        self.path_btn = os.path.abspath(os.path.join(__file__, "..", "..", "media", "light_btn.png"))
        self.icon = gui.QIcon(self.path_btn)
        self.DARK_MODE_BUTTON.setIconSize(core.QSize(52, 24))
        self.FLAF_SWITCH = True
        def button_dark_pressed():
            self.FLAF_SWITCH = not self.FLAF_SWITCH
            if self.FLAF_SWITCH:
                self.path_btn = os.path.abspath(os.path.join(__file__, "..", "..", "media", "light_btn.png"))
                path_mode = os.path.abspath(os.path.join(__file__, "..", "..", "media", "light_mode.png"))
            else:
                self.path_btn = gui.QIcon(os.path.abspath(os.path.join(__file__, "..", "..", "media", "dark_btn.png")))
                path_mode = os.path.abspath(os.path.join(__file__, "..", "..", "media", "dark_mode.png"))
            self.content_frame.setStyleSheet(f"""
                                    #CONTENT_FRAME {{
                                    background-image: url({path_mode});
                                    }}""")
            self.icon = gui.QIcon(self.path_btn)
            self.DARK_MODE_BUTTON.setIcon(self.icon)

        self.DARK_MODE_BUTTON.setIcon(self.icon)
        self.FRAME_BUTTON_LAYOUT.addWidget(self.DARK_MODE_BUTTON)
        self.DARK_MODE_BUTTON.setStyleSheet("border-radius: 20px; background-color: transparent") 
        self.DARK_MODE_BUTTON.clicked.connect(button_dark_pressed)
        self.LEFT_FRAME_LAYOUT.addWidget(frame_for_button)

        scroll_area = Scroll_frame(left_frame, self.LAYOUT_RIGHT_FRAME, self.LAYOUT_RIGHT_FRAME)
        
        # MAIN_WEATHER = MainInfoWeather(self.LAYOUT_RIGHT_FRAME)
        self.LEFT_FRAME_LAYOUT.addWidget(scroll_area)
        # graphic = Graphic(self.LAYOUT_RIGHT_FRAME)


main_window = MainWindow(window_width = 1200, window_height = 800)
