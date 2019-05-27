// A failed version, the input number length max 5100
// but BigInteger's max is 2^32 4294967296
// the result will overflow any string longer than length 10 lead 4xxx- -!
// what a pitfall!
impor4t java.math.BigInteger;
class Solution{
    

    public String addStrings(String num1, String num2) {
        int digit = 0;
        BigInteger sum = new BigInteger("0");
        int p1 = num1.length()-1, p2 = num2.length()-1;
        // if(p1==-1&&p2==-1)
        int x = 0,y=0, n=0, newLead=0;
        
        while(p1>=0|p2>=0|digit>0){
            if(p1>=0) x=Character.getNumericValue(num1.charAt(p1));
            else x=0;
            if(p2>=0) y=Character.getNumericValue(num2.charAt(p2));
            else y=0;
         System.out.println(x+y);
            // newLead = ;
            sum = sum.add(BigInteger.valueOf(((x+y+digit)%10)*(int)Math.pow(10,n)));
            // System.out.println(sum);
            digit = (x+y+digit)/10;
            // System.out.println(digit);
            n++;
            p1--;
            p2--;
        }
        // System.out.println(sum);
        return String.valueOf(sum);
    }
}

-------String + string = Another string!------------------------
  //Runtime: 3 ms, faster than 67.51% of Java online submissions for Add Strings.
// referred discussion
class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder sb = new StringBuilder();
        int p1 = num1.length()-1, p2 = num2.length()-1, digit = 0;
        int x, y;
        while(p1>=0|p2>=0|digit>0){
            if(p1>=0) x=Character.getNumericValue(num1.charAt(p1));
            else x=0;
            if(p2>=0) y=Character.getNumericValue(num2.charAt(p2));
            else y=0;
            sb.append((x+y+digit)%10);
            digit = (x+y+digit)/10;
            p1--; p2--;
        }
        return sb.reverse().toString();
    }
}
-----------------Never afraid of refactor!!!---------------
   // Runtime: 2 ms, faster than 97.53% of Java online submissions for Add Strings.

    class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder sb = new StringBuilder();
        int p1 = num1.length()-1, p2 = num2.length()-1, digit = 0;
        int x, y;
        while(p1>=0|p2>=0|digit>0){
            x = p1<0 ? 0:num1.charAt(p1) - '0';
            y = p2<0 ? 0:num2.charAt(p2) - '0';
            sb.append((x+y+digit)%10);
            digit = (x+y+digit)/10;
            p1--; p2--;
        }
        return sb.reverse().toString();
    }
}
