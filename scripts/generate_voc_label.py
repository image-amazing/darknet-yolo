import os, os.path

imageDir ='../darknet/data/VOCdevkit/VOC2007/labels/'
for file in os.listdir(imageDir): 
    fname = '../darknet/data/VOCdevkit/VOC2007/labels/' + file
    text_file = open(fname, "r")

    txtName = '../darknet/data/VOCdevkit/VOC2007/labels1/' + file
    file_1 = open(txtName , "w")
    for lines in text_file.readlines():
		if lines.split()[0] == '5' or lines.split()[0] == '6':
    	    file_1.write('0' + ' ')
		elif lines.split()[0] == '14':
	    	file_1.write('1' + ' ')
		else:
	    	continue
		file_1.write(' '.join([a for a in lines.split()[1:5]]))
    	file_1.write('\n')
    file_1.close()

imageDir ='../darknet/data/VOCdevkit/VOC2012/labels/'
for file in os.listdir(imageDir): 
    fname = '../darknet/data/VOCdevkit/VOC2012/labels/' + file
    text_file = open(fname, "r")

    txtName = '../darknet/data/VOCdevkit/VOC2012/labels1/' + file
    file_1 = open(txtName , "w")
    for lines in text_file.readlines():
		if lines.split()[0] == '5' or lines.split()[0] == '6':
    	    file_1.write('0' + ' ')
		elif lines.split()[0] == '14':
	    	file_1.write('1' + ' ')
		else:
	    	continue
		file_1.write(' '.join([a for a in lines.split()[1:5]]))
    	file_1.write('\n')
    file_1.close()
