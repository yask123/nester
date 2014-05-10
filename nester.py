"""This is nester.py module which provides split() function
 which prints all the items(lists or non lists)"""

def split(the_list):
	"""This function takes positional argument of a list(or nested lists) and prints
       recursively on the screen each element individally """
	for each_item in the_list:
		if isinstance(each_item,list):
			split(each_item)
		else:
			print (each_item)	