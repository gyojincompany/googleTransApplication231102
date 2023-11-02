import sys

from PyQt5 import uic # Qt Designer에서 제작한 ui를 불러와주는 클래스
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import googletrans

form_class =  uic.loadUiType('ui/googleUi.ui')[0]
# Qt Designer에서 제작한 ui 불러오기

class MyGoogleTrans(QMainWindow, form_class):
    def __init__(self): # 초기화자(생성자)
        super().__init__() # 부모 클래스의 초기화자 호출
        self.setupUi(self) # 제작해 놓은 googleUi.ui를 연결
        self.setWindowTitle('구글 번역기') # 번역기 앱의 타이틀
        self.setWindowIcon(QIcon('icon/google.png')) # 번역기 앱의 아이콘
        self.statusBar().showMessage('Google Trans App v1.0 Copyright ⓒ GyojinCompany') # 상태 표시줄


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myApp = MyGoogleTrans()
    myApp.show()
    sys.exit(app.exec_())


