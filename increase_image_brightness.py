import cv2
import glob

count = 0
brightness = 50
for images in glob.glob("data/*.jpg"):
    img = cv2.imread(images)
    img[img < 255-brightness] += brightness  
    img_name = './data_processed' + str(count) + '.jpg'
    print("Creating " + img_name)
    cv2.imwrite(img_name, img)
    count +=1
