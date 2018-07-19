###

# resNetBatchLearn.py

##

import load_data as ld
import os
import ResNetFromFile as rf
from numpy import squeeze

def res_net_batch_learn():
	"""
	"""
	
	path_base = os.path.abspath("..")
	for n_base in range(18):
		print("Iteration " + str(n_base + 1) + ":")
		pos_path = path_base + os.sep + "pos" + str(n_base)
		neg_path = path_base + os.sep + "neg" + str(n_base)

		X_train_orig, X_test_orig, Y_train_orig, Y_test_orig = ld.load_data(pos_path, neg_path)
		X_train = X_train_orig / 255
		X_test = X_test_orig / 255
		Y_train = squeeze(Y_train_orig)
		Y_test = squeeze(Y_test_orig)
		print ("number of training examples = " + str(X_train.shape[0]))
		print ("number of test examples = " + str(X_test.shape[0]))
		print ("X_train shape: " + str(X_train.shape))
		print ("Y_train shape: " + str(Y_train.shape))
		print ("X_test shape: " + str(X_test.shape))
		print ("Y_test shape: " + str(Y_test.shape))
		
		model = rf.load_model_from_json()
		model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

		model.fit(X_train, Y_train, epochs = 5, batch_size = 32)

		preds = model.evaluate(X_test, Y_test)
		print("Loss after " + str(n_base) + " batches = " + str(preds[0]))
		print("Test accuracy after " + str(n_base) + " batches = " + str(preds[1]))

		model.save_weights("modelWeights.h5")
		print("Model weights after " + str(n_base) + " batches saved.")


if __name__ == '__main__':
	res_net_batch_learn()