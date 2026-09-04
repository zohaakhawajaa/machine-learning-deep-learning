import cv2 as cv
img = cv.imshow(r"C:\Users\RGB LAPTOPS\Documents\coding\AI 6 months Mentorship\Deep Learning\ss cute cat.PNG")
#Resize:
resized = cv.resize(img,(640,480))
cv.imshow("resized",resized)
cv.waitKey(0)
cv.destroyAllWindows()
#flip an image:
flipped = cv.flip(img,1)
cv.imshow("original",img)
cv.imshow("flipped",flipped)
cv.waitKey(0)
cv.destroyAllWindows()
#rotate:
rotated = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
#save:
cv.imwrite("output.jpg", img)
#Gaussian BLur:
cv.GaussianBlur(img,(5,5),0)
