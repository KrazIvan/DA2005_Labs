# Lab 3. Iteration, file handling, error handling, and dictionaries. DA2005 Programming techniques HT22. Stockholm University.

# START OF TASK 1

def insert_in_sorted(x,sorted_list): # Soy/beta/дебил version (works only if the list is already sorted).
    here = 0
    for i in sorted_list:
        if i < x:
            here += 1
    sorted_list.insert(here, x)
    return sorted_list

def insert_in_sorted2(x,sorted_list): # Chad/alpha version (works with any list of numbers, and sorts it for you. I made this before seeing the next part of this task, and I had to make a different algorithm for the next function).
    sorted_list.append(x)
    limit = len(sorted_list)
    newList = []
    degree = 0
    while degree < limit:
        newList.append(min(sorted_list))
        sorted_list.remove(min(sorted_list))
        degree += 1
    return newList

# -------------Testing area--------------------------------------------------------------
# Uncomment (and edit) below to run tests.

#print(insert_in_sorted(2,[]))
#print(insert_in_sorted(5,[0,1,3,4]))
#print(insert_in_sorted(2,[0,1,2,3,4]))
#print(insert_in_sorted(2,[2,2]))

#print(insert_in_sorted2(2,[]))
#print(insert_in_sorted2(5,[0,1,3,4]))
#print(insert_in_sorted2(2,[0,1,2,3,4]))
#print(insert_in_sorted2(2,[2,2]))

# ---------------------------------------------------------------------------


def insertion_sort(my_list):
    sorted_list = []
    if len(my_list) == 0:
        return my_list
    else:     
        for x in my_list:
            out = insert_in_sorted(x,sorted_list)
    return out

# -------------Testing area--------------------------------------------------------------
# Uncomment (and edit) below to run tests.

#print(insertion_sort([12,4,3,-1]))
#print(insertion_sort([]))
#print(insertion_sort([12,3,666,420,5,-1,-69,88,42,0,9001]))
#print(insertion_sort([False,True,2,False,-1,True,False,True,False,True,False,True,False,True]))

# ---------------------------------------------------------------------------

# END OF TASK 1
# START OF TASK 2


def matrix_to_sparse(matrix): return {(row, column): matrix[row][column] for row in range(len(matrix)) for column in range(len(matrix[row])) if matrix[row][column] != 0} # ONE LINE! 😎

# -------------Testing area--------------------------------------------------------------
# Uncomment (and edit) below to run tests.

#print(matrix_to_sparse([[1,0,0,2],[0,8,0,0],[0,0,0,5]]))
#print(matrix_to_sparse([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))
#print(matrix_to_sparse([[0,0],[0,0],[0,0],[0,10]]))
#print(matrix_to_sparse([[0,0,False,6],[0,69,False],[0,True,True,False,0],[],[0],[0,0],[0,False,0],[0,0,0,1],[420],[0,10,0,0,0,False,0,0,0,420,0,0,0,0,666,0,0,0,0,True]]))

# ---------------------------------------------------------------------------

# END OF TASK 2
# START OF TASK 3


def annotate(f):
    lines = -1
    words = 0
    with open(f,"r") as text:
        filename, ext = f.rsplit(".", 1)
        with open(f"annotated_{filename}.txt", "w") as w:
            for line in text:
                lines += 1
                words += len(line.split())
                w.write(line.replace("\n", "") + " " + str(lines) + " " + str(words) + "\n")

# -------------Testing area--------------------------------------------------------------
# Uncomment (and edit) below to test.

annotate("infile.txt")   #<---- You need to have a txt file with the same name as the string here, in the same folder as this py file, in order for this function to work.

# ---------------------------------------------------------------------------

# END OF TASK 3
# START OF TASK 4


def og_find_matching_lines(h,s):
    theList = []
    lines = -1
    with open(h,"r") as text:
        for line in text:
            lines += 1
            if s in line:
                theList.append((lines, line))
        return theList

def find_matching_lines(h, s):
    theList = []
    lines = -1
    for line in h:
        lines += 1
        if s in line:
            theList.append((lines, line))
    return theList

# -------------Testing area--------------------------------------------------------------
# Uncomment (and edit) below to run tests.

#h = "infile.txt"    #<---- You need to have a txt file with the same name as this string, in the same folder as this py file, in order for this function to work.
#s = "face"     #<---- Custom, write the string you want to find here. Or just print the ones below to run the sample tests.

#print(og_find_matching_lines(h,s))

#print(og_find_matching_lines(h,"the mob"))
#print(og_find_matching_lines(h,"the"))
#print(og_find_matching_lines(h,"sommar"))

#with open("infile.txt", "r") as infile:
#    print(find_matching_lines(infile, "the mob"))
#    print(find_matching_lines(infile, "the"))
#    print(find_matching_lines(infile, "sommar"))

# ---------------------------------------------------------------------------


def fileExistanceChecker(h): # Checks if the file actually exists.
    try:
        open(h,"r")
        return True
    except FileNotFoundError:
        return False


def find_lines():
    h = input("Hello, which file do you want to search in? ")
    if h.upper() == "Q":
        print("\nShutting down...")
        quit()
    while not fileExistanceChecker(h):
        h = input("\nThis file doesn't exist. Please tell me a file that actually exists. ")
        if h.upper() == "Q":
            print("\nShutting down...")
            quit()
    print("\n\nOk, searching in " + str(h) + ".\n")
    s = input("What are you looking for? ")
    foundTuples = find_matching_lines(h,s)
    print(f"\n\nThe result after searching for \"{s}\" is:\n")
    for tuples in foundTuples:
        print(f"Line {tuples[0]}: {tuples[1].strip()}")
    again = input("\nDo you want to find something else, or quit? Input \"y\" or \"yes\" to search again, or \"q\" to quit. ").upper().replace(".","").replace(" ","")
    while again != "Y" and again != "YES" and again != "Q":
        again = input("\nSorry, I don't understand. Input \"y\" or \"yes\" to search again, or \"q\" to quit. ").upper().replace(".","").replace(" ","")
    if again == "Y" or again == "YES":
        print("\n")
        find_lines()
    if again == "Q":
        print("\nShutting down...")
        quit()

# -------------Testing area--------------------------------------------------------------
# Uncomment below to test.

#print(find_lines())

# ---------------------------------------------------------------------------

# END OF TASK 4
# START OF TASK 5


def save_rows(h):
    theDict = {}
    lines = -1
    for line in h:
            lines += 1
            theDict.update({lines: line.strip()})
    return theDict

# -------------Testing area--------------------------------------------------------------
# Uncomment (and edit) below to test.

#with open('infile2.txt') as hinfile:   #<---- You need to have a txt file with the same name mentioned here, in the same folder as this py file, in order for this function to work.
#    print(save_rows(hinfile))

# ---------------------------------------------------------------------------


def lookup(d, r, c):
    for key in d:
        if key == r:
            try:
                answer = d[key][c]
            except IndexError:
                raise LookupError("Doesn't exist.")
            if answer == " ":
                return "Space"
            return answer
    raise LookupError("Doesn't exist.")


# -------------Testing area--------------------------------------------------------------
# Uncomment (and edit) below to run tests.

#with open('infile2.txt') as hinfile2:        #<---- You need to have a txt file with the name as the string here, in the same folder as this py file, in order for this function to work.
#    d = save_rows(hinfile2)
#    print(lookup(d,0,0))
#    print(lookup(d,2,9))
#    print(lookup(d,2,10))

    #The two below are supposed to give a LookupError for infile2.txt.
#    print(lookup(d,3,0))
#    print(lookup(d,0,7))

# ---------------------------------------------------------------------------


def intChecker(rOrC):      #<---- This function checks if the input is a valid integer.
    try:
        int(rOrC)
        return True
    except ValueError:
        return False

def main():
    infile2 = input('Ange en fil: ').replace(" ","")
    if infile2.upper() == "EXIT":
        quit()
    while not fileExistanceChecker(infile2):
        infile2 = input("\nThis file doesn't exist. Please tell me a file that actually exists. ")
        if infile2.upper() == "EXIT":
            quit()
    with open(infile2) as hinfile2:
        indexed_file = save_rows(hinfile2)
    print("At any point type \"exit\" to quit.\n")
    while True:
        row = input("Provide row: ").lower().replace(" ","")
        while not intChecker(row) and row != "exit":
            row = input("\nInvalid input, try again.\nProvide row: ")
        if row == "exit":
            quit()
        row = int(row)
        column = input("Provide column: ").lower().replace(" ","")
        while not intChecker(column) and column != "exit":
            column = input("\nInvalid input, try again.\nProvide column: ")
        if column == "exit":
            quit()
        column = int(column)
        try:
            print("\n" + lookup(indexed_file, row, column) + "\n")
        except LookupError:
            print("\nWarning: Out of bounds, try again!\n")


# -------------Testing area--------------------------------------------------------------
# Uncomment below to test.

#main()

# ---------------------------------------------------------------------------

# END OF TASK 5