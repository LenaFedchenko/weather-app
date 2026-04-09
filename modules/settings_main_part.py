import PyQt6.QtWidgets as widgets
import PyQt6.QtCore as core
from .frame import Frame_create
from .info_from_api import info_country, info_city_from_coutry, info_geo
import PyQt6.QtWebEngineWidgets as webengine
import folium, io, json, os
import PyQt6.QtCore as core
import PyQt6.QtGui as gui


class Main_part_settings(widgets.QFrame):
    def __init__(self, parent_frame):
        super().__init__()
        self.FRAME_MAIN_LAUYT = widgets.QHBoxLayout()
        self.FRAME_MAIN_LAUYT.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        self.setLayout(self.FRAME_MAIN_LAUYT)
        self.setFixedSize(820, 578)
        self.setStyleSheet("background-color: transparent")
        parent_frame.addWidget(self)
        self.BUTTONS_FRAME_LAYOUT = widgets.QHBoxLayout()
        self.BUTTONS_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.BUTTONS_FRAME = Frame_create(layout = self.BUTTONS_FRAME_LAYOUT, width = 194, height = 578)
        self.BUTTONS_FRAME.setStyleSheet("border-radius:0px; background-color: transparent")
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

        self.LAYOUT_TOG_BTNS = widgets.QVBoxLayout()
        self.TOG_BTNS = Frame_create(self.LAYOUT_TOG_BTNS, 160, 145, "transparent")
        self.LAYOUT_TOG_BTNS.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.BUTTONS_FRAME_LAYOUT.setContentsMargins(0,0,0, 400)
        self.line = Frame_create(widgets.QVBoxLayout(), 2, 578, "white")
        self.LAYOUT_TOG_BTNS.addWidget(self.search_city)
        self.LAYOUT_TOG_BTNS.addWidget(self.size_app)
        self.LAYOUT_TOG_BTNS.addWidget(self.APP_LANGUAGE)
        self.LAYOUT_TOG_BTNS.addWidget(self.IMAGE_LIST)
        self.BUTTONS_FRAME_LAYOUT.addWidget(self.TOG_BTNS)
        self.BUTTONS_FRAME_LAYOUT.addWidget(self.line)
        self.SEARCH_CITY = ""
        self.LANGUAGE= ""
        self.FRAME_IMAGE= ""
        self.SIZE_APP = ""
        self.WEB_VIEW = webengine.QWebEngineView()
        self.WEB_VIEW.setFixedSize(core.QSize(289, 276))
        
    def button_function(self, text):
        self.selected_country = text
        self.info_city_from_country = info_city_from_coutry(self.selected_country)
        self.box_city.clear()
        for city in self.info_city_from_country:
            self.box_city.addItem(city)
    
    def geo(self):
        self.selected_city = self.box_city.currentText()
        try:
            x, y = info_geo(self.selected_city)
            self.info_selected_city_x = x
            self.info_selected_city_y = y
            self.LABEL_BC1.setText(f"(WGS {x} {y}, UTM, MGRS)")
            self.map_layout.addWidget(self.WEB_VIEW)
            self.SEARCH_MAP = folium.Map(location=(self.info_selected_city_x, self.info_selected_city_y))
            data = io.BytesIO()
            self.SEARCH_MAP.save(data, False)
            data_value = data.getvalue()
            self.WEB_VIEW.setHtml(data_value.decode())
        except Exception as error:
            print(error)
            self.LABEL_BC1.setText("(помилка)")
    def search_city_pressed(self):
        self.list_country = info_country()
        
        self.del_prev_card(self.SEARCH_CITY)
        # self.search_city.setStyleSheet("background-color: rgba(0, 0, 0, 100); border-radius: 5px")
        self.search_layout = widgets.QVBoxLayout()
        self.SEARCH_CITY = Frame_create(layout = self.search_layout, width = 554, height = 588, color = 'transparent')
        self.FRAME_MAIN_LAUYT.addWidget(self.SEARCH_CITY)
        
        self.search_city_layout = widgets.QHBoxLayout()
        self.search_city = Frame_create(self.search_city_layout, 544, 331, "transparent")

        self.added_cities_layout = widgets.QVBoxLayout()
        self.added_cities = Frame_create(self.added_cities_layout, 524, 197, "pink")
        self.added_cities.setStyleSheet("border-radius: 0px; ")
        self.ADDED_TEXT_CITY = widgets.QLabel("Додані міста")
        self.ADDED_TEXT_CITY.setStyleSheet("font-size: 18px; font-weight: 400")
        self.added_cities_layout.addWidget(self.ADDED_TEXT_CITY)
        self.scroll_widget = widgets.QScrollArea(parent= self.added_cities)
        self.scroll_widget.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_widget.setFixedSize(544, 160)
        self.scroll_widget.setStyleSheet("border-radius: 0px; background-color: rgba(0, 0, 0, 51)")
        self.scroll_widget.setWidgetResizable(True)
        self.added_cities_layout.addWidget(self.scroll_widget)
        self.SCROLL_FRAME = widgets.QFrame()
        self.SCROLL_FRAME_LAYOUT = widgets.QVBoxLayout()
        self.SCROLL_FRAME_LAYOUT.setSpacing(0)
        self.SCROLL_FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.SCROLL_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.SCROLL_FRAME.setLayout(self.SCROLL_FRAME_LAYOUT)
        self.scroll_widget.setWidget(self.SCROLL_FRAME)
        self.path_json = os.path.abspath(os.path.join(__file__, "..", "..", "static", "json", "countries.json"))
        with open(self.path_json, "r", encoding="utf-8") as file:
            self.data = json.load(file)
        for city in self.data:
            LAYOYT_CITY_ADDED = widgets.QHBoxLayout()
            city_added = Frame_create(layout = LAYOYT_CITY_ADDED, width = 512, height = 42)
            city_added.setStyleSheet("font-size: 14px; font-weight: 400; background-color: transparent")
            self.SCROLL_FRAME_LAYOUT.addWidget(city_added)
            LABEL_CITY_NAME = widgets.QLabel(f"{city}")
            LABEL_CITY_NAME.setStyleSheet("background-color: transparent; border-radius: 0px;")
            BUTTON_DELETE = widgets.QPushButton()
            self.path_img2 = os.path.abspath(os.path.join(__file__, "..", "..", "media", "trash.png"))
            self.ICON_BUTTON2 = gui.QIcon(self.path_img2)
            BUTTON_DELETE.clicked.connect(
                        # Значение берется в момент создания лямбды, а не при клике
                lambda _, text=LABEL_CITY_NAME.text(), widget=city_added: self.delete(text, widget)
            )
            BUTTON_DELETE.setIcon(self.ICON_BUTTON2)
            BUTTON_DELETE.setFixedSize(20, 20)
            LAYOYT_CITY_ADDED.addWidget(LABEL_CITY_NAME)
            LAYOYT_CITY_ADDED.addStretch()
            LAYOYT_CITY_ADDED.addWidget(BUTTON_DELETE)
        
        self.data_city_layout = widgets.QVBoxLayout()
        self.data_city_layout.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        self.data_city = Frame_create(self.data_city_layout, 239, 301, "transparent")

        # Пошук міста
        self.LABEL = widgets.QLabel("Пошук міста")

        self.map_layout = widgets.QVBoxLayout()
        self.map = Frame_create(self.map_layout, 290, 301, "transparent")

        self.block_inputs_layout = widgets.QVBoxLayout()
        self.block_inputs = Frame_create(self.block_inputs_layout, 249, 194, "transparent")

        self.LABEL_COUNTRY = widgets.QLabel("Країна")
        self.box_countre = widgets.QComboBox(parent = self.data_city)
        self.box_countre.setStyleSheet("background-color: white; color: black; border-radius: 4px")
        self.box_countre.setFixedSize(229, 32)
        for country in self.list_country:
            # print(country)
            self.box_countre.addItem(country)
        
        self.box_countre.currentTextChanged.connect(self.button_function)
        # выбранная страна
        self.selected_country = self.box_countre.currentText()
        self.info_city_from_country = info_city_from_coutry(self.selected_country)
        
        self.LABEL_CITY = widgets.QLabel("Місто")
        self.box_city = widgets.QComboBox(parent = self.data_city)
        self.box_city.setStyleSheet("background-color: white; color: black; border-radius: 4px")
        self.box_city.setFixedSize(209, 32)

        for city in self.info_city_from_country:
            self.box_city.addItem(city)
        self.box_city.setFixedSize(229, 32)
        self.box_city.currentTextChanged.connect(self.geo)
        self.selected_city = self.box_city.currentText()

        # self.info_selected_city_x, self.info_selected_city_y = info_geo(self.selected_city)
        self.LABEL_COORDINATE = widgets.QLabel("Кординати")
        self.box_coordinate_layout = widgets.QVBoxLayout()
        self.box_coordinate = Frame_create(layout = self.box_coordinate_layout, width = 239, height = 32)
        self.box_coordinate.setStyleSheet("background-color: white; border-radius: 4px")

        self.LABEL_BC1 = widgets.QLabel("(немає даних)", self.box_coordinate)
        self.LABEL_BC1.setStyleSheet('color: black; font-size: 10px')
        self.box_coordinate_layout.addWidget(self.LABEL_BC1)
        try:
            x, y = info_geo(self.selected_city)
            self.info_selected_city_x = x
            self.info_selected_city_y = y
            self.LABEL_BC1.setText(f"(WGS {x} {y}, UTM, MGRS)")
            self.map_layout.addWidget(self.WEB_VIEW)
            self.SEARCH_MAP = folium.Map(location=(self.info_selected_city_x, self.info_selected_city_y))
            data = io.BytesIO()
            self.SEARCH_MAP.save(data, False)
            data_value = data.getvalue()
            self.WEB_VIEW.setHtml(data_value.decode())
        except Exception as error:
            print(error)
            self.LABEL_BC1.setText("(помилка)")

        self.SAVE_BUTTON = widgets.QPushButton("Зберегти")
        self.SAVE_BUTTON.clicked.connect(self.add_city)
        self.SAVE_BUTTON.setFixedSize(105, 38)
        self.SAVE_BUTTON.setStyleSheet(""" 
                                        QPushButton {
                                            background-color: rgb(0, 0, 51);
                                            color: white;
                                            border-radius: 4px;
                                        }
                                        QPushButton:hover {
                                            background-color: rgb(0, 0, 80);
                                        }
                                        """)

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
        self.del_prev_card(self.SIZE_APP)
        self.SIZE_APP = Frame_create(layout = widgets.QVBoxLayout(), width = 544, height = 578, color = 'yellow')
        self.FRAME_MAIN_LAUYT.addWidget(self.SIZE_APP)
    def app_language_pressed(self):
        self.del_prev_card(self.LANGUAGE)
        self.LANGUAGE = Frame_create(layout = widgets.QVBoxLayout(), width = 544, height = 578, color = 'red')
        self.FRAME_MAIN_LAUYT.addWidget(self.LANGUAGE)
    def image_list_pressed(self):
        self.del_prev_card(self.FRAME_IMAGE)
        self.FRAME_IMAGE = Frame_create(layout = widgets.QVBoxLayout(), width = 544, height = 578, color = 'blue')
        self.FRAME_MAIN_LAUYT.addWidget(self.FRAME_IMAGE)


    def del_prev_card(self, name_card):
        list_cards = [(self.SEARCH_CITY, self.search_city), (self.LANGUAGE, self.APP_LANGUAGE), (self.FRAME_IMAGE, self.IMAGE_LIST), (self.SIZE_APP, self.size_app)]
        for card, btn in list_cards:
            # if card != "":
            if card != "" and name_card != card:
                card.setParent(None)
                btn.setStyleSheet('text-align: left; background-color: transparent')
            if name_card == card:
                btn.setStyleSheet("background-color: rgba(0, 0, 0, 100); border-radius: 5px")
    def delete(self, text, widget):
        widget.setParent(None)

        with open(self.path_json, "r", encoding="utf-8") as file:
            self.data = json.load(file)
        for city in self.data:
            if city == text:
                # print("lllll")
                self.data.remove(city)
        with open(self.path_json, "w") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def add_city(self):
        with open(self.path_json, "r", encoding="utf-8") as file:
            self.data = json.load(file)
        if self.selected_city not in self.data:
            self.data.append(self.selected_city)
        with open(self.path_json, "w") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)
        # добавление одного города в конец
        LAYOYT_CITY_ADDED = widgets.QHBoxLayout()
        city_added = Frame_create(layout = LAYOYT_CITY_ADDED, width = 512, height = 42)
        city_added.setStyleSheet("font-size: 14px; font-weight: 400; background-color: transparent")
        self.SCROLL_FRAME_LAYOUT.addWidget(city_added)
        LABEL_CITY_NAME = widgets.QLabel(f"{self.selected_city}")
        LABEL_CITY_NAME.setStyleSheet("background-color: transparent; border-radius: 0px;")
        BUTTON_DELETE = widgets.QPushButton()
        self.path_img2 = os.path.abspath(os.path.join(__file__, "..", "..", "media", "trash.png"))
        self.ICON_BUTTON2 = gui.QIcon(self.path_img2)
        BUTTON_DELETE.clicked.connect(
                    # Значение берется в момент создания лямбды, а не при клике
            lambda _, text=LABEL_CITY_NAME.text(): self.delete(text)
        )
        BUTTON_DELETE.setIcon(self.ICON_BUTTON2)
        BUTTON_DELETE.setFixedSize(20, 20)
        LAYOYT_CITY_ADDED.addWidget(LABEL_CITY_NAME)
        LAYOYT_CITY_ADDED.addStretch()
        LAYOYT_CITY_ADDED.addWidget(BUTTON_DELETE)