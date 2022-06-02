#create the Easy Editor photo editor here!
from PyQt5.QtCore import  Qt 
from PyQt5.QtGui import QPixmap
from  PyQt5.QtWidgets import *
import os
from PIL import Image
from PIL import ImageFilter
app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle("The Easy Editor app?")
main_win.resize(900,700)

left_btn = QPushButton("Left")
right_btn = QPushButton("Right")
mirror_btn = QPushButton("Mirror")
sharpness_btn = QPushButton("Sharpness")
b_and_w_btn = QPushButton("B&&W")
folder_btn = QPushButton("Folder")

image_list = list()
image_list = QListWidget()
write_label = QLabel("Image")

main_layout = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(folder_btn)
col1.addWidget(image_list)

col2.addWidget(write_label)

row = QHBoxLayout()
row.addWidget(left_btn)
row.addWidget(right_btn)
row.addWidget(mirror_btn)
row.addWidget(sharpness_btn)
row.addWidget(b_and_w_btn)

col2.addLayout(row)

main_layout.addLayout(col1) 
main_layout.addLayout(col2) 

work_dir = ""
def chooseWorkingDirectory():
    global work_dir
    work_dir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result
            
def showNameList():
    extensions = [".jpg",".jpeg",".png","bmp",".gif"]
    chooseWorkingDirectory()
    filenames = filter(os.listdir(work_dir),extensions)

    image_list.clear()
    for filename in filenames:
        image_list.addItem(filename)
folder_btn.clicked.connect(showNameList)

class ProcessImage():
    def __init__(self):
        self.image = None
        self.directory = None
        self.filename = None
        self.saveDirectory = "Modified/"

    def showImage(self, path):
        write_label.hide()
        pixMapImage = QPixmap(path)
        width, height = write_label.width(), write_label.height()
        pixMapImage = pixMapImage.scaled(width, height, Qt.KeepAspectRatio)
        write_label.setPixmap(pixMapImage)
        write_label.show()

    def saveImage(self):
        path = os.path.join(work_dir, self.saveDirectory)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def BlackAndWhite(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(work_dir, self.saveDirectory, self.filename)
        self.showImage(image_path)

    def Sharp(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(work_dir, self.saveDirectory, self.filename)
        self.showImage(image_path)

    def RotateLeft(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(work_dir, self.saveDirectory, self.filename)
        self.showImage(image_path)

    def RotateRight(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(work_dir, self.saveDirectory, self.filename)
        self.showImage(image_path)

    def Mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(work_dir, self.saveDirectory, self.filename)
        self.showImage(image_path)



    def loadImage(self, filename):
        self.filename = filename
        fullname = os.path.join(work_dir, filename)
        self.image = Image.open(fullname)

def showChosenImage():
    if image_list.currentRow() >= 0:
        filename = image_list.currentItem().text()
        workImage.loadImage(filename)
        workImage.showImage(os.path.join(work_dir, workImage.filename))

workImage = ProcessImage()
image_list.currentRowChanged.connect(showChosenImage)
b_and_w_btn.clicked.connect(workImage.BlackAndWhite)
sharpness_btn.clicked.connect(workImage.Sharp)
left_btn.clicked.connect(workImage.RotateLeft)
right_btn.clicked.connect(workImage.RotateRight)
mirror_btn.clicked.connect(workImage.Mirror)































































main_win.setLayout(main_layout)
main_win.show()
app.exec()