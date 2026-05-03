def e1():
    '''
    This exercise asks you to experiment with
    for loops.
    a. Write a for loop that prints the ASCII code point of each
    character in a string named S . Use the built-in function
    ord(character) to convert each character to its integer
    code point. This function technically returns a Unicode
    code point that may not fall in ASCII’s range, but if you
    restrict its content to ASCII characters, you’ll get back
    ASCII codes. (Test it interactively to see how it works, if
    needed.)
    b. Next, change your loop to compute the sum of the ASCII
    code points of all the characters in a string.
    c. Finally, modify your loop again to return a new list that
    contains the ASCII code points of each character in the
    string. Does the expression map(ord, S) have a similar
    effect? How about [ord(c) for c in S] ? Why?
    '''
    string: str='hack'
    total=0
    lista=[]
    for s in string:
        points=ord(s)
        print(points)
        total+=points
        lista.append(points)
    print(total)
    print(lista)
    print(list(map(ord,string)))
    print([ord(c) for c in string])

def e2():
    '''
        Write Python if and match
        statements that print the first three month names of the year,
        given their relative numbers. For example, given 1, the
        output should be January, and for 3, it should be March (or
        whatever months are named in your locale). Then do the
        same by coding the choice with both a dictionary-key index
        and a list-offset index. How would you handle out-of-range
        month numbers?
    '''
    month: int=int(input('Select your Month(1,2,3):'))
    months_dict: dict = {1:'January', 2:'February', 3:'March'}
    months_list: list = ['January', 'February', 'March']
    while month != 0:
        # with if/else statements
        """ if month == 1:
            print('January')
        elif month == 2:
            print('February')
        elif month == 3:
            print('March')
        else:
            month=int(input('Incorrect Month:'))
            continue """
        # with match-case statements
        """ match month:
            case 1:
                print('January')
            case 2:
                print('February')
            case 3:
                print('March')
            case _:
                month=int(input('Incorrect Month:'))
                continue """
        # with dict-key statement
        print(months_dict.get(month,"Incorrect Month. Try again"))
        # with list index
        print(months_list[month-1] if month < 4 else "Incorrect Month. Try again")
        month=int(input('Select your Month(1,2,3):'))

def e3():
    '''
     Consider the following code,
    which uses a while loop and found flag to search a list of
    powers of 2 for the value of 2 raised to the fifth power (32).
    It’s stored in a module file called power.py:
    L = [1, 2, 4, 8, 16, 32, 64]
    X = 5
    found = False
    i = 0
    while not found and i < len(L):
        if 2 ** X == L[i]:
            found = True
        else:
            i = i+1
    if found:
        print('at index', i)
    else:
        print(X, 'not found')
    $ python3 power.py
    at index 5
    As is, the example doesn’t follow normal Python coding
    techniques. Follow the steps outlined here to improve it (for
    all the transformations, you may either type your code
    interactively or store it in a script file run from the system
    command line or other interface—using a file makes this
    exercise much easier):
    a. First, rewrite this code with a while loop else clause to
    eliminate the found flag and final if statement.
    b. Next, rewrite the example to use a for loop with an
    else clause, to eliminate the explicit list-indexing logic.
    (Hint: to get the index of an item, use the list index
    method— L.index(X) returns the offset of the first X in
    list L .)
    c. Next, remove the loop completely by rewriting the
    example with a simple in operator membership
    expression. (See Chapter 8 for more details, or type this to
    test: 2 in [1, 2, 3] .)
    d. Finally, use a for loop and the list append method to
    generate the powers-of-2 list ( L ) instead of hardcoding a
    list literal.
    '''
    L = []
    X = 5
    i = 0
    """ while i < len(L):
        if 2 ** X == L[i]:
            print('at index', i)
            return
        else:
            i = i + 1
    print(X, 'not found') """

    """ for i in L:
        if 2 ** X == i:
            print('at index', L.index(i))
            return
    print(X, 'not found') """

    """ if (2 ** X) in L:
        print('at index', L.index(2**X))
    else:
        print(X, 'not found') """
    for i in range(0,7):
        L.append(2**i)
    print(L)




if __name__=="__main__":
    #e1()
    #e2()
    e3()
    