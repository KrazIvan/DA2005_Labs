# Lab 1 Explanation #

This lab contains an interactive temperature converter.


# Lab 2 Explanation #

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
    • Terms with coefficient -1 add a minus before the term, but the 1 is not written. For example 2 + -1xˆ2 should instead be 2 + -xˆ2.
    • Terms with coefficient 0 are not written. For example, 0 + 0x + 2xˆ2 should be simplified to 2xˆ2.
    • A list that contains only 0s as elements, for example [0, 0, 0], should be written as 0.


## Task 3 ##

drop_zeroes:
    • Removes all zeros at the end of a polynomial and returns the result.

eq_poly:
    • Tests when two polynomials are equal by ignoring all zeroes at the end and then comparing the rest for equality.


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



# Lab 3 Explanation #

This lab contains several independent tasks involving important basic algorithms, dictionaries, file
handling, and error handling.


## Task 1: Insertion sort ##
Insertion sort is a common sorting algorithm, that is, a method for sorting the elements of a list. The
idea in this algorithm is similar to one way of sorting a deck of cards: take cardsq from the original deck
one at a time and add each card to a new sorted deck of cards in the correct position.

We can divide up the insertion sort algorithm into two subproblems:

    insert_in_sorted:
        # Inserts an element x in an already sorted list sorted_list in an appropriate position so that the list remains sorted.

    insertion_sort:
        # Insertion sort with the help of insert_in_sorted.


## Task 2: sparse matrices ##
We can represent a matrix in Python as a list whose elements are lists of numbers all of the same length.
    For example: 
        [[1, 0, 0, 2], [0, 8, 0, 0], [0, 0, 0, 5]].

A matrix is called sparse if most of its entries are 0. If we represent such a matrix as a list of lists, we
could unnecessarily use up a lot of the computer’s memory, especially if the matrix is very big—imagine
a matrix with many millions of rows and columns that only contains a handful of elements that are not 0.
A better way of representing matrices like this is as a dictionary from coordinates to non-zero elements.
If the coordinates are of the form (row, column) and we begin counting from zero, then the matrix above
can be written in the following way as a dictionary:
    
    {(0, 0): 1, (0, 3): 2, (1, 1): 8, (2, 3): 5}

matrix_to_sparse:
    • Takes in a matrix represented as a list of lists and produces a dictionary as above.


## Task 3: file handling ##

annotate:
    • Takes a filename f as a parameter and writes to a new file annotated_f so that each line in annotated_f contains the original line in f followed by the row number (counting from 0) and total number of words up to and including that row.

## Task 4: searching for strings in files ##

find_matching_lines:
    • Takes a file handle h and a string s. The function should return, in the form of a list of tuples, both the row number (counting from 0) and the contents of each row that contains the string.

find_lines:
    • Asks the user for a file and string and uses the function find_matching_lines to print out the rows where the string was found.


## Task 5: searching by position in files ##
save_rows:
    • Takes a file handle h and saves the line numbers as keys and lines themselves as values in a dictionary. The function should return the dictionary.

lookup:
    • Takes in a dictionary d from numbers to strings as above as well as two coordinates (r,c) which correspond to a row and column in d and returns the character at the position corresponding to the coordinates.

The idea is that lookup will be used together with save_rows (see part c)) and each character in the file
can be said to be at a certain row and column. For example, the word “Hey” in infile2.txt occupies
the three coordinates (0,0), (0,1), (0,2). In the same way, the word “chairs” takes up the coordinates
(2,4), (2,5), . . . , (2,9).

We assume a 0-indexed coordinate system (as is usual in programming).
The following cases should be handled specially:
    • If the row and/or column does not exist in d, then the program should raise a LookupError.
    • If the position is a space, then the string “Space” should be returned.

A code snippet that uses save_rows and lookup that
1. Asks the user for a file and reads in the file to a dictionary (using save_rows).
2. Asks the user to give coordinates for a row number and column number.
3. Uses lookup to fetch and then write out the character in the file at that coordinate.

The user should be able to give several coordinates until they choose to write exit, whereupon the
program should exit.



# Lab 4 Explanation #

The goal of this program is to read in a data file with (invented) data from several batches of measurements,
taken from different points on the plane, and for each batch calculate the average of the measurements
taken inside the unit circle. A point (x, y) in the plane is inside the unit circle if x^2 + y^2 ≤ 1.

Measurements taken outside the unit circle should be ignored. The data file has four columns separated
with commas: it is a so-called csv file (where “csv” stands for comma-separated values). The first number
records which batch a measurement belongs to, while the second and third record the x- and y-coordinates
where the measurement was taken, and the fourth number is the measurement itself.

For example, a data file could contain the following lines:

    1, 0.1, 0.2, 73
    1, 0.11, 0.1, 101
    2, 0.23, -0.01, 17
    2, 0.9, 0.82, 23

Here we have measurements from two batches, 1 and 2, and so the program will calculate two averages.
Note that the last measurement is outside the unit circle.



plot_data(data,f): This function should plot the data stored in the argument data using matplotlib. It should not filter out points outside the unit circle, but you should plot the circle itself along with the points. Does not need to plot any averages. The plotted data should then be saved as a PDF in a file f.pdf (where f is the second parameter to plot_data). The function plot_data should then be called in the main program after the averages have been printed.



# Lab 5 Explanation #

This lab takes a look at a computational problem from modern molecular biology. In DNA sequence analysis, we sometimes want to know how much overlap there is between two sequences (simplified: how much DNA they have in common). This lab support such an analysis with object-oriented code.

The lab contains some test functions. The test functions have two purposes. (1) They make testing easier and faster. It is often convenient to have some basic testing available. Later, we will look at “real” systematic testing. (2) The test is a codified specification of how the functions should work. Everything works as intended when the call test_all() prints "Yay, all good".

The code's functionality is explained by docstrings.