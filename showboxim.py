import cv2
import numpy as np

a= '/home/ubuntu/Desktop/3.jpg'

im = cv2.imread(a)
print (im.shape)
row =np.array([])
col  =np.array([])
# hang= []
# cot = []
for i in range (im.shape[0]): # hang y
	for j in range (im.shape[1]): #cot x
		if im[i,j,0]== 255 and im[i,j,1]== 255 and im[i,j,2]==255:
			row = np.append(row,i)
			col = np.append(col,j)
			row = row.astype(int)
			col = col.astype(int)
			
			# hang.__iadd__([i])
			# cot.__iadd__([j])
		else:
			continue


print (row)
print row.shape
minrow = np.amin(row)
maxrow = np.amax(row)
print minrow
print maxrow
print (col)
print col.shape
mincol = np.amin(col)
maxcol = np.amax(col)
print mincol
print maxcol
cv2.rectangle(im,(mincol,minrow),(maxcol,maxrow),(0,255,0),1)

cv2.imshow('anh',im)
cv2.waitKey(0)
cv2.destroyAllWindows()