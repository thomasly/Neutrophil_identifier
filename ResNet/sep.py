##

# sep.py
# separate dataset

##

import os, shutil

def sep_dataset(subset_size = 500):
	"""
	Separate positive and negative dataset into individual folders.
	Each folder contains subset_size image slides. The folders are named
	from 0.

	input:
	subset_size file numbers in each folder.
	
	output:
	No return values. Files are copied from the original folder to their
	destination folders.
	"""

	# paths to positive/negative images
	pos_path = None
	neg_path = None
	if os.path.exists('../pos'):
		pos_path = os.path.abspath('../pos')
	else:
		print("pos path error")

	if os.path.exists('../neg'):
		neg_path = os.path.abspath('../neg')
	else:
		print("neg path error")

	# sub folders numbering
	pos_folder_num = 0
	neg_folder_num = 0

	path_base = os.path.abspath('..')

	# split positive dataset
	os.mkdir(path_base + os.sep + "pos" + str(pos_folder_num) + os.sep)
	pos_to_path = path_base + os.sep + "pos" + str(pos_folder_num) + os.sep
	counter_i = 0
	for file in os.listdir(pos_path):
		file_path = pos_path + os.sep + str(file)
		shutil.copy2(file_path, pos_to_path)
		counter_i += 1
		if counter_i % 500 == 0:
			pos_folder_num += 1
			os.mkdir(path_base + os.sep + "pos" + str(pos_folder_num))
			pos_to_path = path_base + os.sep + "pos" + str(pos_folder_num)

	# split negative dataset
	os.mkdir(path_base + os.sep + "neg" + str(neg_folder_num) + os.sep)
	neg_to_path = path_base + os.sep + "neg" + str(neg_folder_num) + os.sep
	counter_i = 0
	for file in os.listdir(neg_path):
		file_path = neg_path + os.sep + str(file)
		shutil.copy2(file_path, neg_to_path)
		counter_i += 1
		if counter_i % 500 == 0:
			neg_folder_num += 1
			os.mkdir(path_base + os.sep + "neg" + str(neg_folder_num))
			neg_to_path = path_base + os.sep + "neg" + str(neg_folder_num)

if __name__ == '__main__':
	sep_dataset()
