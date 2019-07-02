import time

from PyQt5 import uic, QtWidgets, QtCore, Qt

import sys

from PyQt5.QtGui import QPixmap, QImage

from PyQt5.QtWidgets import QFileDialog

from Backend.CellArray import CellArray
from Backend.backend import Backend
from Backend.rule import Rule
from Backend.rulesCollection import RulesCollection

Row = 0
line = 0
column = 2

current_exec = -1
tStart = 0
isExec = False
isTime = False



class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('../Interface/lp74.ui', self)
        self.show()

        btn_pause = self.findChild(QtWidgets.QPushButton, "btn_pause")
        btn_screen = self.findChild(QtWidgets.QPushButton, "btn_screen")
        graphic = self.findChild(QtWidgets.QGraphicsView, "graphic")

        btn_screen.setEnabled(False)
        btn_pause.setEnabled(False)

        scene = QtWidgets.QGraphicsScene()
        img = QImage(10, 10, QImage.Format_Mono)
        for i in range(img.height()):
            for j in range(img.height()):
                img.setPixel(i, j, 1)
        pixmap = QPixmap(img)
        pixmap_scaled = pixmap.scaled(graphic.width()-5, graphic.height()-5, QtCore.Qt.IgnoreAspectRatio)
        cont = QtWidgets.QLabel()
        cont.setScaledContents(1)
        cont.setPixmap(pixmap_scaled)
        scene.addWidget(cont)
        graphic.setScene(scene)

        rules = self.findChild(QtWidgets.QGraphicsView, "regle")
        img_rules = QPixmap("../Interface/regle254_600.png")
        img_scaled = img_rules.scaled(rules.width()-3, rules.height()-3, QtCore.Qt.IgnoreAspectRatio)
        container = QtWidgets.QLabel()
        container.setScaledContents(1)
        container.setPixmap(img_scaled)
        rule_scene = QtWidgets.QGraphicsScene()
        rule_scene.addWidget(container)
        rules.setScene(rule_scene)

        check1 = self.findChild(QtWidgets.QCheckBox, "check1")
        check2 = self.findChild(QtWidgets.QCheckBox, "check2")
        check3 = self.findChild(QtWidgets.QCheckBox, "check3")
        check4 = self.findChild(QtWidgets.QCheckBox, "check4")
        check5 = self.findChild(QtWidgets.QCheckBox, "check5")
        check6 = self.findChild(QtWidgets.QCheckBox, "check6")
        check7 = self.findChild(QtWidgets.QCheckBox, "check7")
        check8 = self.findChild(QtWidgets.QCheckBox, "check8")
        check1.stateChanged.connect(lambda: state(1, self))
        check2.stateChanged.connect(lambda: state(2, self))
        check3.stateChanged.connect(lambda: state(3, self))
        check4.stateChanged.connect(lambda: state(4, self))
        check5.stateChanged.connect(lambda: state(5, self))
        check6.stateChanged.connect(lambda: state(6, self))
        check7.stateChanged.connect(lambda: state(7, self))
        check8.stateChanged.connect(lambda: state(8, self))

        cbb_regle = self.findChild(QtWidgets.QComboBox, "cbb_regle")
        f = open("../Interface/regles.txt", "r")
        for x in f.readlines():
            splited = x.split(";")
            cbb_regle.addItem(splited[0], splited[1])
        dic = eval(cbb_regle.currentData())

        if dic['111'] == 1:
            check1.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check1.setCheckState(2)
        if dic['110'] == 1:
            check2.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check2.setCheckState(2)
        if dic['101'] == 1:
            check3.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check3.setCheckState(2)
        if dic['100'] == 1:
            check4.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check4.setCheckState(2)
        if dic['011'] == 1:
            check5.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check5.setCheckState(2)
        if dic['010'] == 1:
            check6.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check6.setCheckState(2)
        if dic['001'] == 1:
            check7.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check7.setCheckState(2)
        if dic['000'] == 1:
            check8.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check8.setCheckState(2)

        cbb_regle.currentIndexChanged.connect(lambda: regles(self))
        f.close()


def regles(self):

    check1 = self.findChild(QtWidgets.QCheckBox, "check1")
    check2 = self.findChild(QtWidgets.QCheckBox, "check2")
    check3 = self.findChild(QtWidgets.QCheckBox, "check3")
    check4 = self.findChild(QtWidgets.QCheckBox, "check4")
    check5 = self.findChild(QtWidgets.QCheckBox, "check5")
    check6 = self.findChild(QtWidgets.QCheckBox, "check6")
    check7 = self.findChild(QtWidgets.QCheckBox, "check7")
    check8 = self.findChild(QtWidgets.QCheckBox, "check8")
    cbb_regle = self.findChild(QtWidgets.QComboBox, "cbb_regle")
    if cbb_regle.currentData():
        dic = eval(cbb_regle.currentData())

        if dic['111'] == 1:
            check1.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check1.setCheckState(2)
        else:
            check1.setStyleSheet("QCheckBox::indicator {background-color: white; border: 1px solid}")
        if dic['110'] == 1:
            check2.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check2.setCheckState(2)
        else:
            check2.setStyleSheet("QCheckBox::indicator {background-color: white; border: 1px solid}")
        if dic['101'] == 1:
            check3.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check3.setCheckState(2)
        else:
            check3.setStyleSheet("QCheckBox::indicator {background-color: white; border: 1px solid}")
        if dic['100'] == 1:
            check4.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check4.setCheckState(2)
        else:
            check4.setStyleSheet("QCheckBox::indicator {background-color: white; border: 1px solid}")
        if dic['011'] == 1:
            check5.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check5.setCheckState(2)
        else:
            check5.setStyleSheet("QCheckBox::indicator {background-color: white; border: 1px solid}")
        if dic['010'] == 1:
            check6.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check6.setCheckState(2)
        else:
            check6.setStyleSheet("QCheckBox::indicator {background-color: white; border: 1px solid}")
        if dic['001'] == 1:
            check7.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check7.setCheckState(2)
        else:
            check7.setStyleSheet("QCheckBox::indicator {background-color: white; border: 1px solid}")
        if dic['000'] == 1:
            check8.setStyleSheet("QCheckBox::indicator {background-color: black}")
            check8.setCheckState(2)
        else:
            check8.setStyleSheet("QCheckBox::indicator {background-color: white; border: 1px solid}")


def state(i, self):
    check = self.findChild(QtWidgets.QCheckBox, "check"+str(i))
    if check.isChecked():
        check.setStyleSheet("QCheckBox::indicator {background-color: black}")
    else:
        check.setStyleSheet("QCheckBox::indicator {background-color: white; border: 1px solid}")


def resizeMatrice():
    global line, matrix

    for i in range(line-1):
        matrix[i].append(0)
        matrix[i].insert(0, 0)
    return matrix


def matrice(engine, nb_exec, code, matrix):

    if code ==0:
        Line = []
        matrix = []
        cells = engine.getCellArray()
        for i in range(nb_exec):
            for e in cells:
                if e:
                    Line.append(1)
                else:
                    Line.append(0)
            matrix.append(Line)
            Line = []
            engine.tick()

        return matrix
    else:
        Line = []
        cells = engine.getCellArray()
        for e in cells:
            if e:
                Line.append(1)
            else:
                Line.append(0)
        matrix.append(Line)
        Line = []
        engine.tick()
        return matrix


def etape(self, timer, engine, matrix):
    global Row, line, column, current_exec, tStart

    sp_exec = self.findChild(QtWidgets.QSpinBox, "sp_nbexec")
    sp_temps = self.findChild(QtWidgets.QSpinBox, "sp_temps")
    nb_exec = sp_exec.value()
    nb_temps = sp_temps.value()

    total_exec = nb_exec
    current_exec += 1

    print(isTime)
    if isTime:
        matrix = matrice(engine, 0, 1, matrix)

    print('Exec total = ' + str(total_exec) + ' | current  = ' + str(current_exec) + ' | time = ' + str(time.time() - tStart))

    if isExec and current_exec >= total_exec:
        timer.stop()
        timer.disconnect()
        del timer
        del matrix
        popup = QtWidgets.QMessageBox().information(self, "Fin de l'éxécution", str(current_exec) + " itérations effectuées. Simulation terminée.", QtWidgets.QMessageBox.Ok)
        btn_start.setEnabled(True)
        btn_screen.setEnabled(True)
        return

    if isTime and (time.time() - tStart) > nb_temps:
        timer.stop()
        del timer
        del matrix
        popup = QtWidgets.QMessageBox().information(self, "Fin de l'éxécution", str(nb_temps) + " secondes écoulées. Simulation terminée.", QtWidgets.QMessageBox.Ok)
        btn_start.setEnabled(True)
        btn_screen.setEnabled(True)
        return

    graphic = self.findChild(QtWidgets.QGraphicsView, "graphic")
    scene = QtWidgets.QGraphicsScene()
    img = QImage(len(matrix[0]), line-1, QImage.Format_Mono)

    if isExec:
        for i in range(line):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    img.setPixel(j, i, 0)
                else:
                    img.setPixel(j, i, 1)
    if isTime:
        for i in range(line):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    img.setPixel(j, i, 0)
                else:
                    img.setPixel(j, i, 1)

    pixmap = QPixmap(img)
    pixmap_scaled = pixmap.scaled(graphic.width() - 5, graphic.height() - 5, QtCore.Qt.IgnoreAspectRatio)
    cont = QtWidgets.QLabel()
    cont.setScaledContents(1)
    cont.setPixmap(pixmap_scaled)
    scene.addWidget(cont)
    graphic.setScene(scene)
    line = line + 1


def resetvar():
    global tStart, current_exec, Row, line, column
    column = 2
    line = 1
    Row = 0
    current_exec = -1
    matrix = []
    tStart = time.time()


def start(self):
    sp_taille = self.findChild(QtWidgets.QSpinBox, "sp_taille")
    if (isTime == False and isExec == False) or sp_taille.value() == 0:
        popup = QtWidgets.QMessageBox().information(self, "Pas de paramètres",  " Vous devez choisir un nombre d'éxécution ou une durée", QtWidgets.QMessageBox.Ok)
        return
    resetvar()
    btn_start.setEnabled(False)
    btn_pause.setEnabled(True)
    btn_screen.setEnabled(False)
    check2 = self.findChild(QtWidgets.QCheckBox, "check2")
    check3 = self.findChild(QtWidgets.QCheckBox, "check3")
    check4 = self.findChild(QtWidgets.QCheckBox, "check4")
    check5 = self.findChild(QtWidgets.QCheckBox, "check5")
    check6 = self.findChild(QtWidgets.QCheckBox, "check6")
    check7 = self.findChild(QtWidgets.QCheckBox, "check7")
    check8 = self.findChild(QtWidgets.QCheckBox, "check8")
    rule1 = Rule(False, 0, 0, 0)
    rule2 = Rule(False, 0, 0, 1)
    rule3 = Rule(False, 0, 1, 0)
    rule4 = Rule(False, 0, 1, 1)
    rule5 = Rule(False, 1, 0, 0)
    rule6 = Rule(False, 1, 0, 1)
    rule7 = Rule(False, 1, 1, 0)
    rule8 = Rule(False, 1, 1, 1)
    rules = {rule1: not check1.isChecked(), rule2: not check2.isChecked(), rule3: not check3.isChecked(), rule4: not check4.isChecked(), rule5: not check5.isChecked(), rule6: not check6.isChecked(), rule7: not check7.isChecked(), rule8: not check8.isChecked()}

    cells = CellArray(sp_taille.value())
    rules = RulesCollection(rules)
    engine = Backend(rules, cells)

    sp_exec = self.findChild(QtWidgets.QSpinBox, "sp_nbexec")
    sp_temps = self.findChild(QtWidgets.QSpinBox, "sp_temps")
    nb_exec = sp_exec.value()
    nb_temps = sp_temps.value()

    total_exec = nb_exec
    matrix = []
    if isExec:
        matrix = matrice(engine, total_exec,0,matrix)

    timer = QtCore.QTimer()
    timer.timeout.connect(lambda: etape(self, timer, engine, matrix))

    timer.setInterval(100)
    timer.start()
    btn_pause.pressed.connect(lambda: pause(timer, window))


def StateSpinExec(self):
    global isExec
    radioButtonExec = self.findChild(QtWidgets.QRadioButton, "rb_is_exec")
    sp_exec = self.findChild(QtWidgets.QSpinBox, "sp_nbexec")
    if radioButtonExec.isChecked():
        sp_exec.setEnabled(True)
        isExec = True
    else:
        sp_exec.setEnabled(False)
        isExec = False


def StateSpinTemps(self):
    global isTime
    radioButtonTemps = self.findChild(QtWidgets.QRadioButton, "rb_is_time")
    sp_temps = self.findChild(QtWidgets.QSpinBox, "sp_temps")
    if radioButtonTemps.isChecked():
        sp_temps.setEnabled(True)
        isTime = True
    else:
        sp_temps.setEnabled(False)
        isTime = False


def save(self):
    check1 = self.findChild(QtWidgets.QCheckBox, "check1")
    check2 = self.findChild(QtWidgets.QCheckBox, "check2")
    check3 = self.findChild(QtWidgets.QCheckBox, "check3")
    check4 = self.findChild(QtWidgets.QCheckBox, "check4")
    check5 = self.findChild(QtWidgets.QCheckBox, "check5")
    check6 = self.findChild(QtWidgets.QCheckBox, "check6")
    check7 = self.findChild(QtWidgets.QCheckBox, "check7")
    check8 = self.findChild(QtWidgets.QCheckBox, "check8")
    regle = {"111": int(check1.isChecked()), "110": int(check2.isChecked()), "101": int(check3.isChecked()), "100": int(check4.isChecked()), "011": int(check5.isChecked()), "010": int(check6.isChecked()), "001": int(check7.isChecked()), "000": int(check8.isChecked())}
    text, popup = QtWidgets.QInputDialog.getText(self, 'Nom de la règle', 'Entrez le nom de la règle:')
    if popup:
        f = open("../Interface/regles.txt", "a")
        string = text + ";" + str(regle) + "\n"
        f.write(string)
        f.close()
        cbb_regle = self.findChild(QtWidgets.QComboBox, "cbb_regle")
        cbb_regle.clear()
        f = open("../Interface/regles.txt", "r")
        for x in f.readlines():
            splited = x.split(";")
            cbb_regle.addItem(splited[0], splited[1])
        popup = QtWidgets.QMessageBox().information(self, "Sauvegarde effectuée",  "La règle a été sauvegardée avec succés", QtWidgets.QMessageBox.Ok)


def pause(timer, self):
    btn_screen = self.findChild(QtWidgets.QPushButton, "btn_screen")
    if timer.isActive():
        timer.stop()
        btn_screen.setEnabled(True)
    else:
        timer.start()
        btn_screen.setEnabled(False)


def screen(self):
    graphic = self.findChild(QtWidgets.QGraphicsView, "graphic")
    scene = graphic.scene()
    pixmap = graphic.grab(scene.sceneRect().toRect())
    dlg = QFileDialog()
    dlg.setAcceptMode(QFileDialog.AcceptSave)
    dlg.setNameFilters(["Images (*.png *.jpg)"])
    dlg.selectNameFilter("Images (*.png *.jpg)")
    if dlg.exec_():
        pixmap.save(dlg.selectedFiles()[0])
        popup = QtWidgets.QMessageBox().information(self, "Fichier sauvegardé", "L'image a été sauvegardé : " + dlg.selectedFiles()[0], QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()

    btn_start = window.findChild(QtWidgets.QPushButton, "btn_start")
    btn_pause = window.findChild(QtWidgets.QPushButton, "btn_pause")
    btn_exit = window.findChild(QtWidgets.QPushButton, "btn_exit")
    btn_save = window.findChild(QtWidgets.QPushButton, "btn_save")
    btn_screen = window.findChild(QtWidgets.QPushButton, "btn_screen")

    check1 = window.findChild(QtWidgets.QCheckBox, "check1")

    radioButtonExec = window.findChild(QtWidgets.QRadioButton, "rb_is_exec")
    radioButtonExec.toggled.connect(lambda: StateSpinExec(window))

    radioButtonTemps = window.findChild(QtWidgets.QRadioButton, "rb_is_time")
    radioButtonTemps.toggled.connect(lambda: StateSpinTemps(window))

    btn_start.pressed.connect(lambda: start(window))
    btn_save.pressed.connect(lambda: save(window))
    btn_exit.pressed.connect(app.quit)
    btn_screen.pressed.connect(lambda: screen(window))

    sys.exit(app.exec_())