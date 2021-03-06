from PIL import Image
import numpy as np
import cv2
import imutils
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

################################################
#kmeans 3

path = r"C:\Users\Franklin Qiu\Documents\Ann Arbor.PNG"
img = cv2.imread(path)
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 1.0)
K = 7
ret,label,center=cv2.kmeans(Z,K,None,criteria,50,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

path = r"C:\Users\Franklin Qiu\Documents\Ann Arbor Means3.PNG"
meansIMG = Image.fromarray(res2)
if meansIMG.mode != 'RGB':
    meansIMG = meansIMG.convert('RGB')
meansIMG.save(path)


path = r"C:\Users\Franklin Qiu\Documents\Ann Arbor Means3.PNG"
image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 50, 255, cv2.THRESH_BINARY)[1]
th = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 1)

cnts = cv2.findContours(th.copy(), cv2.RETR_LIST,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
imga = image
imga[:,:,:] = 255
cv2.drawContours(imga, cnts, -1, (0, 0, 0), 1)

path = r"C:\Users\Franklin Qiu\Documents\Ann Arbor Means6.PNG"
meansIMG = Image.fromarray(imga)
if meansIMG.mode != 'RGB':
    meansIMG = meansIMG.convert('RGB')
meansIMG.save(path)