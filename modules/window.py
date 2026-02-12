import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import os

from .app import app_obj
from .title_bar import Title_bar
from utils import api_request
from .scroll_frame import Scroll_frame
from .load_img import ImageLoad
from .graphic import Graphic
from .frame import Frame_create

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
        content_frame = Frame_create(layout= self.CONTENT_FRAME_LAYOUT)
        # для того, что бы фон применялся не глобально
        content_frame.setObjectName("CONTENT_FRAME")
        content_frame.setLayout(self.CONTENT_FRAME_LAYOUT)
        path = os.path.abspath(os.path.join(__file__, "..", "..", "media", "bg_color.png"))
        content_frame.setStyleSheet(f"""
                                        #CONTENT_FRAME {{
                                        background-image: url({path});
                                        }}""")
        
        self.CENTRAL_WIDGET_LAYOUT.addWidget(content_frame)

        self.LEFT_FRAME_LAYOUT = widgets.QVBoxLayout()
        left_frame = Frame_create(layout= self.LEFT_FRAME_LAYOUT, width=370, height= 800)
        left_frame.setLayout(self.LEFT_FRAME_LAYOUT)
        left_frame.setStyleSheet("background-color: rgba(0, 0, 0, 51)")
        scroll_area = Scroll_frame(left_frame)
        self.LEFT_FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.LEFT_FRAME_LAYOUT.addWidget(scroll_area)
        
        self.CONTENT_FRAME_LAYOUT.addWidget(left_frame)
        graphic = Graphic(self.CONTENT_FRAME_LAYOUT)


main_window = MainWindow(window_width = 1200, window_height = 800)
