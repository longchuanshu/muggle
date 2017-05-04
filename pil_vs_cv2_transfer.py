#OpenCV 的 Python binding cv2 库使用 numpy 数组保存图片数据，
#当需要使用 PIL/Pillow 来处理图片时，需要将 cv2 读取的图片格式转换成 PIL/Pillow 的 Image:

import cv2  
from PIL import Image  

cv2_img = cv2.imread('test.jpg')  
pil_img = Image.fromarray(cv2_img)

#处理好之后转回 cv2 格式(numpy array):

import cv2  
import numpy  
from PIL import Image  

cv2_img = cv2.imread('test.jpg')  
pil_img = Image.fromarray(cv2_img)  

# process image with PIL/Pillow as you like...  

img = numpy.array(pil_img, dtype=numpy.uint8)
