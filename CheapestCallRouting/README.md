usage:
python3 cheapest.py or cheapest2.py
python3 test.py or test2.py

test.py is unittest cases for cheapest.py
test2.py is unittest cases for cheapest2.py

cheapest.py use split to convert input from input.txt,then reorder the list by price, 
cheapest2.py use regex to convert input and find the lowest price for each prefix,
both implement search the phone number from its own longest prefix.

to test FileNotExistError, move @skip to test_routing_result
