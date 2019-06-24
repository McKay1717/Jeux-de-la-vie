from PyQt5 import uic, QtWidgets, QtCore, QtGui

import sys

from PyQt5.QtGui import QPixmap, QImage

Row = 0
Size = 10
line = 1
column = 2

matrix = [[] for i in range(2)]
matrix[0] = [0, 1, 0]
matrix[1] = [1, 0, 1]


class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('../Interface/lp74.ui', self)
        self.show()

        btn_pause = self.findChild(QtWidgets.QPushButton, "btn_pause")
        btn_screen = self.findChild(QtWidgets.QPushButton, "btn_screen")
        cbb_regle = self.findChild(QtWidgets.QComboBox,"cbb_regle")
        graphic = self.findChild(QtWidgets.QGraphicsView, "graphic")
        txt_temps= self.findChild(QtWidgets.QLineEdit, "txt_temps")
        check1 = self.findChild(QtWidgets.QCheckBox, "check1")
        check2 = self.findChild(QtWidgets.QCheckBox, "check2")
        check3 = self.findChild(QtWidgets.QCheckBox, "check3")
        check4 = self.findChild(QtWidgets.QCheckBox, "check4")
        check5 = self.findChild(QtWidgets.QCheckBox, "check5")
        check6 = self.findChild(QtWidgets.QCheckBox, "check6")
        check7 = self.findChild(QtWidgets.QCheckBox, "check7")
        check8 = self.findChild(QtWidgets.QCheckBox, "check8")
        check9 = self.findChild(QtWidgets.QCheckBox, "check9")

        btn_screen.setEnabled(False)
        btn_pause.setEnabled(False)

        scene = QtWidgets.QGraphicsScene()
        img = QImage(10, 10, QImage.Format_Mono)
        for i in range(img.height()):
            for j in range(img.height()):
                img.setPixel(i, j, 0)
        pixmap = QPixmap(img)
        pixmap_scaled = pixmap.scaled(graphic.width()-5, graphic.height()-5, QtCore.Qt.IgnoreAspectRatio)
        cont = QtWidgets.QLabel()
        cont.setScaledContents(1)
        cont.setPixmap(pixmap_scaled)
        scene.addWidget(cont)
        graphic.setScene(scene)


def resizeMatrice():
    global line, matrix

    for i in range(line-1):
        matrix[i].append(0)
        matrix[i].insert(0, 0)
    return matrix

def matrice(taille):
    global line, column, matrix
    '''matrix = [[0 for x in range(taille)] for y in range(taille)]
    for i in range(taille):
        for j in range(taille):
            if i+j == 5 or i-j == 5:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    return matrix'''
    matrix[line].append(0)
    matrix[line].insert(0,0)

    resizeMatrice()

    newLine = []
    for i in range(len(matrix[line])):
        if matrix[line][i] == 0:
            newLine.append(1)
        else:
            newLine.append(0)
    matrix.append(newLine)
    line = line + 1
    column = column + 1
    return matrix


def etape(self, timer):
    global Row, Size, line, column
    taille = self.findChild(QtWidgets.QLineEdit, "txt_nbexec")
    int_taille = int(taille.text())
    matrix = matrice(int_taille)

    if Row > len(matrix):
        timer.stop()
        popup = QtWidgets.QMessageBox().information(self, "Fin de l'éxécution", "La simulation est terminée", QtWidgets.QMessageBox.Ok)
        btn_start.setEnabled(True)
        return
    # if Row % 5 == 0:
    #    Size = Size + 5

    graphic = self.findChild(QtWidgets.QGraphicsView, "graphic")
    scene = QtWidgets.QGraphicsScene()
    img = QImage(len(matrix[0]), line-1, QImage.Format_Mono)

    for i in range(line-1):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                img.setPixel(j, i, 1)
            else:
                img.setPixel(j, i, 0)

    for i in range(line):
        print('')
        for j in range(len(matrix[i])):
            print(' ', matrix[i][j], end='')
        print('')



    pixmap = QPixmap(img)
    pixmap_scaled = pixmap.scaled(graphic.width() - 5, graphic.height() - 5, QtCore.Qt.IgnoreAspectRatio)
    cont = QtWidgets.QLabel()
    cont.setScaledContents(1)
    cont.setPixmap(pixmap_scaled)
    scene.addWidget(cont)
    graphic.setScene(scene)
    Row = Row + 1


def start(self, timer):
    btn_start.setEnabled(False)
    btn_pause = self.findChild(QtWidgets.QPushButton, "btn_pause")
    btn_pause.setEnabled(True)
    timer.setInterval(100)
    timer.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()

    txt_exec = window.findChild(QtWidgets.QLineEdit, "txt_exec")
    btn_start = window.findChild(QtWidgets.QPushButton, "btn_start")
    btn_exit = window.findChild(QtWidgets.QPushButton, "btn_exit")

    timer = QtCore.QTimer()
    timer.timeout.connect(lambda: etape(window, timer))

    btn_start.pressed.connect(lambda: start(window, timer))
    btn_exit.pressed.connect(app.quit)

    sys.exit(app.exec_())