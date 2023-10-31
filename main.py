import sys
import csv
import sqlite3 as sql
import statistics as st

from UI.projectUI import Ui_mainWindow
from UI.helpUI import Ui_helpWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

WINDOW_SIZE = [500, 300]


class DataStatistics(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(*WINDOW_SIZE)
        self.helpBtn.clicked.connect(self.help_window)
        self.csvFileBtn.clicked.connect(self.btn_selector)
        self.txtFileBtn.clicked.connect(self.btn_selector)
        self.saveBtn.clicked.connect(self.save_table)

        self.csvInput.clicked.connect(self.get_data)
        self.txtInput.clicked.connect(self.get_data)

        self.btnSel = {self.csvFileBtn: self.csvInput,
                       self.txtFileBtn: self.txtInput}

        self.f_data = []

    def help_window(self):
        self.help = HelpWindow()
        self.help.show()

    def statistics_data(self, data):
        if data:
            return [round(st.fmean(data), 5),
                    min(data),
                    max(data),
                    max(data) - min(data),
                    st.median(data),
                    st.mode(data),
                    round(st.variance(data), 5)]
        else:
            return None

    def btn_selector(self):
        for i in self.btnSel:
            if self.sender() == i:
                self.btnSel[self.sender()].setEnabled(True)
            else:
                self.btnSel[i].setEnabled(False)

    def get_data(self):
        self.f_data = []
        if self.sender() == self.csvInput:
            self.file_name = QFileDialog.getOpenFileName(self, "Выберите файл", "",
                                                         "Таблица (*.csv)")[0]
            if self.file_name:
                with open(self.file_name, "r", encoding="utf8") as file:
                    reader = csv.DictReader(file, delimiter=";")
                    data = sorted(reader, key=lambda x: x["title"])
                    for i in data:
                        for j in i["data"].split(","):
                            self.f_data.append(float(j))
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Ошибка: нет файла")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
        elif self.sender() == self.txtInput:
            self.file_name = QFileDialog.getOpenFileName(self, "Выберите файл", "",
                                                         "Текстовый файл (*.txt)")[0]
            if self.file_name:
                with open(self.file_name, "r", encoding="utf8") as file:
                    data = file.read().split(";")
                    for i in data:
                        if i:
                            self.f_data.append(float(i))
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Ошибка: нет файла")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

    def save_table(self):
        data_table = self.statistics_data(self.f_data)
        if data_table:
            con = sql.connect(f"tables/{self.nameEdit.text()}.db")

            cur = con.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS statistics_data
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                'Путь до данных' TEXT, 
                'Среднее арифметическое' REAL, 
                'Минимум' REAL,
                'Максимум' REAL, 
                'Размах' REAL,
                'Медиана' REAL, 
                'Мода' REAL,
                'Дисперсия' REAL)""")

            # Вставка данных в таблицу
            cur.execute("""INSERT INTO statistics_data ('Путь до данных', 
                'Среднее арифметическое', 
                'Минимум',
                'Максимум',
                'Размах',
                'Медиана', 
                'Мода',
                'Дисперсия')
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                        (self.file_name, data_table[0], data_table[1], data_table[2], data_table[3],
                         data_table[4], data_table[5], data_table[6]))

            con.commit()
            con.close()
            msg = QMessageBox()
            msg.setWindowTitle("Успешно")
            msg.setText("Успех: данные сохранены")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Ошибка: нет данных")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()


class HelpWindow(QMainWindow, Ui_helpWindow):
    def __init__(self):
        super().__init__()
        self.move(1000, 300)
        self.setupUi(self)
        self.setFixedSize(*WINDOW_SIZE)


StyleSheet = '''
QMainWindow {
    background-color: rgb(115, 180, 205);
}
'''

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyleSheet(StyleSheet)

    ex = DataStatistics()
    ex.show()
    sys.exit(app.exec_())
