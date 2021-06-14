import argparse
import os
from random import seed
from random import sample

# Add Parser
parser = argparse.ArgumentParser()
   
parser.add_argument("--train", type=int, default=80, help="Percentage of train set")
parser.add_argument("--validation", type=int, default=10, help="Percentage of validation set")
parser.add_argument("--test", type=int, default=10, help="Percentage of test set")

args = parser.parse_args()

def get_difference_from_2_list(list1, list2):
	set_list1 = set(list1)
	set_list2 = set(list2)

	diff = list(set_list1.difference(set_list2))

	return diff

def get_split_data(list_id):
	# # Train Set
	# Menghitung jumlah data train
	n_train = (count * args.train) / 100
	# Random
	train = sample(list_id, int(n_train))

	list_id = get_difference_from_2_list(list_id, train)

	# # Validation Set
	# Menghitung jumlah data validation
	n_valid = (count * args.validation) / 100

	# Random
	valid = sample(list_id, int(n_valid))

	# # Test Set
	test = get_difference_from_2_list(list_id, valid)

	return train, valid, test


# Check train set
if((args.train < args.validation) or (args.train < args.test) ):
	print("Train set must has a biggest Percentage")
	exit()

# Check total percentage
total = args.train + args.validation + args.test
if(total > 100):
	print("Total Percentage must 100%")
	exit()

# Menghitung Jumlah Data
count = 0
list_id = []
for file in os.listdir("img"):
    if file.endswith(".jpg"):       
        list_id.append(count)
        count+=1

train, valid, test = get_split_data(list_id)

# Overwrite text file
t = open("train.txt", "w")
t.close()
v = open("valid.txt", "w")
v.close()
te = open("test.txt", "w")
te.close()

count = 0
for file in os.listdir("img"):
	if file.endswith(".jpg"):
		if(count in train):
			f = open("train.txt", "a")
			f.write("data/img/"+file+"\n")
			f.close()
		elif(count in valid):
			f = open("valid.txt", "a")
			f.write("data/img/"+file+"\n")
			f.close()
		else:
			f = open("test.txt", "a")
			f.write("data/img/"+file+"\n")
			f.close()

		count+=1

