# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: Tharaka Ratnayake
# Purpose   : Terrain generator code for micromouse maze
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import re
import time



maze_dic = {}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(715, 778)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        

        #--------------------------------------------------------------------
        
        self.R5C6_R5C7_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R5C6_R5C7_Vertical.setGeometry(QtCore.QRect(256, 214, 8, 33))
        self.R5C6_R5C7_Vertical.setText("")
        self.R5C6_R5C7_Vertical.setObjectName("R5C6_R5C7_Vertical")
        self.R5C6_R5C7_Vertical.clicked.connect(partial(self.addtodict,self.R5C6_R5C7_Vertical))     

        #--------------------------------------------------------------------

        self.R7C2_R8C2_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R7C2_R8C2_Horizontal.setGeometry(QtCore.QRect(60, 350, 39, 8))
        self.R7C2_R8C2_Horizontal.setText("")
        self.R7C2_R8C2_Horizontal.setObjectName("R7C2_R8C2_Horizontal")
        self.R7C2_R8C2_Horizontal.clicked.connect(partial(self.addtodict,self.R7C2_R8C2_Horizontal))
        

        #--------------------------------------------------------------------
        
        self.Left_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Left_1.setGeometry(QtCore.QRect(20, 20, 8, 33))
        self.Left_1.setText("")
        self.Left_1.setObjectName("Left_1")
        self.Left_1.setStyleSheet("background-color: red")
        self.Left_1.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R4C13_R4C14_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R4C13_R4C14_Vertical.setGeometry(QtCore.QRect(530, 164, 8, 33))
        self.R4C13_R4C14_Vertical.setText("")
        self.R4C13_R4C14_Vertical.setObjectName("R4C13_R4C14_Vertical")
        self.R4C13_R4C14_Vertical.clicked.connect(partial(self.addtodict,self.R4C13_R4C14_Vertical))
        

        #--------------------------------------------------------------------
        
        self.R2C10_R3C10_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R2C10_R3C10_Horizontal.setGeometry(QtCore.QRect(380, 100, 39, 8))
        self.R2C10_R3C10_Horizontal.setText("")
        self.R2C10_R3C10_Horizontal.setObjectName("R2C10_R3C10_Horizontal")
        self.R2C10_R3C10_Horizontal.clicked.connect(partial(self.addtodict,self.R2C10_R3C10_Horizontal))


        #--------------------------------------------------------------------
        
        self.R12C7_R13C7_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R12C7_R13C7_Horizontal.setGeometry(QtCore.QRect(260, 600, 39, 8))
        self.R12C7_R13C7_Horizontal.setText("")
        self.R12C7_R13C7_Horizontal.setObjectName("R12C7_R13C7_Horizontal")
        self.R12C7_R13C7_Horizontal.clicked.connect(partial(self.addtodict,self.R12C7_R13C7_Horizontal))

        #--------------------------------------------------------------------
        
        self.R2C5_R3C5_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R2C5_R3C5_Horizontal.setGeometry(QtCore.QRect(180, 100, 39, 8))
        self.R2C5_R3C5_Horizontal.setText("")
        self.R2C5_R3C5_Horizontal.setObjectName("R2C5_R3C5_Horizontal")
        self.R2C5_R3C5_Horizontal.clicked.connect(partial(self.addtodict,self.R2C5_R3C5_Horizontal))

        #--------------------------------------------------------------------
        
        self.R10C7_R11C7_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R10C7_R11C7_Horizontal.setGeometry(QtCore.QRect(260, 500, 39, 8))
        self.R10C7_R11C7_Horizontal.setText("")
        self.R10C7_R11C7_Horizontal.setObjectName("R10C7_R11C7_Horizontal")
        self.R10C7_R11C7_Horizontal.clicked.connect(partial(self.addtodict,self.R10C7_R11C7_Horizontal))

        #--------------------------------------------------------------------
        
        self.R13C11_R13C12_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R13C11_R13C12_Vertical.setGeometry(QtCore.QRect(455, 614, 8, 33))
        self.R13C11_R13C12_Vertical.setText("")
        self.R13C11_R13C12_Vertical.setObjectName("R13C11_R13C12_Vertical")
        self.R13C11_R13C12_Vertical.clicked.connect(partial(self.addtodict,self.R13C11_R13C12_Vertical))

        #--------------------------------------------------------------------
        
        self.R3C3_R4C3_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R3C3_R4C3_Horizontal.setGeometry(QtCore.QRect(100, 150, 39, 8))
        self.R3C3_R4C3_Horizontal.setText("")
        self.R3C3_R4C3_Horizontal.setObjectName("R3C3_R4C3_Horizontal")
        self.R3C3_R4C3_Horizontal.clicked.connect(partial(self.addtodict,self.R3C3_R4C3_Horizontal))

        #--------------------------------------------------------------------
        
        self.R12C2_R12C3_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R12C2_R12C3_Vertical.setGeometry(QtCore.QRect(94, 564, 8, 33))
        self.R12C2_R12C3_Vertical.setText("")
        self.R12C2_R12C3_Vertical.setObjectName("R12C2_R12C3_Vertical")
        self.R12C2_R12C3_Vertical.clicked.connect(partial(self.addtodict,self.R12C2_R12C3_Vertical))

        #--------------------------------------------------------------------
        
        self.Left_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Left_4.setGeometry(QtCore.QRect(20, 164, 8, 33))
        self.Left_4.setText("")
        self.Left_4.setObjectName("Left_4")
        self.Left_4.setStyleSheet("background-color: red")
        self.Left_4.setEnabled(False)
        
        #--------------------------------------------------------------------
        
        self.R9C10_R9C11_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R9C10_R9C11_Vertical.setGeometry(QtCore.QRect(416, 414, 8, 33))
        self.R9C10_R9C11_Vertical.setText("")
        self.R9C10_R9C11_Vertical.setObjectName("R9C10_R9C11_Vertical")
        self.R9C10_R9C11_Vertical.clicked.connect(partial(self.addtodict,self.R9C10_R9C11_Vertical))

        #--------------------------------------------------------------------
        
        self.R8C5_R9C5_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R8C5_R9C5_Horizontal.setGeometry(QtCore.QRect(180, 400, 39, 8))
        self.R8C5_R9C5_Horizontal.setText("")
        self.R8C5_R9C5_Horizontal.setObjectName("R8C5_R9C5_Horizontal")
        self.R8C5_R9C5_Horizontal.clicked.connect(partial(self.addtodict,self.R8C5_R9C5_Horizontal))

        #--------------------------------------------------------------------
        
        self.R10C11_R11C11_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R10C11_R11C11_Horizontal.setGeometry(QtCore.QRect(420, 500, 39, 8))
        self.R10C11_R11C11_Horizontal.setText("")
        self.R10C11_R11C11_Horizontal.setObjectName("R10C11_R11C11_Horizontal")
        self.R10C11_R11C11_Horizontal.clicked.connect(partial(self.addtodict,self.R10C11_R11C11_Horizontal))

        #--------------------------------------------------------------------
        
        self.R5C12_R5C13_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R5C12_R5C13_Vertical.setGeometry(QtCore.QRect(497, 214, 8, 33))
        self.R5C12_R5C13_Vertical.setText("")
        self.R5C12_R5C13_Vertical.setObjectName("R5C12_R5C13_Vertical")
        self.R5C12_R5C13_Vertical.clicked.connect(partial(self.addtodict,self.R5C12_R5C13_Vertical))

        #--------------------------------------------------------------------
        
        self.R8C8_R8C9_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R8C8_R8C9_Vertical.setGeometry(QtCore.QRect(334, 364, 8, 33))
        self.R8C8_R8C9_Vertical.setText("")
        self.R8C8_R8C9_Vertical.setObjectName("R8C8_R8C9_Vertical")
        self.R8C8_R8C9_Vertical.clicked.connect(partial(self.addtodict,self.R8C8_R8C9_Vertical))

        #--------------------------------------------------------------------
        
        self.R1C6_R1C7_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R1C6_R1C7_Vertical.setGeometry(QtCore.QRect(256, 20, 8, 33))
        self.R1C6_R1C7_Vertical.setText("")
        self.R1C6_R1C7_Vertical.setObjectName("R1C6_R1C7_Vertical")
        self.R1C6_R1C7_Vertical.clicked.connect(partial(self.addtodict,self.R1C6_R1C7_Vertical))

        #--------------------------------------------------------------------
        
        self.R1C13_R2C13_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R1C13_R2C13_Horizontal.setGeometry(QtCore.QRect(500, 56, 39, 8))
        self.R1C13_R2C13_Horizontal.setText("")
        self.R1C13_R2C13_Horizontal.setObjectName("R1C13_R2C13_Horizontal")
        self.R1C13_R2C13_Horizontal.clicked.connect(partial(self.addtodict,self.R1C13_R2C13_Horizontal))

        #--------------------------------------------------------------------
        
        self.R8C2_R8C3_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R8C2_R8C3_Vertical.setGeometry(QtCore.QRect(94, 364, 8, 33))
        self.R8C2_R8C3_Vertical.setText("")
        self.R8C2_R8C3_Vertical.setObjectName("R8C2_R8C3_Vertical")
        self.R8C2_R8C3_Vertical.clicked.connect(partial(self.addtodict,self.R8C2_R8C3_Vertical))

        #--------------------------------------------------------------------
        
        self.R9C7_R9C8_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R9C7_R9C8_Vertical.setGeometry(QtCore.QRect(296, 414, 8, 33))
        self.R9C7_R9C8_Vertical.setText("")
        self.R9C7_R9C8_Vertical.setObjectName("R9C7_R9C8_Vertical")
        self.R9C7_R9C8_Vertical.clicked.connect(partial(self.addtodict,self.R9C7_R9C8_Vertical))

        #--------------------------------------------------------------------
        
        self.R1C10_R2C10_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R1C10_R2C10_Horizontal.setGeometry(QtCore.QRect(380, 56, 39, 8))
        self.R1C10_R2C10_Horizontal.setText("")
        self.R1C10_R2C10_Horizontal.setObjectName("R1C10_R2C10_Horizontal")
        self.R1C10_R2C10_Horizontal.clicked.connect(partial(self.addtodict,self.R1C10_R2C10_Horizontal))

        #--------------------------------------------------------------------
        
        self.R12C11_R13C11_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R12C11_R13C11_Horizontal.setGeometry(QtCore.QRect(420, 600, 39, 8))
        self.R12C11_R13C11_Horizontal.setText("")
        self.R12C11_R13C11_Horizontal.setObjectName("R12C11_R13C11_Horizontal")
        self.R12C11_R13C11_Horizontal.clicked.connect(partial(self.addtodict,self.R12C11_R13C11_Horizontal))

        #--------------------------------------------------------------------
        
        self.Lower_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Lower_7.setGeometry(QtCore.QRect(260, 700, 39, 8))
        self.Lower_7.setText("")
        self.Lower_7.setObjectName("Lower_7")
        self.Lower_7.setStyleSheet("background-color: red")
        self.Lower_7.setEnabled(False)
        
        #--------------------------------------------------------------------
        
        self.R2C11_R2C12_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R2C11_R2C12_Vertical.setGeometry(QtCore.QRect(455, 64, 8, 33))
        self.R2C11_R2C12_Vertical.setText("")
        self.R2C11_R2C12_Vertical.setObjectName("R2C11_R2C12_Vertical")
        self.R2C11_R2C12_Vertical.clicked.connect(partial(self.addtodict,self.R2C11_R2C12_Vertical))

        #--------------------------------------------------------------------
        
        self.R3C6_R3C7_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R3C6_R3C7_Vertical.setGeometry(QtCore.QRect(256, 114, 8, 33))
        self.R3C6_R3C7_Vertical.setText("")
        self.R3C6_R3C7_Vertical.setObjectName("R3C6_R3C7_Vertical")
        self.R3C6_R3C7_Vertical.clicked.connect(partial(self.addtodict,self.R3C6_R3C7_Vertical))

        #--------------------------------------------------------------------
        
        self.Left_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Left_3.setGeometry(QtCore.QRect(20, 114, 8, 33))
        self.Left_3.setText("")
        self.Left_3.setObjectName("Left_3")
        self.Left_3.setStyleSheet("background-color: red")
        self.Left_3.setEnabled(False)
        
        #--------------------------------------------------------------------
        
        self.R12C13_R12C14_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R12C13_R12C14_Vertical.setGeometry(QtCore.QRect(530, 564, 8, 33))
        self.R12C13_R12C14_Vertical.setText("")
        self.R12C13_R12C14_Vertical.setObjectName("R12C13_R12C14_Vertical")
        self.R12C13_R12C14_Vertical.clicked.connect(partial(self.addtodict,self.R12C13_R12C14_Vertical))

        #--------------------------------------------------------------------
        
        self.R6C14_R7C14_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R6C14_R7C14_Horizontal.setGeometry(QtCore.QRect(540, 300, 39, 8))
        self.R6C14_R7C14_Horizontal.setText("")
        self.R6C14_R7C14_Horizontal.setObjectName("R6C14_R7C14_Horizontal")
        self.R6C14_R7C14_Horizontal.clicked.connect(partial(self.addtodict,self.R6C14_R7C14_Horizontal))

        #--------------------------------------------------------------------
        
        self.R6C11_R6C12_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R6C11_R6C12_Vertical.setGeometry(QtCore.QRect(455, 264, 8, 33))
        self.R6C11_R6C12_Vertical.setText("")
        self.R6C11_R6C12_Vertical.setObjectName("R6C11_R6C12_Vertical")
        self.R6C11_R6C12_Vertical.clicked.connect(partial(self.addtodict,self.R6C11_R6C12_Vertical))

        #--------------------------------------------------------------------
        
        self.R9C8_R10C8_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R9C8_R10C8_Horizontal.setGeometry(QtCore.QRect(300, 450, 39, 8))
        self.R9C8_R10C8_Horizontal.setText("")
        self.R9C8_R10C8_Horizontal.setObjectName("R9C8_R10C8_Horizontal")
        self.R9C8_R10C8_Horizontal.clicked.connect(partial(self.addtodict,self.R9C8_R10C8_Horizontal))

        #--------------------------------------------------------------------
        
        self.R8C13_R8C14_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R8C13_R8C14_Vertical.setGeometry(QtCore.QRect(530, 364, 8, 33))
        self.R8C13_R8C14_Vertical.setText("")
        self.R8C13_R8C14_Vertical.setObjectName("R8C13_R8C14_Vertical")
        self.R8C13_R8C14_Vertical.clicked.connect(partial(self.addtodict,self.R8C13_R8C14_Vertical))

        #--------------------------------------------------------------------
        
        self.R10C9_R11C9_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R10C9_R11C9_Horizontal.setGeometry(QtCore.QRect(340, 500, 39, 8))
        self.R10C9_R11C9_Horizontal.setText("")
        self.R10C9_R11C9_Horizontal.setObjectName("R10C9_R11C9_Horizontal")
        self.R10C9_R11C9_Horizontal.clicked.connect(partial(self.addtodict,self.R10C9_R11C9_Horizontal))

        #--------------------------------------------------------------------
        
        self.R1C5_R2C5_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R1C5_R2C5_Horizontal.setGeometry(QtCore.QRect(180, 56, 39, 8))
        self.R1C5_R2C5_Horizontal.setText("")
        self.R1C5_R2C5_Horizontal.setObjectName("R1C5_R2C5_Horizontal")
        self.R1C5_R2C5_Horizontal.clicked.connect(partial(self.addtodict,self.R1C5_R2C5_Horizontal))

        #--------------------------------------------------------------------
        
        self.R8C6_R8C7_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R8C6_R8C7_Vertical.setGeometry(QtCore.QRect(256, 364, 8, 33))
        self.R8C6_R8C7_Vertical.setText("")
        self.R8C6_R8C7_Vertical.setObjectName("R8C6_R8C7_Vertical")
        self.R8C6_R8C7_Vertical.clicked.connect(partial(self.addtodict,self.R8C6_R8C7_Vertical))

        #--------------------------------------------------------------------
        
        self.R1C9_R1C10_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R1C9_R1C10_Vertical.setGeometry(QtCore.QRect(376, 20, 8, 33))
        self.R1C9_R1C10_Vertical.setText("")
        self.R1C9_R1C10_Vertical.setObjectName("R1C9_R1C10_Vertical")
        self.R1C9_R1C10_Vertical.clicked.connect(partial(self.addtodict,self.R1C9_R1C10_Vertical))

        #--------------------------------------------------------------------
        
        self.R10C2_R10C3_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R10C2_R10C3_Vertical.setGeometry(QtCore.QRect(94, 464, 8, 33))
        self.R10C2_R10C3_Vertical.setText("")
        self.R10C2_R10C3_Vertical.setObjectName("R10C2_R10C3_Vertical")
        self.R10C2_R10C3_Vertical.clicked.connect(partial(self.addtodict,self.R10C2_R10C3_Vertical))

        #--------------------------------------------------------------------
        
        self.R11C14_R12C14_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R11C14_R12C14_Horizontal.setGeometry(QtCore.QRect(540, 550, 39, 8))
        self.R11C14_R12C14_Horizontal.setText("")
        self.R11C14_R12C14_Horizontal.setObjectName("R11C14_R12C14_Horizontal")
        self.R11C14_R12C14_Horizontal.clicked.connect(partial(self.addtodict,self.R11C14_R12C14_Horizontal))

        #--------------------------------------------------------------------
        
        self.R1C4_R1C5_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R1C4_R1C5_Vertical.setGeometry(QtCore.QRect(175, 20, 8, 33))
        self.R1C4_R1C5_Vertical.setText("")
        self.R1C4_R1C5_Vertical.setObjectName("R1C4_R1C5_Vertical")
        self.R1C4_R1C5_Vertical.clicked.connect(partial(self.addtodict,self.R1C4_R1C5_Vertical))

        #--------------------------------------------------------------------
        
        self.R13C13_R14C13_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R13C13_R14C13_Horizontal.setGeometry(QtCore.QRect(500, 650, 39, 8))
        self.R13C13_R14C13_Horizontal.setText("")
        self.R13C13_R14C13_Horizontal.setObjectName("R13C13_R14C13_Horizontal")
        self.R13C13_R14C13_Horizontal.clicked.connect(partial(self.addtodict,self.R13C13_R14C13_Horizontal))

        #--------------------------------------------------------------------
        
        self.R2C14_R3C14_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R2C14_R3C14_Horizontal.setGeometry(QtCore.QRect(540, 100, 39, 8))
        self.R2C14_R3C14_Horizontal.setText("")
        self.R2C14_R3C14_Horizontal.setObjectName("R2C14_R3C14_Horizontal")
        self.R2C14_R3C14_Horizontal.clicked.connect(partial(self.addtodict,self.R2C14_R3C14_Horizontal))

        #--------------------------------------------------------------------
        
        self.R5C9_R5C10_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R5C9_R5C10_Vertical.setGeometry(QtCore.QRect(376, 214, 8, 33))
        self.R5C9_R5C10_Vertical.setText("")
        self.R5C9_R5C10_Vertical.setObjectName("R5C9_R5C10_Vertical")
        self.R5C9_R5C10_Vertical.clicked.connect(partial(self.addtodict,self.R5C9_R5C10_Vertical))

        #--------------------------------------------------------------------
        
        self.R2C3_R3C3_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R2C3_R3C3_Horizontal.setGeometry(QtCore.QRect(100, 100, 39, 8))
        self.R2C3_R3C3_Horizontal.setText("")
        self.R2C3_R3C3_Horizontal.setObjectName("R2C3_R3C3_Horizontal")
        self.R2C3_R3C3_Horizontal.clicked.connect(partial(self.addtodict,self.R2C3_R3C3_Horizontal))

        #--------------------------------------------------------------------
        
        self.R13C14_R14C14_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R13C14_R14C14_Horizontal.setGeometry(QtCore.QRect(540, 650, 39, 8))
        self.R13C14_R14C14_Horizontal.setText("")
        self.R13C14_R14C14_Horizontal.setObjectName("R13C14_R14C14_Horizontal")
        self.R13C14_R14C14_Horizontal.clicked.connect(partial(self.addtodict,self.R13C14_R14C14_Horizontal))

        #--------------------------------------------------------------------
        
        self.R6C12_R7C12_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R6C12_R7C12_Horizontal.setGeometry(QtCore.QRect(460, 300, 39, 8))
        self.R6C12_R7C12_Horizontal.setText("")
        self.R6C12_R7C12_Horizontal.setObjectName("R6C12_R7C12_Horizontal")
        self.R6C12_R7C12_Horizontal.clicked.connect(partial(self.addtodict,self.R6C12_R7C12_Horizontal))

        #--------------------------------------------------------------------
        
        self.R12C13_R13C13_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R12C13_R13C13_Horizontal.setGeometry(QtCore.QRect(500, 600, 39, 8))
        self.R12C13_R13C13_Horizontal.setText("")
        self.R12C13_R13C13_Horizontal.setObjectName("R12C13_R13C13_Horizontal")
        self.R12C13_R13C13_Horizontal.clicked.connect(partial(self.addtodict,self.R12C13_R13C13_Horizontal))

        #--------------------------------------------------------------------
        
        self.R1C6_R2C6_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R1C6_R2C6_Horizontal.setGeometry(QtCore.QRect(220, 56, 39, 8))
        self.R1C6_R2C6_Horizontal.setText("")
        self.R1C6_R2C6_Horizontal.setObjectName("R1C6_R2C6_Horizontal")
        self.R1C6_R2C6_Horizontal.clicked.connect(partial(self.addtodict,self.R1C6_R2C6_Horizontal))

        #--------------------------------------------------------------------
        
        self.R12C12_R13C12_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R12C12_R13C12_Horizontal.setGeometry(QtCore.QRect(460, 600, 39, 8))
        self.R12C12_R13C12_Horizontal.setText("")
        self.R12C12_R13C12_Horizontal.setObjectName("R12C12_R13C12_Horizontal")
        self.R12C12_R13C12_Horizontal.clicked.connect(partial(self.addtodict,self.R12C12_R13C12_Horizontal))

        #--------------------------------------------------------------------
        
        self.R7C2_R7C3_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R7C2_R7C3_Vertical.setGeometry(QtCore.QRect(94, 314, 8, 33))
        self.R7C2_R7C3_Vertical.setText("")
        self.R7C2_R7C3_Vertical.setObjectName("R7C2_R7C3_Vertical")
        self.R7C2_R7C3_Vertical.clicked.connect(partial(self.addtodict,self.R7C2_R7C3_Vertical))

        #--------------------------------------------------------------------
        
        self.R5C1_R5C2_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R5C1_R5C2_Vertical.setGeometry(QtCore.QRect(54, 214, 8, 33))
        self.R5C1_R5C2_Vertical.setText("")
        self.R5C1_R5C2_Vertical.setObjectName("R5C1_R5C2_Vertical")
        self.R5C1_R5C2_Vertical.clicked.connect(partial(self.addtodict,self.R5C1_R5C2_Vertical))

        #--------------------------------------------------------------------
        
        self.Left_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Left_7.setGeometry(QtCore.QRect(20, 314, 8, 33))
        self.Left_7.setText("")
        self.Left_7.setObjectName("Left_7")
        self.Left_7.setStyleSheet("background-color: red")
        self.Left_7.setEnabled(False)
        
        #--------------------------------------------------------------------
        
        self.R2C12_R3C12_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R2C12_R3C12_Horizontal.setGeometry(QtCore.QRect(460, 100, 39, 8))
        self.R2C12_R3C12_Horizontal.setText("")
        self.R2C12_R3C12_Horizontal.setObjectName("R2C12_R3C12_Horizontal")
        self.R2C12_R3C12_Horizontal.clicked.connect(partial(self.addtodict,self.R2C12_R3C12_Horizontal))

        #--------------------------------------------------------------------
        
        self.R11C1_R12C1_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R11C1_R12C1_Horizontal.setGeometry(QtCore.QRect(20, 550, 39, 8))
        self.R11C1_R12C1_Horizontal.setText("")
        self.R11C1_R12C1_Horizontal.setObjectName("R11C1_R12C1_Horizontal")
        self.R11C1_R12C1_Horizontal.clicked.connect(partial(self.addtodict,self.R11C1_R12C1_Horizontal))

        #--------------------------------------------------------------------
        
        self.R5C7_R5C8_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R5C7_R5C8_Vertical.setGeometry(QtCore.QRect(296, 214, 8, 33))
        self.R5C7_R5C8_Vertical.setText("")
        self.R5C7_R5C8_Vertical.setObjectName("R5C7_R5C8_Vertical")
        self.R5C7_R5C8_Vertical.clicked.connect(partial(self.addtodict,self.R5C7_R5C8_Vertical))


        
        self.R7C3_R7C4_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R7C3_R7C4_Vertical.setGeometry(QtCore.QRect(135, 314, 8, 33))
        self.R7C3_R7C4_Vertical.setText("")
        self.R7C3_R7C4_Vertical.setObjectName("R7C3_R7C4_Vertical")
        self.R7C3_R7C4_Vertical.clicked.connect(partial(self.addtodict,self.R7C3_R7C4_Vertical))

        #--------------------------------------------------------------------
        
        self.R10C1_R11C1_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R10C1_R11C1_Horizontal.setGeometry(QtCore.QRect(20, 500, 39, 8))
        self.R10C1_R11C1_Horizontal.setText("")
        self.R10C1_R11C1_Horizontal.setObjectName("R10C1_R11C1_Horizontal")
        self.R10C1_R11C1_Horizontal.clicked.connect(partial(self.addtodict,self.R10C1_R11C1_Horizontal))

        #--------------------------------------------------------------------
        
        self.R13C6_R14C6_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R13C6_R14C6_Horizontal.setGeometry(QtCore.QRect(220, 650, 39, 8))
        self.R13C6_R14C6_Horizontal.setText("")
        self.R13C6_R14C6_Horizontal.setObjectName("R13C6_R14C6_Horizontal")
        self.R13C6_R14C6_Horizontal.clicked.connect(partial(self.addtodict,self.R13C6_R14C6_Horizontal))

        #--------------------------------------------------------------------
        
        self.R12C3_R12C4_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R12C3_R12C4_Vertical.setGeometry(QtCore.QRect(135, 564, 8, 33))
        self.R12C3_R12C4_Vertical.setText("")
        self.R12C3_R12C4_Vertical.setObjectName("R12C3_R12C4_Vertical")
        self.R12C3_R12C4_Vertical.clicked.connect(partial(self.addtodict,self.R12C3_R12C4_Vertical))

        #--------------------------------------------------------------------
        
        self.Lower_11 = QtWidgets.QPushButton(self.centralwidget)
        self.Lower_11.setGeometry(QtCore.QRect(420, 700, 39, 8))
        self.Lower_11.setText("")
        self.Lower_11.setObjectName("Lower_11")
        self.Lower_11.setStyleSheet("background-color: red")
        self.Lower_11.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R2C8_R3C8_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R2C8_R3C8_Horizontal.setGeometry(QtCore.QRect(300, 100, 39, 8))
        self.R2C8_R3C8_Horizontal.setText("")
        self.R2C8_R3C8_Horizontal.setObjectName("R2C8_R3C8_Horizontal")
        self.R2C8_R3C8_Horizontal.clicked.connect(partial(self.addtodict,self.R2C8_R3C8_Horizontal))

        #--------------------------------------------------------------------
        
        self.R2C1_R3C1_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R2C1_R3C1_Horizontal.setGeometry(QtCore.QRect(20, 100, 39, 8))
        self.R2C1_R3C1_Horizontal.setText("")
        self.R2C1_R3C1_Horizontal.setObjectName("R2C1_R3C1_Horizontal")
        self.R2C1_R3C1_Horizontal.clicked.connect(partial(self.addtodict,self.R2C1_R3C1_Horizontal))

        #--------------------------------------------------------------------
        
        self.R4C7_R4C8_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R4C7_R4C8_Vertical.setGeometry(QtCore.QRect(296, 164, 8, 33))
        self.R4C7_R4C8_Vertical.setText("")
        self.R4C7_R4C8_Vertical.setObjectName("R4C7_R4C8_Vertical")
        self.R4C7_R4C8_Vertical.clicked.connect(partial(self.addtodict,self.R4C7_R4C8_Vertical))

        #--------------------------------------------------------------------
        
        self.R10C8_R10C9_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R10C8_R10C9_Vertical.setGeometry(QtCore.QRect(334, 464, 8, 33))
        self.R10C8_R10C9_Vertical.setText("")
        self.R10C8_R10C9_Vertical.setObjectName("R10C8_R10C9_Vertical")
        self.R10C8_R10C9_Vertical.clicked.connect(partial(self.addtodict,self.R10C8_R10C9_Vertical))

        #--------------------------------------------------------------------
        
        self.R13C7_R14C7_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R13C7_R14C7_Horizontal.setGeometry(QtCore.QRect(260, 650, 39, 8))
        self.R13C7_R14C7_Horizontal.setText("")
        self.R13C7_R14C7_Horizontal.setObjectName("R13C7_R14C7_Horizontal")
        self.R13C7_R14C7_Horizontal.clicked.connect(partial(self.addtodict,self.R13C7_R14C7_Horizontal))

        #--------------------------------------------------------------------
        
        self.R7C13_R7C14_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R7C13_R7C14_Vertical.setGeometry(QtCore.QRect(530, 314, 8, 33))
        self.R7C13_R7C14_Vertical.setText("")
        self.R7C13_R7C14_Vertical.setObjectName("R7C13_R7C14_Vertical")
        self.R7C13_R7C14_Vertical.clicked.connect(partial(self.addtodict,self.R7C13_R7C14_Vertical))

        #--------------------------------------------------------------------
        
        self.R12C1_R13C1_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R12C1_R13C1_Horizontal.setGeometry(QtCore.QRect(20, 600, 39, 8))
        self.R12C1_R13C1_Horizontal.setText("")
        self.R12C1_R13C1_Horizontal.setObjectName("R12C1_R13C1_Horizontal")
        self.R12C1_R13C1_Horizontal.clicked.connect(partial(self.addtodict,self.R12C1_R13C1_Horizontal))

        #--------------------------------------------------------------------
        
        self.R8C14_R9C14_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R8C14_R9C14_Horizontal.setGeometry(QtCore.QRect(540, 400, 39, 8))
        self.R8C14_R9C14_Horizontal.setText("")
        self.R8C14_R9C14_Horizontal.setObjectName("R8C14_R9C14_Horizontal")
        self.R8C14_R9C14_Horizontal.clicked.connect(partial(self.addtodict,self.R8C14_R9C14_Horizontal))

        #--------------------------------------------------------------------
        
        self.R8C1_R9C1_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R8C1_R9C1_Horizontal.setGeometry(QtCore.QRect(20, 400, 39, 8))
        self.R8C1_R9C1_Horizontal.setText("")
        self.R8C1_R9C1_Horizontal.setObjectName("R8C1_R9C1_Horizontal")
        self.R8C1_R9C1_Horizontal.clicked.connect(partial(self.addtodict,self.R8C1_R9C1_Horizontal))

        #--------------------------------------------------------------------
        
        self.R3C11_R4C11_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R3C11_R4C11_Horizontal.setGeometry(QtCore.QRect(420, 150, 39, 8))
        self.R3C11_R4C11_Horizontal.setText("")
        self.R3C11_R4C11_Horizontal.setObjectName("R3C11_R4C11_Horizontal")
        self.R3C11_R4C11_Horizontal.clicked.connect(partial(self.addtodict,self.R3C11_R4C11_Horizontal))

        #--------------------------------------------------------------------
        
        self.R3C2_R4C2_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R3C2_R4C2_Horizontal.setGeometry(QtCore.QRect(60, 150, 39, 8))
        self.R3C2_R4C2_Horizontal.setText("")
        self.R3C2_R4C2_Horizontal.setObjectName("R3C2_R4C2_Horizontal")
        self.R3C2_R4C2_Horizontal.clicked.connect(partial(self.addtodict,self.R3C2_R4C2_Horizontal))

        #--------------------------------------------------------------------
        
        self.R13C10_R13C11_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R13C10_R13C11_Vertical.setGeometry(QtCore.QRect(416, 614, 8, 33))
        self.R13C10_R13C11_Vertical.setText("")
        self.R13C10_R13C11_Vertical.setObjectName("R13C10_R13C11_Vertical")
        self.R13C10_R13C11_Vertical.clicked.connect(partial(self.addtodict,self.R13C10_R13C11_Vertical))

        #--------------------------------------------------------------------
        
        self.R5C3_R5C4_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R5C3_R5C4_Vertical.setGeometry(QtCore.QRect(135, 214, 8, 33))
        self.R5C3_R5C4_Vertical.setText("")
        self.R5C3_R5C4_Vertical.setObjectName("R5C3_R5C4_Vertical")
        self.R5C3_R5C4_Vertical.clicked.connect(partial(self.addtodict,self.R5C3_R5C4_Vertical))

        #--------------------------------------------------------------------
        
        self.R7C3_R8C3_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R7C3_R8C3_Horizontal.setGeometry(QtCore.QRect(100, 350, 39, 8))
        self.R7C3_R8C3_Horizontal.setText("")
        self.R7C3_R8C3_Horizontal.setObjectName("R7C3_R8C3_Horizontal")
        self.R7C3_R8C3_Horizontal.clicked.connect(partial(self.addtodict,self.R7C3_R8C3_Horizontal))

        #--------------------------------------------------------------------
        
        self.R11C7_R11C8_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R11C7_R11C8_Vertical.setGeometry(QtCore.QRect(296, 514, 8, 33))
        self.R11C7_R11C8_Vertical.setText("")
        self.R11C7_R11C8_Vertical.setObjectName("R11C7_R11C8_Vertical")
        self.R11C7_R11C8_Vertical.clicked.connect(partial(self.addtodict,self.R11C7_R11C8_Vertical))

        #--------------------------------------------------------------------
        
        self.R13C2_R13C3_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R13C2_R13C3_Vertical.setGeometry(QtCore.QRect(94, 614, 8, 33))
        self.R13C2_R13C3_Vertical.setText("")
        self.R13C2_R13C3_Vertical.setObjectName("R13C2_R13C3_Vertical")
        self.R13C2_R13C3_Vertical.clicked.connect(partial(self.addtodict,self.R13C2_R13C3_Vertical))

        #--------------------------------------------------------------------
        
        self.R7C6_R7C7_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R7C6_R7C7_Vertical.setGeometry(QtCore.QRect(256, 314, 8, 33))
        self.R7C6_R7C7_Vertical.setText("")
        self.R7C6_R7C7_Vertical.setObjectName("R7C6_R7C7_Vertical")
        self.R7C6_R7C7_Vertical.clicked.connect(partial(self.addtodict,self.R7C6_R7C7_Vertical))

        #--------------------------------------------------------------------
        
        self.R14C1_R14C2_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R14C1_R14C2_Vertical.setGeometry(QtCore.QRect(54, 664, 8, 33))
        self.R14C1_R14C2_Vertical.setText("")
        self.R14C1_R14C2_Vertical.setObjectName("R14C1_R14C2_Vertical")
        self.R14C1_R14C2_Vertical.clicked.connect(partial(self.addtodict,self.R14C1_R14C2_Vertical))

        #--------------------------------------------------------------------
        
        self.R6C1_R6C2_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R6C1_R6C2_Vertical.setGeometry(QtCore.QRect(54, 264, 8, 33))
        self.R6C1_R6C2_Vertical.setText("")
        self.R6C1_R6C2_Vertical.setObjectName("R6C1_R6C2_Vertical")
        self.R6C1_R6C2_Vertical.clicked.connect(partial(self.addtodict,self.R6C1_R6C2_Vertical))

        #--------------------------------------------------------------------
        
        self.R4C10_R4C11_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R4C10_R4C11_Vertical.setGeometry(QtCore.QRect(416, 164, 8, 33))
        self.R4C10_R4C11_Vertical.setText("")
        self.R4C10_R4C11_Vertical.setObjectName("R4C10_R4C11_Vertical")
        self.R4C10_R4C11_Vertical.clicked.connect(partial(self.addtodict,self.R4C10_R4C11_Vertical))

        #--------------------------------------------------------------------
        
        self.Lower_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Lower_6.setGeometry(QtCore.QRect(220, 700, 39, 8))
        self.Lower_6.setText("")
        self.Lower_6.setObjectName("Lower_6")
        self.Lower_6.setStyleSheet("background-color: red")
        self.Lower_6.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R11C8_R11C9_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R11C8_R11C9_Vertical.setGeometry(QtCore.QRect(334, 514, 8, 33))
        self.R11C8_R11C9_Vertical.setText("")
        self.R11C8_R11C9_Vertical.setObjectName("R11C8_R11C9_Vertical")
        self.R11C8_R11C9_Vertical.clicked.connect(partial(self.addtodict,self.R11C8_R11C9_Vertical))

        #--------------------------------------------------------------------
        
        self.R1C10_R1C11_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R1C10_R1C11_Vertical.setGeometry(QtCore.QRect(416, 20, 8, 33))
        self.R1C10_R1C11_Vertical.setText("")
        self.R1C10_R1C11_Vertical.setObjectName("R1C10_R1C11_Vertical")
        self.R1C10_R1C11_Vertical.clicked.connect(partial(self.addtodict,self.R1C10_R1C11_Vertical))

        #--------------------------------------------------------------------
        
        self.R4C13_R5C13_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R4C13_R5C13_Horizontal.setGeometry(QtCore.QRect(500, 200, 39, 8))
        self.R4C13_R5C13_Horizontal.setText("")
        self.R4C13_R5C13_Horizontal.setObjectName("R4C13_R5C13_Horizontal")
        self.R4C13_R5C13_Horizontal.clicked.connect(partial(self.addtodict,self.R4C13_R5C13_Horizontal))

        #--------------------------------------------------------------------
        
        self.R6C13_R6C14_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R6C13_R6C14_Vertical.setGeometry(QtCore.QRect(530, 264, 8, 33))
        self.R6C13_R6C14_Vertical.setText("")
        self.R6C13_R6C14_Vertical.setObjectName("R6C13_R6C14_Vertical")
        self.R6C13_R6C14_Vertical.clicked.connect(partial(self.addtodict,self.R6C13_R6C14_Vertical))

        #--------------------------------------------------------------------
        
        self.Left_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Left_2.setGeometry(QtCore.QRect(20, 64, 8, 33))
        self.Left_2.setText("")
        self.Left_2.setObjectName("Left_2")
        self.Left_2.setStyleSheet("background-color: red")
        self.Left_2.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R3C10_R3C11_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R3C10_R3C11_Vertical.setGeometry(QtCore.QRect(416, 114, 8, 33))
        self.R3C10_R3C11_Vertical.setText("")
        self.R3C10_R3C11_Vertical.setObjectName("R3C10_R3C11_Vertical")
        self.R3C10_R3C11_Vertical.clicked.connect(partial(self.addtodict,self.R3C10_R3C11_Vertical))

        #--------------------------------------------------------------------
        
        self.R4C2_R4C3_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R4C2_R4C3_Vertical.setGeometry(QtCore.QRect(94, 164, 8, 33))
        self.R4C2_R4C3_Vertical.setText("")
        self.R4C2_R4C3_Vertical.setObjectName("R4C2_R4C3_Vertical")
        self.R4C2_R4C3_Vertical.clicked.connect(partial(self.addtodict,self.R4C2_R4C3_Vertical))

        #--------------------------------------------------------------------
        
        self.R3C9_R3C10_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R3C9_R3C10_Vertical.setGeometry(QtCore.QRect(376, 114, 8, 33))
        self.R3C9_R3C10_Vertical.setText("")
        self.R3C9_R3C10_Vertical.setObjectName("R3C9_R3C10_Vertical")
        self.R3C9_R3C10_Vertical.clicked.connect(partial(self.addtodict,self.R3C9_R3C10_Vertical))

        #--------------------------------------------------------------------
        
        self.R10C5_R10C6_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R10C5_R10C6_Vertical.setGeometry(QtCore.QRect(215, 464, 8, 33))
        self.R10C5_R10C6_Vertical.setText("")
        self.R10C5_R10C6_Vertical.setObjectName("R10C5_R10C6_Vertical")
        self.R10C5_R10C6_Vertical.clicked.connect(partial(self.addtodict,self.R10C5_R10C6_Vertical))

        #--------------------------------------------------------------------
        
        self.R2C10_R2C11_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R2C10_R2C11_Vertical.setGeometry(QtCore.QRect(416, 64, 8, 33))
        self.R2C10_R2C11_Vertical.setText("")
        self.R2C10_R2C11_Vertical.setObjectName("R2C10_R2C11_Vertical")
        self.R2C10_R2C11_Vertical.clicked.connect(partial(self.addtodict,self.R2C10_R2C11_Vertical))

        #--------------------------------------------------------------------
        
        self.R12C12_R12C13_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R12C12_R12C13_Vertical.setGeometry(QtCore.QRect(497, 564, 8, 33))
        self.R12C12_R12C13_Vertical.setText("")
        self.R12C12_R12C13_Vertical.setObjectName("R12C12_R12C13_Vertical")
        self.R12C12_R12C13_Vertical.clicked.connect(partial(self.addtodict,self.R12C12_R12C13_Vertical))

        #--------------------------------------------------------------------
        
        self.R3C5_R3C6_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R3C5_R3C6_Vertical.setGeometry(QtCore.QRect(215, 114, 8, 33))
        self.R3C5_R3C6_Vertical.setText("")
        self.R3C5_R3C6_Vertical.setObjectName("R3C5_R3C6_Vertical")
        self.R3C5_R3C6_Vertical.clicked.connect(partial(self.addtodict,self.R3C5_R3C6_Vertical))

        #--------------------------------------------------------------------
        
        self.R13C7_R13C8_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R13C7_R13C8_Vertical.setGeometry(QtCore.QRect(296, 614, 8, 33))
        self.R13C7_R13C8_Vertical.setText("")
        self.R13C7_R13C8_Vertical.setObjectName("R13C7_R13C8_Vertical")
        self.R13C7_R13C8_Vertical.clicked.connect(partial(self.addtodict,self.R13C7_R13C8_Vertical))

        #--------------------------------------------------------------------
        
        self.Upper_14 = QtWidgets.QPushButton(self.centralwidget)
        self.Upper_14.setGeometry(QtCore.QRect(540, 10, 39, 8))
        self.Upper_14.setText("")
        self.Upper_14.setObjectName("Upper_14")
        self.Upper_14.setStyleSheet("background-color: red")
        self.Upper_14.setEnabled(False)
       
        #--------------------------------------------------------------------
        
        self.R7C9_R7C10_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R7C9_R7C10_Vertical.setGeometry(QtCore.QRect(376, 314, 8, 33))
        self.R7C9_R7C10_Vertical.setText("")
        self.R7C9_R7C10_Vertical.setObjectName("R7C9_R7C10_Vertical")
        self.R7C9_R7C10_Vertical.clicked.connect(partial(self.addtodict,self.R7C9_R7C10_Vertical))

        #--------------------------------------------------------------------
        
        self.R3C1_R4C1_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R3C1_R4C1_Horizontal.setGeometry(QtCore.QRect(20, 150, 39, 8))
        self.R3C1_R4C1_Horizontal.setText("")
        self.R3C1_R4C1_Horizontal.setObjectName("R3C1_R4C1_Horizontal")
        self.R3C1_R4C1_Horizontal.clicked.connect(partial(self.addtodict,self.R3C1_R4C1_Horizontal))

        #--------------------------------------------------------------------
        
        self.R7C12_R8C12_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R7C12_R8C12_Horizontal.setGeometry(QtCore.QRect(460, 350, 39, 8))
        self.R7C12_R8C12_Horizontal.setText("")
        self.R7C12_R8C12_Horizontal.setObjectName("R7C12_R8C12_Horizontal")
        self.R7C12_R8C12_Horizontal.clicked.connect(partial(self.addtodict,self.R7C12_R8C12_Horizontal))

        #--------------------------------------------------------------------
        
        self.R2C2_R3C2_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R2C2_R3C2_Horizontal.setGeometry(QtCore.QRect(60, 100, 39, 8))
        self.R2C2_R3C2_Horizontal.setText("")
        self.R2C2_R3C2_Horizontal.setObjectName("R2C2_R3C2_Horizontal")
        self.R2C2_R3C2_Horizontal.clicked.connect(partial(self.addtodict,self.R2C2_R3C2_Horizontal))

        #--------------------------------------------------------------------
        
        self.R6C12_R6C13_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R6C12_R6C13_Vertical.setGeometry(QtCore.QRect(497, 264, 8, 33))
        self.R6C12_R6C13_Vertical.setText("")
        self.R6C12_R6C13_Vertical.setObjectName("R6C12_R6C13_Vertical")
        self.R6C12_R6C13_Vertical.clicked.connect(partial(self.addtodict,self.R6C12_R6C13_Vertical))

        #--------------------------------------------------------------------
        
        self.Right_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Right_5.setGeometry(QtCore.QRect(570, 214, 8, 33))
        self.Right_5.setText("")
        self.Right_5.setObjectName("Right_5")
        self.Right_5.setStyleSheet("background-color: red")
        self.Right_5.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R10C3_R11C3_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R10C3_R11C3_Horizontal.setGeometry(QtCore.QRect(100, 500, 39, 8))
        self.R10C3_R11C3_Horizontal.setText("")
        self.R10C3_R11C3_Horizontal.setObjectName("R10C3_R11C3_Horizontal")
        self.R10C3_R11C3_Horizontal.clicked.connect(partial(self.addtodict,self.R10C3_R11C3_Horizontal))

        #--------------------------------------------------------------------
        
        self.R4C8_R4C9_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R4C8_R4C9_Vertical.setGeometry(QtCore.QRect(334, 164, 8, 33))
        self.R4C8_R4C9_Vertical.setText("")
        self.R4C8_R4C9_Vertical.setObjectName("R4C8_R4C9_Vertical")
        self.R4C8_R4C9_Vertical.clicked.connect(partial(self.addtodict,self.R4C8_R4C9_Vertical))

        #--------------------------------------------------------------------
        
        self.R6C4_R7C4_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R6C4_R7C4_Horizontal.setGeometry(QtCore.QRect(140, 300, 39, 8))
        self.R6C4_R7C4_Horizontal.setText("")
        self.R6C4_R7C4_Horizontal.setObjectName("R6C4_R7C4_Horizontal")
        self.R6C4_R7C4_Horizontal.clicked.connect(partial(self.addtodict,self.R6C4_R7C4_Horizontal))

        #--------------------------------------------------------------------
        
        self.R2C7_R2C8_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R2C7_R2C8_Vertical.setGeometry(QtCore.QRect(296, 64, 8, 33))
        self.R2C7_R2C8_Vertical.setText("")
        self.R2C7_R2C8_Vertical.setObjectName("R2C7_R2C8_Vertical")
        self.R2C7_R2C8_Vertical.clicked.connect(partial(self.addtodict,self.R2C7_R2C8_Vertical))

        #--------------------------------------------------------------------
        
        self.R14C13_R14C14_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R14C13_R14C14_Vertical.setGeometry(QtCore.QRect(530, 664, 8, 33))
        self.R14C13_R14C14_Vertical.setText("")
        self.R14C13_R14C14_Vertical.setObjectName("R14C13_R14C14_Vertical")
        self.R14C13_R14C14_Vertical.clicked.connect(partial(self.addtodict,self.R14C13_R14C14_Vertical))

        #--------------------------------------------------------------------
        
        self.R2C3_R2C4_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R2C3_R2C4_Vertical.setGeometry(QtCore.QRect(135, 64, 8, 33))
        self.R2C3_R2C4_Vertical.setText("")
        self.R2C3_R2C4_Vertical.setObjectName("R2C3_R2C4_Vertical")
        self.R2C3_R2C4_Vertical.clicked.connect(partial(self.addtodict,self.R2C3_R2C4_Vertical))

        #--------------------------------------------------------------------
        
        self.R7C11_R7C12_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R7C11_R7C12_Vertical.setGeometry(QtCore.QRect(455, 314, 8, 33))
        self.R7C11_R7C12_Vertical.setText("")
        self.R7C11_R7C12_Vertical.setObjectName("R7C11_R7C12_Vertical")
        self.R7C11_R7C12_Vertical.clicked.connect(partial(self.addtodict,self.R7C11_R7C12_Vertical))

        #--------------------------------------------------------------------
        
        self.R5C6_R6C6_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R5C6_R6C6_Horizontal.setGeometry(QtCore.QRect(220, 250, 39, 8))
        self.R5C6_R6C6_Horizontal.setText("")
        self.R5C6_R6C6_Horizontal.setObjectName("R5C6_R6C6_Horizontal")
        self.R5C6_R6C6_Horizontal.clicked.connect(partial(self.addtodict,self.R5C6_R6C6_Horizontal))

        #--------------------------------------------------------------------
        
        self.Right_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Right_1.setGeometry(QtCore.QRect(570, 20, 8, 33))
        self.Right_1.setText("")
        self.Right_1.setObjectName("Right_1")
        self.Right_1.setStyleSheet("background-color: red")
        self.Right_1.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R11C7_R12C7_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R11C7_R12C7_Horizontal.setGeometry(QtCore.QRect(260, 550, 39, 8))
        self.R11C7_R12C7_Horizontal.setText("")
        self.R11C7_R12C7_Horizontal.setObjectName("R11C7_R12C7_Horizontal")
        self.R11C7_R12C7_Horizontal.clicked.connect(partial(self.addtodict,self.R11C7_R12C7_Horizontal))

        #--------------------------------------------------------------------
        
        self.R13C9_R13C10_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R13C9_R13C10_Vertical.setGeometry(QtCore.QRect(376, 614, 8, 33))
        self.R13C9_R13C10_Vertical.setText("")
        self.R13C9_R13C10_Vertical.setObjectName("R13C9_R13C10_Vertical")
        self.R13C9_R13C10_Vertical.clicked.connect(partial(self.addtodict,self.R13C9_R13C10_Vertical))

        #--------------------------------------------------------------------
        
        self.R5C4_R5C5_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R5C4_R5C5_Vertical.setGeometry(QtCore.QRect(175, 214, 8, 33))
        self.R5C4_R5C5_Vertical.setText("")
        self.R5C4_R5C5_Vertical.setObjectName("R5C4_R5C5_Vertical")
        self.R5C4_R5C5_Vertical.clicked.connect(partial(self.addtodict,self.R5C4_R5C5_Vertical))

        #--------------------------------------------------------------------
        
        self.Upper_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Upper_5.setGeometry(QtCore.QRect(180, 10, 39, 8))
        self.Upper_5.setText("")
        self.Upper_5.setObjectName("Upper_5")
        self.Upper_5.setStyleSheet("background-color: red")
        self.Upper_5.setEnabled(False)
        
        #--------------------------------------------------------------------
        
        self.R9C14_R10C14_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R9C14_R10C14_Horizontal.setGeometry(QtCore.QRect(540, 450, 39, 8))
        self.R9C14_R10C14_Horizontal.setText("")
        self.R9C14_R10C14_Horizontal.setObjectName("R9C14_R10C14_Horizontal")
        self.R9C14_R10C14_Horizontal.clicked.connect(partial(self.addtodict,self.R9C14_R10C14_Horizontal))

        #--------------------------------------------------------------------
        
        self.R13C13_R13C14_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R13C13_R13C14_Vertical.setGeometry(QtCore.QRect(530, 614, 8, 33))
        self.R13C13_R13C14_Vertical.setText("")
        self.R13C13_R13C14_Vertical.setObjectName("R13C13_R13C14_Vertical")
        self.R13C13_R13C14_Vertical.clicked.connect(partial(self.addtodict,self.R13C13_R13C14_Vertical))

        #--------------------------------------------------------------------
        
        self.R12C4_R13C4_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R12C4_R13C4_Horizontal.setGeometry(QtCore.QRect(140, 600, 39, 8))
        self.R12C4_R13C4_Horizontal.setText("")
        self.R12C4_R13C4_Horizontal.setObjectName("R12C4_R13C4_Horizontal")
        self.R12C4_R13C4_Horizontal.clicked.connect(partial(self.addtodict,self.R12C4_R13C4_Horizontal))

        #--------------------------------------------------------------------
        
        self.R9C5_R9C6_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R9C5_R9C6_Vertical.setGeometry(QtCore.QRect(215, 414, 8, 33))
        self.R9C5_R9C6_Vertical.setText("")
        self.R9C5_R9C6_Vertical.setObjectName("R9C5_R9C6_Vertical")
        self.R9C5_R9C6_Vertical.clicked.connect(partial(self.addtodict,self.R9C5_R9C6_Vertical))

        #--------------------------------------------------------------------
        
        self.R6C3_R6C4_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R6C3_R6C4_Vertical.setGeometry(QtCore.QRect(135, 264, 8, 33))
        self.R6C3_R6C4_Vertical.setText("")
        self.R6C3_R6C4_Vertical.setObjectName("R6C3_R6C4_Vertical")
        self.R6C3_R6C4_Vertical.clicked.connect(partial(self.addtodict,self.R6C3_R6C4_Vertical))

        #--------------------------------------------------------------------
        
        self.R6C7_R7C7_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R6C7_R7C7_Horizontal.setGeometry(QtCore.QRect(260, 300, 39, 8))
        self.R6C7_R7C7_Horizontal.setText("")
        self.R6C7_R7C7_Horizontal.setObjectName("R6C7_R7C7_Horizontal")
        self.R6C7_R7C7_Horizontal.clicked.connect(partial(self.addtodict,self.R6C7_R7C7_Horizontal))

        #--------------------------------------------------------------------
        
        self.R3C7_R4C7_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R3C7_R4C7_Horizontal.setGeometry(QtCore.QRect(260, 150, 39, 8))
        self.R3C7_R4C7_Horizontal.setText("")
        self.R3C7_R4C7_Horizontal.setObjectName("R3C7_R4C7_Horizontal")
        self.R3C7_R4C7_Horizontal.clicked.connect(partial(self.addtodict,self.R3C7_R4C7_Horizontal))

        #--------------------------------------------------------------------
        
        self.R12C6_R13C6_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R12C6_R13C6_Horizontal.setGeometry(QtCore.QRect(220, 600, 39, 8))
        self.R12C6_R13C6_Horizontal.setText("")
        self.R12C6_R13C6_Horizontal.setObjectName("R12C6_R13C6_Horizontal")
        self.R12C6_R13C6_Horizontal.clicked.connect(partial(self.addtodict,self.R12C6_R13C6_Horizontal))

        #--------------------------------------------------------------------
        
        self.R14C8_R14C9_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R14C8_R14C9_Vertical.setGeometry(QtCore.QRect(334, 664, 8, 33))
        self.R14C8_R14C9_Vertical.setText("")
        self.R14C8_R14C9_Vertical.setObjectName("R14C8_R14C9_Vertical")
        self.R14C8_R14C9_Vertical.clicked.connect(partial(self.addtodict,self.R14C8_R14C9_Vertical))

        #--------------------------------------------------------------------
        
        self.R8C2_R9C2_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R8C2_R9C2_Horizontal.setGeometry(QtCore.QRect(60, 400, 39, 8))
        self.R8C2_R9C2_Horizontal.setText("")
        self.R8C2_R9C2_Horizontal.setObjectName("R8C2_R9C2_Horizontal")
        self.R8C2_R9C2_Horizontal.clicked.connect(partial(self.addtodict,self.R8C2_R9C2_Horizontal))

        #--------------------------------------------------------------------
        
        self.R2C9_R3C9_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R2C9_R3C9_Horizontal.setGeometry(QtCore.QRect(340, 100, 39, 8))
        self.R2C9_R3C9_Horizontal.setText("")
        self.R2C9_R3C9_Horizontal.setObjectName("R2C9_R3C9_Horizontal")
        self.R2C9_R3C9_Horizontal.clicked.connect(partial(self.addtodict,self.R2C9_R3C9_Horizontal))

        #--------------------------------------------------------------------
        
        self.R3C9_R4C9_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R3C9_R4C9_Horizontal.setGeometry(QtCore.QRect(340, 150, 39, 8))
        self.R3C9_R4C9_Horizontal.setText("")
        self.R3C9_R4C9_Horizontal.setObjectName("R3C9_R4C9_Horizontal")
        self.R3C9_R4C9_Horizontal.clicked.connect(partial(self.addtodict,self.R3C9_R4C9_Horizontal))

        #--------------------------------------------------------------------
        
        self.R9C1_R10C1_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R9C1_R10C1_Horizontal.setGeometry(QtCore.QRect(20, 450, 39, 8))
        self.R9C1_R10C1_Horizontal.setText("")
        self.R9C1_R10C1_Horizontal.setObjectName("R9C1_R10C1_Horizontal")
        self.R9C1_R10C1_Horizontal.clicked.connect(partial(self.addtodict,self.R9C1_R10C1_Horizontal))

        #--------------------------------------------------------------------
        
        self.R11C2_R11C3_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R11C2_R11C3_Vertical.setGeometry(QtCore.QRect(94, 514, 8, 33))
        self.R11C2_R11C3_Vertical.setText("")
        self.R11C2_R11C3_Vertical.setObjectName("R11C2_R11C3_Vertical")
        self.R11C2_R11C3_Vertical.clicked.connect(partial(self.addtodict,self.R11C2_R11C3_Vertical))

        #--------------------------------------------------------------------
        
        self.R5C2_R6C2_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R5C2_R6C2_Horizontal.setGeometry(QtCore.QRect(60, 250, 39, 8))
        self.R5C2_R6C2_Horizontal.setText("")
        self.R5C2_R6C2_Horizontal.setObjectName("R5C2_R6C2_Horizontal")
        self.R5C2_R6C2_Horizontal.clicked.connect(partial(self.addtodict,self.R5C2_R6C2_Horizontal))

        #--------------------------------------------------------------------
        
        self.R1C7_R2C7_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R1C7_R2C7_Horizontal.setGeometry(QtCore.QRect(260, 56, 39, 8))
        self.R1C7_R2C7_Horizontal.setText("")
        self.R1C7_R2C7_Horizontal.setObjectName("R1C7_R2C7_Horizontal")
        self.R1C7_R2C7_Horizontal.clicked.connect(partial(self.addtodict,self.R1C7_R2C7_Horizontal))

        #--------------------------------------------------------------------
        
        self.Left_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Left_5.setGeometry(QtCore.QRect(20, 214, 8, 33))
        self.Left_5.setText("")
        self.Left_5.setObjectName("Left_5")
        self.Left_5.setStyleSheet("background-color: red")
        self.Left_5.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R2C4_R3C4_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R2C4_R3C4_Horizontal.setGeometry(QtCore.QRect(140, 100, 39, 8))
        self.R2C4_R3C4_Horizontal.setText("")
        self.R2C4_R3C4_Horizontal.setObjectName("R2C4_R3C4_Horizontal")
        self.R2C4_R3C4_Horizontal.clicked.connect(partial(self.addtodict,self.R2C4_R3C4_Horizontal))

        #--------------------------------------------------------------------
        
        self.R4C10_R5C10_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R4C10_R5C10_Horizontal.setGeometry(QtCore.QRect(380, 200, 39, 8))
        self.R4C10_R5C10_Horizontal.setText("")
        self.R4C10_R5C10_Horizontal.setObjectName("R4C10_R5C10_Horizontal")
        self.R4C10_R5C10_Horizontal.clicked.connect(partial(self.addtodict,self.R4C10_R5C10_Horizontal))

        #--------------------------------------------------------------------
        
        self.R9C2_R9C3_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R9C2_R9C3_Vertical.setGeometry(QtCore.QRect(94, 414, 8, 33))
        self.R9C2_R9C3_Vertical.setText("")
        self.R9C2_R9C3_Vertical.setObjectName("R9C2_R9C3_Vertical")
        self.R9C2_R9C3_Vertical.clicked.connect(partial(self.addtodict,self.R9C2_R9C3_Vertical))

        #--------------------------------------------------------------------
        
        self.R6C6_R7C6_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R6C6_R7C6_Horizontal.setGeometry(QtCore.QRect(220, 300, 39, 8))
        self.R6C6_R7C6_Horizontal.setText("")
        self.R6C6_R7C6_Horizontal.setObjectName("R6C6_R7C6_Horizontal")
        self.R6C6_R7C6_Horizontal.clicked.connect(partial(self.addtodict,self.R6C6_R7C6_Horizontal))

        #--------------------------------------------------------------------
        
        self.R8C10_R8C11_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R8C10_R8C11_Vertical.setGeometry(QtCore.QRect(416, 364, 8, 33))
        self.R8C10_R8C11_Vertical.setText("")
        self.R8C10_R8C11_Vertical.setObjectName("R8C10_R8C11_Vertical")
        self.R8C10_R8C11_Vertical.clicked.connect(partial(self.addtodict,self.R8C10_R8C11_Vertical))

        #--------------------------------------------------------------------
        
        self.Right_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Right_3.setGeometry(QtCore.QRect(570, 114, 8, 33))
        self.Right_3.setText("")
        self.Right_3.setObjectName("Right_3")
        self.Right_3.setStyleSheet("background-color: red")
        self.Right_3.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R13C3_R13C4_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R13C3_R13C4_Vertical.setGeometry(QtCore.QRect(135, 614, 8, 33))
        self.R13C3_R13C4_Vertical.setText("")
        self.R13C3_R13C4_Vertical.setObjectName("R13C3_R13C4_Vertical")
        self.R13C3_R13C4_Vertical.clicked.connect(partial(self.addtodict,self.R13C3_R13C4_Vertical))

        #--------------------------------------------------------------------
        
        self.R10C4_R11C4_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R10C4_R11C4_Horizontal.setGeometry(QtCore.QRect(140, 500, 39, 8))
        self.R10C4_R11C4_Horizontal.setText("")
        self.R10C4_R11C4_Horizontal.setObjectName("R10C4_R11C4_Horizontal")
        self.R10C4_R11C4_Horizontal.clicked.connect(partial(self.addtodict,self.R10C4_R11C4_Horizontal))

        #--------------------------------------------------------------------
        
        self.Lower_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Lower_9.setGeometry(QtCore.QRect(340, 700, 39, 8))
        self.Lower_9.setText("")
        self.Lower_9.setObjectName("Lower_9")
        self.Lower_9.setStyleSheet("background-color: red")
        self.Lower_9.setEnabled(False)
        
        #--------------------------------------------------------------------
        
        self.R5C13_R5C14_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R5C13_R5C14_Vertical.setGeometry(QtCore.QRect(530, 214, 8, 33))
        self.R5C13_R5C14_Vertical.setText("")
        self.R5C13_R5C14_Vertical.setObjectName("R5C13_R5C14_Vertical")
        self.R5C13_R5C14_Vertical.clicked.connect(partial(self.addtodict,self.R5C13_R5C14_Vertical))

        #--------------------------------------------------------------------
        
        self.R11C9_R12C9_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R11C9_R12C9_Horizontal.setGeometry(QtCore.QRect(340, 550, 39, 8))
        self.R11C9_R12C9_Horizontal.setText("")
        self.R11C9_R12C9_Horizontal.setObjectName("R11C9_R12C9_Horizontal")
        self.R11C9_R12C9_Horizontal.clicked.connect(partial(self.addtodict,self.R11C9_R12C9_Horizontal))

        #--------------------------------------------------------------------
        
        self.R5C10_R6C10_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R5C10_R6C10_Horizontal.setGeometry(QtCore.QRect(380, 250, 39, 8))
        self.R5C10_R6C10_Horizontal.setText("")
        self.R5C10_R6C10_Horizontal.setObjectName("R5C10_R6C10_Horizontal")
        self.R5C10_R6C10_Horizontal.clicked.connect(partial(self.addtodict,self.R5C10_R6C10_Horizontal))

        #--------------------------------------------------------------------
        
        self.R10C10_R11C10_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R10C10_R11C10_Horizontal.setGeometry(QtCore.QRect(380, 500, 39, 8))
        self.R10C10_R11C10_Horizontal.setText("")
        self.R10C10_R11C10_Horizontal.setObjectName("R10C10_R11C10_Horizontal")
        self.R10C10_R11C10_Horizontal.clicked.connect(partial(self.addtodict,self.R10C10_R11C10_Horizontal))

        #--------------------------------------------------------------------
        
        self.R12C1_R12C2_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R12C1_R12C2_Vertical.setGeometry(QtCore.QRect(54, 564, 8, 33))
        self.R12C1_R12C2_Vertical.setText("")
        self.R12C1_R12C2_Vertical.setObjectName("R12C1_R12C2_Vertical")
        self.R12C1_R12C2_Vertical.clicked.connect(partial(self.addtodict,self.R12C1_R12C2_Vertical))

        #--------------------------------------------------------------------
        
        self.R12C5_R13C5_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R12C5_R13C5_Horizontal.setGeometry(QtCore.QRect(180, 600, 39, 8))
        self.R12C5_R13C5_Horizontal.setText("")
        self.R12C5_R13C5_Horizontal.setObjectName("R12C5_R13C5_Horizontal")
        self.R12C5_R13C5_Horizontal.clicked.connect(partial(self.addtodict,self.R12C5_R13C5_Horizontal))

        #--------------------------------------------------------------------
        
        self.R4C11_R4C12_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R4C11_R4C12_Vertical.setGeometry(QtCore.QRect(455, 164, 8, 33))
        self.R4C11_R4C12_Vertical.setText("")
        self.R4C11_R4C12_Vertical.setObjectName("R4C11_R4C12_Vertical")
        self.R4C11_R4C12_Vertical.clicked.connect(partial(self.addtodict,self.R4C11_R4C12_Vertical))

        #--------------------------------------------------------------------
        
        self.R8C12_R9C12_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R8C12_R9C12_Horizontal.setGeometry(QtCore.QRect(460, 400, 39, 8))
        self.R8C12_R9C12_Horizontal.setText("")
        self.R8C12_R9C12_Horizontal.setObjectName("R8C12_R9C12_Horizontal")
        self.R8C12_R9C12_Horizontal.clicked.connect(partial(self.addtodict,self.R8C12_R9C12_Horizontal))

        #--------------------------------------------------------------------
        
        self.R4C12_R4C13_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R4C12_R4C13_Vertical.setGeometry(QtCore.QRect(497, 164, 8, 33))
        self.R4C12_R4C13_Vertical.setText("")
        self.R4C12_R4C13_Vertical.setObjectName("R4C12_R4C13_Vertical")
        self.R4C12_R4C13_Vertical.clicked.connect(partial(self.addtodict,self.R4C12_R4C13_Vertical))

        #--------------------------------------------------------------------
        
        self.Lower_14 = QtWidgets.QPushButton(self.centralwidget)
        self.Lower_14.setGeometry(QtCore.QRect(540, 700, 39, 8))
        self.Lower_14.setText("")
        self.Lower_14.setObjectName("Lower_14")
        self.Lower_14.setStyleSheet("background-color: red")
        self.Lower_14.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R5C4_R6C4_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R5C4_R6C4_Horizontal.setGeometry(QtCore.QRect(140, 250, 39, 8))
        self.R5C4_R6C4_Horizontal.setText("")
        self.R5C4_R6C4_Horizontal.setObjectName("R5C4_R6C4_Horizontal")
        self.R5C4_R6C4_Horizontal.clicked.connect(partial(self.addtodict,self.R5C4_R6C4_Horizontal))

        #--------------------------------------------------------------------
        
        self.R6C9_R7C9_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R6C9_R7C9_Horizontal.setGeometry(QtCore.QRect(340, 300, 39, 8))
        self.R6C9_R7C9_Horizontal.setText("")
        self.R6C9_R7C9_Horizontal.setObjectName("R6C9_R7C9_Horizontal")
        self.R6C9_R7C9_Horizontal.clicked.connect(partial(self.addtodict,self.R6C9_R7C9_Horizontal))

        #--------------------------------------------------------------------
        
        self.R11C12_R11C13_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R11C12_R11C13_Vertical.setGeometry(QtCore.QRect(497, 514, 8, 33))
        self.R11C12_R11C13_Vertical.setText("")
        self.R11C12_R11C13_Vertical.setObjectName("R11C12_R11C13_Vertical")
        self.R11C12_R11C13_Vertical.clicked.connect(partial(self.addtodict,self.R11C12_R11C13_Vertical))

        #--------------------------------------------------------------------
        
        self.R7C1_R7C2_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R7C1_R7C2_Vertical.setGeometry(QtCore.QRect(54, 314, 8, 33))
        self.R7C1_R7C2_Vertical.setText("")
        self.R7C1_R7C2_Vertical.setObjectName("R7C1_R7C2_Vertical")
        self.R7C1_R7C2_Vertical.clicked.connect(partial(self.addtodict,self.R7C1_R7C2_Vertical))

        #--------------------------------------------------------------------
        
        self.Right_11 = QtWidgets.QPushButton(self.centralwidget)
        self.Right_11.setGeometry(QtCore.QRect(570, 514, 8, 33))
        self.Right_11.setText("")
        self.Right_11.setObjectName("Right_11")
        self.Right_11.setStyleSheet("background-color: red")
        self.Right_11.setEnabled(False)
        
        #--------------------------------------------------------------------
        
        self.R6C5_R7C5_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R6C5_R7C5_Horizontal.setGeometry(QtCore.QRect(180, 300, 39, 8))
        self.R6C5_R7C5_Horizontal.setText("")
        self.R6C5_R7C5_Horizontal.setObjectName("R6C5_R7C5_Horizontal")
        self.R6C5_R7C5_Horizontal.clicked.connect(partial(self.addtodict,self.R6C5_R7C5_Horizontal))

        #--------------------------------------------------------------------
        
        self.R13C8_R13C9_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R13C8_R13C9_Vertical.setGeometry(QtCore.QRect(334, 614, 8, 33))
        self.R13C8_R13C9_Vertical.setText("")
        self.R13C8_R13C9_Vertical.setObjectName("R13C8_R13C9_Vertical")
        self.R13C8_R13C9_Vertical.clicked.connect(partial(self.addtodict,self.R13C8_R13C9_Vertical))

        #--------------------------------------------------------------------
        
        self.R7C7_R8C7_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R7C7_R8C7_Horizontal.setGeometry(QtCore.QRect(260, 350, 39, 8))
        self.R7C7_R8C7_Horizontal.setText("")
        self.R7C7_R8C7_Horizontal.setObjectName("R7C7_R8C7_Horizontal")
        self.R7C7_R8C7_Horizontal.clicked.connect(partial(self.addtodict,self.R7C7_R8C7_Horizontal))

        #--------------------------------------------------------------------
        
        self.Left_11 = QtWidgets.QPushButton(self.centralwidget)
        self.Left_11.setGeometry(QtCore.QRect(20, 514, 8, 33))
        self.Left_11.setText("")
        self.Left_11.setObjectName("Left_11")
        self.Left_11.setStyleSheet("background-color: red")
        self.Left_11.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.Lower_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Lower_5.setGeometry(QtCore.QRect(180, 700, 39, 8))
        self.Lower_5.setText("")
        self.Lower_5.setObjectName("Lower_5")
        self.Lower_5.setStyleSheet("background-color: red")
        self.Lower_5.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R10C13_R11C13_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R10C13_R11C13_Horizontal.setGeometry(QtCore.QRect(500, 500, 39, 8))
        self.R10C13_R11C13_Horizontal.setText("")
        self.R10C13_R11C13_Horizontal.setObjectName("R10C13_R11C13_Horizontal")
        self.R10C13_R11C13_Horizontal.clicked.connect(partial(self.addtodict,self.R10C13_R11C13_Horizontal))

        #--------------------------------------------------------------------
        
        self.R6C4_R6C5_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R6C4_R6C5_Vertical.setGeometry(QtCore.QRect(175, 264, 8, 33))
        self.R6C4_R6C5_Vertical.setText("")
        self.R6C4_R6C5_Vertical.setObjectName("R6C4_R6C5_Vertical")
        self.R6C4_R6C5_Vertical.clicked.connect(partial(self.addtodict,self.R6C4_R6C5_Vertical))

        #--------------------------------------------------------------------
        
        self.R5C5_R5C6_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R5C5_R5C6_Vertical.setGeometry(QtCore.QRect(215, 214, 8, 33))
        self.R5C5_R5C6_Vertical.setText("")
        self.R5C5_R5C6_Vertical.setObjectName("R5C5_R5C6_Vertical")
        self.R5C5_R5C6_Vertical.clicked.connect(partial(self.addtodict,self.R5C5_R5C6_Vertical))

        #--------------------------------------------------------------------
        
        self.R14C2_R14C3_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R14C2_R14C3_Vertical.setGeometry(QtCore.QRect(94, 664, 8, 33))
        self.R14C2_R14C3_Vertical.setText("")
        self.R14C2_R14C3_Vertical.setObjectName("R14C2_R14C3_Vertical")
        self.R14C2_R14C3_Vertical.clicked.connect(partial(self.addtodict,self.R14C2_R14C3_Vertical))

        #--------------------------------------------------------------------
        
        self.R4C6_R4C7_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R4C6_R4C7_Vertical.setGeometry(QtCore.QRect(256, 164, 8, 33))
        self.R4C6_R4C7_Vertical.setText("")
        self.R4C6_R4C7_Vertical.setObjectName("R4C6_R4C7_Vertical")
        self.R4C6_R4C7_Vertical.clicked.connect(partial(self.addtodict,self.R4C6_R4C7_Vertical))

        #--------------------------------------------------------------------
        
        self.R8C5_R8C6_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R8C5_R8C6_Vertical.setGeometry(QtCore.QRect(215, 364, 8, 33))
        self.R8C5_R8C6_Vertical.setText("")
        self.R8C5_R8C6_Vertical.setObjectName("R8C5_R8C6_Vertical")
        self.R8C5_R8C6_Vertical.clicked.connect(partial(self.addtodict,self.R8C5_R8C6_Vertical))

        #--------------------------------------------------------------------
        
        self.R9C7_R10C7_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R9C7_R10C7_Horizontal.setGeometry(QtCore.QRect(260, 450, 39, 8))
        self.R9C7_R10C7_Horizontal.setText("")
        self.R9C7_R10C7_Horizontal.setObjectName("R9C7_R10C7_Horizontal")
        self.R9C7_R10C7_Horizontal.clicked.connect(partial(self.addtodict,self.R9C7_R10C7_Horizontal))

        #--------------------------------------------------------------------
        
        self.R7C7_R7C8_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R7C7_R7C8_Vertical.setGeometry(QtCore.QRect(296, 314, 8, 33))
        self.R7C7_R7C8_Vertical.setText("")
        self.R7C7_R7C8_Vertical.setObjectName("R7C7_R7C8_Vertical")
        self.R7C7_R7C8_Vertical.clicked.connect(partial(self.addtodict,self.R7C7_R7C8_Vertical))

        #--------------------------------------------------------------------
        
        self.R6C9_R6C10_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R6C9_R6C10_Vertical.setGeometry(QtCore.QRect(376, 264, 8, 33))
        self.R6C9_R6C10_Vertical.setText("")
        self.R6C9_R6C10_Vertical.setObjectName("R6C9_R6C10_Vertical")
        self.R6C9_R6C10_Vertical.clicked.connect(partial(self.addtodict,self.R6C9_R6C10_Vertical))

        #--------------------------------------------------------------------
        
        self.R3C4_R3C5_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R3C4_R3C5_Vertical.setGeometry(QtCore.QRect(175, 114, 8, 33))
        self.R3C4_R3C5_Vertical.setText("")
        self.R3C4_R3C5_Vertical.setObjectName("R3C4_R3C5_Vertical")
        self.R3C4_R3C5_Vertical.clicked.connect(partial(self.addtodict,self.R3C4_R3C5_Vertical))

        #--------------------------------------------------------------------
        
        self.R13C5_R13C6_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R13C5_R13C6_Vertical.setGeometry(QtCore.QRect(215, 614, 8, 33))
        self.R13C5_R13C6_Vertical.setText("")
        self.R13C5_R13C6_Vertical.setObjectName("R13C5_R13C6_Vertical")
        self.R13C5_R13C6_Vertical.clicked.connect(partial(self.addtodict,self.R13C5_R13C6_Vertical))

        #--------------------------------------------------------------------
        
        self.R5C12_R6C12_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R5C12_R6C12_Horizontal.setGeometry(QtCore.QRect(460, 250, 39, 8))
        self.R5C12_R6C12_Horizontal.setText("")
        self.R5C12_R6C12_Horizontal.setObjectName("R5C12_R6C12_Horizontal")
        self.R5C12_R6C12_Horizontal.clicked.connect(partial(self.addtodict,self.R5C12_R6C12_Horizontal))

        #--------------------------------------------------------------------
        
        self.R2C7_R3C7_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R2C7_R3C7_Horizontal.setGeometry(QtCore.QRect(260, 100, 39, 8))
        self.R2C7_R3C7_Horizontal.setText("")
        self.R2C7_R3C7_Horizontal.setObjectName("R2C7_R3C7_Horizontal")
        self.R2C7_R3C7_Horizontal.clicked.connect(partial(self.addtodict,self.R2C7_R3C7_Horizontal))

        #--------------------------------------------------------------------
        
        self.R11C13_R11C14_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R11C13_R11C14_Vertical.setGeometry(QtCore.QRect(530, 514, 8, 33))
        self.R11C13_R11C14_Vertical.setText("")
        self.R11C13_R11C14_Vertical.setObjectName("R11C13_R11C14_Vertical")
        self.R11C13_R11C14_Vertical.clicked.connect(partial(self.addtodict,self.R11C13_R11C14_Vertical))

        #--------------------------------------------------------------------
        
        self.Right_10 = QtWidgets.QPushButton(self.centralwidget)
        self.Right_10.setGeometry(QtCore.QRect(570, 464, 8, 33))
        self.Right_10.setText("")
        self.Right_10.setObjectName("Right_10")
        self.Right_10.setStyleSheet("background-color: red")
        self.Right_10.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R12C11_R12C12_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R12C11_R12C12_Vertical.setGeometry(QtCore.QRect(455, 564, 8, 33))
        self.R12C11_R12C12_Vertical.setText("")
        self.R12C11_R12C12_Vertical.setObjectName("R12C11_R12C12_Vertical")
        self.R12C11_R12C12_Vertical.clicked.connect(partial(self.addtodict,self.R12C11_R12C12_Vertical))

        #--------------------------------------------------------------------
        
        self.R6C2_R7C2_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R6C2_R7C2_Horizontal.setGeometry(QtCore.QRect(60, 300, 39, 8))
        self.R6C2_R7C2_Horizontal.setText("")
        self.R6C2_R7C2_Horizontal.setObjectName("R6C2_R7C2_Horizontal")
        self.R6C2_R7C2_Horizontal.clicked.connect(partial(self.addtodict,self.R6C2_R7C2_Horizontal))

        #--------------------------------------------------------------------
        
        self.Upper_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Upper_6.setGeometry(QtCore.QRect(220, 10, 39, 8))
        self.Upper_6.setText("")
        self.Upper_6.setObjectName("Upper_6")
        self.Upper_6.setStyleSheet("background-color: red")
        self.Upper_6.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R9C12_R9C13_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R9C12_R9C13_Vertical.setGeometry(QtCore.QRect(497, 414, 8, 33))
        self.R9C12_R9C13_Vertical.setText("")
        self.R9C12_R9C13_Vertical.setObjectName("R9C12_R9C13_Vertical")
        self.R9C12_R9C13_Vertical.clicked.connect(partial(self.addtodict,self.R9C12_R9C13_Vertical))

        #--------------------------------------------------------------------
        
        self.R7C10_R7C11_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R7C10_R7C11_Vertical.setGeometry(QtCore.QRect(416, 314, 8, 33))
        self.R7C10_R7C11_Vertical.setText("")
        self.R7C10_R7C11_Vertical.setObjectName("R7C10_R7C11_Vertical")
        self.R7C10_R7C11_Vertical.clicked.connect(partial(self.addtodict,self.R7C10_R7C11_Vertical))

        #--------------------------------------------------------------------
        
        self.Lower_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Lower_8.setGeometry(QtCore.QRect(300, 700, 39, 8))
        self.Lower_8.setText("")
        self.Lower_8.setObjectName("Lower_8")
        self.Lower_8.setStyleSheet("background-color: red")
        self.Lower_8.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R11C11_R11C12_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R11C11_R11C12_Vertical.setGeometry(QtCore.QRect(455, 514, 8, 33))
        self.R11C11_R11C12_Vertical.setText("")
        self.R11C11_R11C12_Vertical.setObjectName("R11C11_R11C12_Vertical")
        self.R11C11_R11C12_Vertical.clicked.connect(partial(self.addtodict,self.R11C11_R11C12_Vertical))

        #--------------------------------------------------------------------
        
        self.R13C9_R14C9_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R13C9_R14C9_Horizontal.setGeometry(QtCore.QRect(340, 650, 39, 8))
        self.R13C9_R14C9_Horizontal.setText("")
        self.R13C9_R14C9_Horizontal.setObjectName("R13C9_R14C9_Horizontal")
        self.R13C9_R14C9_Horizontal.clicked.connect(partial(self.addtodict,self.R13C9_R14C9_Horizontal))

        #--------------------------------------------------------------------
        
        self.Left_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Left_6.setGeometry(QtCore.QRect(20, 264, 8, 33))
        self.Left_6.setText("")
        self.Left_6.setObjectName("Left_6")
        self.Left_6.setStyleSheet("background-color: red")
        self.Left_6.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R9C5_R10C5_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R9C5_R10C5_Horizontal.setGeometry(QtCore.QRect(180, 450, 39, 8))
        self.R9C5_R10C5_Horizontal.setText("")
        self.R9C5_R10C5_Horizontal.setObjectName("R9C5_R10C5_Horizontal")
        self.R9C5_R10C5_Horizontal.clicked.connect(partial(self.addtodict,self.R9C5_R10C5_Horizontal))

        #--------------------------------------------------------------------
        
        self.R13C2_R14C2_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R13C2_R14C2_Horizontal.setGeometry(QtCore.QRect(60, 650, 39, 8))
        self.R13C2_R14C2_Horizontal.setText("")
        self.R13C2_R14C2_Horizontal.setObjectName("R13C2_R14C2_Horizontal")
        self.R13C2_R14C2_Horizontal.clicked.connect(partial(self.addtodict,self.R13C2_R14C2_Horizontal))

        #--------------------------------------------------------------------
        
        self.Left_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Left_8.setGeometry(QtCore.QRect(20, 364, 8, 33))
        self.Left_8.setText("")
        self.Left_8.setObjectName("Left_8")
        self.Left_8.setStyleSheet("background-color: red")
        self.Left_8.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R5C8_R5C9_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R5C8_R5C9_Vertical.setGeometry(QtCore.QRect(334, 214, 8, 33))
        self.R5C8_R5C9_Vertical.setText("")
        self.R5C8_R5C9_Vertical.setObjectName("R5C8_R5C9_Vertical")
        self.R5C8_R5C9_Vertical.clicked.connect(partial(self.addtodict,self.R5C8_R5C9_Vertical))

        #--------------------------------------------------------------------
        
        self.R3C5_R4C5_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R3C5_R4C5_Horizontal.setGeometry(QtCore.QRect(180, 150, 39, 8))
        self.R3C5_R4C5_Horizontal.setText("")
        self.R3C5_R4C5_Horizontal.setObjectName("R3C5_R4C5_Horizontal")
        self.R3C5_R4C5_Horizontal.clicked.connect(partial(self.addtodict,self.R3C5_R4C5_Horizontal))

        #--------------------------------------------------------------------
        
        self.R10C12_R11C12_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R10C12_R11C12_Horizontal.setGeometry(QtCore.QRect(460, 500, 39, 8))
        self.R10C12_R11C12_Horizontal.setText("")
        self.R10C12_R11C12_Horizontal.setObjectName("R10C12_R11C12_Horizontal")
        self.R10C12_R11C12_Horizontal.clicked.connect(partial(self.addtodict,self.R10C12_R11C12_Horizontal))

        #--------------------------------------------------------------------
        
        self.R2C12_R2C13_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R2C12_R2C13_Vertical.setGeometry(QtCore.QRect(497, 64, 8, 33))
        self.R2C12_R2C13_Vertical.setText("")
        self.R2C12_R2C13_Vertical.setObjectName("R2C12_R2C13_Vertical")
        self.R2C12_R2C13_Vertical.clicked.connect(partial(self.addtodict,self.R2C12_R2C13_Vertical))

        #--------------------------------------------------------------------
        
        self.R13C12_R14C12_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R13C12_R14C12_Horizontal.setGeometry(QtCore.QRect(460, 650, 39, 8))
        self.R13C12_R14C12_Horizontal.setText("")
        self.R13C12_R14C12_Horizontal.setObjectName("R13C12_R14C12_Horizontal")
        self.R13C12_R14C12_Horizontal.clicked.connect(partial(self.addtodict,self.R13C12_R14C12_Horizontal))

        #--------------------------------------------------------------------
        
        self.R5C13_R6C13_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R5C13_R6C13_Horizontal.setGeometry(QtCore.QRect(500, 250, 39, 8))
        self.R5C13_R6C13_Horizontal.setText("")
        self.R5C13_R6C13_Horizontal.setObjectName("R5C13_R6C13_Horizontal")
        self.R5C13_R6C13_Horizontal.clicked.connect(partial(self.addtodict,self.R5C13_R6C13_Horizontal))

        #--------------------------------------------------------------------
        
        self.R8C13_R9C13_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R8C13_R9C13_Horizontal.setGeometry(QtCore.QRect(500, 400, 39, 8))
        self.R8C13_R9C13_Horizontal.setText("")
        self.R8C13_R9C13_Horizontal.setObjectName("R8C13_R9C13_Horizontal")
        self.R8C13_R9C13_Horizontal.clicked.connect(partial(self.addtodict,self.R8C13_R9C13_Horizontal))

        #--------------------------------------------------------------------
        
        self.Left_13 = QtWidgets.QPushButton(self.centralwidget)
        self.Left_13.setGeometry(QtCore.QRect(20, 614, 8, 33))
        self.Left_13.setText("")
        self.Left_13.setObjectName("Left_13")
        self.Left_13.setStyleSheet("background-color: red")
        self.Left_13.setEnabled(False)
        

        #--------------------------------------------------------------------
        
        self.R11C11_R12C11_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R11C11_R12C11_Horizontal.setGeometry(QtCore.QRect(420, 550, 39, 8))
        self.R11C11_R12C11_Horizontal.setText("")
        self.R11C11_R12C11_Horizontal.setObjectName("R11C11_R12C11_Horizontal")
        self.R11C11_R12C11_Horizontal.clicked.connect(partial(self.addtodict,self.R11C11_R12C11_Horizontal))

        #--------------------------------------------------------------------
        
        self.R11C8_R12C8_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R11C8_R12C8_Horizontal.setGeometry(QtCore.QRect(300, 550, 39, 8))
        self.R11C8_R12C8_Horizontal.setText("")
        self.R11C8_R12C8_Horizontal.setObjectName("R11C8_R12C8_Horizontal")
        self.R11C8_R12C8_Horizontal.clicked.connect(partial(self.addtodict,self.R11C8_R12C8_Horizontal))

        #--------------------------------------------------------------------
        
        self.R7C6_R8C6_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R7C6_R8C6_Horizontal.setGeometry(QtCore.QRect(220, 350, 39, 8))
        self.R7C6_R8C6_Horizontal.setText("")
        self.R7C6_R8C6_Horizontal.setObjectName("R7C6_R8C6_Horizontal")
        self.R7C6_R8C6_Horizontal.clicked.connect(partial(self.addtodict,self.R7C6_R8C6_Horizontal))

        #--------------------------------------------------------------------
        
        self.Lower_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Lower_4.setGeometry(QtCore.QRect(140, 700, 39, 8))
        self.Lower_4.setText("")
        self.Lower_4.setObjectName("Lower_4")
        self.Lower_4.setStyleSheet("background-color: red")
        self.Lower_4.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R4C3_R4C4_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R4C3_R4C4_Vertical.setGeometry(QtCore.QRect(135, 164, 8, 33))
        self.R4C3_R4C4_Vertical.setText("")
        self.R4C3_R4C4_Vertical.setObjectName("R4C3_R4C4_Vertical")
        self.R4C3_R4C4_Vertical.clicked.connect(partial(self.addtodict,self.R4C3_R4C4_Vertical))

        #--------------------------------------------------------------------
        
        self.R11C6_R12C6_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R11C6_R12C6_Horizontal.setGeometry(QtCore.QRect(220, 550, 39, 8))
        self.R11C6_R12C6_Horizontal.setText("")
        self.R11C6_R12C6_Horizontal.setObjectName("R11C6_R12C6_Horizontal")
        self.R11C6_R12C6_Horizontal.clicked.connect(partial(self.addtodict,self.R11C6_R12C6_Horizontal))

        #--------------------------------------------------------------------
        
        self.R8C10_R9C10_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R8C10_R9C10_Horizontal.setGeometry(QtCore.QRect(380, 400, 39, 8))
        self.R8C10_R9C10_Horizontal.setText("")
        self.R8C10_R9C10_Horizontal.setObjectName("R8C10_R9C10_Horizontal")
        self.R8C10_R9C10_Horizontal.clicked.connect(partial(self.addtodict,self.R8C10_R9C10_Horizontal))

        #--------------------------------------------------------------------
        
        self.R14C11_R14C12_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R14C11_R14C12_Vertical.setGeometry(QtCore.QRect(455, 664, 8, 33))
        self.R14C11_R14C12_Vertical.setText("")
        self.R14C11_R14C12_Vertical.setObjectName("R14C11_R14C12_Vertical")
        self.R14C11_R14C12_Vertical.clicked.connect(partial(self.addtodict,self.R14C11_R14C12_Vertical))

        #--------------------------------------------------------------------
        
        self.Right_12 = QtWidgets.QPushButton(self.centralwidget)
        self.Right_12.setGeometry(QtCore.QRect(570, 564, 8, 33))
        self.Right_12.setText("")
        self.Right_12.setObjectName("Right_12")
        self.Right_12.setStyleSheet("background-color: red")
        self.Right_12.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R11C13_R12C13_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R11C13_R12C13_Horizontal.setGeometry(QtCore.QRect(500, 550, 39, 8))
        self.R11C13_R12C13_Horizontal.setText("")
        self.R11C13_R12C13_Horizontal.setObjectName("R11C13_R12C13_Horizontal")
        self.R11C13_R12C13_Horizontal.clicked.connect(partial(self.addtodict,self.R11C13_R12C13_Horizontal))

        #--------------------------------------------------------------------
        
        self.R1C2_R2C2_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R1C2_R2C2_Horizontal.setGeometry(QtCore.QRect(60, 56, 39, 8))
        self.R1C2_R2C2_Horizontal.setText("")
        self.R1C2_R2C2_Horizontal.setObjectName("R1C2_R2C2_Horizontal")
        self.R1C2_R2C2_Horizontal.clicked.connect(partial(self.addtodict,self.R1C2_R2C2_Horizontal))

        #--------------------------------------------------------------------
        
        self.R4C9_R4C10_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R4C9_R4C10_Vertical.setGeometry(QtCore.QRect(376, 164, 8, 33))
        self.R4C9_R4C10_Vertical.setText("")
        self.R4C9_R4C10_Vertical.setObjectName("R4C9_R4C10_Vertical")
        self.R4C9_R4C10_Vertical.clicked.connect(partial(self.addtodict,self.R4C9_R4C10_Vertical))

        #--------------------------------------------------------------------
        
        self.R10C8_R11C8_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R10C8_R11C8_Horizontal.setGeometry(QtCore.QRect(300, 500, 39, 8))
        self.R10C8_R11C8_Horizontal.setText("")
        self.R10C8_R11C8_Horizontal.setObjectName("R10C8_R11C8_Horizontal")
        self.R10C8_R11C8_Horizontal.clicked.connect(partial(self.addtodict,self.R10C8_R11C8_Horizontal))

        #--------------------------------------------------------------------
        
        self.R6C11_R7C11_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R6C11_R7C11_Horizontal.setGeometry(QtCore.QRect(420, 300, 39, 8))
        self.R6C11_R7C11_Horizontal.setText("")
        self.R6C11_R7C11_Horizontal.setObjectName("R6C11_R7C11_Horizontal")
        self.R6C11_R7C11_Horizontal.clicked.connect(partial(self.addtodict,self.R6C11_R7C11_Horizontal))

        #--------------------------------------------------------------------
        
        self.R2C13_R2C14_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R2C13_R2C14_Vertical.setGeometry(QtCore.QRect(530, 64, 8, 33))
        self.R2C13_R2C14_Vertical.setText("")
        self.R2C13_R2C14_Vertical.setObjectName("R2C13_R2C14_Vertical")
        self.R2C13_R2C14_Vertical.clicked.connect(partial(self.addtodict,self.R2C13_R2C14_Vertical))

        #--------------------------------------------------------------------
        
        self.R9C4_R10C4_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R9C4_R10C4_Horizontal.setGeometry(QtCore.QRect(140, 450, 39, 8))
        self.R9C4_R10C4_Horizontal.setText("")
        self.R9C4_R10C4_Horizontal.setObjectName("R9C4_R10C4_Horizontal")
        self.R9C4_R10C4_Horizontal.clicked.connect(partial(self.addtodict,self.R9C4_R10C4_Horizontal))

        #--------------------------------------------------------------------
        
        self.Right_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Right_4.setGeometry(QtCore.QRect(570, 164, 8, 33))
        self.Right_4.setText("")
        self.Right_4.setObjectName("Right_4")
        self.Right_4.setStyleSheet("background-color: red")
        self.Right_4.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.Upper_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Upper_4.setGeometry(QtCore.QRect(140, 10, 39, 8))
        self.Upper_4.setText("")
        self.Upper_4.setObjectName("Upper_4")
        self.Upper_4.setStyleSheet("background-color: red")
        self.Upper_4.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.Lower_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Lower_3.setGeometry(QtCore.QRect(100, 700, 39, 8))
        self.Lower_3.setText("")
        self.Lower_3.setObjectName("Lower_3")
        self.Lower_3.setStyleSheet("background-color: red")
        self.Lower_3.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.Right_14 = QtWidgets.QPushButton(self.centralwidget)
        self.Right_14.setGeometry(QtCore.QRect(570, 664, 8, 33))
        self.Right_14.setText("")
        self.Right_14.setObjectName("Right_14")
        self.Right_14.setStyleSheet("background-color: red")
        self.Right_14.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R6C6_R6C7_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R6C6_R6C7_Vertical.setGeometry(QtCore.QRect(256, 264, 8, 33))
        self.R6C6_R6C7_Vertical.setText("")
        self.R6C6_R6C7_Vertical.setObjectName("R6C6_R6C7_Vertical")
        self.R6C6_R6C7_Vertical.clicked.connect(partial(self.addtodict,self.R6C6_R6C7_Vertical))

        #--------------------------------------------------------------------
        
        self.R12C4_R12C5_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R12C4_R12C5_Vertical.setGeometry(QtCore.QRect(175, 564, 8, 33))
        self.R12C4_R12C5_Vertical.setText("")
        self.R12C4_R12C5_Vertical.setObjectName("R12C4_R12C5_Vertical")
        self.R12C4_R12C5_Vertical.clicked.connect(partial(self.addtodict,self.R12C4_R12C5_Vertical))

        #--------------------------------------------------------------------
        
        self.R8C11_R8C12_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R8C11_R8C12_Vertical.setGeometry(QtCore.QRect(455, 364, 8, 33))
        self.R8C11_R8C12_Vertical.setText("")
        self.R8C11_R8C12_Vertical.setObjectName("R8C11_R8C12_Vertical")
        self.R8C11_R8C12_Vertical.clicked.connect(partial(self.addtodict,self.R8C11_R8C12_Vertical))

        #--------------------------------------------------------------------
        
        self.R2C9_R2C10_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R2C9_R2C10_Vertical.setGeometry(QtCore.QRect(376, 64, 8, 33))
        self.R2C9_R2C10_Vertical.setText("")
        self.R2C9_R2C10_Vertical.setObjectName("R2C9_R2C10_Vertical")
        self.R2C9_R2C10_Vertical.clicked.connect(partial(self.addtodict,self.R2C9_R2C10_Vertical))

        #--------------------------------------------------------------------
        
        self.R7C10_R8C10_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R7C10_R8C10_Horizontal.setGeometry(QtCore.QRect(380, 350, 39, 8))
        self.R7C10_R8C10_Horizontal.setText("")
        self.R7C10_R8C10_Horizontal.setObjectName("R7C10_R8C10_Horizontal")
        self.R7C10_R8C10_Horizontal.clicked.connect(partial(self.addtodict,self.R7C10_R8C10_Horizontal))

        #--------------------------------------------------------------------
        
        self.R4C1_R4C2_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R4C1_R4C2_Vertical.setGeometry(QtCore.QRect(54, 164, 8, 33))
        self.R4C1_R4C2_Vertical.setText("")
        self.R4C1_R4C2_Vertical.setObjectName("R4C1_R4C2_Vertical")
        self.R4C1_R4C2_Vertical.clicked.connect(partial(self.addtodict,self.R4C1_R4C2_Vertical))

        #--------------------------------------------------------------------
        
        self.Upper_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Upper_9.setGeometry(QtCore.QRect(340, 10, 39, 8))
        self.Upper_9.setText("")
        self.Upper_9.setObjectName("Upper_9")
        self.Upper_9.setStyleSheet("background-color: red")
        self.Upper_9.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R4C8_R5C8_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R4C8_R5C8_Horizontal.setGeometry(QtCore.QRect(300, 200, 39, 8))
        self.R4C8_R5C8_Horizontal.setText("")
        self.R4C8_R5C8_Horizontal.setObjectName("R4C8_R5C8_Horizontal")
        self.R4C8_R5C8_Horizontal.clicked.connect(partial(self.addtodict,self.R4C8_R5C8_Horizontal))

        #--------------------------------------------------------------------
        
        self.R1C14_R2C14_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R1C14_R2C14_Horizontal.setGeometry(QtCore.QRect(540, 56, 39, 8))
        self.R1C14_R2C14_Horizontal.setText("")
        self.R1C14_R2C14_Horizontal.setObjectName("R1C14_R2C14_Horizontal")
        self.R1C14_R2C14_Horizontal.clicked.connect(partial(self.addtodict,self.R1C14_R2C14_Horizontal))

        #--------------------------------------------------------------------
        
        self.R2C5_R2C6_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R2C5_R2C6_Vertical.setGeometry(QtCore.QRect(215, 64, 8, 33))
        self.R2C5_R2C6_Vertical.setText("")
        self.R2C5_R2C6_Vertical.setObjectName("R2C5_R2C6_Vertical")
        self.R2C5_R2C6_Vertical.clicked.connect(partial(self.addtodict,self.R2C5_R2C6_Vertical))

        #--------------------------------------------------------------------
        
        self.R6C5_R6C6_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R6C5_R6C6_Vertical.setGeometry(QtCore.QRect(215, 264, 8, 33))
        self.R6C5_R6C6_Vertical.setText("")
        self.R6C5_R6C6_Vertical.setObjectName("R6C5_R6C6_Vertical")
        self.R6C5_R6C6_Vertical.clicked.connect(partial(self.addtodict,self.R6C5_R6C6_Vertical))

        #--------------------------------------------------------------------
        
        self.R13C8_R14C8_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R13C8_R14C8_Horizontal.setGeometry(QtCore.QRect(300, 650, 39, 8))
        self.R13C8_R14C8_Horizontal.setText("")
        self.R13C8_R14C8_Horizontal.setObjectName("R13C8_R14C8_Horizontal")
        self.R13C8_R14C8_Horizontal.clicked.connect(partial(self.addtodict,self.R13C8_R14C8_Horizontal))

        #--------------------------------------------------------------------
        
        self.R9C6_R10C6_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R9C6_R10C6_Horizontal.setGeometry(QtCore.QRect(220, 450, 39, 8))
        self.R9C6_R10C6_Horizontal.setText("")
        self.R9C6_R10C6_Horizontal.setObjectName("R9C6_R10C6_Horizontal")
        self.R9C6_R10C6_Horizontal.clicked.connect(partial(self.addtodict,self.R9C6_R10C6_Horizontal))

        #--------------------------------------------------------------------
        
        self.R12C8_R12C9_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R12C8_R12C9_Vertical.setGeometry(QtCore.QRect(334, 564, 8, 33))
        self.R12C8_R12C9_Vertical.setText("")
        self.R12C8_R12C9_Vertical.setObjectName("R12C8_R12C9_Vertical")
        self.R12C8_R12C9_Vertical.clicked.connect(partial(self.addtodict,self.R12C8_R12C9_Vertical))

        #--------------------------------------------------------------------
        
        self.R5C10_R5C11_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R5C10_R5C11_Vertical.setGeometry(QtCore.QRect(416, 214, 8, 33))
        self.R5C10_R5C11_Vertical.setText("")
        self.R5C10_R5C11_Vertical.setObjectName("R5C10_R5C11_Vertical")
        self.R5C10_R5C11_Vertical.clicked.connect(partial(self.addtodict,self.R5C10_R5C11_Vertical))

        #--------------------------------------------------------------------
        
        self.R14C4_R14C5_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R14C4_R14C5_Vertical.setGeometry(QtCore.QRect(175, 664, 8, 33))
        self.R14C4_R14C5_Vertical.setText("")
        self.R14C4_R14C5_Vertical.setObjectName("R14C4_R14C5_Vertical")
        self.R14C4_R14C5_Vertical.clicked.connect(partial(self.addtodict,self.R14C4_R14C5_Vertical))

        #--------------------------------------------------------------------
        
        self.R9C8_R9C9_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R9C8_R9C9_Vertical.setGeometry(QtCore.QRect(334, 414, 8, 33))
        self.R9C8_R9C9_Vertical.setText("")
        self.R9C8_R9C9_Vertical.setObjectName("R9C8_R9C9_Vertical")
        self.R9C8_R9C9_Vertical.clicked.connect(partial(self.addtodict,self.R9C8_R9C9_Vertical))

        #--------------------------------------------------------------------
        
        self.R4C4_R5C4_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R4C4_R5C4_Horizontal.setGeometry(QtCore.QRect(140, 200, 39, 8))
        self.R4C4_R5C4_Horizontal.setText("")
        self.R4C4_R5C4_Horizontal.setObjectName("R4C4_R5C4_Horizontal")
        self.R4C4_R5C4_Horizontal.clicked.connect(partial(self.addtodict,self.R4C4_R5C4_Horizontal))

        #--------------------------------------------------------------------
        
        self.R8C7_R9C7_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R8C7_R9C7_Horizontal.setGeometry(QtCore.QRect(260, 400, 39, 8))
        self.R8C7_R9C7_Horizontal.setText("")
        self.R8C7_R9C7_Horizontal.setObjectName("R8C7_R9C7_Horizontal")
        self.R8C7_R9C7_Horizontal.clicked.connect(partial(self.addtodict,self.R8C7_R9C7_Horizontal))

        #--------------------------------------------------------------------
        
        self.R9C2_R10C2_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R9C2_R10C2_Horizontal.setGeometry(QtCore.QRect(60, 450, 39, 8))
        self.R9C2_R10C2_Horizontal.setText("")
        self.R9C2_R10C2_Horizontal.setObjectName("R9C2_R10C2_Horizontal")
        self.R9C2_R10C2_Horizontal.clicked.connect(partial(self.addtodict,self.R9C2_R10C2_Horizontal))

        #--------------------------------------------------------------------
        
        self.R6C2_R6C3_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R6C2_R6C3_Vertical.setGeometry(QtCore.QRect(94, 264, 8, 33))
        self.R6C2_R6C3_Vertical.setText("")
        self.R6C2_R6C3_Vertical.setObjectName("R6C2_R6C3_Vertical")
        self.R6C2_R6C3_Vertical.clicked.connect(partial(self.addtodict,self.R6C2_R6C3_Vertical))

        #--------------------------------------------------------------------
        
        self.R10C4_R10C5_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R10C4_R10C5_Vertical.setGeometry(QtCore.QRect(175, 464, 8, 33))
        self.R10C4_R10C5_Vertical.setText("")
        self.R10C4_R10C5_Vertical.setObjectName("R10C4_R10C5_Vertical")
        self.R10C4_R10C5_Vertical.clicked.connect(partial(self.addtodict,self.R10C4_R10C5_Vertical))

        #--------------------------------------------------------------------
        
        self.R13C12_R13C13_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R13C12_R13C13_Vertical.setGeometry(QtCore.QRect(497, 614, 8, 33))
        self.R13C12_R13C13_Vertical.setText("")
        self.R13C12_R13C13_Vertical.setObjectName("R13C12_R13C13_Vertical")
        self.R13C12_R13C13_Vertical.clicked.connect(partial(self.addtodict,self.R13C12_R13C13_Vertical))

        #--------------------------------------------------------------------
        
        self.R5C3_R6C3_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R5C3_R6C3_Horizontal.setGeometry(QtCore.QRect(100, 250, 39, 8))
        self.R5C3_R6C3_Horizontal.setText("")
        self.R5C3_R6C3_Horizontal.setObjectName("R5C3_R6C3_Horizontal")
        self.R5C3_R6C3_Horizontal.clicked.connect(partial(self.addtodict,self.R5C3_R6C3_Horizontal))

        #--------------------------------------------------------------------
        
        self.R4C2_R5C2_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R4C2_R5C2_Horizontal.setGeometry(QtCore.QRect(60, 200, 39, 8))
        self.R4C2_R5C2_Horizontal.setText("")
        self.R4C2_R5C2_Horizontal.setObjectName("R4C2_R5C2_Horizontal")
        self.R4C2_R5C2_Horizontal.clicked.connect(partial(self.addtodict,self.R4C2_R5C2_Horizontal))

        #--------------------------------------------------------------------
        
        self.R1C2_R1C3_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R1C2_R1C3_Vertical.setGeometry(QtCore.QRect(94, 20, 8, 33))
        self.R1C2_R1C3_Vertical.setText("")
        self.R1C2_R1C3_Vertical.setObjectName("R1C2_R1C3_Vertical")
        self.R1C2_R1C3_Vertical.clicked.connect(partial(self.addtodict,self.R1C2_R1C3_Vertical))

        #--------------------------------------------------------------------
        
        self.R14C3_R14C4_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R14C3_R14C4_Vertical.setGeometry(QtCore.QRect(135, 664, 8, 33))
        self.R14C3_R14C4_Vertical.setText("")
        self.R14C3_R14C4_Vertical.setObjectName("R14C3_R14C4_Vertical")
        self.R14C3_R14C4_Vertical.clicked.connect(partial(self.addtodict,self.R14C3_R14C4_Vertical))

        #--------------------------------------------------------------------
        
        self.Upper_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Upper_1.setGeometry(QtCore.QRect(20, 10, 39, 8))
        self.Upper_1.setText("")
        self.Upper_1.setObjectName("Upper_1")
        self.Upper_1.setStyleSheet("background-color: red")
        self.Upper_1.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R9C12_R10C12_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R9C12_R10C12_Horizontal.setGeometry(QtCore.QRect(460, 450, 39, 8))
        self.R9C12_R10C12_Horizontal.setText("")
        self.R9C12_R10C12_Horizontal.setObjectName("R9C12_R10C12_Horizontal")
        self.R9C12_R10C12_Horizontal.clicked.connect(partial(self.addtodict,self.R9C12_R10C12_Horizontal))

        #--------------------------------------------------------------------
        
        self.R8C3_R8C4_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R8C3_R8C4_Vertical.setGeometry(QtCore.QRect(135, 364, 8, 33))
        self.R8C3_R8C4_Vertical.setText("")
        self.R8C3_R8C4_Vertical.setObjectName("R8C3_R8C4_Vertical")
        self.R8C3_R8C4_Vertical.clicked.connect(partial(self.addtodict,self.R8C3_R8C4_Vertical))

        #--------------------------------------------------------------------
        
        self.Right_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Right_2.setGeometry(QtCore.QRect(570, 64, 8, 33))
        self.Right_2.setText("")
        self.Right_2.setObjectName("Right_2")
        self.Right_2.setStyleSheet("background-color: red")
        self.Right_2.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.Upper_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Upper_3.setGeometry(QtCore.QRect(100, 10, 39, 8))
        self.Upper_3.setText("")
        self.Upper_3.setObjectName("Upper_3")
        self.Upper_3.setStyleSheet("background-color: red")
        self.Upper_3.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R14C7_R14C8_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R14C7_R14C8_Vertical.setGeometry(QtCore.QRect(296, 664, 8, 33))
        self.R14C7_R14C8_Vertical.setText("")
        self.R14C7_R14C8_Vertical.setObjectName("R14C7_R14C8_Vertical")
        self.R14C7_R14C8_Vertical.clicked.connect(partial(self.addtodict,self.R14C7_R14C8_Vertical))

        #--------------------------------------------------------------------
        
        self.R6C13_R7C13_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R6C13_R7C13_Horizontal.setGeometry(QtCore.QRect(500, 300, 39, 8))
        self.R6C13_R7C13_Horizontal.setText("")
        self.R6C13_R7C13_Horizontal.setObjectName("R6C13_R7C13_Horizontal")
        self.R6C13_R7C13_Horizontal.clicked.connect(partial(self.addtodict,self.R6C13_R7C13_Horizontal))

        #--------------------------------------------------------------------
        
        self.R1C13_R1C14_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R1C13_R1C14_Vertical.setGeometry(QtCore.QRect(530, 20, 8, 33))
        self.R1C13_R1C14_Vertical.setText("")
        self.R1C13_R1C14_Vertical.setObjectName("R1C13_R1C14_Vertical")
        self.R1C13_R1C14_Vertical.clicked.connect(partial(self.addtodict,self.R1C13_R1C14_Vertical))

        #--------------------------------------------------------------------
        
        self.R10C7_R10C8_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R10C7_R10C8_Vertical.setGeometry(QtCore.QRect(296, 464, 8, 33))
        self.R10C7_R10C8_Vertical.setText("")
        self.R10C7_R10C8_Vertical.setObjectName("R10C7_R10C8_Vertical")
        self.R10C7_R10C8_Vertical.clicked.connect(partial(self.addtodict,self.R10C7_R10C8_Vertical))

        #--------------------------------------------------------------------
        
        self.R11C9_R11C10_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R11C9_R11C10_Vertical.setGeometry(QtCore.QRect(376, 514, 8, 33))
        self.R11C9_R11C10_Vertical.setText("")
        self.R11C9_R11C10_Vertical.setObjectName("R11C9_R11C10_Vertical")
        self.R11C9_R11C10_Vertical.clicked.connect(partial(self.addtodict,self.R11C9_R11C10_Vertical))

        #--------------------------------------------------------------------
        
        self.R9C4_R9C5_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R9C4_R9C5_Vertical.setGeometry(QtCore.QRect(175, 414, 8, 33))
        self.R9C4_R9C5_Vertical.setText("")
        self.R9C4_R9C5_Vertical.setObjectName("R9C4_R9C5_Vertical")
        self.R9C4_R9C5_Vertical.clicked.connect(partial(self.addtodict,self.R9C4_R9C5_Vertical))

        #--------------------------------------------------------------------
        
        self.R5C5_R6C5_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R5C5_R6C5_Horizontal.setGeometry(QtCore.QRect(180, 250, 39, 8))
        self.R5C5_R6C5_Horizontal.setText("")
        self.R5C5_R6C5_Horizontal.setObjectName("R5C5_R6C5_Horizontal")
        self.R5C5_R6C5_Horizontal.clicked.connect(partial(self.addtodict,self.R5C5_R6C5_Horizontal))

        #--------------------------------------------------------------------
        
        self.R1C9_R2C9_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R1C9_R2C9_Horizontal.setGeometry(QtCore.QRect(340, 56, 39, 8))
        self.R1C9_R2C9_Horizontal.setText("")
        self.R1C9_R2C9_Horizontal.setObjectName("R1C9_R2C9_Horizontal")
        self.R1C9_R2C9_Horizontal.clicked.connect(partial(self.addtodict,self.R1C9_R2C9_Horizontal))

        #--------------------------------------------------------------------
        
        self.Left_14 = QtWidgets.QPushButton(self.centralwidget)
        self.Left_14.setGeometry(QtCore.QRect(20, 664, 8, 33))
        self.Left_14.setText("")
        self.Left_14.setObjectName("Left_14")
        self.Left_14.setStyleSheet("background-color: red")
        self.Left_14.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R12C14_R13C14_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R12C14_R13C14_Horizontal.setGeometry(QtCore.QRect(540, 600, 39, 8))
        self.R12C14_R13C14_Horizontal.setText("")
        self.R12C14_R13C14_Horizontal.setObjectName("R12C14_R13C14_Horizontal")
        self.R12C14_R13C14_Horizontal.clicked.connect(partial(self.addtodict,self.R12C14_R13C14_Horizontal))

        #--------------------------------------------------------------------
        
        self.Right_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Right_9.setGeometry(QtCore.QRect(570, 414, 8, 33))
        self.Right_9.setText("")
        self.Right_9.setObjectName("Right_9")
        self.Right_9.setStyleSheet("background-color: red")
        self.Right_9.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R10C6_R11C6_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R10C6_R11C6_Horizontal.setGeometry(QtCore.QRect(220, 500, 39, 8))
        self.R10C6_R11C6_Horizontal.setText("")
        self.R10C6_R11C6_Horizontal.setObjectName("R10C6_R11C6_Horizontal")
        self.R10C6_R11C6_Horizontal.clicked.connect(partial(self.addtodict,self.R10C6_R11C6_Horizontal))

        #--------------------------------------------------------------------
        
        self.R14C9_R14C10_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R14C9_R14C10_Vertical.setGeometry(QtCore.QRect(376, 664, 8, 33))
        self.R14C9_R14C10_Vertical.setText("")
        self.R14C9_R14C10_Vertical.setObjectName("R14C9_R14C10_Vertical")
        self.R14C9_R14C10_Vertical.clicked.connect(partial(self.addtodict,self.R14C9_R14C10_Vertical))

        #--------------------------------------------------------------------
        
        self.R13C1_R13C2_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R13C1_R13C2_Vertical.setGeometry(QtCore.QRect(54, 614, 8, 33))
        self.R13C1_R13C2_Vertical.setText("")
        self.R13C1_R13C2_Vertical.setObjectName("R13C1_R13C2_Vertical")
        self.R13C1_R13C2_Vertical.clicked.connect(partial(self.addtodict,self.R13C1_R13C2_Vertical))

        #--------------------------------------------------------------------
        
        self.R8C4_R9C4_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R8C4_R9C4_Horizontal.setGeometry(QtCore.QRect(140, 400, 39, 8))
        self.R8C4_R9C4_Horizontal.setText("")
        self.R8C4_R9C4_Horizontal.setObjectName("R8C4_R9C4_Horizontal")
        self.R8C4_R9C4_Horizontal.clicked.connect(partial(self.addtodict,self.R8C4_R9C4_Horizontal))

        #--------------------------------------------------------------------
        
        self.R13C3_R14C3_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R13C3_R14C3_Horizontal.setGeometry(QtCore.QRect(100, 650, 39, 8))
        self.R13C3_R14C3_Horizontal.setText("")
        self.R13C3_R14C3_Horizontal.setObjectName("R13C3_R14C3_Horizontal")
        self.R13C3_R14C3_Horizontal.clicked.connect(partial(self.addtodict,self.R13C3_R14C3_Horizontal))

        #--------------------------------------------------------------------
        
        self.R13C5_R14C5_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R13C5_R14C5_Horizontal.setGeometry(QtCore.QRect(180, 650, 39, 8))
        self.R13C5_R14C5_Horizontal.setText("")
        self.R13C5_R14C5_Horizontal.setObjectName("R13C5_R14C5_Horizontal")
        self.R13C5_R14C5_Horizontal.clicked.connect(partial(self.addtodict,self.R13C5_R14C5_Horizontal))

        #--------------------------------------------------------------------
        
        self.R10C2_R11C2_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R10C2_R11C2_Horizontal.setGeometry(QtCore.QRect(60, 500, 39, 8))
        self.R10C2_R11C2_Horizontal.setText("")
        self.R10C2_R11C2_Horizontal.setObjectName("R10C2_R11C2_Horizontal")
        self.R10C2_R11C2_Horizontal.clicked.connect(partial(self.addtodict,self.R10C2_R11C2_Horizontal))

        #--------------------------------------------------------------------
        
        self.R5C7_R6C7_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R5C7_R6C7_Horizontal.setGeometry(QtCore.QRect(260, 250, 39, 8))
        self.R5C7_R6C7_Horizontal.setText("")
        self.R5C7_R6C7_Horizontal.setObjectName("R5C7_R6C7_Horizontal")
        self.R5C7_R6C7_Horizontal.clicked.connect(partial(self.addtodict,self.R5C7_R6C7_Horizontal))

        #--------------------------------------------------------------------
        
        self.R7C1_R8C1_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R7C1_R8C1_Horizontal.setGeometry(QtCore.QRect(20, 350, 39, 8))
        self.R7C1_R8C1_Horizontal.setText("")
        self.R7C1_R8C1_Horizontal.setObjectName("R7C1_R8C1_Horizontal")
        self.R7C1_R8C1_Horizontal.clicked.connect(partial(self.addtodict,self.R7C1_R8C1_Horizontal))

        #--------------------------------------------------------------------
        
        self.R4C12_R5C12_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R4C12_R5C12_Horizontal.setGeometry(QtCore.QRect(460, 200, 39, 8))
        self.R4C12_R5C12_Horizontal.setText("")
        self.R4C12_R5C12_Horizontal.setObjectName("R4C12_R5C12_Horizontal")
        self.R4C12_R5C12_Horizontal.clicked.connect(partial(self.addtodict,self.R4C12_R5C12_Horizontal))

        #--------------------------------------------------------------------
        
        self.Lower_12 = QtWidgets.QPushButton(self.centralwidget)
        self.Lower_12.setGeometry(QtCore.QRect(460, 700, 39, 8))
        self.Lower_12.setText("")
        self.Lower_12.setObjectName("Lower_12")
        self.Lower_12.setStyleSheet("background-color: red")
        self.Lower_12.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R1C3_R1C4_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R1C3_R1C4_Vertical.setGeometry(QtCore.QRect(135, 20, 8, 33))
        self.R1C3_R1C4_Vertical.setText("")
        self.R1C3_R1C4_Vertical.setObjectName("R1C3_R1C4_Vertical")
        self.R1C3_R1C4_Vertical.clicked.connect(partial(self.addtodict,self.R1C3_R1C4_Vertical))

        #--------------------------------------------------------------------
        
        self.R8C1_R8C2_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R8C1_R8C2_Vertical.setGeometry(QtCore.QRect(54, 364, 8, 33))
        self.R8C1_R8C2_Vertical.setText("")
        self.R8C1_R8C2_Vertical.setObjectName("R8C1_R8C2_Vertical")
        self.R8C1_R8C2_Vertical.clicked.connect(partial(self.addtodict,self.R8C1_R8C2_Vertical))

        #--------------------------------------------------------------------
        
        self.R7C5_R8C5_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R7C5_R8C5_Horizontal.setGeometry(QtCore.QRect(180, 350, 39, 8))
        self.R7C5_R8C5_Horizontal.setText("")
        self.R7C5_R8C5_Horizontal.setObjectName("R7C5_R8C5_Horizontal")
        self.R7C5_R8C5_Horizontal.clicked.connect(partial(self.addtodict,self.R7C5_R8C5_Horizontal))

        #--------------------------------------------------------------------
        
        self.Upper_13 = QtWidgets.QPushButton(self.centralwidget)
        self.Upper_13.setGeometry(QtCore.QRect(500, 10, 39, 8))
        self.Upper_13.setText("")
        self.Upper_13.setObjectName("Upper_13")
        self.Upper_13.setStyleSheet("background-color: red")
        self.Upper_13.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R3C13_R4C13_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R3C13_R4C13_Horizontal.setGeometry(QtCore.QRect(500, 150, 39, 8))
        self.R3C13_R4C13_Horizontal.setText("")
        self.R3C13_R4C13_Horizontal.setObjectName("R3C13_R4C13_Horizontal")
        self.R3C13_R4C13_Horizontal.clicked.connect(partial(self.addtodict,self.R3C13_R4C13_Horizontal))

        #--------------------------------------------------------------------
        
        self.R10C12_R10C13_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R10C12_R10C13_Vertical.setGeometry(QtCore.QRect(497, 464, 8, 33))
        self.R10C12_R10C13_Vertical.setText("")
        self.R10C12_R10C13_Vertical.setObjectName("R10C12_R10C13_Vertical")
        self.R10C12_R10C13_Vertical.clicked.connect(partial(self.addtodict,self.R10C12_R10C13_Vertical))

        #--------------------------------------------------------------------
        
        self.R9C11_R10C11_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R9C11_R10C11_Horizontal.setGeometry(QtCore.QRect(420, 450, 39, 8))
        self.R9C11_R10C11_Horizontal.setText("")
        self.R9C11_R10C11_Horizontal.setObjectName("R9C11_R10C11_Horizontal")
        self.R9C11_R10C11_Horizontal.clicked.connect(partial(self.addtodict,self.R9C11_R10C11_Horizontal))

        #--------------------------------------------------------------------
        
        self.Lower_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Lower_1.setGeometry(QtCore.QRect(20, 700, 39, 8))
        self.Lower_1.setText("")
        self.Lower_1.setObjectName("Lower_1")
        self.Lower_1.setStyleSheet("background-color: red")
        self.Lower_1.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R1C12_R1C13_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R1C12_R1C13_Vertical.setGeometry(QtCore.QRect(497, 20, 8, 33))
        self.R1C12_R1C13_Vertical.setText("")
        self.R1C12_R1C13_Vertical.setObjectName("R1C12_R1C13_Vertical")
        self.R1C12_R1C13_Vertical.clicked.connect(partial(self.addtodict,self.R1C12_R1C13_Vertical))

        #--------------------------------------------------------------------
        
        self.Lower_10 = QtWidgets.QPushButton(self.centralwidget)
        self.Lower_10.setGeometry(QtCore.QRect(380, 700, 39, 8))
        self.Lower_10.setText("")
        self.Lower_10.setObjectName("Lower_10")
        self.Lower_10.setStyleSheet("background-color: red")
        self.Lower_10.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R13C11_R14C11_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R13C11_R14C11_Horizontal.setGeometry(QtCore.QRect(420, 650, 39, 8))
        self.R13C11_R14C11_Horizontal.setText("")
        self.R13C11_R14C11_Horizontal.setObjectName("R13C11_R14C11_Horizontal")
        self.R13C11_R14C11_Horizontal.clicked.connect(partial(self.addtodict,self.R13C11_R14C11_Horizontal))

        #--------------------------------------------------------------------
        
        self.R5C1_R6C1_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R5C1_R6C1_Horizontal.setGeometry(QtCore.QRect(20, 250, 39, 8))
        self.R5C1_R6C1_Horizontal.setText("")
        self.R5C1_R6C1_Horizontal.setObjectName("R5C1_R6C1_Horizontal")
        self.R5C1_R6C1_Horizontal.clicked.connect(partial(self.addtodict,self.R5C1_R6C1_Horizontal))

        #--------------------------------------------------------------------
        
        self.R6C8_R7C8_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R6C8_R7C8_Horizontal.setGeometry(QtCore.QRect(300, 300, 39, 8))
        self.R6C8_R7C8_Horizontal.setText("")
        self.R6C8_R7C8_Horizontal.setObjectName("R6C8_R7C8_Horizontal")
        self.R6C8_R7C8_Horizontal.clicked.connect(partial(self.addtodict,self.R6C8_R7C8_Horizontal))

        #--------------------------------------------------------------------
        
        self.R12C2_R13C2_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R12C2_R13C2_Horizontal.setGeometry(QtCore.QRect(60, 600, 39, 8))
        self.R12C2_R13C2_Horizontal.setText("")
        self.R12C2_R13C2_Horizontal.setObjectName("R12C2_R13C2_Horizontal")
        self.R12C2_R13C2_Horizontal.clicked.connect(partial(self.addtodict,self.R12C2_R13C2_Horizontal))

        #--------------------------------------------------------------------
        
        self.R5C14_R6C14_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R5C14_R6C14_Horizontal.setGeometry(QtCore.QRect(540, 250, 39, 8))
        self.R5C14_R6C14_Horizontal.setText("")
        self.R5C14_R6C14_Horizontal.setObjectName("R5C14_R6C14_Horizontal")
        self.R5C14_R6C14_Horizontal.clicked.connect(partial(self.addtodict,self.R5C14_R6C14_Horizontal))

        #--------------------------------------------------------------------
        
        self.R11C4_R12C4_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R11C4_R12C4_Horizontal.setGeometry(QtCore.QRect(140, 550, 39, 8))
        self.R11C4_R12C4_Horizontal.setText("")
        self.R11C4_R12C4_Horizontal.setObjectName("R11C4_R12C4_Horizontal")
        self.R11C4_R12C4_Horizontal.clicked.connect(partial(self.addtodict,self.R11C4_R12C4_Horizontal))

        #--------------------------------------------------------------------
        
        self.R8C9_R8C10_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R8C9_R8C10_Vertical.setGeometry(QtCore.QRect(376, 364, 8, 33))
        self.R8C9_R8C10_Vertical.setText("")
        self.R8C9_R8C10_Vertical.setObjectName("R8C9_R8C10_Vertical")
        self.R8C9_R8C10_Vertical.clicked.connect(partial(self.addtodict,self.R8C9_R8C10_Vertical))

        #--------------------------------------------------------------------
        
        self.R9C13_R9C14_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R9C13_R9C14_Vertical.setGeometry(QtCore.QRect(530, 414, 8, 33))
        self.R9C13_R9C14_Vertical.setText("")
        self.R9C13_R9C14_Vertical.setObjectName("R9C13_R9C14_Vertical")
        self.R9C13_R9C14_Vertical.clicked.connect(partial(self.addtodict,self.R9C13_R9C14_Vertical))

        #--------------------------------------------------------------------
        
        self.R4C9_R5C9_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R4C9_R5C9_Horizontal.setGeometry(QtCore.QRect(340, 200, 39, 8))
        self.R4C9_R5C9_Horizontal.setText("")
        self.R4C9_R5C9_Horizontal.setObjectName("R4C9_R5C9_Horizontal")
        self.R4C9_R5C9_Horizontal.clicked.connect(partial(self.addtodict,self.R4C9_R5C9_Horizontal))

        #--------------------------------------------------------------------
        
        self.R9C11_R9C12_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R9C11_R9C12_Vertical.setGeometry(QtCore.QRect(455, 414, 8, 33))
        self.R9C11_R9C12_Vertical.setText("")
        self.R9C11_R9C12_Vertical.setObjectName("R9C11_R9C12_Vertical")
        self.R9C11_R9C12_Vertical.clicked.connect(partial(self.addtodict,self.R9C11_R9C12_Vertical))

        #--------------------------------------------------------------------
        
        self.R4C3_R5C3_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R4C3_R5C3_Horizontal.setGeometry(QtCore.QRect(100, 200, 39, 8))
        self.R4C3_R5C3_Horizontal.setText("")
        self.R4C3_R5C3_Horizontal.setObjectName("R4C3_R5C3_Horizontal")
        self.R4C3_R5C3_Horizontal.clicked.connect(partial(self.addtodict,self.R4C3_R5C3_Horizontal))

        #--------------------------------------------------------------------
        
        self.R11C3_R11C4_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R11C3_R11C4_Vertical.setGeometry(QtCore.QRect(135, 514, 8, 33))
        self.R11C3_R11C4_Vertical.setText("")
        self.R11C3_R11C4_Vertical.setObjectName("R11C3_R11C4_Vertical")
        self.R11C3_R11C4_Vertical.clicked.connect(partial(self.addtodict,self.R11C3_R11C4_Vertical))

        #--------------------------------------------------------------------
        
        self.R1C8_R2C8_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R1C8_R2C8_Horizontal.setGeometry(QtCore.QRect(300, 56, 39, 8))
        self.R1C8_R2C8_Horizontal.setText("")
        self.R1C8_R2C8_Horizontal.setObjectName("R1C8_R2C8_Horizontal")
        self.R1C8_R2C8_Horizontal.clicked.connect(partial(self.addtodict,self.R1C8_R2C8_Horizontal))

        #--------------------------------------------------------------------
        
        self.R6C7_R6C8_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R6C7_R6C8_Vertical.setGeometry(QtCore.QRect(296, 264, 8, 33))
        self.R6C7_R6C8_Vertical.setText("")
        self.R6C7_R6C8_Vertical.setObjectName("R6C7_R6C8_Vertical")
        self.R6C7_R6C8_Vertical.clicked.connect(partial(self.addtodict,self.R6C7_R6C8_Vertical))

        #--------------------------------------------------------------------
        
        self.R7C4_R8C4_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R7C4_R8C4_Horizontal.setGeometry(QtCore.QRect(140, 350, 39, 8))
        self.R7C4_R8C4_Horizontal.setText("")
        self.R7C4_R8C4_Horizontal.setObjectName("R7C4_R8C4_Horizontal")
        self.R7C4_R8C4_Horizontal.clicked.connect(partial(self.addtodict,self.R7C4_R8C4_Horizontal))

        #--------------------------------------------------------------------
        
        self.R12C6_R12C7_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R12C6_R12C7_Vertical.setGeometry(QtCore.QRect(256, 564, 8, 33))
        self.R12C6_R12C7_Vertical.setText("")
        self.R12C6_R12C7_Vertical.setObjectName("R12C6_R12C7_Vertical")
        self.R12C6_R12C7_Vertical.clicked.connect(partial(self.addtodict,self.R12C6_R12C7_Vertical))

        #--------------------------------------------------------------------
        
        self.Lower_13 = QtWidgets.QPushButton(self.centralwidget)
        self.Lower_13.setGeometry(QtCore.QRect(500, 700, 39, 8))
        self.Lower_13.setText("")
        self.Lower_13.setObjectName("Lower_13")
        self.Lower_13.setStyleSheet("background-color: red")
        self.Lower_13.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R3C10_R4C10_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R3C10_R4C10_Horizontal.setGeometry(QtCore.QRect(380, 150, 39, 8))
        self.R3C10_R4C10_Horizontal.setText("")
        self.R3C10_R4C10_Horizontal.setObjectName("R3C10_R4C10_Horizontal")
        self.R3C10_R4C10_Horizontal.clicked.connect(partial(self.addtodict,self.R3C10_R4C10_Horizontal))

        #--------------------------------------------------------------------
        
        self.R3C14_R4C14_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R3C14_R4C14_Horizontal.setGeometry(QtCore.QRect(540, 150, 39, 8))
        self.R3C14_R4C14_Horizontal.setText("")
        self.R3C14_R4C14_Horizontal.setObjectName("R3C14_R4C14_Horizontal")
        self.R3C14_R4C14_Horizontal.clicked.connect(partial(self.addtodict,self.R3C14_R4C14_Horizontal))

        #--------------------------------------------------------------------
        
        self.R4C14_R5C14_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R4C14_R5C14_Horizontal.setGeometry(QtCore.QRect(540, 200, 39, 8))
        self.R4C14_R5C14_Horizontal.setText("")
        self.R4C14_R5C14_Horizontal.setObjectName("R4C14_R5C14_Horizontal")
        self.R4C14_R5C14_Horizontal.clicked.connect(partial(self.addtodict,self.R4C14_R5C14_Horizontal))

        #--------------------------------------------------------------------
        
        self.R1C4_R2C4_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R1C4_R2C4_Horizontal.setGeometry(QtCore.QRect(140, 56, 39, 8))
        self.R1C4_R2C4_Horizontal.setText("")
        self.R1C4_R2C4_Horizontal.setObjectName("R1C4_R2C4_Horizontal")
        self.R1C4_R2C4_Horizontal.clicked.connect(partial(self.addtodict,self.R1C4_R2C4_Horizontal))

        #--------------------------------------------------------------------
        
        self.R9C3_R10C3_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R9C3_R10C3_Horizontal.setGeometry(QtCore.QRect(100, 450, 39, 8))
        self.R9C3_R10C3_Horizontal.setText("")
        self.R9C3_R10C3_Horizontal.setObjectName("R9C3_R10C3_Horizontal")
        self.R9C3_R10C3_Horizontal.clicked.connect(partial(self.addtodict,self.R9C3_R10C3_Horizontal))

        #--------------------------------------------------------------------
        
        self.R7C8_R8C8_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R7C8_R8C8_Horizontal.setGeometry(QtCore.QRect(300, 350, 39, 8))
        self.R7C8_R8C8_Horizontal.setText("")
        self.R7C8_R8C8_Horizontal.setObjectName("R7C8_R8C8_Horizontal")
        self.R7C8_R8C8_Horizontal.clicked.connect(partial(self.addtodict,self.R7C8_R8C8_Horizontal))

        #--------------------------------------------------------------------
        
        self.R2C6_R2C7_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R2C6_R2C7_Vertical.setGeometry(QtCore.QRect(256, 64, 8, 33))
        self.R2C6_R2C7_Vertical.setText("")
        self.R2C6_R2C7_Vertical.setObjectName("R2C6_R2C7_Vertical")
        self.R2C6_R2C7_Vertical.clicked.connect(partial(self.addtodict,self.R2C6_R2C7_Vertical))

        #--------------------------------------------------------------------
        
        self.R10C13_R10C14_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R10C13_R10C14_Vertical.setGeometry(QtCore.QRect(530, 464, 8, 33))
        self.R10C13_R10C14_Vertical.setText("")
        self.R10C13_R10C14_Vertical.setObjectName("R10C13_R10C14_Vertical")
        self.R10C13_R10C14_Vertical.clicked.connect(partial(self.addtodict,self.R10C13_R10C14_Vertical))

        #--------------------------------------------------------------------
        
        self.R7C8_R7C9_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R7C8_R7C9_Vertical.setGeometry(QtCore.QRect(334, 314, 8, 33))
        self.R7C8_R7C9_Vertical.setText("")
        self.R7C8_R7C9_Vertical.setObjectName("R7C8_R7C9_Vertical")
        self.R7C8_R7C9_Vertical.clicked.connect(partial(self.addtodict,self.R7C8_R7C9_Vertical))

        #--------------------------------------------------------------------
        
        self.R13C6_R13C7_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R13C6_R13C7_Vertical.setGeometry(QtCore.QRect(256, 614, 8, 33))
        self.R13C6_R13C7_Vertical.setText("")
        self.R13C6_R13C7_Vertical.setObjectName("R13C6_R13C7_Vertical")
        self.R13C6_R13C7_Vertical.clicked.connect(partial(self.addtodict,self.R13C6_R13C7_Vertical))

        #--------------------------------------------------------------------
        
        self.R2C13_R3C13_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R2C13_R3C13_Horizontal.setGeometry(QtCore.QRect(500, 100, 39, 8))
        self.R2C13_R3C13_Horizontal.setText("")
        self.R2C13_R3C13_Horizontal.setObjectName("R2C13_R3C13_Horizontal")
        self.R2C13_R3C13_Horizontal.clicked.connect(partial(self.addtodict,self.R2C13_R3C13_Horizontal))

        #--------------------------------------------------------------------
        
        self.R7C13_R8C13_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R7C13_R8C13_Horizontal.setGeometry(QtCore.QRect(500, 350, 39, 8))
        self.R7C13_R8C13_Horizontal.setText("")
        self.R7C13_R8C13_Horizontal.setObjectName("R7C13_R8C13_Horizontal")
        self.R7C13_R8C13_Horizontal.clicked.connect(partial(self.addtodict,self.R7C13_R8C13_Horizontal))

        #--------------------------------------------------------------------
        
        self.R10C6_R10C7_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R10C6_R10C7_Vertical.setGeometry(QtCore.QRect(256, 464, 8, 33))
        self.R10C6_R10C7_Vertical.setText("")
        self.R10C6_R10C7_Vertical.setObjectName("R10C6_R10C7_Vertical")
        self.R10C6_R10C7_Vertical.clicked.connect(partial(self.addtodict,self.R10C6_R10C7_Vertical))

        #--------------------------------------------------------------------
        
        self.Left_10 = QtWidgets.QPushButton(self.centralwidget)
        self.Left_10.setGeometry(QtCore.QRect(20, 464, 8, 33))
        self.Left_10.setText("")
        self.Left_10.setObjectName("Left_10")
        self.Left_10.setStyleSheet("background-color: red")
        self.Left_10.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R14C12_R14C13_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R14C12_R14C13_Vertical.setGeometry(QtCore.QRect(497, 664, 8, 33))
        self.R14C12_R14C13_Vertical.setText("")
        self.R14C12_R14C13_Vertical.setObjectName("R14C12_R14C13_Vertical")
        self.R14C12_R14C13_Vertical.clicked.connect(partial(self.addtodict,self.R14C12_R14C13_Vertical))

        #--------------------------------------------------------------------
        
        self.R11C2_R12C2_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R11C2_R12C2_Horizontal.setGeometry(QtCore.QRect(60, 550, 39, 8))
        self.R11C2_R12C2_Horizontal.setText("")
        self.R11C2_R12C2_Horizontal.setObjectName("R11C2_R12C2_Horizontal")
        self.R11C2_R12C2_Horizontal.clicked.connect(partial(self.addtodict,self.R11C2_R12C2_Horizontal))

        #--------------------------------------------------------------------
        
        self.R13C10_R14C10_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R13C10_R14C10_Horizontal.setGeometry(QtCore.QRect(380, 650, 39, 8))
        self.R13C10_R14C10_Horizontal.setText("")
        self.R13C10_R14C10_Horizontal.setObjectName("R13C10_R14C10_Horizontal")
        self.R13C10_R14C10_Horizontal.clicked.connect(partial(self.addtodict,self.R13C10_R14C10_Horizontal))

        #--------------------------------------------------------------------
        
        self.R6C10_R6C11_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R6C10_R6C11_Vertical.setGeometry(QtCore.QRect(416, 264, 8, 33))
        self.R6C10_R6C11_Vertical.setText("")
        self.R6C10_R6C11_Vertical.setObjectName("R6C10_R6C11_Vertical")
        self.R6C10_R6C11_Vertical.clicked.connect(partial(self.addtodict,self.R6C10_R6C11_Vertical))

        #--------------------------------------------------------------------
        
        self.R10C14_R11C14_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R10C14_R11C14_Horizontal.setGeometry(QtCore.QRect(540, 500, 39, 8))
        self.R10C14_R11C14_Horizontal.setText("")
        self.R10C14_R11C14_Horizontal.setObjectName("R10C14_R11C14_Horizontal")
        self.R10C14_R11C14_Horizontal.clicked.connect(partial(self.addtodict,self.R10C14_R11C14_Horizontal))

        #--------------------------------------------------------------------
        
        self.R3C8_R3C9_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R3C8_R3C9_Vertical.setGeometry(QtCore.QRect(334, 114, 8, 33))
        self.R3C8_R3C9_Vertical.setText("")
        self.R3C8_R3C9_Vertical.setObjectName("R3C8_R3C9_Vertical")
        self.R3C8_R3C9_Vertical.clicked.connect(partial(self.addtodict,self.R3C8_R3C9_Vertical))

        #--------------------------------------------------------------------
        
        self.Lower_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Lower_2.setGeometry(QtCore.QRect(60, 700, 39, 8))
        self.Lower_2.setText("")
        self.Lower_2.setObjectName("Lower_2")
        self.Lower_2.setStyleSheet("background-color: red")
        self.Lower_2.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.Right_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Right_8.setGeometry(QtCore.QRect(570, 364, 8, 33))
        self.Right_8.setText("")
        self.Right_8.setObjectName("Right_8")
        self.Right_8.setStyleSheet("background-color: red")
        self.Right_8.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.Left_12 = QtWidgets.QPushButton(self.centralwidget)
        self.Left_12.setGeometry(QtCore.QRect(20, 564, 8, 33))
        self.Left_12.setText("")
        self.Left_12.setObjectName("Left_12")
        self.Left_12.setStyleSheet("background-color: red")
        self.Left_12.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.Upper_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Upper_8.setGeometry(QtCore.QRect(300, 10, 39, 8))
        self.Upper_8.setText("")
        self.Upper_8.setObjectName("Upper_8")
        self.Upper_8.setStyleSheet("background-color: red")
        self.Upper_8.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.Upper_11 = QtWidgets.QPushButton(self.centralwidget)
        self.Upper_11.setGeometry(QtCore.QRect(420, 10, 39, 8))
        self.Upper_11.setText("")
        self.Upper_11.setObjectName("Upper_11")
        self.Upper_11.setStyleSheet("background-color: red")
        self.Upper_11.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R3C13_R3C14_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R3C13_R3C14_Vertical.setGeometry(QtCore.QRect(530, 114, 8, 33))
        self.R3C13_R3C14_Vertical.setText("")
        self.R3C13_R3C14_Vertical.setObjectName("R3C13_R3C14_Vertical")
        self.R3C13_R3C14_Vertical.clicked.connect(partial(self.addtodict,self.R3C13_R3C14_Vertical))

        #--------------------------------------------------------------------
        
        self.R12C9_R13C9_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R12C9_R13C9_Horizontal.setGeometry(QtCore.QRect(340, 600, 39, 8))
        self.R12C9_R13C9_Horizontal.setText("")
        self.R12C9_R13C9_Horizontal.setObjectName("R12C9_R13C9_Horizontal")
        self.R12C9_R13C9_Horizontal.clicked.connect(partial(self.addtodict,self.R12C9_R13C9_Horizontal))

        #--------------------------------------------------------------------
        
        self.R3C2_R3C3_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R3C2_R3C3_Vertical.setGeometry(QtCore.QRect(94, 114, 8, 33))
        self.R3C2_R3C3_Vertical.setText("")
        self.R3C2_R3C3_Vertical.setObjectName("R3C2_R3C3_Vertical")
        self.R3C2_R3C3_Vertical.clicked.connect(partial(self.addtodict,self.R3C2_R3C3_Vertical))

        #--------------------------------------------------------------------
        
        self.R9C10_R10C10_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R9C10_R10C10_Horizontal.setGeometry(QtCore.QRect(380, 450, 39, 8))
        self.R9C10_R10C10_Horizontal.setText("")
        self.R9C10_R10C10_Horizontal.setObjectName("R9C10_R10C10_Horizontal")
        self.R9C10_R10C10_Horizontal.clicked.connect(partial(self.addtodict,self.R9C10_R10C10_Horizontal))

        #--------------------------------------------------------------------
        
        self.R12C9_R12C10_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R12C9_R12C10_Vertical.setGeometry(QtCore.QRect(376, 564, 8, 33))
        self.R12C9_R12C10_Vertical.setText("")
        self.R12C9_R12C10_Vertical.setObjectName("R12C9_R12C10_Vertical")
        self.R12C9_R12C10_Vertical.clicked.connect(partial(self.addtodict,self.R12C9_R12C10_Vertical))

        #--------------------------------------------------------------------
        
        self.R3C4_R4C4_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R3C4_R4C4_Horizontal.setGeometry(QtCore.QRect(140, 150, 39, 8))
        self.R3C4_R4C4_Horizontal.setText("")
        self.R3C4_R4C4_Horizontal.setObjectName("R3C4_R4C4_Horizontal")
        self.R3C4_R4C4_Horizontal.clicked.connect(partial(self.addtodict,self.R3C4_R4C4_Horizontal))

        #--------------------------------------------------------------------
        
        self.R8C11_R9C11_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R8C11_R9C11_Horizontal.setGeometry(QtCore.QRect(420, 400, 39, 8))
        self.R8C11_R9C11_Horizontal.setText("")
        self.R8C11_R9C11_Horizontal.setObjectName("R8C11_R9C11_Horizontal")
        self.R8C11_R9C11_Horizontal.clicked.connect(partial(self.addtodict,self.R8C11_R9C11_Horizontal))

        #--------------------------------------------------------------------
        
        self.R7C5_R7C6_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R7C5_R7C6_Vertical.setGeometry(QtCore.QRect(215, 314, 8, 33))
        self.R7C5_R7C6_Vertical.setText("")
        self.R7C5_R7C6_Vertical.setObjectName("R7C5_R7C6_Vertical")
        self.R7C5_R7C6_Vertical.clicked.connect(partial(self.addtodict,self.R7C5_R7C6_Vertical))

        #--------------------------------------------------------------------
        
        self.R12C8_R13C8_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R12C8_R13C8_Horizontal.setGeometry(QtCore.QRect(300, 600, 39, 8))
        self.R12C8_R13C8_Horizontal.setText("")
        self.R12C8_R13C8_Horizontal.setObjectName("R12C8_R13C8_Horizontal")
        self.R12C8_R13C8_Horizontal.clicked.connect(partial(self.addtodict,self.R12C8_R13C8_Horizontal))

        #--------------------------------------------------------------------
        
        self.R14C6_R14C7_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R14C6_R14C7_Vertical.setGeometry(QtCore.QRect(256, 664, 8, 33))
        self.R14C6_R14C7_Vertical.setText("")
        self.R14C6_R14C7_Vertical.setObjectName("R14C6_R14C7_Vertical")
        self.R14C6_R14C7_Vertical.clicked.connect(partial(self.addtodict,self.R14C6_R14C7_Vertical))

        #--------------------------------------------------------------------
        
        self.R4C4_R4C5_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R4C4_R4C5_Vertical.setGeometry(QtCore.QRect(175, 164, 8, 33))
        self.R4C4_R4C5_Vertical.setText("")
        self.R4C4_R4C5_Vertical.setObjectName("R4C4_R4C5_Vertical")
        self.R4C4_R4C5_Vertical.clicked.connect(partial(self.addtodict,self.R4C4_R4C5_Vertical))

        #--------------------------------------------------------------------
        
        self.R12C10_R13C10_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R12C10_R13C10_Horizontal.setGeometry(QtCore.QRect(380, 600, 39, 8))
        self.R12C10_R13C10_Horizontal.setText("")
        self.R12C10_R13C10_Horizontal.setObjectName("R12C10_R13C10_Horizontal")
        self.R12C10_R13C10_Horizontal.clicked.connect(partial(self.addtodict,self.R12C10_R13C10_Horizontal))

        #--------------------------------------------------------------------
        
        self.R10C1_R10C2_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R10C1_R10C2_Vertical.setGeometry(QtCore.QRect(54, 464, 8, 33))
        self.R10C1_R10C2_Vertical.setText("")
        self.R10C1_R10C2_Vertical.setObjectName("R10C1_R10C2_Vertical")
        self.R10C1_R10C2_Vertical.clicked.connect(partial(self.addtodict,self.R10C1_R10C2_Vertical))

        #--------------------------------------------------------------------
        
        self.Upper_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Upper_7.setGeometry(QtCore.QRect(260, 10, 39, 8))
        self.Upper_7.setText("")
        self.Upper_7.setObjectName("Upper_7")
        self.Upper_7.setStyleSheet("background-color: red")
        self.Upper_7.setEnabled(False)
        
        #--------------------------------------------------------------------
        
        self.R4C7_R5C7_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R4C7_R5C7_Horizontal.setGeometry(QtCore.QRect(260, 200, 39, 8))
        self.R4C7_R5C7_Horizontal.setText("")
        self.R4C7_R5C7_Horizontal.setObjectName("R4C7_R5C7_Horizontal")
        self.R4C7_R5C7_Horizontal.clicked.connect(partial(self.addtodict,self.R4C7_R5C7_Horizontal))

        #--------------------------------------------------------------------
        
        self.R9C9_R9C10_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R9C9_R9C10_Vertical.setGeometry(QtCore.QRect(376, 414, 8, 33))
        self.R9C9_R9C10_Vertical.setText("")
        self.R9C9_R9C10_Vertical.setObjectName("R9C9_R9C10_Vertical")
        self.R9C9_R9C10_Vertical.clicked.connect(partial(self.addtodict,self.R9C9_R9C10_Vertical))

        #--------------------------------------------------------------------
        
        self.R4C11_R5C11_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R4C11_R5C11_Horizontal.setGeometry(QtCore.QRect(420, 200, 39, 8))
        self.R4C11_R5C11_Horizontal.setText("")
        self.R4C11_R5C11_Horizontal.setObjectName("R4C11_R5C11_Horizontal")
        self.R4C11_R5C11_Horizontal.clicked.connect(partial(self.addtodict,self.R4C11_R5C11_Horizontal))

        #--------------------------------------------------------------------
        
        self.R6C8_R6C9_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R6C8_R6C9_Vertical.setGeometry(QtCore.QRect(334, 264, 8, 33))
        self.R6C8_R6C9_Vertical.setText("")
        self.R6C8_R6C9_Vertical.setObjectName("R6C8_R6C9_Vertical")
        self.R6C8_R6C9_Vertical.clicked.connect(partial(self.addtodict,self.R6C8_R6C9_Vertical))

        #--------------------------------------------------------------------
        
        self.R8C8_R9C8_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R8C8_R9C8_Horizontal.setGeometry(QtCore.QRect(300, 400, 39, 8))
        self.R8C8_R9C8_Horizontal.setText("")
        self.R8C8_R9C8_Horizontal.setObjectName("R8C8_R9C8_Horizontal")
        self.R8C8_R9C8_Horizontal.clicked.connect(partial(self.addtodict,self.R8C8_R9C8_Horizontal))

        #--------------------------------------------------------------------
        
        self.R10C10_R10C11_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R10C10_R10C11_Vertical.setGeometry(QtCore.QRect(416, 464, 8, 33))
        self.R10C10_R10C11_Vertical.setText("")
        self.R10C10_R10C11_Vertical.setObjectName("R10C10_R10C11_Vertical")
        self.R10C10_R10C11_Vertical.clicked.connect(partial(self.addtodict,self.R10C10_R10C11_Vertical))

        #--------------------------------------------------------------------
        
        self.R11C3_R12C3_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R11C3_R12C3_Horizontal.setGeometry(QtCore.QRect(100, 550, 39, 8))
        self.R11C3_R12C3_Horizontal.setText("")
        self.R11C3_R12C3_Horizontal.setObjectName("R11C3_R12C3_Horizontal")
        self.R11C3_R12C3_Horizontal.clicked.connect(partial(self.addtodict,self.R11C3_R12C3_Horizontal))

        #--------------------------------------------------------------------
        
        self.R2C2_R2C3_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R2C2_R2C3_Vertical.setGeometry(QtCore.QRect(94, 64, 8, 33))
        self.R2C2_R2C3_Vertical.setText("")
        self.R2C2_R2C3_Vertical.setObjectName("R2C2_R2C3_Vertical")
        self.R2C2_R2C3_Vertical.clicked.connect(partial(self.addtodict,self.R2C2_R2C3_Vertical))

        #--------------------------------------------------------------------
        
        self.R8C7_R8C8_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R8C7_R8C8_Vertical.setGeometry(QtCore.QRect(296, 364, 8, 33))
        self.R8C7_R8C8_Vertical.setText("")
        self.R8C7_R8C8_Vertical.setObjectName("R8C7_R8C8_Vertical")
        self.R8C7_R8C8_Vertical.clicked.connect(partial(self.addtodict,self.R8C7_R8C8_Vertical))

        #--------------------------------------------------------------------
        
        self.R3C12_R4C12_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R3C12_R4C12_Horizontal.setGeometry(QtCore.QRect(460, 150, 39, 8))
        self.R3C12_R4C12_Horizontal.setText("")
        self.R3C12_R4C12_Horizontal.setObjectName("R3C12_R4C12_Horizontal")
        self.R3C12_R4C12_Horizontal.clicked.connect(partial(self.addtodict,self.R3C12_R4C12_Horizontal))

        #--------------------------------------------------------------------
        
        self.R11C10_R11C11_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R11C10_R11C11_Vertical.setGeometry(QtCore.QRect(416, 514, 8, 33))
        self.R11C10_R11C11_Vertical.setText("")
        self.R11C10_R11C11_Vertical.setObjectName("R11C10_R11C11_Vertical")
        self.R11C10_R11C11_Vertical.clicked.connect(partial(self.addtodict,self.R11C10_R11C11_Vertical))

        #--------------------------------------------------------------------
        
        self.R10C9_R10C10_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R10C9_R10C10_Vertical.setGeometry(QtCore.QRect(376, 464, 8, 33))
        self.R10C9_R10C10_Vertical.setText("")
        self.R10C9_R10C10_Vertical.setObjectName("R10C9_R10C10_Vertical")
        self.R10C9_R10C10_Vertical.clicked.connect(partial(self.addtodict,self.R10C9_R10C10_Vertical))

        #--------------------------------------------------------------------
        
        self.R9C1_R9C2_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R9C1_R9C2_Vertical.setGeometry(QtCore.QRect(54, 414, 8, 33))
        self.R9C1_R9C2_Vertical.setText("")
        self.R9C1_R9C2_Vertical.setObjectName("R9C1_R9C2_Vertical")
        self.R9C1_R9C2_Vertical.clicked.connect(partial(self.addtodict,self.R9C1_R9C2_Vertical))

        #--------------------------------------------------------------------
        
        self.R6C10_R7C10_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R6C10_R7C10_Horizontal.setGeometry(QtCore.QRect(380, 300, 39, 8))
        self.R6C10_R7C10_Horizontal.setText("")
        self.R6C10_R7C10_Horizontal.setObjectName("R6C10_R7C10_Horizontal")
        self.R6C10_R7C10_Horizontal.clicked.connect(partial(self.addtodict,self.R6C10_R7C10_Horizontal))

        #--------------------------------------------------------------------
        
        self.R12C10_R12C11_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R12C10_R12C11_Vertical.setGeometry(QtCore.QRect(416, 564, 8, 33))
        self.R12C10_R12C11_Vertical.setText("")
        self.R12C10_R12C11_Vertical.setObjectName("R12C10_R12C11_Vertical")
        self.R12C10_R12C11_Vertical.clicked.connect(partial(self.addtodict,self.R12C10_R12C11_Vertical))

        #--------------------------------------------------------------------
        
        self.R7C12_R7C13_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R7C12_R7C13_Vertical.setGeometry(QtCore.QRect(497, 314, 8, 33))
        self.R7C12_R7C13_Vertical.setText("")
        self.R7C12_R7C13_Vertical.setObjectName("R7C12_R7C13_Vertical")
        self.R7C12_R7C13_Vertical.clicked.connect(partial(self.addtodict,self.R7C12_R7C13_Vertical))

        #--------------------------------------------------------------------
        
        self.R14C5_R14C6_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R14C5_R14C6_Vertical.setGeometry(QtCore.QRect(215, 664, 8, 33))
        self.R14C5_R14C6_Vertical.setText("")
        self.R14C5_R14C6_Vertical.setObjectName("R14C5_R14C6_Vertical")
        self.R14C5_R14C6_Vertical.clicked.connect(partial(self.addtodict,self.R14C5_R14C6_Vertical))

        #--------------------------------------------------------------------
        
        self.R13C4_R13C5_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R13C4_R13C5_Vertical.setGeometry(QtCore.QRect(175, 614, 8, 33))
        self.R13C4_R13C5_Vertical.setText("")
        self.R13C4_R13C5_Vertical.setObjectName("R13C4_R13C5_Vertical")
        self.R13C4_R13C5_Vertical.clicked.connect(partial(self.addtodict,self.R13C4_R13C5_Vertical))

        #--------------------------------------------------------------------
        
        self.R6C1_R7C1_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R6C1_R7C1_Horizontal.setGeometry(QtCore.QRect(20, 300, 39, 8))
        self.R6C1_R7C1_Horizontal.setText("")
        self.R6C1_R7C1_Horizontal.setObjectName("R6C1_R7C1_Horizontal")
        self.R6C1_R7C1_Horizontal.clicked.connect(partial(self.addtodict,self.R6C1_R7C1_Horizontal))

        #--------------------------------------------------------------------
        
        self.R5C2_R5C3_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R5C2_R5C3_Vertical.setGeometry(QtCore.QRect(94, 214, 8, 33))
        self.R5C2_R5C3_Vertical.setText("")
        self.R5C2_R5C3_Vertical.setObjectName("R5C2_R5C3_Vertical")
        self.R5C2_R5C3_Vertical.clicked.connect(partial(self.addtodict,self.R5C2_R5C3_Vertical))

        #--------------------------------------------------------------------
        
        self.R3C7_R3C8_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R3C7_R3C8_Vertical.setGeometry(QtCore.QRect(296, 114, 8, 33))
        self.R3C7_R3C8_Vertical.setText("")
        self.R3C7_R3C8_Vertical.setObjectName("R3C7_R3C8_Vertical")
        self.R3C7_R3C8_Vertical.clicked.connect(partial(self.addtodict,self.R3C7_R3C8_Vertical))

        #--------------------------------------------------------------------
        
        self.R2C8_R2C9_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R2C8_R2C9_Vertical.setGeometry(QtCore.QRect(334, 64, 8, 33))
        self.R2C8_R2C9_Vertical.setText("")
        self.R2C8_R2C9_Vertical.setObjectName("R2C8_R2C9_Vertical")
        self.R2C8_R2C9_Vertical.clicked.connect(partial(self.addtodict,self.R2C8_R2C9_Vertical))

        #--------------------------------------------------------------------
        
        self.R9C3_R9C4_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R9C3_R9C4_Vertical.setGeometry(QtCore.QRect(135, 414, 8, 33))
        self.R9C3_R9C4_Vertical.setText("")
        self.R9C3_R9C4_Vertical.setObjectName("R9C3_R9C4_Vertical")
        self.R9C3_R9C4_Vertical.clicked.connect(partial(self.addtodict,self.R9C3_R9C4_Vertical))

        #--------------------------------------------------------------------
        
        self.R12C5_R12C6_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R12C5_R12C6_Vertical.setGeometry(QtCore.QRect(215, 564, 8, 33))
        self.R12C5_R12C6_Vertical.setText("")
        self.R12C5_R12C6_Vertical.setObjectName("R12C5_R12C6_Vertical")
        self.R12C5_R12C6_Vertical.clicked.connect(partial(self.addtodict,self.R12C5_R12C6_Vertical))

        #--------------------------------------------------------------------
        
        self.R12C7_R12C8_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R12C7_R12C8_Vertical.setGeometry(QtCore.QRect(296, 564, 8, 33))
        self.R12C7_R12C8_Vertical.setText("")
        self.R12C7_R12C8_Vertical.setObjectName("R12C7_R12C8_Vertical")
        self.R12C7_R12C8_Vertical.clicked.connect(partial(self.addtodict,self.R12C7_R12C8_Vertical))

        #--------------------------------------------------------------------
        
        self.R2C1_R2C2_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R2C1_R2C2_Vertical.setGeometry(QtCore.QRect(54, 64, 8, 33))
        self.R2C1_R2C2_Vertical.setText("")
        self.R2C1_R2C2_Vertical.setObjectName("R2C1_R2C2_Vertical")
        self.R2C1_R2C2_Vertical.clicked.connect(partial(self.addtodict,self.R2C1_R2C2_Vertical))

        #--------------------------------------------------------------------
        
        self.R1C8_R1C9_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R1C8_R1C9_Vertical.setGeometry(QtCore.QRect(334, 20, 8, 33))
        self.R1C8_R1C9_Vertical.setText("")
        self.R1C8_R1C9_Vertical.setObjectName("R1C8_R1C9_Vertical")
        self.R1C8_R1C9_Vertical.clicked.connect(partial(self.addtodict,self.R1C8_R1C9_Vertical))

        #--------------------------------------------------------------------
        
        self.R13C1_R14C1_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R13C1_R14C1_Horizontal.setGeometry(QtCore.QRect(20, 650, 39, 8))
        self.R13C1_R14C1_Horizontal.setText("")
        self.R13C1_R14C1_Horizontal.setObjectName("R13C1_R14C1_Horizontal")
        self.R13C1_R14C1_Horizontal.clicked.connect(partial(self.addtodict,self.R13C1_R14C1_Horizontal))

        #--------------------------------------------------------------------
        
        self.R8C6_R9C6_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R8C6_R9C6_Horizontal.setGeometry(QtCore.QRect(220, 400, 39, 8))
        self.R8C6_R9C6_Horizontal.setText("")
        self.R8C6_R9C6_Horizontal.setObjectName("R8C6_R9C6_Horizontal")
        self.R8C6_R9C6_Horizontal.clicked.connect(partial(self.addtodict,self.R8C6_R9C6_Horizontal))

        #--------------------------------------------------------------------
        
        self.R2C6_R3C6_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R2C6_R3C6_Horizontal.setGeometry(QtCore.QRect(220, 100, 39, 8))
        self.R2C6_R3C6_Horizontal.setText("")
        self.R2C6_R3C6_Horizontal.setObjectName("R2C6_R3C6_Horizontal")
        self.R2C6_R3C6_Horizontal.clicked.connect(partial(self.addtodict,self.R2C6_R3C6_Horizontal))

        #--------------------------------------------------------------------
        
        self.R3C12_R3C13_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R3C12_R3C13_Vertical.setGeometry(QtCore.QRect(497, 114, 8, 33))
        self.R3C12_R3C13_Vertical.setText("")
        self.R3C12_R3C13_Vertical.setObjectName("R3C12_R3C13_Vertical")
        self.R3C12_R3C13_Vertical.clicked.connect(partial(self.addtodict,self.R3C12_R3C13_Vertical))

        #--------------------------------------------------------------------
        
        self.R1C5_R1C6_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R1C5_R1C6_Vertical.setGeometry(QtCore.QRect(215, 20, 8, 33))
        self.R1C5_R1C6_Vertical.setText("")
        self.R1C5_R1C6_Vertical.setObjectName("R1C5_R1C6_Vertical")
        self.R1C5_R1C6_Vertical.clicked.connect(partial(self.addtodict,self.R1C5_R1C6_Vertical))

        #--------------------------------------------------------------------
        
        self.Upper_10 = QtWidgets.QPushButton(self.centralwidget)
        self.Upper_10.setGeometry(QtCore.QRect(380, 10, 39, 8))
        self.Upper_10.setText("")
        self.Upper_10.setObjectName("Upper_10")
        self.Upper_10.setStyleSheet("background-color: red")
        self.Upper_10.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R5C11_R6C11_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R5C11_R6C11_Horizontal.setGeometry(QtCore.QRect(420, 250, 39, 8))
        self.R5C11_R6C11_Horizontal.setText("")
        self.R5C11_R6C11_Horizontal.setObjectName("R5C11_R6C11_Horizontal")
        self.R5C11_R6C11_Horizontal.clicked.connect(partial(self.addtodict,self.R5C11_R6C11_Horizontal))

        #--------------------------------------------------------------------
        
        self.R4C5_R5C5_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R4C5_R5C5_Horizontal.setGeometry(QtCore.QRect(180, 200, 39, 8))
        self.R4C5_R5C5_Horizontal.setText("")
        self.R4C5_R5C5_Horizontal.setObjectName("R4C5_R5C5_Horizontal")
        self.R4C5_R5C5_Horizontal.clicked.connect(partial(self.addtodict,self.R4C5_R5C5_Horizontal))

        #--------------------------------------------------------------------
        
        self.R3C6_R4C6_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R3C6_R4C6_Horizontal.setGeometry(QtCore.QRect(220, 150, 39, 8))
        self.R3C6_R4C6_Horizontal.setText("")
        self.R3C6_R4C6_Horizontal.setObjectName("R3C6_R4C6_Horizontal")
        self.R3C6_R4C6_Horizontal.clicked.connect(partial(self.addtodict,self.R3C6_R4C6_Horizontal))

        #--------------------------------------------------------------------
        
        self.R3C8_R4C8_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R3C8_R4C8_Horizontal.setGeometry(QtCore.QRect(300, 150, 39, 8))
        self.R3C8_R4C8_Horizontal.setText("")
        self.R3C8_R4C8_Horizontal.setObjectName("R3C8_R4C8_Horizontal")
        self.R3C8_R4C8_Horizontal.clicked.connect(partial(self.addtodict,self.R3C8_R4C8_Horizontal))

        #--------------------------------------------------------------------
        
        self.R9C13_R10C13_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R9C13_R10C13_Horizontal.setGeometry(QtCore.QRect(500, 450, 39, 8))
        self.R9C13_R10C13_Horizontal.setText("")
        self.R9C13_R10C13_Horizontal.setObjectName("R9C13_R10C13_Horizontal")
        self.R9C13_R10C13_Horizontal.clicked.connect(partial(self.addtodict,self.R9C13_R10C13_Horizontal))

        #--------------------------------------------------------------------
        
        self.R3C3_R3C4_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R3C3_R3C4_Vertical.setGeometry(QtCore.QRect(135, 114, 8, 33))
        self.R3C3_R3C4_Vertical.setText("")
        self.R3C3_R3C4_Vertical.setObjectName("R3C3_R3C4_Vertical")
        self.R3C3_R3C4_Vertical.clicked.connect(partial(self.addtodict,self.R3C3_R3C4_Vertical))

        #--------------------------------------------------------------------
        
        self.R10C11_R10C12_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R10C11_R10C12_Vertical.setGeometry(QtCore.QRect(455, 464, 8, 33))
        self.R10C11_R10C12_Vertical.setText("")
        self.R10C11_R10C12_Vertical.setObjectName("R10C11_R10C12_Vertical")
        self.R10C11_R10C12_Vertical.clicked.connect(partial(self.addtodict,self.R10C11_R10C12_Vertical))

        #--------------------------------------------------------------------
        
        self.R1C3_R2C3_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R1C3_R2C3_Horizontal.setGeometry(QtCore.QRect(100, 56, 39, 8))
        self.R1C3_R2C3_Horizontal.setText("")
        self.R1C3_R2C3_Horizontal.setObjectName("R1C3_R2C3_Horizontal")
        self.R1C3_R2C3_Horizontal.clicked.connect(partial(self.addtodict,self.R1C3_R2C3_Horizontal))

        #--------------------------------------------------------------------
        
        self.R11C1_R11C2_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R11C1_R11C2_Vertical.setGeometry(QtCore.QRect(54, 514, 8, 33))
        self.R11C1_R11C2_Vertical.setText("")
        self.R11C1_R11C2_Vertical.setObjectName("R11C1_R11C2_Vertical")
        self.R11C1_R11C2_Vertical.clicked.connect(partial(self.addtodict,self.R11C1_R11C2_Vertical))

        #--------------------------------------------------------------------
        
        self.Right_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Right_7.setGeometry(QtCore.QRect(570, 314, 8, 33))
        self.Right_7.setText("")
        self.Right_7.setObjectName("Right_7")
        self.Right_7.setStyleSheet("background-color: red")
        self.Right_7.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R11C12_R12C12_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R11C12_R12C12_Horizontal.setGeometry(QtCore.QRect(460, 550, 39, 8))
        self.R11C12_R12C12_Horizontal.setText("")
        self.R11C12_R12C12_Horizontal.setObjectName("R11C12_R12C12_Horizontal")
        self.R11C12_R12C12_Horizontal.clicked.connect(partial(self.addtodict,self.R11C12_R12C12_Horizontal))

        #--------------------------------------------------------------------
        
        self.R13C4_R14C4_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R13C4_R14C4_Horizontal.setGeometry(QtCore.QRect(140, 650, 39, 8))
        self.R13C4_R14C4_Horizontal.setText("")
        self.R13C4_R14C4_Horizontal.setObjectName("R13C4_R14C4_Horizontal")
        self.R13C4_R14C4_Horizontal.clicked.connect(partial(self.addtodict,self.R13C4_R14C4_Horizontal))

        #--------------------------------------------------------------------
        
        self.R1C7_R1C8_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R1C7_R1C8_Vertical.setGeometry(QtCore.QRect(296, 20, 8, 33))
        self.R1C7_R1C8_Vertical.setText("")
        self.R1C7_R1C8_Vertical.setObjectName("R1C7_R1C8_Vertical")
        self.R1C7_R1C8_Vertical.clicked.connect(partial(self.addtodict,self.R1C7_R1C8_Vertical))

        #--------------------------------------------------------------------
        
        self.R3C11_R3C12_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R3C11_R3C12_Vertical.setGeometry(QtCore.QRect(455, 114, 8, 33))
        self.R3C11_R3C12_Vertical.setText("")
        self.R3C11_R3C12_Vertical.setObjectName("R3C11_R3C12_Vertical")
        self.R3C11_R3C12_Vertical.clicked.connect(partial(self.addtodict,self.R3C11_R3C12_Vertical))

        #--------------------------------------------------------------------
        
        self.R10C3_R10C4_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R10C3_R10C4_Vertical.setGeometry(QtCore.QRect(135, 464, 8, 33))
        self.R10C3_R10C4_Vertical.setText("")
        self.R10C3_R10C4_Vertical.setObjectName("R10C3_R10C4_Vertical")
        self.R10C3_R10C4_Vertical.clicked.connect(partial(self.addtodict,self.R10C3_R10C4_Vertical))

        #--------------------------------------------------------------------
        
        self.Left_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Left_9.setGeometry(QtCore.QRect(20, 414, 8, 33))
        self.Left_9.setText("")
        self.Left_9.setObjectName("Left_9")
        self.Left_9.setStyleSheet("background-color: red")
        self.Left_9.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R11C5_R11C6_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R11C5_R11C6_Vertical.setGeometry(QtCore.QRect(215, 514, 8, 33))
        self.R11C5_R11C6_Vertical.setText("")
        self.R11C5_R11C6_Vertical.setObjectName("R11C5_R11C6_Vertical")
        self.R11C5_R11C6_Vertical.clicked.connect(partial(self.addtodict,self.R11C5_R11C6_Vertical))

        #--------------------------------------------------------------------
        
        self.R1C1_R1C2_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R1C1_R1C2_Vertical.setGeometry(QtCore.QRect(54, 20, 8, 33))
        self.R1C1_R1C2_Vertical.setText("")
        self.R1C1_R1C2_Vertical.setObjectName("R1C1_R1C2_Vertical")
        self.R1C1_R1C2_Vertical.clicked.connect(partial(self.addtodict,self.R1C1_R1C2_Vertical))

        #--------------------------------------------------------------------
        
        self.R8C9_R9C9_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R8C9_R9C9_Horizontal.setGeometry(QtCore.QRect(340, 400, 39, 8))
        self.R8C9_R9C9_Horizontal.setText("")
        self.R8C9_R9C9_Horizontal.setObjectName("R8C9_R9C9_Horizontal")
        self.R8C9_R9C9_Horizontal.clicked.connect(partial(self.addtodict,self.R8C9_R9C9_Horizontal))

        #--------------------------------------------------------------------
        
        self.R1C11_R2C11_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R1C11_R2C11_Horizontal.setGeometry(QtCore.QRect(420, 56, 39, 8))
        self.R1C11_R2C11_Horizontal.setText("")
        self.R1C11_R2C11_Horizontal.setObjectName("R1C11_R2C11_Horizontal")
        self.R1C11_R2C11_Horizontal.clicked.connect(partial(self.addtodict,self.R1C11_R2C11_Horizontal))

        #--------------------------------------------------------------------
        
        self.R4C6_R5C6_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R4C6_R5C6_Horizontal.setGeometry(QtCore.QRect(220, 200, 39, 8))
        self.R4C6_R5C6_Horizontal.setText("")
        self.R4C6_R5C6_Horizontal.setObjectName("R4C6_R5C6_Horizontal")
        self.R4C6_R5C6_Horizontal.clicked.connect(partial(self.addtodict,self.R4C6_R5C6_Horizontal))

        #--------------------------------------------------------------------
        
        self.R14C10_R14C11_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R14C10_R14C11_Vertical.setGeometry(QtCore.QRect(416, 664, 8, 33))
        self.R14C10_R14C11_Vertical.setText("")
        self.R14C10_R14C11_Vertical.setObjectName("R14C10_R14C11_Vertical")
        self.R14C10_R14C11_Vertical.clicked.connect(partial(self.addtodict,self.R14C10_R14C11_Vertical))

        #--------------------------------------------------------------------
        
        self.R4C5_R4C6_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R4C5_R4C6_Vertical.setGeometry(QtCore.QRect(215, 164, 8, 33))
        self.R4C5_R4C6_Vertical.setText("")
        self.R4C5_R4C6_Vertical.setObjectName("R4C5_R4C6_Vertical")
        self.R4C5_R4C6_Vertical.clicked.connect(partial(self.addtodict,self.R4C5_R4C6_Vertical))

        #--------------------------------------------------------------------
        
        self.R11C5_R12C5_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R11C5_R12C5_Horizontal.setGeometry(QtCore.QRect(180, 550, 39, 8))
        self.R11C5_R12C5_Horizontal.setText("")
        self.R11C5_R12C5_Horizontal.setObjectName("R11C5_R12C5_Horizontal")
        self.R11C5_R12C5_Horizontal.clicked.connect(partial(self.addtodict,self.R11C5_R12C5_Horizontal))

        #--------------------------------------------------------------------
        
        self.R5C9_R6C9_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R5C9_R6C9_Horizontal.setGeometry(QtCore.QRect(340, 250, 39, 8))
        self.R5C9_R6C9_Horizontal.setText("")
        self.R5C9_R6C9_Horizontal.setObjectName("R5C9_R6C9_Horizontal")
        self.R5C9_R6C9_Horizontal.clicked.connect(partial(self.addtodict,self.R5C9_R6C9_Horizontal))

        #--------------------------------------------------------------------
        
        self.R7C11_R8C11_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R7C11_R8C11_Horizontal.setGeometry(QtCore.QRect(420, 350, 39, 8))
        self.R7C11_R8C11_Horizontal.setText("")
        self.R7C11_R8C11_Horizontal.setObjectName("R7C11_R8C11_Horizontal")
        self.R7C11_R8C11_Horizontal.clicked.connect(partial(self.addtodict,self.R7C11_R8C11_Horizontal))

        #--------------------------------------------------------------------
        
        self.R9C6_R9C7_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R9C6_R9C7_Vertical.setGeometry(QtCore.QRect(256, 414, 8, 33))
        self.R9C6_R9C7_Vertical.setText("")
        self.R9C6_R9C7_Vertical.setObjectName("R9C6_R9C7_Vertical")
        self.R9C6_R9C7_Vertical.clicked.connect(partial(self.addtodict,self.R9C6_R9C7_Vertical))

        #--------------------------------------------------------------------
        
        self.R1C1_R2C1_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R1C1_R2C1_Horizontal.setGeometry(QtCore.QRect(20, 56, 39, 8))
        self.R1C1_R2C1_Horizontal.setText("")
        self.R1C1_R2C1_Horizontal.setObjectName("R1C1_R2C1_Horizontal")
        self.R1C1_R2C1_Horizontal.clicked.connect(partial(self.addtodict,self.R1C1_R2C1_Horizontal))

        #--------------------------------------------------------------------
        
        self.R5C8_R6C8_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R5C8_R6C8_Horizontal.setGeometry(QtCore.QRect(300, 250, 39, 8))
        self.R5C8_R6C8_Horizontal.setText("")
        self.R5C8_R6C8_Horizontal.setObjectName("R5C8_R6C8_Horizontal")
        self.R5C8_R6C8_Horizontal.clicked.connect(partial(self.addtodict,self.R5C8_R6C8_Horizontal))

        #--------------------------------------------------------------------
        
        self.R10C5_R11C5_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R10C5_R11C5_Horizontal.setGeometry(QtCore.QRect(180, 500, 39, 8))
        self.R10C5_R11C5_Horizontal.setText("")
        self.R10C5_R11C5_Horizontal.setObjectName("R10C5_R11C5_Horizontal")
        self.R10C5_R11C5_Horizontal.clicked.connect(partial(self.addtodict,self.R10C5_R11C5_Horizontal))

        #--------------------------------------------------------------------
        
        self.R11C6_R11C7_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R11C6_R11C7_Vertical.setGeometry(QtCore.QRect(256, 514, 8, 33))
        self.R11C6_R11C7_Vertical.setText("")
        self.R11C6_R11C7_Vertical.setObjectName("R11C6_R11C7_Vertical")
        self.R11C6_R11C7_Vertical.clicked.connect(partial(self.addtodict,self.R11C6_R11C7_Vertical))

        #--------------------------------------------------------------------
        
        self.Right_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Right_6.setGeometry(QtCore.QRect(570, 264, 8, 33))
        self.Right_6.setText("")
        self.Right_6.setObjectName("Right_6")
        self.Right_6.setStyleSheet("background-color: red")
        self.Right_6.setEnabled(False)

        #--------------------------------------------------------------------

        self.R2C4_R2C5_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R2C4_R2C5_Vertical.setGeometry(QtCore.QRect(175, 64, 8, 33))
        self.R2C4_R2C5_Vertical.setText("")
        self.R2C4_R2C5_Vertical.setObjectName("R2C4_R2C5_Vertical")
        self.R2C4_R2C5_Vertical.clicked.connect(partial(self.addtodict,self.R2C4_R2C5_Vertical))

        #--------------------------------------------------------------------
        
        self.R11C4_R11C5_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R11C4_R11C5_Vertical.setGeometry(QtCore.QRect(175, 514, 8, 33))
        self.R11C4_R11C5_Vertical.setText("")
        self.R11C4_R11C5_Vertical.setObjectName("R11C4_R11C5_Vertical")
        self.R11C4_R11C5_Vertical.clicked.connect(partial(self.addtodict,self.R11C4_R11C5_Vertical))

        #--------------------------------------------------------------------
        
        self.R8C3_R9C3_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R8C3_R9C3_Horizontal.setGeometry(QtCore.QRect(100, 400, 39, 8))
        self.R8C3_R9C3_Horizontal.setText("")
        self.R8C3_R9C3_Horizontal.setObjectName("R8C3_R9C3_Horizontal")
        self.R8C3_R9C3_Horizontal.clicked.connect(partial(self.addtodict,self.R8C3_R9C3_Horizontal))

        #--------------------------------------------------------------------
        
        self.R1C11_R1C12_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R1C11_R1C12_Vertical.setGeometry(QtCore.QRect(455, 20, 8, 33))
        self.R1C11_R1C12_Vertical.setText("")
        self.R1C11_R1C12_Vertical.setObjectName("R1C11_R1C12_Vertical")
        self.R1C11_R1C12_Vertical.clicked.connect(partial(self.addtodict,self.R1C11_R1C12_Vertical))

        #--------------------------------------------------------------------
        
        self.R7C14_R8C14_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R7C14_R8C14_Horizontal.setGeometry(QtCore.QRect(540, 350, 39, 8))
        self.R7C14_R8C14_Horizontal.setText("")
        self.R7C14_R8C14_Horizontal.setObjectName("R7C14_R8C14_Horizontal")
        self.R7C14_R8C14_Horizontal.clicked.connect(partial(self.addtodict,self.R7C14_R8C14_Horizontal))

        #--------------------------------------------------------------------
        
        self.R9C9_R10C9_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R9C9_R10C9_Horizontal.setGeometry(QtCore.QRect(340, 450, 39, 8))
        self.R9C9_R10C9_Horizontal.setText("")
        self.R9C9_R10C9_Horizontal.setObjectName("R9C9_R10C9_Horizontal")
        self.R9C9_R10C9_Horizontal.clicked.connect(partial(self.addtodict,self.R9C9_R10C9_Horizontal))

        #--------------------------------------------------------------------
        
        self.R8C12_R8C13_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R8C12_R8C13_Vertical.setGeometry(QtCore.QRect(497, 364, 8, 33))
        self.R8C12_R8C13_Vertical.setText("")
        self.R8C12_R8C13_Vertical.setObjectName("R8C12_R8C13_Vertical")
        self.R8C12_R8C13_Vertical.clicked.connect(partial(self.addtodict,self.R8C12_R8C13_Vertical))

        #--------------------------------------------------------------------
        
        self.R2C11_R3C11_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R2C11_R3C11_Horizontal.setGeometry(QtCore.QRect(420, 100, 39, 8))
        self.R2C11_R3C11_Horizontal.setText("")
        self.R2C11_R3C11_Horizontal.setObjectName("R2C11_R3C11_Horizontal")
        self.R2C11_R3C11_Horizontal.clicked.connect(partial(self.addtodict,self.R2C11_R3C11_Horizontal))

        #--------------------------------------------------------------------
        
        self.R8C4_R8C5_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R8C4_R8C5_Vertical.setGeometry(QtCore.QRect(175, 364, 8, 33))
        self.R8C4_R8C5_Vertical.setText("")
        self.R8C4_R8C5_Vertical.setObjectName("R8C4_R8C5_Vertical")
        self.R8C4_R8C5_Vertical.clicked.connect(partial(self.addtodict,self.R8C4_R8C5_Vertical))

        #--------------------------------------------------------------------
        
        self.R5C11_R5C12_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R5C11_R5C12_Vertical.setGeometry(QtCore.QRect(455, 214, 8, 33))
        self.R5C11_R5C12_Vertical.setText("")
        self.R5C11_R5C12_Vertical.setObjectName("R5C11_R5C12_Vertical")
        self.R5C11_R5C12_Vertical.clicked.connect(partial(self.addtodict,self.R5C11_R5C12_Vertical))

        #--------------------------------------------------------------------
        
        self.R7C9_R8C9_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R7C9_R8C9_Horizontal.setGeometry(QtCore.QRect(340, 350, 39, 8))
        self.R7C9_R8C9_Horizontal.setText("")
        self.R7C9_R8C9_Horizontal.setObjectName("R7C9_R8C9_Horizontal")
        self.R7C9_R8C9_Horizontal.clicked.connect(partial(self.addtodict,self.R7C9_R8C9_Horizontal))

        #--------------------------------------------------------------------
        
        self.Upper_12 = QtWidgets.QPushButton(self.centralwidget)
        self.Upper_12.setGeometry(QtCore.QRect(460, 10, 39, 8))
        self.Upper_12.setText("")
        self.Upper_12.setObjectName("Upper_12")
        self.Upper_12.setStyleSheet("background-color: red")
        self.Upper_12.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R6C3_R7C3_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R6C3_R7C3_Horizontal.setGeometry(QtCore.QRect(100, 300, 39, 8))
        self.R6C3_R7C3_Horizontal.setText("")
        self.R6C3_R7C3_Horizontal.setObjectName("R6C3_R7C3_Horizontal")
        self.R6C3_R7C3_Horizontal.clicked.connect(partial(self.addtodict,self.R6C3_R7C3_Horizontal))

        #--------------------------------------------------------------------
        
        self.R12C3_R13C3_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R12C3_R13C3_Horizontal.setGeometry(QtCore.QRect(100, 600, 39, 8))
        self.R12C3_R13C3_Horizontal.setText("")
        self.R12C3_R13C3_Horizontal.setObjectName("R12C3_R13C3_Horizontal")
        self.R12C3_R13C3_Horizontal.clicked.connect(partial(self.addtodict,self.R12C3_R13C3_Horizontal))

        #--------------------------------------------------------------------
        
        self.R7C4_R7C5_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R7C4_R7C5_Vertical.setGeometry(QtCore.QRect(175, 314, 8, 33))
        self.R7C4_R7C5_Vertical.setText("")
        self.R7C4_R7C5_Vertical.setObjectName("R7C4_R7C5_Vertical")
        self.R7C4_R7C5_Vertical.clicked.connect(partial(self.addtodict,self.R7C4_R7C5_Vertical))

        #--------------------------------------------------------------------
        
        self.R3C1_R3C2_Vertical = QtWidgets.QPushButton(self.centralwidget)
        self.R3C1_R3C2_Vertical.setGeometry(QtCore.QRect(54, 114, 8, 33))
        self.R3C1_R3C2_Vertical.setText("")
        self.R3C1_R3C2_Vertical.setObjectName("R3C1_R3C2_Vertical")
        self.R3C1_R3C2_Vertical.clicked.connect(partial(self.addtodict,self.R3C1_R3C2_Vertical))

        #--------------------------------------------------------------------
        
        self.Right_13 = QtWidgets.QPushButton(self.centralwidget)
        self.Right_13.setGeometry(QtCore.QRect(570, 614, 8, 33))
        self.Right_13.setText("")
        self.Right_13.setObjectName("Right_13")
        self.Right_13.setStyleSheet("background-color: red")
        self.Right_13.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R1C12_R2C12_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R1C12_R2C12_Horizontal.setGeometry(QtCore.QRect(460, 56, 39, 8))
        self.R1C12_R2C12_Horizontal.setText("")
        self.R1C12_R2C12_Horizontal.setObjectName("R1C12_R2C12_Horizontal")
        self.R1C12_R2C12_Horizontal.clicked.connect(partial(self.addtodict,self.R1C12_R2C12_Horizontal))

        #--------------------------------------------------------------------
        
        self.Upper_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Upper_2.setGeometry(QtCore.QRect(60, 10, 39, 8))
        self.Upper_2.setText("")
        self.Upper_2.setObjectName("Upper_2")
        self.Upper_2.setStyleSheet("background-color: red")
        self.Upper_2.setEnabled(False)

        #--------------------------------------------------------------------
        
        self.R11C10_R12C10_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R11C10_R12C10_Horizontal.setGeometry(QtCore.QRect(380, 550, 39, 8))
        self.R11C10_R12C10_Horizontal.setText("")
        self.R11C10_R12C10_Horizontal.setObjectName("R11C10_R12C10_Horizontal")
        self.R11C10_R12C10_Horizontal.clicked.connect(partial(self.addtodict,self.R11C10_R12C10_Horizontal))

        #--------------------------------------------------------------------
        
        self.R4C1_R5C1_Horizontal = QtWidgets.QPushButton(self.centralwidget)
        self.R4C1_R5C1_Horizontal.setGeometry(QtCore.QRect(20, 200, 39, 8))
        self.R4C1_R5C1_Horizontal.setText("")
        self.R4C1_R5C1_Horizontal.setObjectName("R4C1_R5C1_Horizontal")
        self.R4C1_R5C1_Horizontal.clicked.connect(partial(self.addtodict,self.R4C1_R5C1_Horizontal))

        #--------------------------------------------------------------------


        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(partial(self.toStr))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Generate"))


    def generate(self):
        print(maze_dic)

    def addtodict(self,btnObject):
        try:
            if maze_dic[btnObject] == True:
                #("background-color: rgb(255, 255, 255)");
                btnObject.setStyleSheet("")
                maze_dic[btnObject] = False
                #print("turn white")
            elif maze_dic[btnObject] == False:
                btnObject.setStyleSheet("background-color: red")
                maze_dic[btnObject] = True
                #print("turn red")
                
        except:
            maze_dic[btnObject] = True
            btnObject.setStyleSheet("background-color: red")
            #print("Initialize turn red")

    def toStr(self):
        string = []
        print(maze_dic)
        print(len(maze_dic))
        for i in maze_dic:
            if maze_dic[i] :
                s =  i.objectName().split("_")
                #print(s[0],s[1],s[2])
            
                #=========================================
                # let's extract rows and columns of
                # each cells
                #=========================================

                temp1 = s[0].split("C")
                temp2 = s[1].split("C")

                r1 = int(temp1[0][1:])
                c1 = int(temp1[1])
                r2 = int(temp2[0][1:])
                c2 = int(temp2[1])

                if(s[2]== "Horizontal"):
                    #print("wm.cells["+ str(r1-1) +"]["+ str(c1-1) +"].walls[2] = 1;")
                    #print("wm.cells["+ str(r2-1) +"]["+ str(c2-1) +"].walls[0] = 1;")

                    string.append( "wm.cells["+ str(r1-1) +"]["+ str(c1-1) +"].walls[2] = 1;")
                    string.append( "wm.cells["+ str(r2-1) +"]["+ str(c2-1) +"].walls[0] = 1;")
                
                elif (s[2]== "Vertical") :
                    #print("wm.cells["+ str(r1-1) +"]["+ str(c1-1) +"].walls[1] = 1;")
                    #print("wm.cells["+ str(r2-1) +"]["+ str(c2-1) +"].walls[3] = 1;")

                    string.append( "wm.cells["+ str(r1-1) +"]["+ str(c1-1) +"].walls[1] = 1;")
                    string.append( "wm.cells["+ str(r2-1) +"]["+ str(c2-1) +"].walls[3] = 1;")

        #print(string)
        filename = "wall_maze" + str(int(time.time())) + ".txt"
        f = open(filename, 'w+')
        for i in string:
            f.write(i)
            f.write("\n")
        f.close()
        print("Maze generated in " + filename)
        print("This maze generator was written by Tharaka Sachintha Ratnayake")
        
       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
