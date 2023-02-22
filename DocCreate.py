import sys

from PyQt5.uic.properties import QtGui
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(800, 600)
        self.setWindowIcon(QIcon("resources/img/menubar/logo-main.png"))
        # Устанавливаем название окна
        self.setWindowTitle("CozyOffice DocCreate")
        # Создаем панель основного меню
        main_menu = self.menuBar()
        # Добавляем в него меню actions
        file_menu = main_menu.addMenu("File")
        edit_menu = main_menu.addMenu("Edit")
        preference_menu = main_menu.addMenu("Preferences")

        main_menu_font = main_menu.font()
        main_menu_font.setPointSize(15)

        # Добавляем действия в меню (иконку, название)
        newdoc = QAction(QIcon("resources/img/menubar/new-doc.png"), "New Document", self)
        opendoc = QAction(QIcon("resources/img/menubar/open-doc.png"), "Open Document", self)
        savedoc = QAction(QIcon("resources/img/menubar/save-doc.png"), "Save Document", self)
        # saveAction.setShortcut("Ctrl+S")
        file_menu.addAction(newdoc)
        file_menu.addAction(opendoc)
        file_menu.addAction(savedoc)

        undoedit = QAction(QIcon("resources/img/menubar/undo-edit.png"), "Undo action", self)
        redoedit = QAction(QIcon("resources/img/menubar/redo-edit.png"), "Redo action", self)
        historyedit = QAction(QIcon("resources/img/menubar/history-edit.png"), "View actions history", self)
        edit_menu.addAction(undoedit)
        edit_menu.addAction(redoedit)
        edit_menu.addAction(historyedit)

        preferences_pref = QAction(QIcon("resources/img/menubar/pref-pref.png"), "Preferences", self)
        about_pref = QAction(QIcon("resources/img/menubar/about-pref.png"), "About application", self)
        help_pref = QAction(QIcon("resources/img/menubar/help-pref.png"), "Help", self)
        preference_menu.addAction(preferences_pref)
        preference_menu.addAction(about_pref)
        preference_menu.addAction(help_pref)







        # Создаем панель для слайдера
        self.workspace = QToolBar(self)
        # Установили размеры иконки панели
        self.workspace.setIconSize(QSize(16, 16))
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.workspace)

        self.selcolorChooser = QComboBox()
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "Selection color...")
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "No selection")
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "White")
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "Black")
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "Gray")
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "Yellow")
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "Green")
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "Blue")
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "Red")
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "Pink")
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "Light gray")
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "Light yellow")
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "Light green")
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "Light blue")
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "Light red")
        self.selcolorChooser.addItem(QIcon("resources/img/toolbar/bucket.png"), "Light pink")
        self.workspace.addWidget(self.selcolorChooser)


        self.texcolorChooser = QComboBox()
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "Text color...")
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "No selection")
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "White")
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "Black")
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "Gray")
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "Yellow")
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "Green")
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "Blue")
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "Red")
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "Pink")
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "Light gray")
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "Light yellow")
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "Light green")
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "Light blue")
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "Light red")
        self.texcolorChooser.addItem(QIcon("resources/img/toolbar/brush.png"), "Light pink")
        self.workspace.addWidget(self.texcolorChooser)


        bold_icon = QIcon()
        bold_icon.addPixmap(QPixmap('resources/img/toolbar/font-bold.png'))
        self.boldButton = QPushButton()
        self.boldButton.setIcon(bold_icon)
        self.boldButton.setCheckable(True)
        self.workspace.addWidget(self.boldButton)


        under_icon = QIcon()
        under_icon.addPixmap(QPixmap('resources/img/toolbar/font-under.png'))
        self.underButton = QPushButton()
        self.underButton.setIcon(under_icon)
        self.underButton.setCheckable(True)
        self.workspace.addWidget(self.underButton)


        cursive_icon = QIcon()
        cursive_icon.addPixmap(QPixmap('resources/img/toolbar/font-cursive.png'))
        self.cursiveButton = QPushButton()
        self.cursiveButton.setIcon(cursive_icon)
        self.cursiveButton.setCheckable(True)
        self.workspace.addWidget(self.cursiveButton)







# Приложению нужен один (и только один) экземпляр QApplication.
# Передаем sys.argv, чтобы разрешить аргументы командной строки для приложения.
app = QApplication(sys.argv)

# Создаем экземпляр окна и отображаем его (по умолчанию он скрыт)
window = MainWindow()
window.show()

# Запускаем цикл событий
app.exec()