from PyQt5 import uic, QtWidgets, QtGui, QtCore
import matplotlib.image as mpimg

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QColor, QImage

Row = 0
Size = 10
line = 2
column = 3
matrix = [[0, 1, 0], [1, 0, 1]]

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('../Interface/lp74.ui', self)
        self.show()

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

        scene = QtWidgets.QGraphicsScene()
        img = QImage(10,10,QImage.Format_Mono)
        for i in range (img.height()):
            for j in range (img.height()):
                img.setPixel(i,j,0)
        pixmap = QPixmap(img)
        pixmap_scaled = pixmap.scaled(graphic.width()-5,graphic.height()-5,QtCore.Qt.IgnoreAspectRatio)
        cont = QtWidgets.QLabel()
        cont.setScaledContents(1)
        cont.setPixmap(pixmap_scaled)
        scene.addWidget(cont)
        graphic.setScene(scene)

def matrice():
    global line, column
    #matrix = [[0 for x in range(int(taille))] for y in range(int(taille))]
    #for i in range(10):
    #    for j in range(10):
     #       if (i+j == 5 or i-j == 5):
      #          matrix[i][j] = 1
       #     else:
        #        matrix[i][j] = 0
    #return matrix

    matrix[line].append(0)
    matrix[line].insert(0)
    newLine = []
    for i in range(column):
        if matrix[2].index(i) == 0:
            newLine.append(1)
        else:
            newLine.append(0)

    matrix.append(newLine)
    line = line + 1
    column = column + 1
    return matrix


def etape(self):
    global Row, Size
    matrix = matrice()
    if Row > len(matrix):
        return
    # if Row % 5 == 0:
    #    Size = Size + 5
    graphic = self.findChild(QtWidgets.QGraphicsView, "graphic")
    scene = QtWidgets.QGraphicsScene()
    img = QImage(Size, Size, QImage.Format_Mono)
    for i in range(img.height()):
        for j in range(img.height()):
            img.setPixel(i, j, 0)
    for i in range(Row):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                img.setPixel(j, i, 1)
    pixmap = QPixmap(img)
    pixmap_scaled = pixmap.scaled(graphic.width() - 5, graphic.height() - 5, QtCore.Qt.IgnoreAspectRatio)
    cont = QtWidgets.QLabel()
    cont.setScaledContents(1)
    cont.setPixmap(pixmap_scaled)
    scene.addWidget(cont)
    graphic.setScene(scene)
    Row = Row + 1
    self.accepted().connect(lambda: lancer(self))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()

    txt_temps = self.findChild(QtWidgets.QLineEdit, "txt_temps")
    timer = QtCore.QTimer()
    timer.timeout.connect(lambda: etape(window))
    timer.setInterval(1000)
    timer.start()
    sys.exit(app.exec_())