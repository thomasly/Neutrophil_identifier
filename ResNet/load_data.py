##

# load_data.py

##

import os, sys

import numpy as np
# import panda as pd
from PIL import Image


def load_data(pos_path = None, neg_path = None, max_pos = 500, max_neg = 500, train_only = False, test = False):
	"""
	load pil image data into numpy arrays

	input:
	pil images in pos/neg folders

	output:
	training data as X_train_orig
	training data labels as Y_train_orig
	test data as X_test_orig
	test data labels as Y_test_orig
	"""

	pos_img = []
	neg_img = []

	# paths to positive/negative images
	
	if pos_path is None and os.path.exists('../pos'):
		pos_path = os.path.abspath('../pos')
	if neg_path is None and os.path.exists('../neg'):
		neg_path = os.path.abspath('../neg') 

	# open positive/negative images and transform them into np arrays
	i = 0
	for file in os.listdir(pos_path):
		img_path = pos_path + os.sep + str(file)
		img = Image.open(str(img_path))
		pos_img.append(np.array(img))
		i += 1
		if i >= max_pos:
			break

	i = 0
	for file in os.listdir(neg_path):
		img_path = neg_path + os.sep + str(file)
		img = Image.open(str(img_path))
		neg_img.append(np.array(img))
		i += 1
		if i >= max_neg:
			break

	# remove the transparency channel
	# add labels to the images
	pos_img = np.array(pos_img)[:, :, :, 0:3]
	pos_label = np.ones(pos_img.shape[0])
	neg_img = np.array(neg_img)[:, :, :, 0:3]
	neg_label = np.zeros(neg_img.shape[0])

	# combine positive and negative datasets
	X = np.concatenate((pos_img, neg_img), axis=0)
	Y = np.concatenate((pos_label, neg_label), axis=0)
	
	# number of samples
	n_X = X.shape[0]

	# shuffle the combined datasets
	perm = np.random.permutation(n_X)
	X = X[perm]
	Y = Y[perm]

	# determine the images number of test set
	n_test = 0
	if test:
		n_test = np.int(n_X)
	elif train_only:
		n_test = 0
	else:
		n_test = np.int(n_X / 10)
		# if test set number is less than 1 (total data number is less than 10)
		# add 1 to test set
		if n_test == 0:
			n_test += 1

	# determine the number of training set
	n_train = n_X - n_test
	
	# split data into training set and test set
	X_train_orig = X[0:n_train]
	Y_train_orig = Y[0:n_train]
	X_test_orig = []
	Y_test_orig = []
	if not train_only:
		X_test_orig = X[-n_test:]
		Y_test_orig = Y[-n_test:]
	

	return X_train_orig, X_test_orig, Y_train_orig, Y_test_orig


if __name__ == "__main__":
	load_data()
	



	#return X_train_orig, X_test_orig, Y_train_orig, Y_test_orig
