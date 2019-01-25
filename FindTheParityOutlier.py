def find_outlier(integers):
    even=[]
    odd=[]
    for i in range(0,3):
        if (integers[i]%2)==0:
            even.append(integers[i])
        if (integers[i]%2)==1:
            odd.append(integers[i])
    #print(len)        
    if len(odd)==1:
        return odd[0]
        
    elif len(even)==1:
        return even[0]
    
    elif len(odd)==3:
        for i in range(3,len(integers)):
            if integers[i]%2==0:
                 return integers[i]
		
    elif len(even) == 3:
    	for i in range(3,len(integers)):
        	if (integers[i]%2)==1:
    	        	return integers[i]
				
	else:
		return None

'''	
class Test(unittest.TestCase):
	def assert_equals(self):
		self.assertEqual(find_outlier([1,1,2]),2)
	
if __name__ == '__main__':
    unittest.main()
'''
#tring to run test locally but haven't figured out yet
'''
the cleverest
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
'''

