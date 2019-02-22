import re

def Routing():

	


def ConvertInput():
	try:
		with open("input.txt") as f:
			inputTxt=f.read()
	except FileNotFoundError:
		raise FileNotFoundError("You need to put operators list in input.txt")
	
	#find all the operators name,i.g.A of Operator A
	pattern1=r'(\bOperator\b)\s+([A-Z])'
	operators=re.findall(pattern1,inputTxt)
	operatorNames=[x[1] for x in operators]

	#Split text into each pricelist
	inputTxt=inputTxt[:-1]
	inputTxt=inputTxt.split("\n\n")

	#Convert each pricelist into a dict
	pattern2=r'([0-9]+)\s+(\d+\.?\d*)'
	lists=list()
	for each in inputTxt:
		lists.append(dict((x,y) for x,y in re.findall(pattern2,each)))

if __name__=="__main__":
	number=input("Please dial your number:\n")
	result=Routing(number)
	if result!=None:
		print("The lowest price is ",result)
	else:
		print("The number you dailed is unreachable.")
	
