import re


def Routing(number):
    if number == "":
        return None
    lists, operatorNames = ConvertInput()

    # create prefixes of number
    prefix_set = []
    for each_list in lists:
        prefix_set.extend(x for x in each_list.keys())
    prefix_set = list(set(prefix_set))  # reduce duplicate
    # create lowest prefix:price & prefix:operatorname

    # find the cheapest for each prefix
    lowest_name = {}
    lowest_price = {}
    for prefix in prefix_set:
        lowest_price.update({prefix : 10000.00})
        # make sure the price is big enough to be updated
        lowest_name.update({prefix : ""})
        for i, each_list in enumerate(lists):
                if prefix not in each_list:
                    continue
                if each_list[prefix] < lowest_price[prefix]:
                    lowest_price.update({prefix : each_list[prefix]})
                    lowest_name.update({prefix : operatorNames[i]})

    # sort lowest_price by longest prefix and search match for number
    lowest_price_sorted = dict(sorted(lowest_price.items(), key=lambda x : len(x[0]), reverse = True))

    for i in range(len(number), 0, -1):
        preFix = number[:i]
        if preFix in lowest_price_sorted.keys():
            return lowest_price_sorted[preFix], lowest_name[preFix]


def ConvertInput():
    try:
        with open("input.txt") as f:
            inputTxt = f.read()
    except FileNotFoundError:
    	raise FileNotFoundError("You need to put operators list in input.txt")
    # find all the operators name,i.g.A of Operator A
    pattern1 = r'(\bOperator\b)\s+([A-Z])'
    operators = re.findall(pattern1, inputTxt)
    operatorNames = [x[1] for x in operators]

    # Split text into each pricelist
    inputTxt = inputTxt[:-1]
    inputTxt = inputTxt.split("\n\n")

    # Convert each pricelist into a dict
    pattern2 = r'([0-9]+)\s+(\d+\.?\d*)'
    lists = []
    for each in inputTxt:
        lists.append(dict((x, float(y)) for x, y in re.findall(pattern2, each)))
    # print(lists)
    return lists, operatorNames

if __name__ == "__main__":

    number = input("Please dial your number:\n")

    result = Routing(number)
    if result is not None:
        print('The cheapest price is $%.2f/min,Operator %s.' % (result[0], result[1]))
    else:
        print("The number you dailed is unreachable.")
