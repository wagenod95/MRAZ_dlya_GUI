# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_choose_algorithm = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_choose_algorithm.setGeometry(QtCore.QRect(10, 10, 251, 201))
        self.tab_choose_algorithm.setObjectName("tab_choose_algorithm")
        self.tab_nsko = QtWidgets.QWidget()
        self.tab_nsko.setObjectName("tab_nsko")
        self.tool_train_or_test_nsko = QtWidgets.QToolBox(self.tab_nsko)
        self.tool_train_or_test_nsko.setEnabled(True)
        self.tool_train_or_test_nsko.setGeometry(QtCore.QRect(0, 0, 251, 171))
        self.tool_train_or_test_nsko.setObjectName("tool_train_or_test_nsko")
        self.tool_train_nsko = QtWidgets.QWidget()
        self.tool_train_nsko.setGeometry(QtCore.QRect(0, 0, 251, 117))
        self.tool_train_nsko.setObjectName("tool_train_nsko")
        self.spin_in_param_step_nsko = QtWidgets.QDoubleSpinBox(self.tool_train_nsko)
        self.spin_in_param_step_nsko.setGeometry(QtCore.QRect(150, 20, 62, 22))
        self.spin_in_param_step_nsko.setMaximum(1.0)
        self.spin_in_param_step_nsko.setSingleStep(0.01)
        self.spin_in_param_step_nsko.setProperty("value", 0.5)
        self.spin_in_param_step_nsko.setObjectName("spin_in_param_step_nsko")
        self.lable_in_param_step_nsko = QtWidgets.QLabel(self.tool_train_nsko)
        self.lable_in_param_step_nsko.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.lable_in_param_step_nsko.setWordWrap(True)
        self.lable_in_param_step_nsko.setObjectName("lable_in_param_step_nsko")
        self.push_train_nsko = QtWidgets.QPushButton(self.tool_train_nsko)
        self.push_train_nsko.setGeometry(QtCore.QRect(50, 70, 114, 32))
        self.push_train_nsko.setStyleSheet("")
        self.push_train_nsko.setObjectName("push_train_nsko")
        self.tool_train_or_test_nsko.addItem(self.tool_train_nsko, "")
        self.tool_test_nsko = QtWidgets.QWidget()
        self.tool_test_nsko.setEnabled(True)
        self.tool_test_nsko.setGeometry(QtCore.QRect(0, 0, 251, 117))
        self.tool_test_nsko.setObjectName("tool_test_nsko")
        self.push_test_nsko = QtWidgets.QPushButton(self.tool_test_nsko)
        self.push_test_nsko.setGeometry(QtCore.QRect(50, 50, 114, 32))
        self.push_test_nsko.setStyleSheet("")
        self.push_test_nsko.setObjectName("push_test_nsko")
        self.tool_train_or_test_nsko.addItem(self.tool_test_nsko, "")
        self.tab_choose_algorithm.addTab(self.tab_nsko, "")
        self.tab_hebb = QtWidgets.QWidget()
        self.tab_hebb.setObjectName("tab_hebb")
        self.tool_train_or_test_hebb = QtWidgets.QToolBox(self.tab_hebb)
        self.tool_train_or_test_hebb.setEnabled(True)
        self.tool_train_or_test_hebb.setGeometry(QtCore.QRect(0, 0, 251, 171))
        self.tool_train_or_test_hebb.setObjectName("tool_train_or_test_hebb")
        self.tool_train_hebb = QtWidgets.QWidget()
        self.tool_train_hebb.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.tool_train_hebb.setObjectName("tool_train_hebb")
        self.lable_in_param = QtWidgets.QLabel(self.tool_train_hebb)
        self.lable_in_param.setGeometry(QtCore.QRect(10, 10, 201, 51))
        self.lable_in_param.setWordWrap(True)
        self.lable_in_param.setObjectName("lable_in_param")
        self.push_train_hebb = QtWidgets.QPushButton(self.tool_train_hebb)
        self.push_train_hebb.setGeometry(QtCore.QRect(50, 70, 114, 32))
        self.push_train_hebb.setStyleSheet("")
        self.push_train_hebb.setObjectName("push_train_hebb")
        self.tool_train_or_test_hebb.addItem(self.tool_train_hebb, "")
        self.tool_test_hebb = QtWidgets.QWidget()
        self.tool_test_hebb.setEnabled(True)
        self.tool_test_hebb.setGeometry(QtCore.QRect(0, 0, 251, 117))
        self.tool_test_hebb.setObjectName("tool_test_hebb")
        self.push_test_hebb = QtWidgets.QPushButton(self.tool_test_hebb)
        self.push_test_hebb.setGeometry(QtCore.QRect(50, 50, 114, 32))
        self.push_test_hebb.setStyleSheet("")
        self.push_test_hebb.setObjectName("push_test_hebb")
        self.tool_train_or_test_hebb.addItem(self.tool_test_hebb, "")
        self.tab_choose_algorithm.addTab(self.tab_hebb, "")
        self.tab_perzeptron = QtWidgets.QWidget()
        self.tab_perzeptron.setObjectName("tab_perzeptron")
        self.tool_train_or_test_perzeptron = QtWidgets.QToolBox(self.tab_perzeptron)
        self.tool_train_or_test_perzeptron.setEnabled(True)
        self.tool_train_or_test_perzeptron.setGeometry(QtCore.QRect(0, 0, 251, 171))
        self.tool_train_or_test_perzeptron.setObjectName("tool_train_or_test_perzeptron")
        self.tool_train_perzeptron = QtWidgets.QWidget()
        self.tool_train_perzeptron.setGeometry(QtCore.QRect(0, 0, 251, 117))
        self.tool_train_perzeptron.setObjectName("tool_train_perzeptron")
        self.lable_in_param_perzeptron = QtWidgets.QLabel(self.tool_train_perzeptron)
        self.lable_in_param_perzeptron.setGeometry(QtCore.QRect(10, 10, 201, 51))
        self.lable_in_param_perzeptron.setWordWrap(True)
        self.lable_in_param_perzeptron.setObjectName("lable_in_param_perzeptron")
        self.push_train_perzeptron = QtWidgets.QPushButton(self.tool_train_perzeptron)
        self.push_train_perzeptron.setGeometry(QtCore.QRect(50, 70, 114, 32))
        self.push_train_perzeptron.setStyleSheet("")
        self.push_train_perzeptron.setObjectName("push_train_perzeptron")
        self.tool_train_or_test_perzeptron.addItem(self.tool_train_perzeptron, "")
        self.tool_test_perzeptron = QtWidgets.QWidget()
        self.tool_test_perzeptron.setEnabled(True)
        self.tool_test_perzeptron.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.tool_test_perzeptron.setObjectName("tool_test_perzeptron")
        self.push_test_perzeptron = QtWidgets.QPushButton(self.tool_test_perzeptron)
        self.push_test_perzeptron.setGeometry(QtCore.QRect(50, 50, 114, 32))
        self.push_test_perzeptron.setStyleSheet("")
        self.push_test_perzeptron.setObjectName("push_test_perzeptron")
        self.tool_train_or_test_perzeptron.addItem(self.tool_test_perzeptron, "")
        self.tab_choose_algorithm.addTab(self.tab_perzeptron, "")
        self.tool_enter_data = QtWidgets.QToolBox(self.centralwidget)
        self.tool_enter_data.setGeometry(QtCore.QRect(10, 220, 251, 161))
        self.tool_enter_data.setObjectName("tool_enter_data")
        self.tool_train_data = QtWidgets.QWidget()
        self.tool_train_data.setGeometry(QtCore.QRect(0, 0, 251, 107))
        self.tool_train_data.setObjectName("tool_train_data")
        self.push_choose_train_y = QtWidgets.QPushButton(self.tool_train_data)
        self.push_choose_train_y.setGeometry(QtCore.QRect(0, 40, 114, 32))
        self.push_choose_train_y.setObjectName("push_choose_train_y")
        self.push_choose_train_x = QtWidgets.QPushButton(self.tool_train_data)
        self.push_choose_train_x.setGeometry(QtCore.QRect(0, 0, 114, 32))
        self.push_choose_train_x.setObjectName("push_choose_train_x")
        self.lable_push_choose_train_x = QtWidgets.QLabel(self.tool_train_data)
        self.lable_push_choose_train_x.setGeometry(QtCore.QRect(120, 0, 121, 31))
        self.lable_push_choose_train_x.setText("")
        self.lable_push_choose_train_x.setObjectName("lable_push_choose_train_x")
        self.lable_push_choose_train_y = QtWidgets.QLabel(self.tool_train_data)
        self.lable_push_choose_train_y.setGeometry(QtCore.QRect(120, 40, 121, 31))
        self.lable_push_choose_train_y.setText("")
        self.lable_push_choose_train_y.setObjectName("lable_push_choose_train_y")
        self.edit_out_file_train = QtWidgets.QTextEdit(self.tool_train_data)
        self.edit_out_file_train.setGeometry(QtCore.QRect(120, 80, 121, 21))
        self.edit_out_file_train.setObjectName("edit_out_file_train")
        self.lable_edit_out_file_train = QtWidgets.QLabel(self.tool_train_data)
        self.lable_edit_out_file_train.setGeometry(QtCore.QRect(0, 80, 111, 21))
        self.lable_edit_out_file_train.setWordWrap(True)
        self.lable_edit_out_file_train.setObjectName("lable_edit_out_file_train")
        self.tool_enter_data.addItem(self.tool_train_data, "")
        self.tool_test_data = QtWidgets.QWidget()
        self.tool_test_data.setGeometry(QtCore.QRect(0, 0, 251, 107))
        self.tool_test_data.setObjectName("tool_test_data")
        self.edit_out_file_test = QtWidgets.QTextEdit(self.tool_test_data)
        self.edit_out_file_test.setGeometry(QtCore.QRect(120, 60, 121, 20))
        self.edit_out_file_test.setObjectName("edit_out_file_test")
        self.lable_test_file = QtWidgets.QLabel(self.tool_test_data)
        self.lable_test_file.setGeometry(QtCore.QRect(120, 10, 121, 31))
        self.lable_test_file.setText("")
        self.lable_test_file.setObjectName("lable_test_file")
        self.lable_edit_out_file_test = QtWidgets.QLabel(self.tool_test_data)
        self.lable_edit_out_file_test.setGeometry(QtCore.QRect(10, 60, 101, 21))
        self.lable_edit_out_file_test.setWordWrap(True)
        self.lable_edit_out_file_test.setObjectName("lable_edit_out_file_test")
        self.push_choose_test_file = QtWidgets.QPushButton(self.tool_test_data)
        self.push_choose_test_file.setEnabled(True)
        self.push_choose_test_file.setGeometry(QtCore.QRect(10, 10, 101, 32))
        self.push_choose_test_file.setObjectName("push_choose_test_file")
        self.tool_enter_data.addItem(self.tool_test_data, "")
        self.lable_out_vector = QtWidgets.QLabel(self.centralwidget)
        self.lable_out_vector.setGeometry(QtCore.QRect(660, 0, 71, 31))
        self.lable_out_vector.setWordWrap(True)
        self.lable_out_vector.setObjectName("lable_out_vector")
        self.list_out_vector = QtWidgets.QListWidget(self.centralwidget)
        self.list_out_vector.setGeometry(QtCore.QRect(660, 40, 71, 251))
        self.list_out_vector.setObjectName("list_out_vector")
        self.table_in_matrix = QtWidgets.QTableView(self.centralwidget)
        self.table_in_matrix.setGeometry(QtCore.QRect(280, 40, 371, 251))
        self.table_in_matrix.setObjectName("table_in_matrix")
        self.lable_in_matrix = QtWidgets.QLabel(self.centralwidget)
        self.lable_in_matrix.setGeometry(QtCore.QRect(280, 10, 111, 16))
        self.lable_in_matrix.setObjectName("lable_in_matrix")
        self.push_load_matrix = QtWidgets.QPushButton(self.centralwidget)
        self.push_load_matrix.setGeometry(QtCore.QRect(420, 10, 191, 23))
        self.push_load_matrix.setObjectName("push_load_matrix")
        self.push_draw_2D = QtWidgets.QPushButton(self.centralwidget)
        self.push_draw_2D.setGeometry(QtCore.QRect(330, 320, 111, 51))
        self.push_draw_2D.setCheckable(False)
        self.push_draw_2D.setObjectName("push_draw_2D")
        self.push_draw_3D = QtWidgets.QPushButton(self.centralwidget)
        self.push_draw_3D.setGeometry(QtCore.QRect(460, 320, 111, 51))
        self.push_draw_3D.setObjectName("push_draw_3D")
        self.push_save_images = QtWidgets.QPushButton(self.centralwidget)
        self.push_save_images.setGeometry(QtCore.QRect(590, 320, 111, 51))
        self.push_save_images.setObjectName("push_save_images")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_choose_algorithm.setCurrentIndex(1)
        self.tool_train_or_test_nsko.setCurrentIndex(0)
        self.tool_train_or_test_hebb.setCurrentIndex(1)
        self.tool_train_or_test_perzeptron.setCurrentIndex(0)
        self.tool_enter_data.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lable_in_param_step_nsko.setText(_translate("MainWindow", "Шаг покоординатного спуска: 100*h"))
        self.push_train_nsko.setText(_translate("MainWindow", "Обучиться"))
        self.tool_train_or_test_nsko.setItemText(self.tool_train_or_test_nsko.indexOf(self.tool_train_nsko), _translate("MainWindow", "Обучение"))
        self.push_test_nsko.setText(_translate("MainWindow", "Классифицировать"))
        self.tool_train_or_test_nsko.setItemText(self.tool_train_or_test_nsko.indexOf(self.tool_test_nsko), _translate("MainWindow", "Классификация"))
        self.tab_choose_algorithm.setTabText(self.tab_choose_algorithm.indexOf(self.tab_nsko), _translate("MainWindow", "НСКО"))
        self.lable_in_param.setText(_translate("MainWindow", "Входные параметры: \n"
"    тренировочная матрица\n"
"    вектор классов"))
        self.push_train_hebb.setText(_translate("MainWindow", "Обучиться"))
        self.tool_train_or_test_hebb.setItemText(self.tool_train_or_test_hebb.indexOf(self.tool_train_hebb), _translate("MainWindow", "Обучение"))
        self.push_test_hebb.setText(_translate("MainWindow", "Классифицировать"))
        self.tool_train_or_test_hebb.setItemText(self.tool_train_or_test_hebb.indexOf(self.tool_test_hebb), _translate("MainWindow", "Классификация"))
        self.tab_choose_algorithm.setTabText(self.tab_choose_algorithm.indexOf(self.tab_hebb), _translate("MainWindow", "Хэббе"))
        self.lable_in_param_perzeptron.setText(_translate("MainWindow", "Входные параметры: \n"
"    тренировочная матрица\n"
"    вектор классов"))
        self.push_train_perzeptron.setText(_translate("MainWindow", "Обучиться"))
        self.tool_train_or_test_perzeptron.setItemText(self.tool_train_or_test_perzeptron.indexOf(self.tool_train_perzeptron), _translate("MainWindow", "Обучение"))
        self.push_test_perzeptron.setText(_translate("MainWindow", "Классифицировать"))
        self.tool_train_or_test_perzeptron.setItemText(self.tool_train_or_test_perzeptron.indexOf(self.tool_test_perzeptron), _translate("MainWindow", "Классификация"))
        self.tab_choose_algorithm.setTabText(self.tab_choose_algorithm.indexOf(self.tab_perzeptron), _translate("MainWindow", "Прецептрон"))
        self.push_choose_train_y.setText(_translate("MainWindow", "Train Y"))
        self.push_choose_train_x.setText(_translate("MainWindow", "Train X"))
        self.edit_out_file_train.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\'; font-size:13pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\'; font-size:13pt;\"><br /></p></body></html>"))
        self.lable_edit_out_file_train.setText(_translate("MainWindow", "Выходной файл:"))
        self.tool_enter_data.setItemText(self.tool_enter_data.indexOf(self.tool_train_data), _translate("MainWindow", "Обучение"))
        self.edit_out_file_test.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\'; font-size:13pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\'; font-size:13pt;\"><br /></p></body></html>"))
        self.lable_edit_out_file_test.setText(_translate("MainWindow", "Выходной файл:"))
        self.push_choose_test_file.setText(_translate("MainWindow", "Test X"))
        self.tool_enter_data.setItemText(self.tool_enter_data.indexOf(self.tool_test_data), _translate("MainWindow", "Классификация"))
        self.lable_out_vector.setText(_translate("MainWindow", "Выходной вектор ~"))
        self.lable_in_matrix.setText(_translate("MainWindow", "Входная матрица:"))
        self.push_load_matrix.setText(_translate("MainWindow", "Загрузить матрице для обучения"))
        self.push_draw_2D.setText(_translate("MainWindow", "Нарисовать 2D \n"
"классификатор"))
        self.push_draw_3D.setText(_translate("MainWindow", "Нарисовать 3D \n"
"классификатор"))
        self.push_save_images.setText(_translate("MainWindow", "Сохранить график"))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_MainWindow()
    myapp.show()
    sys.exit(app.exec_())