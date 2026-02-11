import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import os

from .app import app_obj
from .title_bar import Title_bar
from utils import api_request
from .scroll_frame import Scroll_frame
from .load_img import ImageLoad

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
        
        self.CONTENT_FRAME = widgets.QFrame(self.CENTRAL_WIDGET)
        self.CONTENT_FRAME_LAYOUT = widgets.QHBoxLayout()
        self.CONTENT_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        # для того, что бы фон применялся не глобально
        self.CONTENT_FRAME.setObjectName("CONTENT_FRAME")
        self.CONTENT_FRAME.setLayout(self.CONTENT_FRAME_LAYOUT)
        path = os.path.abspath(os.path.join(__file__, "..", "..", "media", "bg_color.png"))
        self.CONTENT_FRAME.setStyleSheet(f"""
                                        #CONTENT_FRAME {{
                                        background-image: url({path});
                                        }}""")
        
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.CONTENT_FRAME)
        scroll_area = Scroll_frame(parent= self.CONTENT_FRAME)
        
        self.CONTENT_FRAME_LAYOUT.addWidget(scroll_area)
        
        self.FRAME = widgets.QFrame(parent = self.CONTENT_FRAME)
        self.FRAME.setStyleSheet("background-color: red; ")
        self.FRAME.setFixedSize(788, 197)
        
        self.FRAME_LAYOUT = widgets.QVBoxLayout()
        self.FRAME.setLayout(self.FRAME_LAYOUT)
        
        self.CONTENT_FRAME_LAYOUT.addWidget(self.FRAME)
        
        self.FRAME1 = widgets.QFrame(parent = self.FRAME)
        self.FRAME1.setStyleSheet("background-color: green; ")
        self.FRAME1.setFixedSize(730, 24)
        
        self.FRAME1_LAYOUT = widgets.QHBoxLayout()
        self.FRAME1.setLayout(self.FRAME1_LAYOUT)
        
        self.FRAME_LAYOUT.addWidget(self.FRAME1)
        
        self.FRAME2 = widgets.QFrame(parent = self.FRAME)
        self.FRAME2.setStyleSheet("background-color: blue; ")
        self.FRAME2.setFixedWidth(730)
        
        self.FRAME2_LAYOUT = widgets.QHBoxLayout()
        self.FRAME2_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.FRAME2_LAYOUT.setSpacing(10)
        self.FRAME2_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        self.FRAME2.setLayout(self.FRAME2_LAYOUT)
        
        self.FRAME_LAYOUT.addWidget(self.FRAME2)
        
        self.TEMPERATURE_GRAPH_FRAME = widgets.QFrame(parent = self.FRAME2)
        self.TEMPERATURE_GRAPH_FRAME.setMaximumSize(727, 136)
        
        self.TEMPERATURE_GRAPH_FRAME_LAYOUT = widgets.QHBoxLayout()
        self.TEMPERATURE_GRAPH_FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.TEMPERATURE_GRAPH_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignBottom)
        self.TEMPERATURE_GRAPH_FRAME.setLayout(self.TEMPERATURE_GRAPH_FRAME_LAYOUT)
        
        self.FRAME2_LAYOUT.addWidget(self.TEMPERATURE_GRAPH_FRAME)
        
        data_dict = api_request("Miami")
        for hour_data in data_dict["list"]:
            temperature = int(hour_data["main"]["temp"])
            
            height = 0
            
            if temperature < 0 :
                height = (temperature * -2)  + 30
            elif temperature == 0:
                height = 30
            else:
                height = temperature * 2 
            
            self.COLUMN = widgets.QFrame(self.TEMPERATURE_GRAPH_FRAME)
            self.COLUMN.setFixedSize(core.QSize(8, height))
            self.COLUMN.setStyleSheet("background-color: gray; ")
            self.TEMPERATURE_GRAPH_FRAME_LAYOUT.addWidget(self.COLUMN, alignment = core.Qt.AlignmentFlag.AlignBottom)


main_window = MainWindow(window_width = 1200, window_height = 800)
