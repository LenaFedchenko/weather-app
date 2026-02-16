import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import json
from .frame import Frame_create
from utils import api_request_func

class Graphic:
        def __init__(self, content_frame):
            self.FRAME_LAYOUT = widgets.QVBoxLayout()
            frame = Frame_create(self.FRAME_LAYOUT, color= "red", width=799, height= 197)
            content_frame.addWidget(frame)

            self.FRAME1_LAYOUT = widgets.QHBoxLayout()
            frame1 = Frame_create(layout= self.FRAME1_LAYOUT, color="green", width=730, height= 24)
            self.FRAME_LAYOUT.addWidget(frame1)

            self.FRAME2_LAYOUT = widgets.QHBoxLayout()
            self.FRAME2_LAYOUT.setContentsMargins(0, 0, 0, 0)
            self.FRAME2_LAYOUT.setSpacing(10)
            self.FRAME2_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
            frame2 = Frame_create(self.FRAME2_LAYOUT, color= "blue")
            frame2.setFixedWidth(730)
            self.FRAME_LAYOUT.addWidget(frame2)
            
            self.TEMPERATURE_GRAPH_FRAME_LAYOUT = widgets.QHBoxLayout()
            self.TEMPERATURE_GRAPH_FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0)
            self.TEMPERATURE_GRAPH_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignBottom)
            temperature_graph_frame = Frame_create(layout=self.TEMPERATURE_GRAPH_FRAME_LAYOUT, width= None, height=None)
            temperature_graph_frame.setMaximumSize(727, 136)
            
            self.FRAME2_LAYOUT.addWidget(temperature_graph_frame)
            data_dict = api_request_func("Miami")
            for hour_data in data_dict["list"]:
                temperature = int(hour_data["main"]["temp"])
                
                height = 0
                
                if temperature < 0 :
                    height = (temperature * -2)  + 30
                elif temperature == 0:
                    height = 30
                else:
                    height = temperature * 2 
                
                self.COLUMN = widgets.QFrame(temperature_graph_frame)
                self.COLUMN.setFixedSize(core.QSize(8, height))
                self.COLUMN.setStyleSheet("background-color: gray; ")
                self.TEMPERATURE_GRAPH_FRAME_LAYOUT.addWidget(self.COLUMN, alignment = core.Qt.AlignmentFlag.AlignBottom)
