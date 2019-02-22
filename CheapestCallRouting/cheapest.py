import operator
#from the longest prefix search 
#reorder each list according to price
#input as a .text file

def Routing(number):
	if number=="":
		return None 
	OperatorNames,Lists=ConvertInputText()

	#reorder each list by lowest price
	Sorted_Lists=list()
	for each in Lists:
		sorted_e=sorted(each.items(),key=operator.itemgetter(1))
		Sorted_Lists.append(sorted_e)

	#create a list of prefix from the longest
	preFixes=list()
	for i in range(1,len(number)+1):
		preFix=number[:i]
		preFixes.insert(0,preFix)
	
	OperotorName=""	
	lowestPrice=10000 #set price bit of impossible high
	for preFix in preFixes:
		for i,eachList in enumerate(Lists):
			if preFix in eachList:
				if float(eachList[preFix])<lowestPrice:
					#save the lowest price
					lowestPrice=eachList[preFix]
					OperotorName=OperatorNames[i]
			if lowestPrice !=10000:
				return lowestPrice,OperotorName 



#breack data into a set of dictionary
def ConvertInputText():
	try:
		with open("input.txt") as f:
			data=f.read()
	except FileNotFoundError:
		raise FileNotFoundError("You need to put operators list in input.txt")

	#for easier to sperate each Operator's name and list
	data=data.replace("\n\n",";")
	data=data.replace(":\n",";")
	#remove the last extra \n,otheriwise split the list into dict won't work 
	data=data[:-1]
	
	Lists=data.split(";")

	OperatorNames=list()
	for i in range(len(Lists)):
		if i%2==0:
			OperatorNames.append(Lists[i])
		else:
			Lists[i]=dict((x.strip(),y.strip()) for x,y in (e.split('\t ') for e in Lists[i].split('\n')))
	for each in Lists:
		if each[0]=="O":
			Lists.remove(each)

	return OperatorNames,Lists

if __name__=="__main__":
	number=input("Please dial your number:\n")
	result=Routing(number)
	if result!=None:
		print("The lowest price is ",result)
	else:
		print("The number you dailed is unreachable.")
		
