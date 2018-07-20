##
# test_model.py
##

import load_data as ld 
import ResNetFromFile as rf
from keras.models import Model
from numpy import squeeze

def test_model(model, data_size):
	"""
	Test the model performence.

	Input:
	model - keras model
	data_size - the size of test dataset

	output:
	None
	"""

	# load test dataset
	print("Testing the model...")
	print("Test dataset size: " + str(data_size) + "\n")
	_, X_test_orig, _, Y_test_orig = ld.load_data(
		pos_path = '../pos16', 
		neg_path = '../neg19', 
		max_pos = data_size, 
		max_neg = data_size,
		test = True)

	# normalize test dataset
	X_test = X_test_orig / 255
	Y_test = squeeze(Y_test_orig)
	print("X_test shape: " + str(X_test.shape))
	print("Y_test shape: " + str(Y_test.shape) + "\n")

	model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

	# print the test results
	print("Evaluating...")
	preds = model.evaluate(X_test, Y_test)
	print ("Loss = " + str(preds[0]))
	print ("Test Accuracy = " + str(preds[1]))


def main():
	model = rf.load_model_from_json()
	test_model(model, 500)


if __name__ == '__main__':
	main()