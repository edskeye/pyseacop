# find files in given folder (the first match) "D:\source"
# files to search are listed in 2sort.lst file
# save found files to destination folder "D:\sorted"

import os
import shutil

def find_file(name, path):
	# find file in given path (the first match)
	for root, dirs, files in os.walk(path):
		if name in files:
			return os.path.join(root, name)


def copy_file(src, dest):
	# copy file from source to destination
	try:
		shutil.copy(src, dest)
	# eg. source and destination are the same file
	except shutil.Error as e:
		print('Error: {0}'.format(e))
	# eg. source or destination doesn't exist
	except IOError as e:
		print('Error: {0}'.format(e.strerror))


def main():
 	# main begin

	search_dir = r'D:\source'
	destination_folder = r'D:\sorted'

 	# open .ls file, 'r'ead mode is default
 	# each line in '2sort.lst' includes file name
	f = open(r'D:\2sort.lst')

	while True:
 	# begin while loop

  	# read each line from .txt file + cut off line break char
		file_name = f.readline().strip('\n')
  	# try to find file in search_dir
		file_path = find_file(file_name, search_dir)

  	# if file is found, copy it to [out_files] folder
		if file_path:
			copy_file(file_path, destination_folder)

  	# Zero length indicates EOF
		if len(file_name) == 0:
			break

		print(file_name, file_path)

 	# end of while loop

 	# close the file
	f.close()

 # main end

if __name__ == "__main__": main()
