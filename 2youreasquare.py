import math
def is_square(n): 
   if n>=0:
        return (math.sqrt(n)-int(math.sqrt(n)))==0
   else:
       return False
	   
#cleverest
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;

