import PyQt6.QtWidgets as widgets
import PyQt6.QtCore as core
from .frame import Frame_create


class Main_part_settings(widgets.QFrame):
    def __init__(self, parent_frame):
        super().__init__()
        self.FRAME_MAIN_LAUYT = widgets.QHBoxLayout()
        self.setLayout(self.FRAME_MAIN_LAUYT)
        self.setFixedSize(820, 578)
        self.setStyleSheet("background-color: transparent")
        parent_frame.addWidget(self)
        self.BUTTONS_FRAME_LAYOUT = widgets.QVBoxLayout()
        self.BUTTONS_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.BUTTONS_FRAME = Frame_create(layout = self.BUTTONS_FRAME_LAYOUT, width = 194, height = 578, color = 'green')
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
        
        

    def search_city_pressed(self):
        # try:
            # self.SIZE_APP.setParent(None)
            # self.LANGUAGE.setParent(None)
            # self.FRAME_IMAGE.setParent(None)
        # except:
            self.search_layout = widgets.QVBoxLayout()
            self.SEARCH_CITY = Frame_create(layout = self.search_layout, width = 554, height = 588, color = 'transparent')
            self.FRAME_MAIN_LAUYT.addWidget(self.SEARCH_CITY)
            
            self.search_city_layout = widgets.QHBoxLayout()
            self.search_city = Frame_create(self.search_city_layout, 544, 331, "transparent")
            
            self.added_cities_layout = widgets.QVBoxLayout()
            self.added_cities = Frame_create(self.added_cities_layout, 524, 197, "pink")

            
            self.data_city_layout = widgets.QVBoxLayout()
            self.data_city_layout.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
            self.data_city = Frame_create(self.data_city_layout, 239, 301, "transparent")

            # Пошук міста
            self.LABEL = widgets.QLabel("Пошук міста")

            self.map_layout = widgets.QVBoxLayout()
            self.map = Frame_create(self.map_layout, 290, 301, "yellow")

            self.block_inputs_layout = widgets.QVBoxLayout()
            self.block_inputs = Frame_create(self.block_inputs_layout, 239, 194, "transparent")

            self.LABEL_COUNTRY = widgets.QLabel("Країна")
            self.box_countre = widgets.QComboBox(parent = self.data_city)
            self.box_countre.setStyleSheet("background-color: white; color: black; border-radius: 4px")
            self.box_countre.setFixedSize(209, 32)
            self.box_countre.addItem("Італія")
            self.box_countre.addItem("Пункт2")
            self.box_countre.addItem("Пункт3")

            self.LABEL_CITY = widgets.QLabel("Місто")
            self.box_city = widgets.QComboBox(parent = self.data_city)
            self.box_city.setStyleSheet("background-color: white; color: black; border-radius: 4px")
            self.box_city.setFixedSize(209, 32)
            self.box_city.addItem("Виберіть місто")
            self.box_city.addItem("Пункт2")
            self.box_city.addItem("Пункт3")
            self.box_city.setFixedSize(229, 32)
            
            self.LABEL_COORDINATE = widgets.QLabel("Кординати")
            self.box_coordinate = widgets.QComboBox(parent = self.data_city)
            self.box_coordinate.setStyleSheet("background-color: white; color: black; border-radius: 4px")
            self.box_coordinate.setFixedSize(209, 32)
            self.box_coordinate.addItem("(WGS 84,UTM,MGRS)")
            self.box_coordinate.addItem("Пункт2")
            self.box_coordinate.addItem("Пункт3")
            self.box_coordinate.setFixedSize(229, 32)

            self.SAVE_BUTTON = widgets.QPushButton("Зберегти")
            self.SAVE_BUTTON.setFixedSize(105, 38)
            self.SAVE_BUTTON.setStyleSheet("background-color: rgb(0, 0, 51); color: white; border-radius: 4px")


            self.data_city_layout.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
            self.block_inputs_layout.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
            self.block_inputs_layout.addWidget(self.LABEL_COUNTRY, alignment=core.Qt.AlignmentFlag.AlignLeft)
            self.block_inputs_layout.addWidget(self.box_countre, alignment=core.Qt.AlignmentFlag.AlignLeft)

            self.block_inputs_layout.addWidget(self.LABEL_CITY, alignment=core.Qt.AlignmentFlag.AlignLeft)
            self.block_inputs_layout.addWidget(self.box_city, alignment=core.Qt.AlignmentFlag.AlignLeft)
            self.data_city_layout.setContentsMargins(5, 0, 0, 0)
            self.block_inputs_layout.setContentsMargins(5, 0, 0, 0)
            self.block_inputs_layout.addStretch()
            self.data_city_layout.addStretch()

            self.data_city_layout.addWidget(self.LABEL)
            self.data_city_layout.addWidget(self.block_inputs)

            self.block_inputs_layout.addWidget(self.LABEL_COUNTRY)
            self.block_inputs_layout.addWidget(self.box_countre)

            self.block_inputs_layout.addWidget(self.LABEL_CITY)
            self.block_inputs_layout.addWidget(self.box_city)

            self.block_inputs_layout.addWidget(self.LABEL_COORDINATE)
            self.block_inputs_layout.addWidget(self.box_coordinate)

            self.search_city_layout.addWidget(self.data_city)
            self.search_city_layout.addWidget(self.map)
            
            self.data_city_layout.addWidget(self.SAVE_BUTTON)

            self.search_layout.addWidget(self.search_city)
            self.search_layout.addWidget(self.added_cities)
            
    def size_app_pressed(self):
        # try:
            self.SEARCH_CITY.setParent(None)
            self.LANGUAGE.setParent(None)
            self.FRAME_IMAGE.setParent(None)
        # except:
            self.SIZE_APP = Frame_create(layout = widgets.QVBoxLayout(), width = 544, height = 578, color = 'yellow')
            self.FRAME_MAIN_LAUYT.addWidget(self.SIZE_APP)
        # self.SIZE_APP = Frame_create(layout = widgets.QVBoxLayout(), width = 544, height = 578, color = 'yellow')
        # self.FRAME_MAIN_LAUYT.addWidget(self.SIZE_APP)
    def app_language_pressed(self):
        # try:
            self.SEARCH_CITY.setParent(None)
            self.SIZE_APP.setParent(None)
            self.FRAME_IMAGE.setParent(None)
        # except:
            self.LANGUAGE = Frame_create(layout = widgets.QVBoxLayout(), width = 544, height = 578, color = 'red')
            self.FRAME_MAIN_LAUYT.addWidget(self.LANGUAGE)
        # self.LANGUAGE = Frame_create(layout = widgets.QVBoxLayout(), width = 544, height = 578, color = 'red')
        # self.FRAME_MAIN_LAUYT.addWidget(self.LANGUAGE)
    def image_list_pressed(self):
        # try:
            self.SIZE_APP.setParent(None)
            self.LANGUAGE.setParent(None)
            self.SEARCH_CITY.setParent(None)
        # except:
            self.FRAME_IMAGE = Frame_create(layout = widgets.QVBoxLayout(), width = 544, height = 578, color = 'blue')
            self.FRAME_MAIN_LAUYT.addWidget(self.FRAME_IMAGE)
        # self.FRAME_IMAGE = Frame_create(layout = widgets.QVBoxLayout(), width = 544, height = 578, color = 'blue')
        # self.FRAME_MAIN_LAUYT.addWidget(self.FRAME_IMAGE)

