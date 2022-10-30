from PIL import ImageGrab,ImageOps
import pyautogui
from numpy import*
while True:
    xl,yl,a,b = 334,371,54,36
    xl,yl,a,b = 750,450,54,36
    box = (xl,yl,xl+a,yl+b)
    image = ImageGrab.grab(box)
    gray = ImageOps.grayscale(image)
    a = array(gray.getcolors())
    value = a.sum() 
    print(value )
    if(value != 2060):pyautogui.press('space')
#Made By Interview Candidate Phobphoomin Siriboon
