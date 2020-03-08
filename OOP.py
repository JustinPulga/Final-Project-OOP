import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class BMI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(500,500,500,500)
        self.title = "BMI Calculator"
        self.textboxlbl = QLabel("<h3>Welcome to BMI Calculator<h3>",self)
        self.textboxlbl.move(140,20)
        self.textboxlbl.resize(300,20)
        self.textboxlbl1 = QLabel("Please input your data:",self)
        self.textboxlbl1.move(175,35)
        self.textboxlbl1.resize(300,20)
        
        self.textbox10 = QLineEdit(self)
        self.textboxlbl10 = QLabel("<h3>First Name:<h3>", self)
        self.textboxlbl10.move(100,79)
        self.textbox10.setText("")
        self.textbox10.move(180,70)
        self.textbox10.resize(280,30)
        
        self.textbox20 = QLineEdit(self)
        self.textboxlbl20 = QLabel("<h3>Last Name:<h3>", self)
        self.textboxlbl20.move(100,119)
        self.textbox20.setText("")
        self.textbox20.move(180,110)
        self.textbox20.resize(280,30)

        self.textbox30 = QLineEdit(self)
        self.textboxlbl30 = QLabel("<h3>Age:<h3>", self)
        self.textboxlbl30.move(100,159)
        self.textbox30.setText("")
        self.textbox30.move(180,150)
        self.textbox30.resize(280,30)

        
        self.textbox40 = QLineEdit(self)
        self.textboxlbl40 = QLabel("<h3>Sex:<h3>", self)
        self.textboxlbl40.move(100,199)
        self.textbox40.setText("")
        self.textbox40.move(180,190)
        self.textbox40.resize(280,30)

        self.textbox2 = QLineEdit(self)
        self.textboxlbl2 = QLabel("<h3>Height:<h3>", self)
        self.textboxlbl2.move(100,239)
        self.textbox2.setText("")
        self.textbox2.move(180,230)
        self.textbox2.resize(280,30)

        self.textbox1 = QLineEdit(self)
        self.textboxlbl1 = QLabel("<h3>Weight:<h3>", self)
        self.textboxlbl1.move(100,279)
        self.textbox1.setText("")
        self.textbox1.move(180,270)
        self.textbox1.resize(280,30)

        self.textbox3 = QLineEdit(self)
        self.textboxlbl3 = QLabel("<h3>Your Body Mass Index is:<h3>",self)
        self.textboxlbl3.move(20,319)
        self.textboxlbl3.resize(300,20)
        self.textbox3.setText("")
        self.textbox3.move(190,310)
        self.textbox3.resize(280,30)
        

        self.button = QPushButton('Submit',self)
        self.button.setToolTip("Submit your Information")
        self.button.move(80,450)
        self.button.clicked.connect(self.data)
        self.button1 = QPushButton('Clear', self)
        self.button1.setToolTip("Clear all your information")
        self.button1.move(200,450)
        self.button1.clicked.connect(self.clear)
        self.button2 = QPushButton('Back', self)
        self.button2.setToolTip("Back to the main window")
        self.button2.move(320,450)
        self.button2.clicked.connect(self.back)

        
        self.show()

    @pyqtSlot()
    def data(self):
        fn = self.textbox10.text()
        ln = self.textbox20.text()
        age = int(self.textbox30.text())
        sex = self.textbox40.text
        height = float(self.textbox2.text())
        weight = int(self.textbox1.text())
        self.bmi_comp(height,weight)
        self.submitdata(fn, ln, age, height, weight,sex)
    def bmi_comp(self,height,weight):
         bmi1 = weight/height**2
         self.textbox3.setText(f"{bmi1}")
    def clear(self):
        self.textbox10.setText("")
        self.textbox20.setText("")
        self.textbox30.setText("")
        self.textbox40.setText("")
        self.textbox2.setText("")
        self.textbox1.setText("")
    def back(self):
        BMI.close(self)
    def submitdata(self, fn, ln, age, height, weight,sex):
        submitting = QMessageBox.question(self, "Submitting Data", "Are you sure want to submit this information?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
        if submitting == QMessageBox.Yes and fn != "" and ln != "" and age != "" and height != "" and weight != "" and sex != "":
            f = open("Information.txt", 'w')
            f.write(f"First Name: {fn}\nLast Name: {ln}\nAge: {age}\nHeight: {height}\nWeight: {weight}\nSex: {sex}")
            f.close
            QMessageBox.information(self, "Evaluation", "Data Inputted!", QMessageBox.Ok, QMessageBox.Ok)
        
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and fn == "" and ln == "" and age == "" and height == "" and weight == "" and sex == "":
            pass
        elif submitting == QMessageBox.No and fn == "" or ln == "" or age == "" or height == "" or weight == "" and sex == "":
            QMessageBox.warning(self, "Error","Please complete the blanked field", QMessageBox.Ok, QMessageBox.Ok)

            
class BMR(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMR Calculator")
        self.setGeometry(500,500,500,500)
        self.title = "BMR Calculator"
        self.textboxlbl = QLabel("<h3>Welcome to BMR Calculator<h3>",self)
        self.textboxlbl.move(140,20)
        self.textboxlbl.resize(300,20)
        self.textboxlbl1 = QLabel("Please input your data:",self)
        self.textboxlbl1.move(175,35)
        self.textboxlbl1.resize(300,20)

        self.textbox10 = QLineEdit(self)
        self.textboxlbl10 = QLabel("<h3>First Name:<h3>", self)
        self.textboxlbl10.move(100,79)
        self.textbox10.setText("")
        self.textbox10.move(180,70)
        self.textbox10.resize(280,30)
        
        self.textbox20 = QLineEdit(self)
        self.textboxlbl20 = QLabel("<h3>Last Name:<h3>", self)
        self.textboxlbl20.move(100,119)
        self.textbox20.setText("")
        self.textbox20.move(180,110)
        self.textbox20.resize(280,30)

        self.textbox30 = QLineEdit(self)
        self.textboxlbl30 = QLabel("<h3>Age:<h3>", self)
        self.textboxlbl30.move(100,159)
        self.textbox30.setText("")
        self.textbox30.move(180,150)
        self.textbox30.resize(280,30)

        
        self.textbox40 = QLineEdit(self)
        self.textboxlbl40 = QLabel("<h3>Sex:<h3>", self)
        self.textboxlbl40.move(100,199)
        self.textbox40.setText("")
        self.textbox40.move(180,190)
        self.textbox40.resize(280,30)

        self.textbox2 = QLineEdit(self)
        self.textboxlbl2 = QLabel("<h3>Height:<h3>", self)
        self.textboxlbl2.move(100,239)
        self.textbox2.setText("")
        self.textbox2.move(180,230)
        self.textbox2.resize(280,30)

        self.textbox1 = QLineEdit(self)
        self.textboxlbl1 = QLabel("<h3>Weight:<h3>", self)
        self.textboxlbl1.move(100,279)
        self.textbox1.setText("")
        self.textbox1.move(180,260)
        self.textbox1.resize(280,30)

        self.textbox3 = QLineEdit(self)
        self.textboxlbl3 = QLabel("<h3>Your Basal Metabolic Rate is:<h3>",self)
        self.textboxlbl3.move(20,319)
        self.textboxlbl3.resize(300,20)
        self.textbox3.setText("")
        self.textbox3.move(190,310)
        self.textbox3.resize(280,30)
        

        self.button = QPushButton('Submit',self)
        self.button.setToolTip("Submit your Information")
        self.button.move(80,450)
        self.button.clicked.connect(self.data)
        self.button1 = QPushButton('Clear', self)
        self.button1.setToolTip("Clear all your information")
        self.button1.move(200,450)
        self.button1.clicked.connect(self.clear)
        self.button2 = QPushButton('Back', self)
        self.button2.setToolTip("Back to the main window")
        self.button2.move(320,450)
        self.button2.clicked.connect(self.back)

        
        self.show()

    @pyqtSlot()
    def data(self):
        fn = self.textbox10.text()
        ln = self.textbox20.text()
        age = int(self.textbox30.text())
        sex = self.textbox40.text
        height = float(self.textbox2.text())
        weight = int(self.textbox1.text())
        self.bmr_comp(sex,age,height,weight)
        self.submitdata(fn, ln, age, height, weight,sex)
    def bmr_comp(self,sex,age,height,weight):
        if sex == Male:
            bmr = 66+(13.7*weight)+(5*height)-(6.8*age)
            self.textbox3.setText(f"{bmr}")
        elif sex == Female:
            bmr = 655.1+(4.35*weight)+(4.7*height)-(4.7*age)
            self.textbox3.setText(f"{bmr}")
    def clear(self):
        self.textbox10.setText("")
        self.textbox20.setText("")
        self.textbox30.setText("")
        self.textbox40.setText("")
        self.textbox2.setText("")
        self.textbox1.setText("")
    def back(self):
        BMI.close(self)
    def submitdata(self, fn, ln, age, height, weight,sex):
        submitting = QMessageBox.question(self, "Submitting Data", "Are you sure want to submit this information?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
        if submitting == QMessageBox.Yes and fn != "" and ln != "" and age != "" and height != "" and weight != "" and sex != "":
            f = open("Information.txt", 'w')
            f.write(f"First Name: {fn}\nLast Name: {ln}\nAge: {age}\nHeight: {height}\nWeight: {weight}\nSex: {sex}")
            f.close
            QMessageBox.information(self, "Evaluation", "Data Inputted!", QMessageBox.Ok, QMessageBox.Ok)
        
        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and fn == "" and ln == "" and age == "" and height == "" and weight == "" and sex == "":
            pass
        elif submitting == QMessageBox.No and fn == "" or ln == "" or age == "" or height == "" or weight == "" and sex == "":
            QMessageBox.warning(self, "Error","Please complete the blanked field", QMessageBox.Ok, QMessageBox.Ok)


class BMIandBmrCalc(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Bmi and Bmr"
        self.x = 500
        self.y = 500
        self.width = 500
        self.height = 500


        self.button = QPushButton('BMI',self)
        self.button.setToolTip("Computes your BMI(Body Mass Index)")
        self.button.move(200,100)
        self.button.resize(100,50)
        self.button.clicked.connect(self.window2)
        
        self.button1 = QPushButton('BMR',self)
        self.button1.setToolTip("Computes your BMR(Basal Metabolic Rate)")
        self.button1.move(200,150)
        self.button1.resize(100,50)

        
        
        self.button1.clicked.connect(self.window3)


        self.main_window()


    def main_window(self):
        self.textboxlbl = QLabel("<h3>Welcome to BMI and BMR Calculator<h3>", self)
        self.textboxlbl.move(140,20)
        self.textboxlbl.resize(300,20)
        self.textboxlbl1 = QLabel("What do you want to compute?",self)
        self.textboxlbl1.move(180,50)
        self.textboxlbl1.resize(300,20)
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)

        self.show()

    def window2(self):
        self.w = BMI()
        self.w.show
    def window3(self):
        self.w = BMR()
        self.w.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BMIandBmrCalc()
    sys.exit(app.exec_())
        

        
        
    
    
