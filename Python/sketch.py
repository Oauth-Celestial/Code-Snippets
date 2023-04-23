import imageio
import numpy as np
import matplotlib.pyplot as p
from scipy import ndimage
from tkinter import *
from PIL import ImageTk, Image


def grayscale(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


def dodge(front, back):
    result = front*255/(255-back)
    result[result > 255] = 255

    result[back == 255] = 255
    return result.astype('uint8')


def makeWindow():
    root = Tk()

   
    root.geometry("800x480")
    image = Image.open("saurabh.jpg")
    
    # Resize the image using resize() method
    resize_image = image.resize((300, 300))
    
    img = ImageTk.PhotoImage(resize_image)
    img = None
    # create label and add resize image
   

   
    label1 = Label(root,image=img)
    button = Button(root,text="Open",width=100,height=10)
    button.place(x=10,y=320)

   
    label1.place(x=10,y=10)
   
    root.mainloop()
    
    # Read the Image
   
    
    # Execute Tkinter
    root.mainloop()
makeWindow()
# img = "saurabh.jpg"  # add your test file path
# s_img = imageio.imread(img)
# # start_img.shape(196, 160, 30)
# gray_img = grayscale(s_img)
# inverted_img = 255 - gray_img
# blur_img = ndimage.filters.gaussian_filter(inverted_img, sigma=5)
# final_img = dodge(blur_img, gray_img)
# p.imshow(final_img, cmap='gray')
# p.imsave("sketch.jpg", # add path to save file
#          final_img, cmap='gray', vmin=0, vmax=255)
