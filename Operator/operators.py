"""
#Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""

'''
Python Arithmetic Operators

Addition    (+)

Subtraction     (-)

Multiplication   (*)

Division    (/)

Modulus (  % :gives the vag shes)

Exponentiation ( ** To the Power type behaviour)

Floor division( // gives no floating ans of division)
x = 15
y = 2
print(x // y)
#output: 7
#the floor division // rounds the result down to the nearest whole number
'''

'''
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	


==  !=  >  >=  <  <=  -------- Comparisons
is  is not  ----------------- identity
in  not in ----------------- membership operators	

###################################
----------Python Identity Operators
is 
is not : it is just opposite to the is operator 
----
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
##########################################################################
######################################
-------------Python Bitwise Operators
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
^	XOR
~	NOT

#####################################################################
#---------Python Membership Operators
in 
not in

x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

######################################
#---------Python Bitwise Operators
not	Logical NOT	operator
and	    AND	and operator
or	    OR operator
###############################################################################

'''