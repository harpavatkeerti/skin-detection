import os
import numpy as np
import cv2
from keras.models import load_model
from keras import backend as K

def asymmetric_loss(y_true,y_pred):
	alpha=0.30
	return K.mean(K.abs(y_pred - y_true)*(alpha*y_true+(1-alpha)*(1-y_true)), axis=-1)

filename_image = '/content/sachin.jpg'#'data/images/test.png'
model_filename = 'models/net.h5'
model = load_model(model_filename, custom_objects={'asymmetric_loss': asymmetric_loss})
img = cv2.imread(filename_image)
# cv2.imshow('image', img)
# print(img.shape)
img = cv2.resize(img, (128, 128), interpolation = cv2.INTER_CUBIC)
# cv2.imwrite('temp.png', img)
# print(img)
lab_image = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
gray_img = lab_image[:,:,0]/255.0
x = np.zeros((1, 128, 128, 1),np.float)
x[0,:,:,0] = gray_img
y_pred = model.predict(x)
# print(y_pred)
# print(y_pred.shape)
z = np.zeros((128,128,3), np.float)
mask = 255*(y_pred[0,:,:,0])
# mask = cv2.cvtColor(mask, cv2.COLOR_LAB2BGR)
# print(mask[0])
count=0
for i in range(128):
  for j in range(128):
    if mask[i][j] == 255.0:
      # print("zzzz", i, j)
      count+=1
      z[i][j][0] = int(img[i][j][0]/255*71)
      z[i][j][1] = int(img[i][j][1]/255*103)
      z[i][j][2] = int(img[i][j][2]/255*180)
    else:
      # print(mask[i][j])
      z[i][j][0] = int(img[i][j][0])
      z[i][j][1] = int(img[i][j][1])
      z[i][j][2] = int(img[i][j][2])

print(count)
# print(mask, mask.shape)
# temp = mask.squeeze()
# print(temp[0].shape)
cv2.imwrite('res.png', z)
