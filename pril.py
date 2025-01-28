import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,QComboBox,QMainWindow, QMessageBox,QLineEdit,QVBoxLayout,QPushButton, QVBoxLayout, QLineEdit,QRadioButton,QButtonGroup)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Приложение")
        self.setGeometry(100,100,400,200)

        self.town = QComboBox()
        self.town.addItems(["Абакан","Москва"])
        self.town.currentTextChanged.connect(self.add_to_list)
        
        self.man = QRadioButton("man")
        self.woman = QRadioButton("woman")
        
        self.sex_group = QButtonGroup()
        self.sex_group.addButton(self.man)
        self.sex_group.addButton(self.woman)
        self.sex_group.buttonClicked.connect(self.Sex)
        
        self.tttt = QRadioButton("починить")
        self.womrrrrr = QRadioButton("починить")
        
        self.group = QButtonGroup()
        self.group.addButton(self.tttt)
        self.group.addButton(self.womrrrrr)
        self.group.buttonClicked.connect(self.add_to_list)

        self.familia = QLineEdit(self)
        self.familia.setPlaceholderText("Введите фамилию")
        self.familia.textChanged.connect(self.add_to_list)

        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Введите имя")
        self.name.textChanged.connect(self.add_to_list)

        self.otchestvo = QLineEdit(self)
        self.otchestvo.setPlaceholderText("Введите отчество")
        self.otchestvo.textChanged.connect(self.add_to_list)

        self.add_button = QPushButton("Добавить",self)

        self.add_button.clicked.connect(self.add_to_list)

        self.label = QLabel(self)

        self.info = QLabel("Выберите город:",self)

        layout = QVBoxLayout()
        layout.addWidget(self.familia)
        layout.addWidget(self.name)
        layout.addWidget(self.otchestvo)
        layout.addWidget(self.info)
        layout.addWidget(self.town)
        layout.addWidget(self.add_button)
        layout.addWidget(self.label)
        
        layout.addWidget(self.man)
        layout.addWidget(self.woman)
        layout.addWidget(self.tttt)
        layout.addWidget(self.womrrrrr)
        

        self.setLayout(layout)

    def add_to_list(self):
        textF = self.familia.text().strip()
        textN = self.name.text().strip()
        textO = self.otchestvo.text().strip()

        textT = self.town.currentText()
        
        #textS = self.sex_group.text().strip()
        
        self.label.setText(textT)

        # if textT == "Абакан":
        #     textT == "Абакан"
        # else: textT == "Москва"

        #if not textF or not textN or not textO:
            #QMessageBox.warning(self,"Внимание","Поле ввода не ждолжно быть пустым!")
            #return

        self.label.setText(f"Фамилия: {textF}\nИмя: {textN}\nОтчество: {textO}\nГород: {textT}")
    
    def Sex(self,button):
        self.label.setText(f"sex: {button.text()}")
        

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
