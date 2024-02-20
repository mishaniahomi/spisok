import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate

import main_design  # импортируем конвертируемый файл дизайна
from models import Employee  # импортируем класс сотрудника


Employee_list = []


class App(QtWidgets.QMainWindow, main_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()  # ссылаемся на родительский класс
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_4.clicked.connect(self.load_from_exel)
        self.pushButton_3.clicked.connect(self.add)
        self.pushButton.clicked.connect(self.save_to_exel)
        self.pushButton_2.clicked.connect(self.save_to_word)
        self.pushButton_5.clicked.connect(self.edit)
        self.pushButton_6.clicked.connect(self.delete)
        self.tableWidget.clicked.connect(self.onclick_table)

    def onclick_table(self):
        try:
            index = self.tableWidget.currentIndex()
            if index.row() != -1:
                self.lineEdit.setText(self.tableWidget.item(index.row(), 0).text())
                self.lineEdit_3.setText(self.tableWidget.item(index.row(), 1).text())
                self.lineEdit_2.setText(self.tableWidget.item(index.row(), 2).text())
                self.lineEdit_4.setText(self.tableWidget.item(index.row(), 3).text())
                self.lineEdit_5.setText(self.tableWidget.item(index.row(), 4).text())
                self.comboBox.setCurrentText(self.tableWidget.item(index.row(), 5).text())
            else:
                QtWidgets.QMessageBox.about(self, "Ошибка!", "Выберите данные!")
        except:
            e = sys.exc_info()[1]
            QtWidgets.QMessageBox.about(self, "Ошибка!", e.args[0])


    def refresh_table(self):  # Для обновления таблицы
        try:
            self.tableWidget.clear()
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setHorizontalHeaderLabels(['Фамилия', 'Имя', 'Отчество', 'Должность', 'Звание', 'Статус'])
            self.tableWidget.horizontalHeader().resizeSection(0, 400)
            global Employee_list
            self.tableWidget.setRowCount(len(Employee_list))
            for i in range(len(Employee_list)):
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(Employee_list[i].surname))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(Employee_list[i].name))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(Employee_list[i].patronymic))
                self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(Employee_list[i].position))
                self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(Employee_list[i].rank))
                self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(Employee_list[i].status))
        except:
            e = sys.exc_info()[1]
            QtWidgets.QMessageBox.about(self, "Ошибка!", e.args[0])

    def load_from_exel(self):  # для загрузки файла exel
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть файл", "", 'Exel (*.xlsx)')
            # Загрузка данных из exel
            df = pd.read_excel(filename[0])
            # Получить список словарей из DataFrame
            employees_dicts = df.to_dict('records')
            global Employee_list
            Employee_list = [
                Employee(**employee_dict)
                for employee_dict in employees_dicts
            ]
            self.refresh_table()
        except:
            e = sys.exc_info()[1]
            QtWidgets.QMessageBox.about(self, "Ошибка!", e.args[0])

    def save_to_exel(self):  # для сохранения файла в exel
        try:
            global Employee_list
            # Создать DataFrame из списка сотрудников
            employees_dicts = [
                {
                    'surname': employee.surname,
                    'name': employee.name,
                    'patronymic': employee.patronymic,
                    'position': employee.position,
                    'rank': employee.rank,
                    'status': employee.status,
                }
                for employee in Employee_list
            ]
            df = pd.DataFrame(employees_dicts)

            filename = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить файл", '{}.xlsx'.format(datetime.now().strftime("%Y-%m-%d %H %M")))
            # Выгрузить DataFrame в Excel-файл
            df.to_excel(filename[0], index=False)
            QtWidgets.QMessageBox.about(self, "Файл сохранён", "Файл успешно сохранен")
        except:
            e = sys.exc_info()[1]
            QtWidgets.QMessageBox.about(self, "Ошибка!", e.args[0])

    def save_to_word(self):  # для сохранения файлов в word

        def generate_report(status: str, directory: str):
            try:
                employees = list(filter(lambda employee: employee.status == status, Employee_list))
                employees_dicts = [
                    {
                        'surname': i.surname,
                        'name': i.name,
                        'patronymic': i.patronymic,
                        'position': i.position,
                        'rank': i.rank,
                        'status': i.status,
                    }
                    for i in employees
                ]
                context = {'employees': employees_dicts}
                doc = DocxTemplate('templates/word/{}_employees.docx'.format(status))
                doc.render(context)
                doc.save("{}/{}_{}.docx".format(directory, status, datetime.now().strftime("%Y-%m-%d %H %M")))
            except:
                e = sys.exc_info()[1]
                QtWidgets.QMessageBox.about(self, "Ошибка!", e.args[0])

        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if directory:
            generate_report('Находящиеся', directory)
            generate_report('Отсутствующие', directory)
            generate_report('В ожидании', directory)
            QtWidgets.QMessageBox.about(self, "Отчёты созданы", "Отчёты успешно созданы")

    def add(self):  # для добавления человека в список
        try:
            surname = self.lineEdit.text()
            self.lineEdit.clear()
            name = self.lineEdit_3.text()
            self.lineEdit_3.clear()
            patronymic = self.lineEdit_2.text()
            self.lineEdit_2.clear()
            position = self.lineEdit_4.text()
            self.lineEdit_4.clear()
            rank = self.lineEdit_5.text()
            status = self.comboBox.currentText()
            newEmployee = Employee(surname=surname, name=name, patronymic=patronymic, position=position, rank=rank, status=status)
            global Employee_list
            Employee_list.append(newEmployee)
            self.refresh_table()
        except:
            e = sys.exc_info()[1]
            QtWidgets.QMessageBox.about(self, "Ошибка!", e.args[0])

    def edit(self):
        try:
            index = self.tableWidget.currentIndex()
            if index.row() != -1:
                Employee_list[index.row()].surname = self.lineEdit.text()
                Employee_list[index.row()].name = self.lineEdit_3.text()
                Employee_list[index.row()].patronymic = self.lineEdit_2.text()
                Employee_list[index.row()].position = self.lineEdit_4.text()
                Employee_list[index.row()].rank = self.lineEdit_5.text()
                Employee_list[index.row()].status = self.comboBox.currentText()
                self.refresh_table()
            else:
                QtWidgets.QMessageBox.about(self, "Ошибка!", "Выберите данные для изменения!")
        except:
            e = sys.exc_info()[1]
            QtWidgets.QMessageBox.about(self, "Ошибка!", e.args[0])

    def delete(self):
        global Employee_list
        try:
            index = self.tableWidget.currentIndex()
            if index.row() != -1:
                Employee_list.pop(index.row())
                self.refresh_table()
            else:
                QtWidgets.QMessageBox.about(self, "Ошибка!", "Выберите данные для удаления!")
        except:
            e = sys.exc_info()[1]
            QtWidgets.QMessageBox.about(self, "Ошибка!", e.args[0])


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = App()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
