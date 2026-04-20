import PyQt6.QtWidgets as widgets
from .frame import Frame_create
from .settings_main_part import Main_part_settings
import PyQt6.QtCore as core

class Modal_settings(widgets.QWidget):
    def __init__(self, frame):
        widgets.QWidget.__init__(self)
        self.setParent(frame)
        MODAL_LAYOUT = widgets.QVBoxLayout()
        self.setLayout(MODAL_LAYOUT)
        # что б модалка не позрачная была
        self.setAttribute(core.Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f"border-radius: 16px; background-color: rgba(0, 0, 0, 150)")
        self.ITEM = 'Українська'
        self.setGeometry(
            (1200 // 2) - 400, 
            (800 // 2) - 350, 
            900, 
            700
        )
        self.HEADER_LAYOUT = widgets.QHBoxLayout()
        self.HEADER = Frame_create(layout = self.HEADER_LAYOUT, width = 860, height = 38, color="transparent")
        self.LABEL_SETTINGS = widgets.QLabel("Налаштування")
        self.LABEL_SETTINGS.setStyleSheet("background-color: transparent")
        self.CLOSE_BUTTON = widgets.QPushButton(text= "X")
        def close_modal():
            self.close()
        self.CLOSE_BUTTON.clicked.connect(close_modal)
        self.CLOSE_BUTTON.setFixedSize(24, 24)
        self.CLOSE_BUTTON.setStyleSheet("background-color: transparent")
        
        self.CONTENT_LAYOUT = widgets.QHBoxLayout()
        self.CONTENT_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.CONTENT_FRAME = Frame_create(layout = self.CONTENT_LAYOUT, width = 860, height = 600, color = "transparent")
        
        self.main_part = Main_part_settings(self.CONTENT_LAYOUT)
        # self.main_part.BUTTON_SAVE.clicked.connect(self.save)
        self.HEADER_LAYOUT.addWidget(self.LABEL_SETTINGS)
        self.HEADER_LAYOUT.addStretch()
        self.HEADER_LAYOUT.addWidget(self.CLOSE_BUTTON)
        MODAL_LAYOUT.addWidget(self.HEADER)
        MODAL_LAYOUT.addWidget(self.CONTENT_FRAME)
        self.show()
    def mousePressEvent(self, event):
        self.ITEM = self.main_part.ITEM
        self.update_language()
        # print(self.ITEM)
    def update_language(self):
        if self.main_part.ITEM == 'Українська':
            self.LABEL_SETTINGS.setText('Налаштування')
            self.main_part.BUTTON_SAVE.setText("Зберегти")
            self.main_part.LANGUAGE_LABEL.setText("Мова")
            self.main_part.ADDED_TEXT_CITY.setText("Додані міста")
            self.main_part.LABEL_CITY.setText("Міста")
            self.main_part.LABEL.setText("Пошук міста")
            self.main_part.LABEL_COUNTRY.setText("Країна")
            self.main_part.LABEL_COORDINATE.setText("Координати")
            self.main_part.LABEL_BC1.setText("(Немає даних)", self.main_part.box_coordinate)
            self.main_part.window_size_lable.setText("Оберіть розмір додатку")
            self.main_part.label_select.setText("Оберіть мову додатку")
            self.main_part.label_lauge.setText("Мова додатку")
            self.main_part.LABEL_LIST.setText("Списки зображень")
            self.main_part.LABEL_LIST2.setText("Список зображень №1")
            self.main_part.LABEL_LIST22.setText("Список зображень №2")
        else:
            self.LABEL_SETTINGS.setText('Settings')
            self.main_part.BUTTON_SAVE.setText("Save")
            self.main_part.LANGUAGE_LABEL.setText("Language")
            self.main_part.ADDED_TEXT_CITY.setText("Added cities")
            self.main_part.LABEL_CITY.setText("Cities")
            self.main_part.LABEL.setText("Search city")
            self.main_part.LABEL_COUNTRY.setText("Country")
            self.main_part.LABEL_COORDINATE.setText("Coordinates")
            self.main_part.LABEL_BC1.setText("(No data)", self.main_part.box_coordinate)
            self.main_part.window_size_lable.setText("Choose app size")
            self.main_part.label_select.setText("Choose app language")
            self.main_part.label_lauge.setText("App language")
            self.main_part.LABEL_LIST.setText("Image lists")
            self.main_part.LABEL_LIST2.setText("Image list №1")
            self.main_part.LABEL_LIST22.setText("Image list №2")
    # def save(self):
    #     print("cliked")
