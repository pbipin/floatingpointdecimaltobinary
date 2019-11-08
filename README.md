# floatingpointdecimaltobinary
Python program that converts floating point decimal to binary
59.65625 is a floating point decimal and its corresponding binary value is 111011.10101. 

Procedure:
1. The whole number part(59) of 59.65625 is divided by 2 until the quotient is 1. The remainder(carry) that is accumulated(either 1 or 0) till the last sequence of operation that gives the quotient 1 is taken in the reverse order of creation, so as to obtain 111011. 
59/2 = 29 (1 is taken as carry)
29/2 = 14 (1 is taken as carry)
14/2 = 7 (1 is taken as carry)
7/2 = 3 (1 is taken as carry)
3/2 = 1 (1 is taken as carry)
So when we reverse the carry, we get 11011. Finally, we place the final quotient at the very beginning of the 11011 to get 11011.
2. The decimal part is multiplied by 2 as many times as the number of decimal places in the final result required. To elaborate, lets take the above menioned example of 59.65625. Here 0.65625 = 65625 * 10^-5. 
0.65625*2 = 1.31250 (1 is taken as carry)
0.31250*2 = 0.62500 (0 is taken as carry)
0.62500*2 = 1.25000 (1 is taken as carry)
0.25000*2 = 0.50000 (0 is taken as carry)
0.50000*2 = 1.00000 (1 is taken as carry)
3. When we bring the calculations together, we obtain 111011.10101
