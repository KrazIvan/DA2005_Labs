### Lab 2 Explanation ###

In this lab, polynomials are represented using lists of coefficients. The word “representation” here
means approximately “way of storing in a computer”. Concretely, we will represent a polynomial like
1+3x+7x^2 in Python as the list [1,3,7]. In general, we will store the coefficient of degree n in the list’s
nth entry.


## Task 1 ##
Suppose that the polynomials p and q are defined as below:


     p := 2 + x^2
     q := -2 + x + x^4

The function stores list representations for these two polynomials in the variables p and q. That
is, write
p = [...]
q = [...]
with the contents of the lists filled in. Using poly_to_string. You should get the following:
>>> poly_to_string(p)
'2 + 0x + 1x^2'
>>> poly_to_string(q)
'-2 + 1x + 0x^2 + 0x^3 + 1x^4'.


## Task 2 ##
In poly_to_string:
• An empty list is converted to 0.
• Terms with coefficent 1 are written without a coefficient. For example, 1xˆ2 should instead be
written xˆ2.
7
• Terms with coefficient -1 add a minus before the term, but the 1 is not written. For example 2 +
-1xˆ2 should instead be 2 + -xˆ2.
• Terms with coefficient 0 are not written. For example, 0 + 0x + 2xˆ2 should be simplified to
2xˆ2.
• A list that contains only 0s as elements, for example [0, 0, 0], should be written as 0.


## Task 3 ##

drop_zeroes:
• Removes all zeros at the end of a polynomial and returns the result.

eq_poly:
• Tests when two polynomials are equal by ignoring all zeroes at the end and then
comparing the rest for equality.


## Task 4 ##

eval_poly:
• Takes a polynomial and a value in a variable x and returns the polynomials value at the point x.


## Task 5 ##
neg_poly:
• Defines negation of polynomials (that is, flip the sign of all coefficients and return the result).

add_poly:
• Defines addition of polynomials (that is, add the coefficients and return the result).

sub_poly:
• Defines subtraction of polynomials.