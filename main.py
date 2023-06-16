from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QMainWindow
import design
import sys
from raschet import Calculation


class CalculationApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculation)

    def calculation(self):
        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "" or self.lineEdit_3.text() == "" or self.lineEdit_4.text() == "" or not self.lineEdit.text().isnumeric() or not self.lineEdit_2.text().isnumeric() or not self.lineEdit_3.text().isnumeric() or not self.lineEdit_4.text().isnumeric():
            self.label_12.setText("Введите все данные!")
        else:
            calc = Calculation(float(self.lineEdit.text()), float(self.lineEdit_2.text()), float(self.lineEdit_3.text()), float(self.lineEdit_4.text()))
            results = calc.calculate_R_mp_0()
            self.label_12.setText("Результаты")
            self.label_9.setText(str(results[0]))
            self.label_10.setText(str(results[1]))
            self.label_11.setText(str(results[2]))


def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = CalculationApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

