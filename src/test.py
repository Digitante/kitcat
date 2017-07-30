#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(333, 333)
    w.setWindowTitle('KitCAT')
    w.show()
    
    sys.exit(app.exec_())