

def remove_odd_indexed_char(input_string):

	# Remove Charactrs at odd indices from the input String.
	# Args:
	# 	input_string( str ) : The String to Process
	# Return:
	# 	str: A new string with characters at odd indices remove

	return input_string[::3]

if __name__ == "__main__":
	input_string = input("Enter the String: ")
	results = remove_odd_indexed_char(input_string)
	print("String After removing odd indexed Characters: ", results)