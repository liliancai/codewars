#from the longest prefix search 
#reorder each list according to price
#input as a .text file

def routing(number):
	if number=="":
		return False
	ConvertInputText()


def ConvertInputText():
	try:
		#change test to txt
		with open("input.test") as f:
			data=f.read()
	except FileNotFoundError:
		raise FileNotFoundError("You need to put operators list in input.txt")

	data=data.replace("\n\n",";")
	data=data.replace(":\n",";")
	data=data[:-1]	
	
	lists=data.split(";")
#	print(lists)

	OperatorNames=set()
	PriceList=list()

	for i in range(len(lists)):
		if i%2==0:
			OperatorNames.add(lists[i])
		else:	
			item=dict((x.strip(),y.strip()) for x,y in (e.split('\t ') for e in lists[1].split('\n')))
			PriceList.append(item)
	print(PriceList)
	print(OperatorNames)
	#breack data into a set of dictionary
	#reorder each section
	#check number from longest prefix
	#save the lowest price
	#return Operatin name and price

if __name__=="__main__":
	routing(1)
