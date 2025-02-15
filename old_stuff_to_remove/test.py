from ImageProcessor import ImageProcessor as ip
from ScrapBooker import ScrapBooker as scbook
from ColorFilter import ColorFilter as cf
import numpy as np
from NumPyCreator import NumPyCreator as myNp

import sys

img_pro = ip()
s = scbook()
cf = cf()
mynp = myNp()


def load_imgs():
	imgs = []
	for path in sys.argv:
		img = img_pro.load(path) 
		imgs.append(img)
	return imgs

def crop_imgs(imgs, crop_heigth, crop_width, crop_posx=0, crop_posy=0):
	return [s.crop(img, (crop_heigth, crop_width), (crop_posy, crop_posx)) for img in imgs]

def thin_imgs(imgs, x, y, thin_posx=0, thin_posy=0):
	return [s.thinall(img, x, y) for img in imgs]

def vec_crop(array):
	return (s.crop(array, (3003, 1920)))
#vfunk = np.vectorize(vec_crop)
#result = vfunk(imgs)

def concate_line(i, x, imgs):
	return np.concatenate(imgs[i * x:(i + 1) * x:], 1)

def concate_matrix(x, y, imgs):
	tmp = []
	for i in range(y):
		tmp.append(concate_line(i, x, imgs))
	return np.concatenate(tmp[::], 0)
	

def thin_imgs_filter(imgs, x, y, shape, thin_posx=0, thin_posy=0):
	return [s.thinundershape(img, x, y, shape) for img in imgs]

sys.argv.pop(0)

crop_heigth = int(sys.argv.pop(0))
crop_width = int(sys.argv.pop(0))

crop_posy = int(sys.argv.pop(0))
crop_posx = int(sys.argv.pop(0))

shape_y = int(sys.argv.pop(0))
shape_x = int(sys.argv.pop(0))

thin_heigth = int(sys.argv.pop(0))
thin_width = int(sys.argv.pop(0))


#img = img_pro.load(sys.argv.pop(0)) 
#
#
#
#print("shape: " + str(img.shape))
#
#print(img.shape)
#print(img.strides)
#
#img = s.crop(img, (420, 420))
#
#img = mynp.reshape_split(img, (20,20))
#
#print(img.shape)
#print(img.strides)
#
##img = [cf.border(f, 5) for f in img]
##[cf.to_red(f[5:5, 5:5]) for f in img]
#
#img[:,:,:10,:10] = 0
#
##imgs = img[:,:]
##imgs[10:,10:, 2] = 0
#
##img = concate_matrix(20, 20, img)
#img = mynp.unshape_split(img, (420, 420))
#
#print(img.shape)
#print(img.strides)
#
#img_pro.save(np.array(img), "out.png")


imgs = load_imgs()


#imgs = thin_imgs_filter(imgs, 5, 5, (3000, 1900))
#imgs = crop_imgs(imgs, crop_heigth, crop_width, crop_posy, crop_posx)
#imgs = [cf.border(img, 20) for img in imgs]
#int(crop_heigth / thin_heigth ), int(crop_width / thin_width)
for img in imgs:
	print(img.shape)
print("shape = " + str(shape_y) + "x" + str(shape_x))
#print("We have at 300dpi :")
#print("img size = " + str()) #str(crop_heigth / 118.1) + "x" + str(crop_width / 118.1)) 
#print("total img size = " + str(img_size / 118.1)) #+ str((crop_heigth * shape_y) / 118.1) + "x" + str((crop_width* shape_x) / 118.1) + " cm")
test = concate_matrix(shape_y,shape_x, imgs)
img_pro.save(test, "test.png");

#print(img[:, 10:10])
#print(img[:, :, 10].shape)
#imgs = img.reshape[imgs.scale[0] / 10  ]
#print(imgs.shape)

#imgs = np.array_split(np.array_split(img, 10, axis=0), 10, axis=1)


#imgs = img
#print(imgs.shape)
#imgs = np.array(np.array_split(imgs, 15, axis=1), dtype=object)
#print(imgs.shape)
#imgs = np.array(np.array_split(imgs, 15, axis=3), dtype=object)
#print(imgs.shape)
#
#for f in imgs:
#    p = 10
#    f[:p,:] = 0
#    f[f.shape[0] - p:] = 0
#    f[:, :p] = 0
#    f[:, f.shape[1] - p:] = 0
#for f in imgs:
#        imgs = [cf.border(img, 5) for img in np.array_split(imgs, 10, axis=1)]
#imgs[:int(img.shape[0] / 2), :] = 0
#img = np.concatenate(imgs[::], 1)



#for i in range(10):
#    posx = int((img.shape[0] / 10) * i)
#    posy = int((img.shape[1] / 10) * i)
#    imgs[posx:posx + 10, posy :posy + 10] = 0
#
#for i in range(x):
#    posx = int((img.shape[0] / x) * i)
#    imgs[posx - 5 :posx + 5, :] = 0
#for i in range(y):
#    posy = int((img.shape[1] / y) * i)
#    imgs[:, posy - 5:posy + 5] = 0



## TODO input in cm
## Keep 2:3 ratio option
## filter



	#return 	[img_pro.load(argv[i]),
	#		img_pro.load(argv[i]),
	#		img_pro.load(argv[i]),
	#		img_pro.load(argv[i])]


#imgs = load_imgs(
#
#i = 1
#line1 = concate_line(5, i);
#i += 5;
#line2 = concate_line(5, i);
#i += 5;
#line2 = concate_line(5, i);
#i += 5;
#line2 = concate_line(5, i);
#i += 5;
#
#		
#
#img1 = i.load("./one_piece_t75/one_piece_t75_001.jpg")
#img2 = i.load("./one_piece_t75/one_piece_t75_002.jpg")
#img3 = i.load("./one_piece_t75/one_piece_t75_003.jpg")
#img4 = i.load("./one_piece_t75/one_piece_t75_004.jpg")
#img5 = i.load("./one_piece_t75/one_piece_t75_005.jpg")
#line1 = np.concatenate([sys.argv[1], sys.argv[2], 1)
#line2 = np.concatenate([sys.argv[1], sys.argv[2], 1)
#line2 = np.concatenate([sys.argv[1], sys.argv[2], 1)
#line2 = np.concatenate([sys.argv[1], sys.argv[2], 1)
#line2 = np.concatenate([sys.argv[1], sys.argv[2], 1)
#res = line1;
#img1 = i.load("./one_piece_t75/one_piece_t75_006.jpg")
#img2 = i.load("./one_piece_t75/one_piece_t75_007.jpg")
#img3 = i.load("./one_piece_t75/one_piece_t75_008.jpg")
#img4 = i.load("./one_piece_t75/one_piece_t75_009.jpg")
#img5 = i.load("./one_piece_t75/one_piece_t75_010.jpg")
#line1 = np.concatenate([img1, img2, img3, img4, img5], 1)
#img5 = i.load("./one_piece_t75/one_piece_t75_010.jpg")
#img5 = i.load("./one_piece_t75/one_piece_t75_011.jpg")
#img5 = i.load("./one_piece_t75/one_piece_t75_012.jpg")
#img5 = i.load("./one_piece_t75/one_piece_t75_013.jpg")
#img5 = i.load("./one_piece_t75/one_piece_t75_014.jpg")
#line1 = np.concatenate([img1, img2, img3, img4, img5], 1)
#res = np.concatenate([res, line1], 0)
#
##line1 = np.concatenate(img1, img1, img3, 0)
##print("\n\n\ntest juxtapose horizontal :\n")
##i.display(s.juxtapose(img, 3, 1))
##i.save(s.juxtapose(img, 3, 1), "test.png")
##print("\n\n\ntest juxtapose vertical :\n")
##i.display(s.juxtapose(img, 3, 0))
##print("\n\n\ntest crop \n")
##i.display(s.crop(img, (100,100)))
##print("\n\n\ntest mosaic horizontal :\n")
##i.display(s.mosaic(img, (2,3)))
##print("\n\n\ntest mosaic vertical :\n")
##i.display(s.mosaic(img, (3,2)))
##print("\n\n\ntest thin horizontal :\n")
##i.display(s.thin(img, 2, 1))
##print("\n\n\ntest thin vertical :\n")
##i.display(s.thin(img, 2, 0))
##print("\n\n\ntest thin horizontal :\n")
##print(s.thin(test, 5, 1))
##print("\n\n\ntest thin verticak :\n")
##print(s.thin(test, 2, 0))
#
##print("\n\n\ntest thin horizontal :\n")
##i.display(s.thin(img, 2, 1))
##print("\n\n\ntest thin horizontal :\n")
##i.display(s.thin(img, 3, 1))
##print("\n\n\ntest thin horizontal :\n")
##i.display(s.thin(img, 4, 1))
##print("\n\n\ntest thin horizontal :\n")
##i.display(s.thin(img, 5, 1))
##print("\n\n\ntest thin horizontal :\n")
##i.display(s.thin(img, 6, 1))
