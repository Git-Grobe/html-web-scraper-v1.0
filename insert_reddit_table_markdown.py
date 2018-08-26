import fileinput

file_name = '/Users/Name/Desktop/freestyle_clearence_webscrape/clearence_product_list.txt'
for line in fileinput.FileInput(file_name,inplace=1):
	if '|' in line:
		line = line.rstrip()
		line = line.replace(',','|',)
		line = line.replace('Price|Product','Price|Product'+'\n'+':-|:-')


	print(line)	 

	








