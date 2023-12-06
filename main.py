import sys
import io
from random import randint

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="draw_button">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>210</y>
      <width>191</width>
      <height>121</height>
     </rect>
    </property>
    <property name="text">
     <string>окружность</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Drawer(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн
        self.draw_button.clicked.connect(self.paint)
        self.update()
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        radius = randint(10, 500)
        qp.drawEllipse(randint(0, 600), randint(50, 300), radius, radius)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Drawer()
    ex.show()
    sys.exit(app.exec_())
