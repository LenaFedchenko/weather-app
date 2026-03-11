import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import json, os
from .frame import Frame_create
from utils import api_request_func
from .load_img import ImageLoad

class Graphic:
    def __init__(self, content_frame, name_city):
        self.FRAME_LAYOUT = widgets.QVBoxLayout()
        self.frame = Frame_create(self.FRAME_LAYOUT, color="transparent",  width=799, height= 197)
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0, 51); border-radius: 10px")
        content_frame.addWidget(self.frame)
        self.LAYOUT_LAYOUT = widgets.QVBoxLayout()
        frame_labl = Frame_create(layout = self.LAYOUT_LAYOUT, color = "transparent", width = 730, height = 24)
        # self.FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.FRAME_LAYOUT.addWidget(frame_labl)
        FRAME1_LAYOUT = widgets.QHBoxLayout()
        FRAME1_LAYOUT.setContentsMargins(0, 0, 0, 0)
        FRAME1_LAYOUT.setSpacing(0)
        frame1 = Frame_create(layout= FRAME1_LAYOUT, color="transparent", width=730, height= 34)
        for i in range(11):
            IMAGE = ImageLoad(16, 16, frame1, 'example.png')
            FRAME1_LAYOUT.addWidget(IMAGE)
        self.FRAME_LAYOUT.addWidget(frame1)

        self.LABEL = widgets.QLabel(text = "Прогноз на 12 годин", parent=frame_labl)
        self.LABEL.setStyleSheet('font-size: 16px')
        self.LABEL.setFixedWidth(200)
        self.FRAME2_LAYOUT = widgets.QHBoxLayout()
        self.FRAME2_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.FRAME2_LAYOUT.setSpacing(10)
        self.FRAME2_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        frame2 = Frame_create(self.FRAME2_LAYOUT)
        frame2.setObjectName("CONTENT")
        path_img = os.path.abspath(os.path.join(__file__, "..", "..", "media", "graphic.png"))
        frame2.setStyleSheet(f'''
                            #CONTENT{{
                                background-image: url({path_img});
                                background-color:transparent
                            
                            }}''')
        frame2.setFixedWidth(730)
        self.FRAME_LAYOUT.addWidget(frame2)
        
        self.TEMPERATURE_GRAPH_FRAME_LAYOUT = widgets.QHBoxLayout()
        self.TEMPERATURE_GRAPH_FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.TEMPERATURE_GRAPH_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignBottom)
        temperature_graph_frame = Frame_create(layout=self.TEMPERATURE_GRAPH_FRAME_LAYOUT, width= None, height=None, color="transparent")
        temperature_graph_frame.setMaximumSize(727, 136)
        
        self.FRAME2_LAYOUT.addWidget(temperature_graph_frame)
        data_dict = api_request_func(name_city)
        list_temp = []
        for hour_data in data_dict["list"]:
            # if int(hour_data["main"]["temp"]) not in list_temp:
            list_temp.append(int(hour_data["main"]["temp"]))
            temperature = int(hour_data["main"]["temp"])
            
            height = 0
            
            base_height = 70
            scale = 2
            height = base_height + (temperature * scale)
            height = max(height, 20)
            height = max(height, 60)
            self.COLUMN = widgets.QFrame(temperature_graph_frame)
            self.COLUMN.setFixedSize(core.QSize(8, height))
            self.COLUMN.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 #FFDF56, stop:1 #87CEFA);")
            self.TEMPERATURE_GRAPH_FRAME_LAYOUT.addWidget(self.COLUMN, alignment = core.Qt.AlignmentFlag.AlignBottom)
        self.LAYOUT_VERTICAL = widgets.QVBoxLayout()
        frame_temp = Frame_create(layout=self.LAYOUT_VERTICAL, color="transparent", width=50, height=146)
        self.LAYOUT_VERTICAL.setContentsMargins(0, 0, 0, 15)
        self.LAYOUT_VERTICAL.setSpacing(0)
        list_temp.sort(reverse= True)
        new_list_temp = []
        for i in list_temp:
            if i not in new_list_temp:
                new_list_temp.append(i)
        a = 0
        for i in new_list_temp:
            a +=1
            if a >=8: 
                break
            label = widgets.QLabel(f'{i}°')
            label.setStyleSheet("font-size: 12px; color: white;")
            label.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
            # label.setFixedHeight(label_height)
            self.LAYOUT_VERTICAL.addWidget(label, alignment=core.Qt.AlignmentFlag.AlignHCenter)


        self.FRAME2_LAYOUT.addWidget(frame_temp, alignment=core.Qt.AlignmentFlag.AlignBottom)
                
    def delete_graphic(self):
        self.frame.setParent(None)