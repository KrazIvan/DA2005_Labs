### Lab 4 Explanation ###

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



plot_data(data,f):

This function should plot the data stored in the argument data using matplotlib. It should not filter out points outside the unit circle, but you should plot the circle itself along with the points. Does not
need to plot any averages. The plotted data should then be saved as a PDF in a file f.pdf (where f is the second parameter to plot_data).
The function plot_data should then be called in the main program after the averages have been printed.
