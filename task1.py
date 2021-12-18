import cv2
import os


location = input("Where is your video?")
cam = cv2.VideoCapture(location)

try:
	if not os.path.exists('data'):
		os.makedirs('data')

except OSError:
	print ('Error: Creating directory of data')


currentframe = 0

while(True):
	
	ret,frame = cam.read()

	if ret:
		name = './data/frame' + str(currentframe) + '.jpg'
		print ('Creating...' + name)


		cv2.imwrite(name, frame)


		currentframe += 1
	else:
		break



import sys
from PIL import Image
import os

folder = "./data/"
os.makedirs('compressed')
folder2 = "./compressed"
for file in os.listdir(folder):
    img = Image.open(folder+file)
    os.chdir(folder2)
    img.save("Compressed_"+file, optimize=True, quality=30)
    print ('Creating...' + "Compressed_"+file)
    os.chdir("../")
