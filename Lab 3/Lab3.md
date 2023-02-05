### Lab 3 Explanation ###

This lab contains several independent tasks involving important basic algorithms, dictionaries, file
handling, and error handling


## Task 1: Insertion sort ##
Insertion sort is a common sorting algorithm, that is, a method for sorting the elements of a list. The
idea in this algorithm is similar to one way of sorting a deck of cards: take cardsq from the original deck
one at a time and add each card to a new sorted deck of cards in the correct position.

We can divide up the insertion sort algorithm into two subproblems:

insert_in_sorted:
• Inserts an element x in an already sorted list sorted_list in an appropriate position so that the list remains sorted

insertion_sort:
• Insertion sort with the help of insert_in_sorted


## Task 2: sparse matrices ##
We can represent a matrix in Python as a list whose elements are lists of numbers all of the same length.
For example: [[1, 0, 0, 2], [0, 8, 0, 0], [0, 0, 0, 5]].

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
• Takes a filename f as a parameter and writes to a new file annotated_f
so that each line in annotated_f contains the original line in f followed by the row number (counting
from 0) and total number of words up to and including that row.

## Task 4: searching for strings in files ##

find_matching_lines:
• Takes a file handle h and a string s. The function
should return, in the form of a list of tuples, both the row number (counting from 0) and the contents of
each row that contains the string.

find_lines:
• Asks the user for a file and string and uses the function
find_matching_lines to print out the rows where the string was found.


## Task 5: searching by position in files ##
save_rows:
• Takes a file handle h and saves the line numbers as keys and lines
themselves as values in a dictionary. The function should return the dictionary.

lookup:
• Takes in a dictionary d from numbers to strings as above as well as two
coordinates (r,c) which correspond to a row and column in d and returns the character at the position
corresponding to the coordinates.

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