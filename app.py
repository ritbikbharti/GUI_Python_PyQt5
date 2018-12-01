# © ritbikbharti,2018
import sys
import csv
import operator
import pandas as pd
import numpy as np
import os.path
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from matplotlib import pyplot as plt

array=[]
a=[]

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.b = QtWidgets.QPushButton('Upload CSV file')
        self.b2 = QtWidgets.QPushButton('Get aggregate data')
        self.b1 = QtWidgets.QPushButton('Get sorted students for your compnay!!')
        self.led = QtWidgets.QLabel('Enter file name')
        self.le = QtWidgets.QLineEdit('')
        self.le1d = QtWidgets.QLabel('Enter name of company  ')
        self.le1 = QtWidgets.QLineEdit('')
        self.le2d = QtWidgets.QLabel('Enter min required CGPA')
        self.le2 = QtWidgets.QLineEdit('')

        datetime = QDateTime.currentDateTime()
        time = datetime.toString()

        self.date = QtWidgets.QLabel(time)
        self.date.setAlignment(Qt.AlignCenter)

        self.pic = QtWidgets.QLabel(self)
        self.pic.setPixmap(QPixmap("KLE-Tech-logo.png"))
        self.pic.setAlignment(Qt.AlignCenter)

        font = QtGui.QFont()
        font.setPointSize(18)
        self.date.setFont(font)

        self.l = QtWidgets.QLabel(" ")
        self.l.setAlignment(Qt.AlignCenter)

        self.l1 = QtWidgets.QLabel('Welcome to Students Placement Eligibility Check System')
        self.l1.setAlignment(Qt.AlignCenter)
        font.setPointSize(22)
        self.l1.setFont(font)

        self.l2 = QtWidgets.QLabel('Here you can upload a csv file of students data and get a new csv file of eligible candidates')
        self.l2.setAlignment(Qt.AlignCenter)
        self.l2.setFont(QFont('Comic Sans MS', 18))

        self.l3 = QtWidgets.QLabel(' ')
        self.l3.setAlignment(Qt.AlignCenter)

        self.l5 = QtWidgets.QLabel(' ')
        self.l5.setAlignment(Qt.AlignCenter)

        self.l6 = QtWidgets.QLabel(' ')
        self.l6.setAlignment(Qt.AlignCenter)

        self.l7 = QtWidgets.QLabel(' ')
        self.l7.setAlignment(Qt.AlignCenter)

        self.l8 = QtWidgets.QLabel(' ')
        self.l8.setAlignment(Qt.AlignCenter)

        self.l9 = QtWidgets.QLabel(' ')
        self.l9.setAlignment(Qt.AlignCenter)

        self.b3 = QtWidgets.QPushButton("Get Histogram of CGPA's of Students")


        v1_box = QtWidgets.QVBoxLayout()
        v1_box.addWidget(self.pic)
        v1_box.addWidget(self.date)
        v1_box.addWidget(self.l1)
        v1_box.addWidget(self.l2)
        v1_box.addStretch()

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addWidget(self.le1d)
        h_box1.addWidget(self.le1)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.le2d)
        h_box2.addWidget(self.le2)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(v1_box)
        v_box.addWidget(self.led)
        v_box.addWidget(self.le)
        v_box.addWidget(self.b)
        v_box.addWidget(self.b2)
        v_box.addWidget(self.l)
        v_box.addWidget(self.l5)
        v_box.addWidget(self.l6)
        v_box.addWidget(self.l7)
        v_box.addWidget(self.l8)
        v_box.addWidget(self.b3)
        v_box.addWidget(self.l9)
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.l3)

        self.setLayout(v_box)
        self.setWindowTitle("STUDENT's PLACEMENT ELIGIBILITY MANAGEMENT SYSTEM")

        self.b.clicked.connect(self.btn_click)
        self.b1.clicked.connect(self.btn1_click)
        self.b2.clicked.connect(self.btn2_click)
        self.b3.clicked.connect(self.graph)

        self.show()

    def btn_click(self):
        file = self.le.text()
        if os.path.isfile(file):
            with open(file, 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for line in reader:
                    array.append(tuple(line))

            if array:
                self.l.setText('File uploaded')
                a.append(1)
            elif not array:
                self.l.setText('Empty file !! Please enter valid file name...')
        else:
            self.l.setText('File not found!! Please enter valid file name...')
            self.l5.setText(" ")
            self.l6.setText(" ")
            self.l7.setText(" ")
            self.l8.setText(" ")

    def btn1_click(self):
        if 1 in a:
            co = self.le1.text()
            mg = self.le2.text()
            if len(co)>=1 and len(mg)>=1 and (any(c.isdigit() for c in mg)) and not (any(c.isalpha() for c in mg)):
                array.sort(key=operator.itemgetter(1), reverse=True)
                with open( co+'.csv' ,'w') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow(["Name" , "CGPA"])
                    for x in array:
                        if x[1]<mg:
                            break
                        filewriter.writerow([x[0], x[1]])

                self.l3.setText('File saved with name ' + co+'.csv')
                del array[:]
                del a[:]
            else:
                self.l3.setText('Error! Please enter valid company name and cgpa first')
        else:
            self.l3.setText('Error! Please upload a valid file first...')

    def btn2_click(self):
        if 1 in a:
            global cgpa
            data = pd.read_csv('persons.csv')
            cgpa = np.array(data['CGPA'])
            max=cgpa.max()
            min=cgpa.min()
            mean=round(cgpa.mean())
            std=round(cgpa.std())
            self.l.setText("The aggregated data of the students")
            self.l5.setText("Max CGPA:       "+ str(max))
            self.l6.setText("Min CGPA:       "+ str(min))
            self.l7.setText("Mean CGPA:       "+ str(mean))
            self.l8.setText("Standard deviation: "+ str(std))
        else:
            self.l7.setText('Error! Please upload a valid file first...')
            self.l5.setText(' ')
            self.l6.setText(' ')
            self.l8.setText(' ')

    def graph(self):
        if 1 in a:
            if cgpa.any():
                plt.bar(range(len(cgpa)), cgpa)
                plt.xlabel('Students')
                plt.ylabel('CGPA')
                plt.show()
                self.l9.setText("Histograph plotted")
                np.delete(cgpa)
            else:
                self.l9.setText("Please calculate aggregated data first")
        else:
            self.l9.setText("Please calculate aggregated data first")

    

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())