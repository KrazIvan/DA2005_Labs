# Lab 2. Polynomials. DA2005 Programming techniques HT22. Stockholm University.

# START OF TASK 1 and 2
def poly_to_string(p_list):
    '''
    Return a string with a nice readable version of the polynomial given in p_list.
    '''
    if len(p_list) == 0:
        return "0"

    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in p_list:
        if coeff == 0 and not degree == 0:
            degree += 1
            continue
        elif coeff == 1 and degree == 1:
            terms.append("x")
        elif coeff == -1 and degree == 1:
            terms.append("-x")
        elif coeff == 1 and degree > 1:
            terms.append("x^" + str(degree))
        elif coeff == -1 and degree > 1:
            terms.append("-x^" + str(degree))
        elif degree == 0:
            terms.append(str(coeff))
        elif degree == 1:
            terms.append(str(coeff) + "x")
        else:
            term = str(coeff) + "x^" + str(degree)
            terms.append(term)
        degree += 1

    final_string = " + ".join(terms) # The string ' + ' is used as "glue" between the elements in the string
    return final_string

# -------------Testing area--------------------------------------------------------------
# Uncomment (and edit) below to run tests.

#p = [2, 0, 1]
#q = [-2, 1, 0, 0, 1]
#mt = []

#print(poly_to_string(p))
#print(poly_to_string(q))
#print(poly_to_string(mt))
#print(poly_to_string([0,0,0]))
#print(poly_to_string([-1, -1, -3]))
#print(poly_to_string([1, 1, -1]))
# ---------------------------------------------------------------------------

# END OF TASK 1 and 2
# START OF TASK 3

def drop_zeroes(p_list):
    while len(p_list) != 0 and p_list[-1] == 0 and p_list.pop() == 0:
        pass
    return p_list

# -------------Testing area--------------------------------------------------------------
# Uncomment (and edit) below to run tests.

#p0 = [2,0,1,0]
#q0 = [0,0,0]

#print(drop_zeroes(p0))
#print(drop_zeroes(q0))
# ---------------------------------------------------------------------------



def eq_poly(p_list, q_list):
    while len(p_list) != 0 and p_list[-1] == 0 and p_list.pop() == 0:
        pass
    while not len(q_list) == 0 and not q_list[-1] != 0 and q_list.pop() == 0:
        pass
    return p_list == q_list

# -------------Testing area--------------------------------------------------------------
# Uncomment (and edit) below to run tests.

#p = [2, 0, 1]
#q = [-2, 1, 0, 0, 1]
#p0 = [2,0,1,0]
#q0 = [0,0,0]

#print(eq_poly(p,p0))
#print(eq_poly(q,p0))
#print(eq_poly(q0,[]))
#print(eq_poly(p0,q0))
#print(eq_poly([],[]))
# ---------------------------------------------------------------------------

# END OF TASK 3
# START OF TASK 4

def eval_poly(p, x):
    if len(p) == 0:
        return int(0)

    number = 0
    degree = 0

    for coeff in p:
        if coeff == 0:
            degree += 1
            continue
        if degree <= 0:
            number += coeff
        elif degree == 1:
            number += x * coeff
        elif degree > 1:
            number += x ** degree * coeff
        degree += 1
    return number

# -------------Testing area--------------------------------------------------------------
# Uncomment (and edit) below to run tests.

p = [2, 0, 1]
q = [-2, 1, 0, 0, 1]
j = [-5, -5, 0, -2, 0, 0, 6]
k = 10
#print(eval_poly(p, 0))
#print(eval_poly(p, 1))
#print(eval_poly(p, 2))
#print(eval_poly(q, 2))
#print(eval_poly(q, -2))
#print(eval_poly(p, True))
#print(eval_poly(p, False))
#print(eval_poly(j, k))
# ---------------------------------------------------------------------------

# END OF TASK 4
# START OF TASK 5

def neg_poly_to_string(p_list): # String polynomial version.
    if len(p_list) == 0:
        return "0"

    terms = []
    degree = 0

    for coeff in p_list:
        if coeff == 0 and not degree == 0:
            degree += 1
            continue
        elif coeff == 1 and degree == 1:
            terms.append("- x")
        elif coeff == -1 and degree == 1:
            terms.append("+ x")
        elif coeff == 1 and degree > 1:
            terms.append("- x^" + str(degree))
        elif coeff == 1 and degree > 1:
            terms.append("+ x^" + str(degree))
        elif degree == 0:
            terms.append(str(coeff-coeff*2))
        elif degree == 1:
            terms.append(str(coeff-coeff*2) + "x")
        elif coeff < 0 and degree >= 2:
            term = "+ " + str(coeff-coeff*2) + "x^" + str(degree)
            terms.append(term)
        elif coeff > 0 and degree >= 2:
            term = "- " + str(coeff) + "x^" + str(degree)
            terms.append(term)
        degree += 1

    final_string = " ".join(terms)
    return final_string

# -------------Testing area--------------------------------------------------------------
# Uncomment (and edit) below to run tests.
#p = [2, 0, 1]
#q = [-2, 1, 0, 0, 1]
#mt = []

#print(neg_poly_to_string(p))
#print(neg_poly_to_string(q))
#print(neg_poly_to_string(mt))
#print(neg_poly_to_string([0,0,0]))
#print(neg_poly_to_string([-1, -1, -3]))
#print(neg_poly_to_string([-1, -1, -3, 6, 7]))
# ---------------------------------------------------------------------------



def neg_poly(p_list): # Returns the negated version of the original list.
    terms = []

    for coeff in p_list:
        terms.append(-coeff)

    return terms

# -------------Testing area--------------------------------------------------------------
# Uncomment (and edit) below to run tests.
#p = [2, 0, 1]
#q = [-2, 1, 0, 0, 1]
#mt = []

#print(neg_poly(p))
#print(neg_poly(q))
#print(neg_poly(mt))
#print(neg_poly([0,0,0]))
#print(neg_poly([-1, -1, -3]))
#print(neg_poly([-1, -1, -3, 6, 7]))
#print(neg_poly([True, False, True, False, True]))
# ---------------------------------------------------------------------------



def add_poly(p_list, q_list):
    terms = []
    if len(p_list) > len(q_list):
        for coeff in range(len(p_list) - len(q_list)):
            q_list.append(int(0))
    if len(q_list) > len(p_list):
        for coeff in range(len(q_list) - len(p_list)):
            p_list.append(int(0))
    for coeff in range(len(p_list)):
            terms.append(p_list[coeff]+q_list[coeff])

    return terms

# -------------Testing area--------------------------------------------------------------
# Uncomment (and edit) below to run tests.
#p0 = [1,2,3,6]
#q0 = [1,-2,5]

#print(add_poly(p0,q0))
#print(add_poly([],[]))
# ---------------------------------------------------------------------------



def sub_poly(p_list, q_list):
    terms = []
    if len(p_list) == 0 and len(q_list) == 0:
        pass
    if len(p_list) == 0 and len(q_list) != 0:
        p_list.append(int(0))
    if len(q_list) == 0 and len(p_list) != 0:
        q_list.append(int(0))
    q_list = neg_poly(q_list)
    if len(p_list) > len(q_list):
        for coeff in range(len(p_list) - len(q_list)):
            q_list.append(int(0))
    if len(q_list) > len(p_list):
        for coeff in range(len(q_list) - len(p_list)):
            p_list.append(int(0))
    for coeff in range(len(p_list)):
            terms.append(p_list[coeff]+q_list[coeff])

    return terms

# -------------Testing area--------------------------------------------------------------
# Uncomment (and edit) below to run tests.
#p0 = [1,2,3,6]
#q0 = [1,-2,5]

#print(sub_poly(p0,q0))
#print(sub_poly([True],[1]))
#print(sub_poly([],[]))
# ---------------------------------------------------------------------------

# END OF TASK 5



# SAMPLE TESTS FOR ALL OF LAB 2:
#p = [2, 0, 1]
#q = [-2, 1, 0, 0, 1]
# p + q = q + p    #<-- Leave as comment.
#print(eq_poly(add_poly(p,q),add_poly(q,p)))
#True    #<-- Leave as comment.

# p - p = 0     #<-- Leave as comment.
#print(eq_poly(sub_poly(p,p),[]))
#True     #<-- Leave as comment.

# p - (- q) = p + q     #<-- Leave as comment.
#print(eq_poly(sub_poly(p,neg_poly(q)),add_poly(p,q)))
#True     #<-- Leave as comment.

# p + p != 0     #<-- Leave as comment.
#print(eq_poly(add_poly(p,p),[]))
#False     #<-- Leave as comment.

# p - q = 4-x+x^2-x^4      #<-- Leave as comment.
#print(eq_poly(sub_poly(p,q),[4, -1, 1, 0, -1]))
#True      #<-- Leave as comment.

# (p + q)(12) = p(12) + q(12)     #<-- Leave as comment.
#print(eval_poly(add_poly(p,q),12) == eval_poly(p,12) + eval_poly(q,12))
#True     #<-- Leave as comment.