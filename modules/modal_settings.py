import PyQt6.QtWidgets as widgets
from .frame import Frame_create
from .settings_main_part import Main_part_settings

class Modal_settings:
    def __init__(self, frame):
        self.MODAL = widgets.QWidget(parent = frame)
        MODAL_LAYOUT = widgets.QVBoxLayout()
        # MODAL_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        self.MODAL.setLayout(MODAL_LAYOUT)
        self.MODAL.setStyleSheet(f"border-radius: 16px; background-color: rgba(0, 0, 0, 100)")
        
        self.MODAL.setGeometry(
            (1200 // 2) - 326, 
            (800 // 2) - 350, 
            790, 
            688
        )
        self.HEADER_LAYOUT = widgets.QHBoxLayout()
        self.HEADER = Frame_create(layout = self.HEADER_LAYOUT, width = 742, height = 38, color="transparent")
        self.LABEL_SETTINGS = widgets.QLabel("Налаштування")
        self.LABEL_SETTINGS.setStyleSheet("background-color: transparent")
        self.CLOSE_BUTTON = widgets.QPushButton(text= "X")
        def close_modal():
            print("bbb")
            self.MODAL.close()
        self.CLOSE_BUTTON.clicked.connect(close_modal)
        self.CLOSE_BUTTON.setFixedSize(24, 24)
        self.CLOSE_BUTTON.setStyleSheet("background-color: transparent")
        
        self.CONTENT_LAYOUT = widgets.QHBoxLayout()
        self.CONTENT_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.CONTENT_FRAME = Frame_create(layout = self.CONTENT_LAYOUT, width = 742, height = 578, color = "transparent")
        
        main_part = Main_part_settings(self.CONTENT_LAYOUT)
        
        self.HEADER_LAYOUT.addWidget(self.LABEL_SETTINGS)
        self.HEADER_LAYOUT.addStretch()
        self.HEADER_LAYOUT.addWidget(self.CLOSE_BUTTON)
        MODAL_LAYOUT.addWidget(self.HEADER)
        MODAL_LAYOUT.addWidget(self.CONTENT_FRAME)
        self.MODAL.show()