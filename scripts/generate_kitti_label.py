import os, os.path
from PIL import Image

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

    
imageDir ='../dataset/images/training/image/'
for file in os.listdir(imageDir):
    imname = imageDir + file
    im=Image.open(imname)
    w= int(im.size[0])
    h= int(im.size[1])   
    nm = file.split('.')
    fname = '../dataset/images/training/label/' + nm[0] + ".txt"
    text_file = open(fname, "r")
    txtName = "../dataset/labels/training/image/" + nm[0] + ".txt"
    file_1 = open(txtName , "w")
	for lines in text_file.readlines():
	    if lines.split()[0] == 'Car' or lines.split()[0] == 'Truck' or lines.split()[0] == 'Van':
    	    file_1.write('0' + ' ')
	    elif lines.split()[0] == 'Pedestrian' or lines.split()[0] == 'Person_sitting':
		    file_1.write('1' + ' ')
	    else:
		    continue
	    box = (float(lines.split()[4]), float(lines.split()[6]), float(lines.split()[5]), float(lines.split()[7]))
	    new_b = convert((w, h), box)
	    file_1.write(' '.join([str(a) for a in new_b]))
    	file_1.write('\n')
	file_1.close()
