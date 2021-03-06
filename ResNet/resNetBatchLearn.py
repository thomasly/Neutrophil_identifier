###

# resNetBatchLearn.py

##

import load_data as ld
import os
import ResNetFromFile as rf
from numpy import squeeze, array
from test_model import *

def res_net_batch_learn(train_only = False):
	"""
	Learn from the sub folders splited by sep.py

	input:
	No arguments. Datasets from disc.

	output:
	Trained Keras model
	"""

	EPOCHS = 10
	BATCH_SIZE = 32
	n_iter =10
	
	# number of dataset is hardcoded. Based on the folder number of positive data subfolders 
	path_base = os.path.abspath("..")
	for i in range(n_iter):
		for n_base in range(15):
			# read dataset from files
			print("Iteration " + str(n_base + 1) + ":")
			pos_path = path_base + os.sep + "pos" + str(n_base)
			neg_path = path_base + os.sep + "neg" + str(n_base)

			X_train_orig, X_test_orig, Y_train_orig, Y_test_orig = ld.load_data(
				pos_path, 
				neg_path, 
				train_only = train_only,
				max_pos=500, 
				max_neg=500)
			
			X_train = X_train_orig / 255.0
			Y_train = squeeze(Y_train_orig)
			X_test = array([])
			Y_test = array([])
			if not train_only:
				X_test = X_test_orig / 255.0
				Y_test = squeeze(Y_test_orig)
			print ("number of training examples = " + str(X_train.shape[0]))
			print ("number of test examples = " + str(X_test.shape[0]))
			print ("X_train shape: " + str(X_train.shape))
			print ("Y_train shape: " + str(Y_train.shape))
			print ("X_test shape: " + str(X_test.shape))
			print ("Y_test shape: " + str(Y_test.shape))
			
			# load model from json file
			model = rf.load_model_from_json()
			model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

			# fit model
			model.fit(X_train, Y_train, epochs = EPOCHS, batch_size = BATCH_SIZE)

			if not train_only:
				# evaluate the model
				preds = model.evaluate(X_test, Y_test)
				print("Loss after " + str(n_base + 1) + " batches = " + str(preds[0]))
				print("Test accuracy after " + str(n_base + 1) + " batches = " + str(preds[1]))

			# save model weights
			model.save_weights("modelWeights.h5")
			print("Model weights after " + str(n_base + 1) + " batches saved.\n")
			print("#"*48 + "\n")

	return model


if __name__ == '__main__':
	model = res_net_batch_learn(train_only = True)
	test_model(model, 500)
