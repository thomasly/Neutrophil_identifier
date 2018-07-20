##

# view_image.py

##

import os
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from keras.layers import Input, MaxPooling2D, Conv2D, Flatten, Dense
from keras.initializers import glorot_uniform
from keras.models import Model

def YangModel(input_shape = (299, 299, 3), classes = 1):

	X_input = Input(input_shape)
	X = MaxPooling2D((3, 3), strides = (3, 3), name = "maxpooling")(X_input)
	X = Conv2D(2, (2, 2), strides = (1,1), name = "cov")(X)
	X = Flatten()(X)
	X = Dense(
		classes, 
		activation='sigmoid', 
		name='fc' + str(classes), 
		kernel_initializer = glorot_uniform())(X)

	model = Model(inputs = X_input, outputs = X, name = "YangModel")
	return model

def view_model_layer():
	model = YangModel()
	model.compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ["accuracy"])

	folder_path = os.path.abspath("..") + os.sep + "pos"
	image_name1 = os.listdir(folder_path)[0]
	image_name2 = os.listdir(folder_path)[1]
	img_path1 = folder_path + os.sep + image_name1
	img_path2 = folder_path + os.sep + image_name2

	images = []
	img1 = np.array(Image.open(img_path1))[:, :, 0:3]
	img2 = np.array(Image.open(img_path2))[:, :, 0:3]
	images.append(img1)
	images.append(img2)
	plt.imshow(img1)
	plt.show()
	images = np.array(images)
	print("img1 shape: " + str(img1.shape))
	print("images shape:" + str(images.shape))
	labels = np.ones(2)
	print("label shape: " + str(labels.shape))

	model.fit(images, labels, epochs = 1, batch_size = 2)
	intermediate_layer_model = Model(inputs = model.input, outputs = model.get_layer("maxpooling").output)
	data = np.ones((1, 299, 299, 3))
	intermediate_output = intermediate_layer_model.predict(images)
	plt.imshow(intermediate_output[0].astype(int))
	plt.show()



if __name__ == '__main__':
	view_model_layer()