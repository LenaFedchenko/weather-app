import PyQt6.QtWidgets as widgets
from .frame import Frame_create
from .settings_main_part import Main_part_settings
import PyQt6.QtCore as core
import config

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
        if config.LANGUAGE == "uk":
            self.LABEL_SETTINGS = widgets.QLabel("Налаштування")
        else:
            self.LABEL_SETTINGS = widgets.QLabel("Settings")
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

    def update_language(self):
        # получаем текущую вкладку, что бы после обновления языка остаться на ней
        current_tab = self.main_part.CURRENT_TAB
        if config.LANGUAGE == "uk":
            self.LABEL_SETTINGS.setText("Налаштування")
        else:
            self.LABEL_SETTINGS.setText("Settings")

        self.main_part.setParent(None)
        self.main_part.deleteLater()
        self.main_part = Main_part_settings(self.CONTENT_LAYOUT)

        if current_tab == "search_city":
            self.main_part.search_city_pressed()
        elif current_tab == "size_app":
            self.main_part.size_app_pressed()
        elif current_tab == "app_language":
            self.main_part.app_language_pressed()
        elif current_tab == "image_list":
            self.main_part.image_list_pressed()
    
