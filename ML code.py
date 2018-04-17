from PIL import Image
import numpy as np
path = r"C:\Users\Franklin Qiu\Documents\Ann Arbor.PNG"

temp_img = Image.open(path)
rgb_img = np.array(temp_img)

rgb_img.shape

gray = np.mean(rgb_img,-1)
greyimg = Image.fromarray(gray)
if greyimg.mode != 'RGB':
    greyimg = greyimg.convert('RGB')

path = r"C:\Users\Franklin Qiu\Documents\Ann Arbor Grey.PNG"
greyimg.save(path)



print "Hello World"