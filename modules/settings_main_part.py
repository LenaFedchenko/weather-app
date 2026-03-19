import PyQt6.QtWidgets as widgets
import PyQt6.QtCore as core
from .frame import Frame_create


class Main_part_settings:
    def __init__(self, parent_frame):
        self.FRAME_MAIN_LAUYT = widgets.QHBoxLayout()
        self.frame_main = Frame_create(layout = self.FRAME_MAIN_LAUYT, width = 742, height = 578, color = "red")
        parent_frame.addWidget(self.frame_main)
        self.BUTTONS_FRAME_LAYOUT = widgets.QVBoxLayout()
        self.BUTTONS_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.BUTTONS_FRAME = Frame_create(layout = self.BUTTONS_FRAME_LAYOUT, width = 174, height = 578, color = 'green')
        self.FRAME_MAIN_LAUYT.addWidget(self.BUTTONS_FRAME)


        self.search_city = widgets.QPushButton(text = "Пошук міста")
        self.search_city.clicked.connect(self.search_city_pressed)
        self.size_app = widgets.QPushButton(text = "Розмір додатку")
        self.size_app.clicked.connect(self.size_app_pressed)
        self.APP_LANGUAGE = widgets.QPushButton(text = "Мова додатку")
        self.APP_LANGUAGE.clicked.connect(self.app_language_pressed)
        self.IMAGE_LIST = widgets.QPushButton(text = "Списки зображень")
        self.IMAGE_LIST.clicked.connect(self.image_list_pressed)

        self.search_city.setStyleSheet('text-align: left;')
        self.size_app.setStyleSheet('text-align: left;')
        self.APP_LANGUAGE.setStyleSheet('text-align: left;')
        self.IMAGE_LIST.setStyleSheet('text-align: left;')

        self.search_city.setFixedSize(158, 35)
        self.size_app.setFixedSize(158, 35)
        self.APP_LANGUAGE.setFixedSize(158, 35)
        self.IMAGE_LIST.setFixedSize(158, 35)

        self.BUTTONS_FRAME_LAYOUT.addWidget(self.search_city)
        self.BUTTONS_FRAME_LAYOUT.addWidget(self.size_app)
        self.BUTTONS_FRAME_LAYOUT.addWidget(self.APP_LANGUAGE)
        self.BUTTONS_FRAME_LAYOUT.addWidget(self.IMAGE_LIST)
        
        

    def clear(self):
        self.SIZE_APP.setParent(None)
    def search_city_pressed(self):
        self.clear()
        self.SEARCH_CITY = Frame_create(layout = widgets.QVBoxLayout(), width = 544, height = 578, color = 'pink')
        self.FRAME_MAIN_LAUYT.addWidget(self.SEARCH_CITY)
    def size_app_pressed(self):
        self.SIZE_APP = Frame_create(layout = widgets.QVBoxLayout(), width = 544, height = 578, color = 'yellow')
        self.FRAME_MAIN_LAUYT.addWidget(self.SIZE_APP)
    def app_language_pressed(self):
        self.LANGUAGE = Frame_create(layout = widgets.QVBoxLayout(), width = 544, height = 578, color = 'red')
        self.FRAME_MAIN_LAUYT.addWidget(self.LANGUAGE)
    def image_list_pressed(self):
        self.FRAME_IMAGE = Frame_create(layout = widgets.QVBoxLayout(), width = 544, height = 578, color = 'blue')
        self.FRAME_MAIN_LAUYT.addWidget(self.FRAME_IMAGE)
    
