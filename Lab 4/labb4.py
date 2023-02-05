# Lab 4. Program structure. DA2005 Programming techniques HT22. Stockholm University.

# Sample data:
# 1, 0.1, 0.2, 73
# 1, 0.11, 0.1, 101
# 2, 0.23, -0.01, 17
# 2, 0.9, 0.82, 23
#
# Pretend this is taken from two (or more) different experiments:
# batch 1 and batch 2.

import matplotlib.pyplot as plt

def file_existance_checker(filename):
    '''
    Function for making sure the file a user inputs actually exists.

    Parameter: File name for a .csv file.

    Returns False if the file doesn't exist, otherwise returns True.

    '''
    try: 
        open(filename, 'r')
        return True
    except FileNotFoundError:
        return False


def float_gestapo(four_vals):
    '''
    Function for making sure the elements in a list can be converts to floats

    Parameter: A list.

    Returns False if the something can't be converted to a float, otherwise True.

    '''
    for val in four_vals:
        try: 
            float(val)
        except ValueError:
            return False
    return True


def unicode_checker(filename):
    '''
    Function for making the file can be interpreted by the data collector.

    Parameter: A file name.

    Returns False if the file can't be interpreted by the data collector, otherwise True.

    '''
    try:
        with open(filename, 'r') as h:
            for line in h:
                line.split(',')
                return True
    except UnicodeDecodeError:
        return False
    


def data_collector(filename):
    '''
    Function for collecting data from an experiment, and for printing warnings related to errors associated with the sample data.

    Parameter: File name for a .csv file.

    Opens said file and returns its information in the form of a dictionary, prints warnings for errors if any are found.

    '''
    data = {}
    with open(filename, 'r') as h:
        for line in h:
            four_vals = line.split(',')
            if len(four_vals) < 4:
                print(f"\nWARNING! Line: \"{line}\" could not be interpreted!\n") # Prints a warning for and ignores lines that have less than 4 values (in sample2.csv, one of the lines returns an empty list).
                continue
            if not float_gestapo(four_vals):
                print(f"Warning: wrong input format for entry: {line}") # Prints a warning for and ignores lines that have elements that can't be converted to floats (sample4.csv contains letters in its data, that can't be converted to floats).
                continue
            batch = four_vals[0]
            if not batch in data:
                data[batch] = []
            data[batch] += [(float(four_vals[1]), float(four_vals[2]), float(four_vals[3]))]
    data = dict(sorted(data.items())) # Sorts the data in order by batch.
    return data

def batch_average_printer(data):
    '''
    Function for printing out the batch and average of the data.

    Parameter: Dictionary with data from an experiment.

    Output: Prints the batch and the avarage.

    '''
    print("Batch\t Average")
    for batch, sample in data.items(): 
        n = 0
        x_sum = 0
        for (x, y, val) in sample:
            if x**2 + y**2 <= 1:
                x_sum += val
                n += 1
        if not n == 0:
            average = x_sum/n
            print(batch, "\t", average)


def plot_data(data,f):
    '''
    Function for plotting experiment data on a graph and creating a PDF of said graph.

    Parameters: Dictionary with data from an experiment, filename of the csv file.

    Output: PDF and display of the graph.

    '''
    fig, ax = plt.subplots()
    colors=["red","green","blue","yellow","purple","orange","lime","magenta","cyan","black","pink","brown","gray","olive"]   # States which colors to use in the graph (WARNING! ONLY WORKS WITH UP TO 14 BATCHES UNLESS MORE COLORS ARE ADDED! And white will look invisible on the graph, so watch out for that too.)
    for batch, sample in data.items():
        for (x, y, val) in sample:
            ax.annotate(val,(x,y),xytext=(5,5),textcoords="offset pixels", color=colors[int(batch)-1]) # Annotates and colors (by batch) each dot with its val.
            ax.plot(x, y, color=colors[int(batch)-1],marker="o")  # Plots and colors (by batch) each dot in the graph, according to their coordinates.
    ax.add_patch(plt.Circle((0,0), 1, fill=False, color="#80abcc"))  # Depicts a unit circle in the graph.
    ax.axis([-1, 1, -1, 1]) # Defines the range of the X axis and Y axis.
    plt.xlim(-1.1, 1.1) # Sets the limit of the X axis.
    plt.ylim(-1.1, 1.1) # Sets the limit of the Y axis.
    plt.savefig((f.rsplit(".", 1)[0] + ".pdf"), format="pdf", bbox_inches="tight") # Saves the graph as a PDF. (WARNING! If a pdf file with the same name as the given csv file already exists in the same folder as this py file, it will be overwritten with this new graph!)
    plt.show() # Displays the graph.


def main():
    '''
    This is the main body of the program.
    '''
    f = input('Which csv file should be analyzed? ')
    while not file_existance_checker(f) or not unicode_checker(f): # Makes sure that the inputted file exists and can be interpreted before proceeding.
        if not file_existance_checker(f): # Warns the user that the file doesn't exist and asks for a new input.
            print("This file does not exist.")
            f = input('Which csv file should be analyzed? ')
            continue
        if not unicode_checker(f): # Warns the user that the file can't be interpreted and asks for a new input.
            print("This file cannot be interpreted.")
            f = input('Which csv file should be analyzed? ')
            continue
    data = data_collector(f) # Collects the data in the form of a dictionary, prints warnings for errors if any are found.
    batch_average_printer(data) # Prints the batch and average.
    plot_data(data,f) # Plots the data on a graph and exports a PDF of the graph.


# Start the main program: this is idiomatic python
if __name__ == '__main__':
    main()

'''
The idea with this idiom is that if this code is loaded as a module,
then the __name__ variable (internal to Python) is not __main__ and
the body of the program is not executed. Consider what would happen
if the main function was not in a function: an import statement (for
example "import o4") would load the functions and then executed
"filename = input(...)" and that is probably not what you want. The
idiom is simply an easy way of ensuring that some code is only
executed when run as an actual program.

Try it out by importing this file into another project!
''' 
