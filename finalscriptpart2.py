import os
import natsort
import cv2

filelist=os.listdir('C:/Users/Dell/Desktop/folder4')
for fichier in filelist[:]: 
    if not(fichier.endswith(".png")):
        filelist.remove(fichier)
finallist = natsort.natsorted(filelist,reverse=False)
#print(finallist)

t = int(len(finallist)/10)
#print(t)
n = 0
x = 1
counter = 0 
while True :

    for counter in range(n, x):
        overlay1 = finallist[counter]
        print(overlay1)
        img = cv2.imread(overlay1)
        #print(img)
        cv2.imwrite("C:/Users/Dell/Desktop/folder5/{}.png".format(counter), img )
        counter += 1
    n = n + t 
    x = x  + t 