def main():
	time=input("Enter a number from 1 to 12:")
	items=input("Enter a noun plural:")
	name=input("Enter a name:")
	scream=input("Enter any sentence:")
	action=input("Enter a verb:")
	print('The story goes...')
	print("It was "+ time + " o\'clock when I heard a knock at the door.")
	print('I opened the door and there was a box full of'+items+ 'with a note saying "From Mr.'+name.title()+'."')
	print('Just as I closed the door I heard a scream "'+scream.upper()+'."')
	print('I froze in place and all I could do was '+action+'.')
	# write your code here



if __name__ == '__main__':
	main()
