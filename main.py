import os
import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLineEdit, QListWidget, QLabel, QHBoxLayout,QListWidgetItem, QCheckBox
from PyQt6.QtGui import QPixmap
import matplotlib.pyplot as plt
from PyQt6.QtCore import Qt

def list_directory_contents(directory):
    login = []
    #print(f"Содержимое папки '{directory}':")
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            continue
            print(f"[Папка] {item}")
        else:
            # Проверяет является ли файл логом
            if item[0] == "L":
                login.append(item)
    return login
# указываем директорию папки проекта с файлами
login_list = list_directory_contents("C:\\moodle project")
print(login_list)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 200, 550, 500)
        self.setWindowTitle("MainWindow")
        #self.setStyleSheet("background-color: rgb(255, 255, 255);")

        # Центральный виджет
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(0, 0, 550, 200)
        #self.label.setText("0")
        # Опционально: масштабируем изображение под размер виджета
        self.label.setScaledContents(True)

        pixmap = QPixmap("C:\\moodle project\лого")
        self.label.setPixmap(pixmap)

        self.Button_file = QPushButton(self.centralwidget)
        self.Button_file.setGeometry(250, 200, 300, 100)
        #self.Button_file.setStyleSheet('background: rgb(255, 255, 255);')
        self.Button_file.setText("Загрузить файлы")
        self.Button_file.clicked.connect(self.open_second_window_for_gownload_file)
        self.gownload_file = None  # Храним ссылку на второе окно

        self.Button_check_student = QPushButton(self.centralwidget)
        self.Button_check_student.setGeometry(250, 300, 300, 100)
        self.Button_check_student.setText("Выбрать студента")
        self.Button_check_student.clicked.connect(self.open_second_window_Check_student)
        self.Check_student = None  # Храним ссылку на второе окно

        self.Button_filter_file = QPushButton(self.centralwidget)
        self.Button_filter_file.setGeometry(250, 400, 300, 100)
        self.Button_filter_file.setText("Фильтровать файл")
        self.Button_filter_file.clicked.connect(self.open_second_window_filtared_file)
        self.gownload_file = None  # Храним ссылку на второе окно

        self.spravka = QPushButton(self.centralwidget)
        self.spravka.setGeometry(0, 450, 100, 50)
        self.spravka.setText("Справка")
        self.spravka.clicked.connect(self.open_spravka)
        self.Check_student = None  # Храним ссылку на второе окно

    # Загрузить файл
    def open_second_window_for_gownload_file(self):
        if self.gownload_file is None or not self.gownload_file.isVisible():
            self.gownload_file = Download_file()
            self.gownload_file.show()

    # Выбрать студента
    def open_second_window_Check_student(self):
        if self.Check_student is None or not self.Check_student.isVisible():
            self.Check_student = Check_student_window()
            self.Check_student.show()

    def open_second_window_filtared_file(self):
        if self.Check_student is None or not self.Check_student.isVisible():
            self.Check_student = Filtared_file()
            self.Check_student.show()

    def open_spravka(self):
        if self.Check_student is None or not self.Check_student.isVisible():
            self.Check_student = Spravka()
            self.Check_student.show()

class Spravka(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Второе окно")
        self.setGeometry(575, 400, 600, 300)

        # Создаем текстовую метку
        self.text_spravka = QLabel("Для работы приложения нужно выполнить следующие шаги: \n"
                                   "1. Создайте папку в локальном диске С и назовите ее moodle project \n"
                                   "2. Загрузите файлы логов, скачанные из мудла в папку moodle project, пример файла LogCSV 12,12,25\n"
                                   "3. Запустите приложение", self)
        self.text_spravka.move(1, 40)  # Позиция текста
        self.text_spravka.resize(700, 100)



# открытие окна при нажатие на кнопку Загрузить файл
class Download_file(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Загрузка")
        self.setGeometry(720, 280, 370, 400)

        layout = QVBoxLayout()

        self.central_widget = QWidget(self)

        # Создание списка
        self.list_widget = QListWidget()

        # Добавление элементов
        self.list_widget.addItems(login_list)

        # Создание метки для отображения выбранного элемента
        self.label = QLabel("Выбран: ")


        # Подключение сигнала изменения выбора
        self.list_widget.itemClicked.connect(self.on_item_selected)

        self.Button_open = QPushButton(self.central_widget)
        self.Button_open.setFixedSize(100, 25)
        self.Button_open.clicked.connect(self.find_student)
        self.Button_open.setText("Открыть")

        self.Button_back = QPushButton(self.central_widget)
        self.Button_back.setFixedSize(100, 25)
        self.Button_back.clicked.connect(self.Button_backk)
        self.Button_back.setText("Назад")

        self.Delete_name = QPushButton(self.central_widget)
        self.Delete_name.setFixedSize(100, 25)
        self.Delete_name.clicked.connect(self.delete_name)
        self.Delete_name.setText("Удалить")

        self.Statistic = QPushButton(self.central_widget)
        self.Statistic.setFixedSize(100, 25)
        self.Statistic.clicked.connect(self.Statistic_stu)
        self.Statistic.setText("Статистика")

        layout.addWidget(self.list_widget)
        layout.addWidget(self.Button_open)
        layout.addWidget(self.Button_back)
        layout.addWidget(self.Delete_name)
        layout.addWidget(self.Statistic)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.a = ""


    # Метод для отлбражения выбранного элемента
    def on_item_selected(self, item):
        self.label.setText(f"Выбран: {item.text()}")
        self.a = item.text()
        print(self.a)
        if self.a in login_list:
            self.f = self.a


    def Statistic_stu(self):
        # График посешаемости студентами платформы Мудл
        check_list_name = []       # для превого графика
        check_list_name_surname = []      # для превого графика
        type_lesson = []  # для второго графика
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                check_list_name.append(item.text())
        check_list = sorted(check_list_name)
        score = 0    # для превого графика
        list_score = []    # для превого графика
        for name in check_list_name:
            for i in self.file_list:
                if name == i[2]:
                    score = score + 1
                type_lesson.append(i[4])

            list_score.append(score)
            score = 0
        score = 0
        surname = ''
        for name_1 in check_list_name:
            for letter in name_1[::-1]:
                if letter != " ":
                    surname = letter + surname
                else:
                    check_list_name_surname.append(surname)
                    surname = ""
                    break

        f, ax = plt.subplots(2,2)
        f.set_size_inches(10,8)
        x = check_list_name_surname
        y = list_score
        ax[0,0].barh(x, y) ; ax[0,0].grid()
        ax[0,0].set_title("График посещаемости студента платформы Moodle")
        ax[0,0].set_xlabel("Колличество входов")
        #ax[0,0].set_ylabel("45")

        # График посешаемости кусов студентами по популярности на платформе Мудл
        list_score_1 = []
        type_lesson = set(type_lesson)
        for type in type_lesson:
            for i in self.file_list:
                if type == i[4]:
                    score = score + 1
            list_score_1.append(score)
            score = 0

        type_lesson = list(type_lesson)

        x1 = type_lesson
        y1 = list_score_1
        ax[1, 1].set_title("Популярность разделов курса")
        ax[1,1].pie(list_score_1, labels=type_lesson)
        ax[1, 1].grid()

        ax[1, 0].set_visible(False) # скрыли с видимости график ax[1, 0]

        plt.savefig('C:\\moodle project\\my_sine_plot.pdf')   # сохранение графика в пдф формате в (C:/Games)
        plt.show()
        #print(list_score_1)
        #print(type_lesson)


    def Button_backk(self):
        self.list_widget.clear()
        self.list_widget.addItems(login_list)
        self.label.setText(f"Выбран: {'Ничего не выбранно'}")
        self.a = ""

    def delete_name(self):
        teachers_list = []  # тут будет список отмеченных имен
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                teachers_list.append(item.text())

        # Удаляем из self.student_list все элементы, которые есть в teachers_list
        list_without_teacher = [item for item in self.student_list if item not in teachers_list]
        # чистим старый список и добавляем новый без преподавателей
        self.list_widget.clear()

        for text in sorted(list_without_teacher):
            item = QListWidgetItem(text)  # создаём элемент списка
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)  # разрешаем галочку (чекбокс)
            item.setCheckState(Qt.CheckState.Unchecked)  # по умолчанию чекбокс не отмечен
            self.list_widget.addItem(item)  # добавляем элемент в список


    def find_student(self):
        if self.a in login_list :
            f_input = open(f"C://moodle project/{self.a}", "r", encoding='utf-8')  # Установка кодировки для русских букв
            s = f_input.readline()
            self.file_list = []
            x = []
            self.student_list = []
            str_elem = ""
            while s != "":
                s = f_input.readline()
                s = s.replace('"', "")  # Убираем кавычки
                s = s.rstrip()  # Убираем управляющий символ \n
                for symb in s:
                    if symb != ",":
                        str_elem = str_elem + symb
                    else:
                        x.append(str_elem)
                        str_elem = ""
                self.file_list.append(x)
                x = [];
                str_elem = ""
            self.file_list.pop()
            for i in self.file_list:
                #if i[2] != "Валерий Викторович Щербак":
                self.student_list.append(i[2])
            student_set = set(self.student_list)
            self.student_list = list(student_set)

            self.list_widget.clear()
            self.list_widget.addItems(sorted(self.student_list))
            # print(student_list)

            # self.list_widget.addItems([])
            self.list_widget.clear()
            # self.list_widget.addItems(student_list)
            # print(student_list)

            # Проходим по каждому элементу и добавляем его в список
            for text in sorted(self.student_list):
                item = QListWidgetItem(text)  # создаём элемент списка
                item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)  # разрешаем галочку (чекбокс)
                item.setCheckState(Qt.CheckState.Unchecked)  # по умолчанию чекбокс не отмечен
                self.list_widget.addItem(item)  # добавляем элемент в список
        print(self.f)
        #print(self.file_list)
        time = [] ; name = []
        for i in self.file_list:
            time.append(i[1])
            name.append(i[2])
        print(time)
        print(name)



# Открытие окна при нажатие на кнопку Выбрать сткдента
class Check_student_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Выбрать студента")
        self.setGeometry(700, 400, 400, 200)

        # Создаем центральный виджет и компоновку
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Поле для ввода текста
        self.text_input = QLineEdit(self.central_widget)
        self.text_input.setPlaceholderText("Введите ФИО студента")  # Подсказка внутри поля
        self.layout.addWidget(self.text_input.setGeometry(10, 50, 380, 30))
        self.layout.addWidget(self.text_input)


        self.knopka_nayti = QPushButton(self.central_widget)
        self.knopka_nayti.setGeometry(100, 120, 200, 50)
        self.layout.addWidget(self.knopka_nayti)
        self.knopka_nayti.setText("Найти")

    def on_item_selected(self, item):
        self.label.setText(f"Выбран: {item.text()}")

# открытие окна при нажатие на кнопку Фильтровать файл
class Filtared_file(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Второе окно")
        self.setGeometry(700, 400, 370, 300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    window.show()
    sys.exit(app.exec())
