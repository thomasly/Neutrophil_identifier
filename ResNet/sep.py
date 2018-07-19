##

# sep.py
# separate dataset

##

import os, shutil

def sep_dataset(subset_size = 500):


	pos_path = None
	neg_path = None

	# paths to positive/negative images
	if os.path.exists('../pos'):
		pos_path = os.path.abspath('../pos')
	if os.path.exists('../neg'):
		neg_path = os.path.abspath('../neg')

	pos_folder_num = 0
	neg_folder_num = 0

	path_base = os.path.abspath('..')

	pos_to_path = os.mkdir(path_base + os.sep + "pos" + str(pos_folder_num))
	counter_i = 0
	for file in os.listdir(pos_path):
		shutil.copy2(file, pos_to_path)
		counter_i += 1
		if counter_i % 500 == 0:
			pos_foler_num += 1
			pos_to_path = os.mkdir(path_base + os.sep + "pos" + str(pos_folder_num))

	neg_to_path = os.mkdir(path_base + os.sep + "neg" + str(neg_folder_num))
	counter_i = 0
	for file in os.listdir(pos_path):
		shutil.copy2(file, pos_to_path)
		counter_i += 1
		if counter_i % 500 == 0:
			neg_foler_num += 1
			neg_to_path = os.mkdir(path_base + os.sep + "pos" + str(neg_folder_num))
