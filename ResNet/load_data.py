##

# load_data.py

##

import os, sys

import numpy as np
# import panda as pd
from PIL import Image


def load_data():

	pos_path = None
	neg_path = None
	pos_img = []
	neg_img = []

	if os.path.exists('../pos'):
		pos_path = os.path.abspath('../pos')
	if os.path.exists('../neg'):
		neg_path = os.path.abspath('../neg') 

	for file in os.listdir(pos_path):
		img_path = pos_path + os.sep + str(file)
		img = Image.open(str(img_path))
		pos_img.append(np.array(img))


	for file in os.listdir(neg_path):
		img_path = neg_path + os.sep + str(file)
		img = Image.open(str(img_path))
		neg_img.append(np.array(img))


	pos_img = np.array(pos_img)[:, :, :, 0:3]
	neg_img = np.array(neg_img)[:, :, :, 0:3]

	return pos_img, neg_img


if __name__ == "__main__":
	load_data()
	



	#return X_train_orig, X_test_orig, Y_train_orig, Y_test_orig
