# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class principal_ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 596)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.Tabs.setTabsClosable(False)
        self.Tabs.setMovable(False)
        self.Tabs.setTabBarAutoHide(False)
        self.Tabs.setObjectName("Tabs")
        self.City = QtWidgets.QWidget()
        self.City.setObjectName("City")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.City)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_2 = QtWidgets.QLabel(self.City)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)
        self.line1_1 = QtWidgets.QLineEdit(self.City)
        self.line1_1.setObjectName("line1_1")
        self.gridLayout_6.addWidget(self.line1_1, 0, 2, 1, 1)
        self.line1_2 = QtWidgets.QLineEdit(self.City)
        self.line1_2.setObjectName("line1_2")
        self.gridLayout_6.addWidget(self.line1_2, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.City)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 2, 0, 1, 1)
        self.line1_3 = QtWidgets.QLineEdit(self.City)
        self.line1_3.setObjectName("line1_3")
        self.gridLayout_6.addWidget(self.line1_3, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.City)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.City)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.City)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_6.addWidget(self.comboBox, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_6)
        self.Tabs.addTab(self.City, "")
        self.Country = QtWidgets.QWidget()
        self.Country.setObjectName("Country")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Country)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_5 = QtWidgets.QLabel(self.Country)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
        self.line1_4 = QtWidgets.QLineEdit(self.Country)
        self.line1_4.setObjectName("line1_4")
        self.gridLayout_5.addWidget(self.line1_4, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        self.Tabs.addTab(self.Country, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_4, 1, 1, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.tab_3)
        self.timeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_4.addWidget(self.timeEdit, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_4.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_4)
        self.Tabs.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget_4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.line1_5 = QtWidgets.QLineEdit(self.tab_4)
        self.line1_5.setObjectName("line1_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line1_5)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.Tabs.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.line1_6 = QtWidgets.QLineEdit(self.tab)
        self.line1_6.setObjectName("line1_6")
        self.gridLayout_3.addWidget(self.line1_6, 0, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 1, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_3.addWidget(self.lineEdit_6, 1, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.Tabs.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_7.addWidget(self.label_12, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_7.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_7.addWidget(self.label_13, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_7.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_7.addWidget(self.label_21, 2, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_7.addWidget(self.lineEdit_7, 2, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_7)
        self.Tabs.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_16 = QtWidgets.QLabel(self.tab_5)
        self.label_16.setObjectName("label_16")
        self.gridLayout_8.addWidget(self.label_16, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_8.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_5)
        self.label_14.setObjectName("label_14")
        self.gridLayout_8.addWidget(self.label_14, 1, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_8.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab_5)
        self.label_15.setObjectName("label_15")
        self.gridLayout_8.addWidget(self.label_15, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_8.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_8)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_10.addWidget(self.tableWidget)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_22 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setAutoFillBackground(False)
        self.label_22.setObjectName("label_22")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.linetotal = QtWidgets.QLineEdit(self.tab_5)
        self.linetotal.setObjectName("linetotal")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.linetotal)
        self.verticalLayout_10.addLayout(self.formLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.tab_5)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_10.addWidget(self.pushButton)
        self.Tabs.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_19 = QtWidgets.QLabel(self.tab_6)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 0, 1, 1)
        self.line1_9 = QtWidgets.QLineEdit(self.tab_6)
        self.line1_9.setObjectName("line1_9")
        self.gridLayout.addWidget(self.line1_9, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab_6)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 1, 0, 1, 1)
        self.line1_8 = QtWidgets.QLineEdit(self.tab_6)
        self.line1_8.setObjectName("line1_8")
        self.gridLayout.addWidget(self.line1_8, 1, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.tab_6)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 0, 1, 1)
        self.line1_7 = QtWidgets.QLineEdit(self.tab_6)
        self.line1_7.setObjectName("line1_7")
        self.gridLayout.addWidget(self.line1_7, 2, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.Tabs.addTab(self.tab_6, "")
        self.verticalLayout_3.addWidget(self.Tabs)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableWidget_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Mostrar_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Mostrar_btn.setObjectName("Mostrar_btn")
        self.horizontalLayout.addWidget(self.Mostrar_btn)
        self.Insertar_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Insertar_btn.setObjectName("Insertar_btn")
        self.horizontalLayout.addWidget(self.Insertar_btn)
        self.Borrar_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Borrar_btn.setObjectName("Borrar_btn")
        self.horizontalLayout.addWidget(self.Borrar_btn)
        self.Actualizar_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Actualizar_btn.setObjectName("Actualizar_btn")
        self.horizontalLayout.addWidget(self.Actualizar_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Tabs.setCurrentIndex(7)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Corporal Gym"))
        self.label_2.setText(_translate("MainWindow", "Nombre"))
        self.label_3.setText(_translate("MainWindow", "Apellido"))
        self.label_4.setText(_translate("MainWindow", "Tipo"))
        self.label.setText(_translate("MainWindow", "Cedula"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Ingrese el tipo "))
        self.comboBox.setItemText(1, _translate("MainWindow", "Miembro"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Entrenador"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.City), _translate("MainWindow", "Persona"))
        self.label_5.setText(_translate("MainWindow", "Disciplina"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Country), _translate("MainWindow", "Disciplina"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Ingrese Disciplina"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "h:mm "))
        self.label_8.setText(_translate("MainWindow", "Horario inicio"))
        self.label_6.setText(_translate("MainWindow", "Entrenador"))
        self.label_7.setText(_translate("MainWindow", "Disciplina"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_3), _translate("MainWindow", "Clase"))
        self.label_10.setText(_translate("MainWindow", "Escoja la clase en la que se va a registrar e ingrese su cedula"))
        self.label_9.setText(_translate("MainWindow", "Cedula"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_4), _translate("MainWindow", "Participacion"))
        self.label_11.setText(_translate("MainWindow", "Descricpcion"))
        self.label_20.setText(_translate("MainWindow", "Stock"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab), _translate("MainWindow", "Inventario"))
        self.label_12.setText(_translate("MainWindow", "Descripcion"))
        self.label_13.setText(_translate("MainWindow", "Precio Actual"))
        self.label_21.setText(_translate("MainWindow", "Stock"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_2), _translate("MainWindow", "Implemento"))
        self.label_16.setText(_translate("MainWindow", "Cedula"))
        self.label_14.setText(_translate("MainWindow", "Item"))
        self.label_15.setText(_translate("MainWindow", "Cantidad"))
        self.label_22.setText(_translate("MainWindow", "Total:"))
        self.linetotal.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "Agregar"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_5), _translate("MainWindow", "Venta"))
        self.label_19.setText(_translate("MainWindow", "Cedula"))
        self.label_17.setText(_translate("MainWindow", "Precio"))
        self.label_18.setText(_translate("MainWindow", "Fecha expiracion"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_6), _translate("MainWindow", "Membresia"))
        self.Mostrar_btn.setText(_translate("MainWindow", "Mostrar datos"))
        self.Insertar_btn.setText(_translate("MainWindow", "Insertar registro"))
        self.Borrar_btn.setText(_translate("MainWindow", "Borrar registro"))
        self.Actualizar_btn.setText(_translate("MainWindow", "Actualizar registro"))
