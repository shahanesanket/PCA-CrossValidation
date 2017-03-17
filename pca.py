import os
import numpy as np
import matplotlib.pyplot as plt

#change the path variable to appropriate file path
path="/home/mindstorm/Desktop/hw45/faces-corrected/"


filenameList = os.listdir(path)
print len(filenameList)
imageArray = []
for file in filenameList:
    singleImage = open(path+file,'rb')
    singleImage.readline()
    singleImage.readline()
    singleImage.readline()
    i=0
    oneImageArray = []
    for i in range(0,45045):
        oneImageArray.append(ord(singleImage.read(1)))
    imageArray.append(oneImageArray)
print 'files loaded...'
imageArray = np.matrix(imageArray)
meanImg = np.mean(imageArray,axis=0)
print 'mean image:',meanImg.shape
"""the mean image is formed correctly by this step"""

for i in range(0,165):
    imageArray[i] = imageArray[i] - meanImg[0]

covar = np.cov(imageArray)
value,vector = np.linalg.eig(covar)
vector = np.matrix(vector)
for i in range(0,10):
    v1 = vector[:,i]
    v1 = np.matrix(v1)
    tempImg = imageArray.transpose() * v1
    tempImg = tempImg.transpose()
    tempImg = tempImg.reshape((231,195))
    plt.imshow(tempImg.astype(int), cmap='Greys')
    plt.savefig('eigenface'+str(i)+'.png')
    plt.show()
print 'eigen images created'