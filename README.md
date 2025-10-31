# NeurIPS 2025 - Google Code Golf Championship

This repository contains the golfed Python programs to the training tasks of the [Abstraction and Reasoning Corpus](https://github.com/fchollet/ARC-AGI) that I wrote for the [NeurIPS 2025 - Google Code Golf Championship](https://www.kaggle.com/competitions/google-code-golf-2025) (disclaimer: not all programs are written by me, some are taken from the various great [notebooks on Kaggle](https://www.kaggle.com/competitions/google-code-golf-2025/code)). The average program has less than 160 bytes (no imports are used). Further optimizing the programs such as compressing them using zlib and using exec (see [this notebook](https://www.kaggle.com/code/cheeseexports/big-zippa)) reduces the average to 147, which placed me on rank 29 on the final leaderboard (out of >6k entrants and >1k teams, and rank 5 among the solo teams). Since I and am not aware of any extensive publicly available collection of Python golfing tricks, I figured I'd write up the various tricks I used here. The majority are general golfing tricks, then there are some at the end which are more arc-specific.

## General Golfing Tricks

### Single-Letter Variable Names
Use single-letter instead of multi-letter variable names whenever possible, which should almost always be possible without having to increase the program size otherwise, since there are at least as many possible such names as the product of the number of letters in the alphabet and the number of casings (that is to say A-Z for both lower- and uppercase as well as the underscore _ gives already 53 options).


```python
# instead of
my_list = [1, 2, 3]

# do
x = [1, 2, 3]
```

### Overwriting Unused Variables
In the unlikely event of needing more than 53 unique variables, it is likely that at the point of requiring the 54th, at least one of the first 53 variables is no longer needed and can hence be overwritten, which is shorter than falling back to multi-letter variable names.


```python
# instead of
aa = 3

# do
a = 3
```

### Avoiding Single-Use Variables
If a variable is only accessed once (which is something that sometimes can be achieved even in cases where it is accessed more than once), then the variable might be unneccessary and can in that case be removed and one can directly put the object where the variable was accessed previously.


```python
# instead of
x = 3
y = x * 2

# do
y = 3 * 2
```

### Avoiding Unneccessary Spaces
The space character is oftentimes not needed, such as after commas or around operators, and can therefore be removed.


```python
# instead of
y = 3 * x

#do
y=3*x
```

### Single-Character Indentation
Each line on the same block must have the same indentation, that is to say the same number of characters preceding the code on that line, however it must not be multiple characters, hence use only one additional character (either a space or a tab) instead of multiple for each new sub-block of code.


```python
# instead of
if x:
    y = 1

# do
if x:
 y = 1
```

### Avoiding Linebreaks After Compound Statements
After compound statements like if, while, for etc, the body of statements that follows (if it itself can be expressed without newlines) must not be on a new line, but can come right after the colon.


```python
# instead of
if x:
    y = 1

# do
if x:y = 1
```

### Avoiding Linebreaks Between Statements

Consecutive statements in lines of code can often be bundled together by replacing the newline with a semicolon, which in and of itself does not reduce the program size as it merely swaps out a character with a different one, but oftentimes still does, i.e. whenever there are indents involved, as in that case the whitespace characters used to indent the lines can be dropped as well.


```python
# instead of
if x:
    y = 1
    z = 2

# do
if x:
    y = 1;z = 2
```

### Chained Assignment

Assignments can be chained, so if two variables are assigned the same value, one can get away with writing the value only once instead of twice.


```python
# instead of
x = 1
y = 1

# do
x = y = 1
```

### Tuple Assignment

When assigning a tuple, the brackets around the tuple entries can be left out.


```python
# instead of
x = (1, 2, 3)

# do
x = 1, 2, 3
```

### Multiple Assignments

Tuple unpacking can also be used to assign multiple variables at once, allowing for example to switch the values of two variables without having to use a temporary variable.


```python
# instead of
tmp = x
x = y
y = tmp

# do
x, y = y, x
```

### Extended Iterable Unpacking

When needing to subdivide an iterable into multiple variables e.g. when the first last values are needed as a variable each, no separate extraction with indexing is required, but unpacking can be used to achieve the same in one go.


```python
x = [1, 2, 3, 4, 5]

# instead of
first = x[0]
middle = x[1:-1]
last = x[-1]

# do
first, *middle, last = x
```

###  Avoiding Consecutive Slicing

When slicing into a list, oftentimes expressions involving consecutive slicing that one might naively do can be compressed into a single slicing, since the syntax allows to specify start, end and step simultaneously.


```python
x = [1, 2, 3, 4, 5]

# instead of
y = x[1:][::-1][1:]

# do
y = x[-2:0:-1]
```

### Implicit Type Conversion

When converting the type of an object, using the constructor functions of the desired container class explicitly can often be avoided by using the respective brackets (square for lists, round for tuples and curly for sets) together with unpacking.


```python
s = 'abcde'

# instead of
x = list(s)
y = tuple(s)
z = set(s)

# do
x = [*s]
y = (*s,)
z = {*s}
```

### Lambda Functions Over Regular Functions

As opposed to defining a function using the def keyword, which oftentimes needs the return keyword, lambda functions don't require a return keyword and can hence be used instead as a shorter alternative, if the function body can be stated as a single-line expression.


```python
# insetad of
def f(x): return x * 2

# do
f = lambda x: x * 2
```

### Dunder Methods Over Lambda

Sometimes, using dunder methods instead of a function that uses their respective operator can be shorter (the available dunder methods can be checked with the builtin dir function).


```python
# instead of
f = lambda x: x * 2
g = lambda x: x + 2
h = lambda x: x < 2

# do
f = (2).__mul__
g = (2).__add__
h = (2).__lt__
```

### Optional Default Arguments

Quite some widely used functions and methods take optional arguments such as default values that are not needed most of the time but could be very handy to allow for shorter code, such as the max and min functions or the get method of dictionaries or the next function (for both of which the default keyword does not need to be specified).


```python
x = []
y = {}

# instead of 
a = max(x) if len(x) > 0 else 1
b = y[2] if 2 in y else 1
c = x[0] if len(x) > 0 else 1

# do
a = max(x, default=1)
b = y.get(2, 1)
c = next(iter(x), 1)
```

### Using Integers Instead Of Booleans

Using 1 instead of True and 0 instead of False is shorter.


```python
x = [1, 3, 5, 8, 9]

# instead of
a = False
for e in x:
    if e % 2 == 0:
        a = True

# do
a = 0
for e in x:
    if e % 2 == 0:
        a = 1
```

### Using And And All

The functions and and all can oftentimes be used to avoid loops with logical operators.


```python
x = [1, 3, 5, 8, 9]

# instead of
a = 0
for e in x:
    if e % 2 == 0:
        a = 1

# do
a = any([e % 2 == 0 for e in x])
```

### Generator Expressions Over List Comprehensions

Sometimes, a list does not actually need to be produced and it suffices to use a generator instead, saving the square brackets - such as if the result is only being used within a function like max, min, sum, any, all, etc.


```python
x = [1, 2, 3, 4, 5]

# instead of
a = any([e % 2 == 0 for e in x])

# do
a = any(e % 2 == 0 for e in x)
```

### Replacing If-Else With Indexing

Branching can be achieved more concisely than with an if-else statement by having a list with the value for the else case as the first entry and the value for the if case as the second entry, and then indexing into that list using the boolean, where False will correspond to the first element (index 0) and True to the second element (index 1).


```python
y = True

# instead of
x = 3 if y else 2

# do
x = [2, 3][y]
```

### Replacing If-Elif-Else With Indexing

If the branching factor is greater than two, a similar trick to avoid the if, elif and else keywords can be applied.


```python
x = 3

# instead of
if x == 1:
    y = 'first'
elif x == 2:
    y = 'second'
elif x == 3:
    y = 'third'

# do
y = ['first', 'second', 'third'][[x == 1, x == 2, x == 3].index(1)]
```

### Replacing If-Elif-Else With Arithmetic

Sometimes, the if-elif-else keywords can be avoided even without having to rely on indexing, namely if the indices can be directly constructed from the conditions.


```python
x = 3

# instead of
y = ['first', 'second', 'third'][[x == 1, x == 2, x == 3].index(1)]

# do
y = ['first', 'second', 'third'][x - 1]
```

### Replacing If-Else With Arithmetic

If branching is done to select between two numbers, it may be quicker to use arithmetic to get the result instead.


```python
y = 1

# instead of 
x = 3 if y else 2
z = 6 if y else 3

# do
x = 2 + y
z = 3 * (y + 1)
```

### Replacing Logical With Arithmetic Or Bitwise Operators

The logical operations using and, or and not can often be compressed by using arithmetic or bitwise operators instead.


```python
a = True
b = False

# instead of
x = a and b
y = a or b
z = not a

# do
x = a * b
y = a | b
z = 1 - a
```

### Subset Testing

In order to check whether a set is a subset of another set, checking whether the set difference is equal to the empty set is cheaper than using the issubset method.


```python
A = {1, 2}
B = {1, 2, 3}

# instead of
x = A.issubset(B)

# do
x = A - B == set()
```

### Empty Set Creation

If an empty set is needed, e.g. for subset testing, and a set is already available, set difference with the same set uses less characters than creating an empty set explicitly.


```python
A = {1, 2}

# instead of
x = set()

# do
x = A - A
```

### Operand Swapping

Sometimes, re-ordering the operands within a commutative operation can allow to save whitespaces, such as when one of the operands does not need whitespace padding, or in the case of natural numbers, where a preceding plus is optional.


```python
x = 1
y = 3
a = [{1}, {2}, {3}]

# instead of 
z = -y + x
b = [e for e in a if e=={x}]

# do
z = x - y
b = [e for e in a if{x}==e]
```

### Flattening Using Sum

To flatten a list of lists or a tuple of tuples into an order-preserving flat list, a naive way would be to do nested comprehension, however one can use sum on the nested container and pass the respective empty container as a value to its optional start parameter.


```python
a = [[1, 2], [3, 4, 5], [6]]
b = ((1, 2), (3, 4, 5), (6,))

# instead of
x = [e for x in a for e in x],
y = (*(e for x in b for e in x),)

# do
x = sum(a,[])
y = sum(b,())
```

### Assigning Methods To Variables

Methods can be assigned to variables, which can allow to save bytes in cases of multiple usage of the same method in non-primitive settings other than e.g. trivial loops.


```python
x = [1, 2, 3, 4]

# instead of
if x.count(1) + x.count(2) > 1:
    x.append(x.count(3))

# do
f = x.count
if f(1) + f(2) > 1:
    x.append(f(3))
```

###  Augmented Assignment Operators For Arithmetic

To modify a numeric variable using some arithmetic, one might by default type the variable, operator and other operand(s) on the right of the assignment operator, however one can avoid having to re-type the variable by using the respective augmented assignment operator instead, which is achieved by prefixing the equal sign with the operator.


```python
x = 3
y = [1, 2, 3]

# instead of
x = x - 1
x = x * 4

# do
x -= 1
x *= 4
```

###  Augmented Assignment Operators For Containers

To add new items to containers such as lists or sets in e.g. a loop, one might use the respective append method for lists or add method for sets, however one can use augmented assignment operators instead and avoid having to type out the methods.


```python
x = [1, 2, 3]
y = {1, 2, 3}

# instead of 
for e in range(4, 10):
    x.append(e)
    y.add(e)

# do
for e in range(4, 10):
    x += [e]
    y |= {e}
```

### Walrus Operator For Lambdas

The walrus operator allows to do assignments as part of expressions and can hence can often be used to e.g. merge the declaration of a variable with it's first-time usage and save characters or even enable variables to begin with, such as in the case of lambda functions.


```python
# instead of
f = lambda x: x.count(1) + x.count(2)

# do 
f = lambda x: (c:=x.count)(1) + c(2)
```

###  Walrus Operator For Loops

The walrus operator can also be used to turn a loop into an expression using list comprehension that might be cheaper as it need not be on a separate line anymore.


```python
x = 3

# instead of
if x < 5:
    for i in range(10):x += i
    x *= 2

# do
if x < 5:x = [(x:=x+i) for i in range(10)][-1]; x *= 2
```

### Loop Collapsing

Nested for loops over ranges can often be collapsed into a single for loop over the product of the sizes and getting the value for the outer loop by doing floor division with the size of the inner loop and the value for the inner loop via modulus with the size of the inner loop.


```python
x = 0

# instead of
for a in range(4):
    for b in range(6):
        x += a * b

# do
for i in range(24):
    a = i // 6
    b = i % 6
    x += a * b
```

### Avoiding Range If Loop Variable Unused

If the loop variable is not needed and say the range keyword is not used elsewhere more than once (in which case it would be worth it to assign it to a variable), it can be cheaper to just loop over a container of the same size instead.


```python
x = 2

# instead of
for i in range(9):
    x *= 2

# do
for i in [0]*9:
    x *= 2
```

### Forcing Same Ranges

If there are multiple ranges of the same sizes but with varying starts, ends or steps, it might be worth enforcing reusing the same range instead and modifying the loop variables correspondingly.


```python
x = 0

# instead of
for i in range(3):
    for j in range(1, 4):
        for k in range(3, 8, 2):
            x += i * j * k

# do
r = range(3)
for i in r:
    for j in r:
        for k in r:
            x += i * (j + 1) * (k * 2 + 3)
```

### Unknown Range

If one is say given two values and doesn't know which is bigger, and wants to iterate over the range they cover, instead of having to call both min and max to determine the start and end, one can use sorted and unpacking instead.


```python
x = 0
a = 9
b = 4

# instead of 
for i in range(min(a, b), max(a, b)):
    x += i

# do
for i in range(*sorted((a, b))):
    x += i
```

### Varying Range Instead Of Conditional Loop

Instead of conditionally looping one can always loop and just have the loop be of size zero in case the condition is not met, which could be shorter in certain cases.


```python
x = 0
y = True
a = [1, 2, 3, 4, 5]

# instead of
if y:
    for i in a:
        x += i

# do
for i in a[:y * len(a)]:x += 1
```

### Combining Comparison Operators

Multiple comparison operations can often be combined into a single expression, especially if the individual sub-statements re-use values.


```python
x = 3
y = 5

# instead of
z = x < 4 and y > 4

# do
z = x < 4 < y
```

### Abusing Logical Operators

If the condition in an if-else statement is not a boolean but some other value considered in a boolean context, such as an empty container or None being falsy or a non-empty container being truthy, then the indexing trick to get rid of if-else does not work as is, and instead of forcing that trick with a call to the bool function which might make it not worthwile, one can abuse the and and or keywords instead.


```python
x = [1, 2, 3]
a = 5
b = 9

# instead of
y = a if x else b

# do
y = x and a or b
```

### Not Truncating All When Zipping

When zipping iterables together, not all need to have the same length, as in case of a length mismatch, the shortest provided iterable's length is being used, hence truncating all the iterables is not needed.


```python
x = [1, 2, 3, 4, 5, 6]

# instead of
y = list(zip(x[:3], x[3:]))

# do
y = list(zip(x, x[3:]))
```

### Avoiding List Comprehensions Using Map

When applying the same function to each element in an iterable, using map can be shorter than list comprehensions.


```python
x = ['banana', 'apple', 'orange']

# instead of
y = [len(e) for e in x]

# do
y =[*map(len, x)]
```

### Avoiding Zipping Using Map

Similarly, map takes multiple iterables, hence can also be used to further avoid zipping in such cases where otherwise a list comprehension might be used.


```python
x = [1, 2, 3, 4, 5, 6]
y = [2, 2, 4, 4, 6, 6]

# instead of
z = [divmod(a,b) for a,b in zip(x,y)]

# do
z = [*map(divmod, x, y)]
```

###  Using Filter

List comprehensions used to sub-select elements can often be avoided by using the filter function, such as by filtering with using int as the function when selecing all non-zero elements.


```python
x = [-2, -1, 0, 1, 2]

# instead of
y = [e for e in x if e]

# do
y = [*filter(int, x)]
```

### Order-Preserving Unique Items

To get all the unique items in a list in the order of first occurrence, the dict's formkeys method can be used instead of e.g. a more involved list comprehension (note that converting to and then back from a set won't necessarily result in the desired order).


```python
x = [1, 3, 2, 3, 1]

# instead of
y = [e for j,e in enumerate(x) if x.index(e) == j]

# do
y=[*{}.fromkeys(x)]
```

### Early Return

Sometimes a break statement (if it is known that it will be triggered) can be avoided by returning early.


```python
# instead of
def f(x):
    a = 0
    for e in x:
        a += e
        if e > 10:
            break
    return a

# do
def f(x):
    a = 0
    for e in x:
        a += e
        if e > 10:
            return a
```

###  Default Arguments For Lambda Functions

Also lambda functions take default arguments which enables using lambda functions in cases where one might otherwise would use the def keyword.


```python
x = 9

# instead of
def f(x):
    return [(a, b, c) for a in range(x) for b in range(x) for c in range(x)]

# do
f = lambda x, r = range: [(a, b, c) for a in r(x) for b in r(x) for c in r(x)]
```

###  Rotations Using Modulo

When there is a rotation of values through which one wants to cycle, instead of explicitly storing the full mapping in a dictionary, using a list and stepping using index and modulus can be cheaper.


```python
x = (0,-1)

# instead of
m = {(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0),(-1,0):(0,1)}
y = m[x]

# do
m = [(0,1),(1,0),(0,-1),(-1,0)]
y = m[(m.index(x) + 1) % len(m)]
```

### Conditional Container Expansion

If a container like a list or set is only expanded conditionally, one can avoid having to use compound statements which might allow to save on newlines.


```python
a = [1, 2, 3]
b = {1, 2, 3}
y = True

# instead of
if y:
    a+=[4]
if y:
    b|={4}

# do
a+=[[],[4]][y]
b|=[b-b,{4}][y]
```

### Extracting Element From Set

If the only value of a set needs to be extracted, using max is cheaper than converting it to a list and then indexing with zero.


```python
x = {3}

# instead of
y = [*x][0]

# do
y = max(x)
```

## ARC-Specific Golfing Tricks

###  Transposing A Grid

When transposing a grid, instead of a nested list comprehension, one can use zip and map with unpacking.


```python
g = [
    [1, 2, 3],
    [4, 5, 6]
]

# instead of 
h = [[g[i][j] for i in range(len(g))] for j in range(len(g[0]))]

# do
h = [*map(list,zip(*g))]
```

### Rotating A Grid

When rotating a grid clockwise by 90 degrees, instead of a nested list comprehension, one can use list and reversion instead.


```python
g = [
    [1, 2, 3],
    [4, 5, 6]
]

# instead of 
h = [[g[len(g) - i - 1][j] for i in range(len(g))] for j in range(len(g[0]))]

# do
h = [*map(list,zip(*g[::-1]))]
```

### Getting The Set Of Symbols

When getting the set of symbols of a grid, a nested list comprehension or for loop can be avoided by using flattening with sum.


```python
g = [
    [1, 2, 3],
    [4, 2, 4]
]

# instead of
c = set([e for r in g for e in r])

# do
c = {*sum(g,[])}
```

### Most Common Symbol

To get the most common symbol in a grid, one can use max and count as the key.


```python
g = [
    [1, 4, 3],
    [4, 2, 4]
]

# instead of
d = {}
for i,r in enumerate(g):
    for j,e in enumerate(r):
        d[e] = d.get(e, 0) + 1
m = max(d.items(),key=lambda x:x[1])[0]

# do
s = sum(g,[])
m = max(s,key=s.count)
```

### Getting First Coordinate Of Symbol

When getting the coordinates of the first occurrence of a symbol on a grid (in row-column order), using flattening, index and divmod can be cheaper than a e.g. a nested loop.


```python
g = [
    [1, 2, 3],
    [4, 2, 4]
]
c = 4

# instead of
i, j = [(i, j) for i,r in enumerate(g) for j,e in enumerate(r) if e == c][0]

# do
s = sum(g,[]);
i, j = divmod(s.index(c), len(g[0]))
```

### Coordinates Of Cells With Symbols At Boundary

When e.g. getting all coordinates of cells with symbol 0 (9), testing for smaller than 1 (greater than 8) is cheaper than testing for equality with 0 (9), since all symbols are within range(10).


```python
g = [
    [0, 9, 0],
    [0, 9, 9],
    [9, 9, 0],
]

# instead of
z = {(i, j) for i,r in enumerate(g) for j,e in enumerate(r) if e==0}
n = {(i, j) for i,r in enumerate(g) for j,e in enumerate(r) if e==9}

# do
z = {(i, j) for i,r in enumerate(g) for j,e in enumerate(r) if e<1}
n = {(i, j) for i,r in enumerate(g) for j,e in enumerate(r) if e>8}
```

### Coordinates Of Cells With Symbols Not In Set

When one wants to get all coordinates of cells with symbols that are e.g. neither 0 nor 7, instead of checking for non-containment in a container, the modulus operator can be used as a hack.


```python
g = [
    [0, 9, 3],
    [1, 9, 7],
    [9, 7, 0],
]

# instead of
s = {(i, j) for i,r in enumerate(g) for j,e in enumerate(r) if e not in {0, 7}}

# do
s = {(i, j) for i,r in enumerate(g) for j,e in enumerate(r) if e%7}
```

### Within-Bounds-Checking

Sometimes, one has to avoid indices going out of bounds to avoid errors, which can be achieved more cheaply by merging the horizontal and vertical boundary checks.


```python
g = [
    [0, 9, 3],
    [1, 9, 7],
]
s = {(0, 3), (1, 2), (5, 2), (-1, 4), (1, 1)}

# instead of
x = {(i, j) for i,j in s if 0<=i<len(g) and 0<=j<len(g[0])}

# do
x = {(i, j) for i,j in s if len(g)>i>-1<j<len(g[0])}
```

### Avoiding Value Not In List

Instead of conditionally using the index method on a list only when the value of interest is present, one can avoid the checking by simply adding the value to the list, which sometimes achieves the same end result.


```python
g = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1]
]

# instead of
i = min(r.index(1) for r in g if 1 in r)

# do
i = min((r+[1]).index(1) for r in g)
```

### Getting The Bounding Box

Oftentimes, the bounding box of a set of coordinates is needed, in which case map and sorted and zip with unpacking provides a fairly short solution.


```python
s = {(0, 3), (1, 2), (5, 2), (0, 4), (1, 1)}

# instead of
i = min(i for i,j in s)
j = max(i for i,j in s)
x = min(j for i,j in s)
y = max(j for i,j in s)

# do
(i,*_,j),(x,*_,y)=map(sorted,zip(*s))
```

### Conditional Transpose

For many tasks, it is simpler to implement the core of the program only for a certain orientation (horizontal or vertical) of the grid and then conditionally transpose the grid as a first and last operation depending on the state of the input grid, instead of redundantly for both, which can be achieved efficiently with a helper function.


```python
g = [
    [1, 2, 3, 4],
    [5, 3, 4, 2]
]

# instead of
f = len(g[0]) < len(g)
if f:
    g = [*zip(*g)]
    g = [r[1::-1] for r in g]
    g = [*zip(*g)]
else:
    g = [r[1::-1] for r in g]

# do
f = lambda x: [x,[*zip(*g)]][len(g[0]) < len(g)]
g = f([r[1::-1] for r in f(g)])
```

### Rotating Four Times

Similarly, it can be cheaper to rotate four times and each time apply certain functionality as opposed to avoiding rotating at the cost of having the functionality needing to be potentially much more involved.


```python
g = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# instead of
g[0][1:-1] = [1] * (len(g[0]) - 2)
g[-1][1:-1] = [1] * (len(g[0]) - 2)
for i in range(1, len(g) - 1):
    g[i][0] = 1
    g[i][-1] = 1

# do
for _ in[0]*4:
    g=[*map(list,zip(*g[::-1]))]
    g[0][1:-1] = [1] * (len(g[0]) - 2)
```

### Hardcoding As Much As Possible

For many tasks, many things are hardcoded and hence need thus not be inferred then, such as grid sizes, symbols, object sizes, etc.


```python
g = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# instead of
d = len(g) * len(g[0])

# do
d = 9
```

###  Neighborhood

There are more and less efficient ways to get the eight neighbors of a cell, e.g. nested list comprehension wins over explicit neighbor enumeration.


```python
i, j = 3, 4

# instead of
n = {(i+1,j),(i,j+1),(i-1,j),(i,j-1),(i-1,j-1),(i+1,j+1),(i-1,j+1),(i+1,j-1)}

# do
n = {(i+x,j+y)for x in(-1,0,1)for y in(-1,0,1)if x|y}
```

### Recoloring

When replacing all occurrences of a symbol in a grid with another, converting the grid to string, doing string replacement, and converting the result back to a grid using eval is cheaper than a nested list comprehension.


```python
g = [
    [1, 2, 3, 4],
    [5, 3, 4, 2]
]

# instead of
h = [[0 if e == 3 else e for e in r] for r in g]

# do
h = eval(str(g).replace(*'30'))
```

### Number Of Unique Symbols

When determining the number of unique symbols minus one (say, because the background color is not relevant), counting the unique characters after converting the grid to a string is cheaper than flattening.


```python
g = [
    [0, 0, 3, 4],
    [0, 2, 0, 0]
]

# instead of
n = len({*sum(g,[])})-1

# do
n = len({*str(g)})-5
```

### Copying A Grid

Rarely, a copy of a grid is needed, in which case converting to string and using eval is cheaper than a list comprehension.


```python
g = [
    [0, 0, 3, 4],
    [0, 2, 0, 0]
]

## instead of
h = [r[:]for r in g]

# do
h = eval(str(g))
```

### Keeping Only Rows With Non-Zero Symbols

Sometimes it is useful to filter out all rows which consist of only zeros, in which case filter with max is a cheap option.


```python
g = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1]
]

# instead of
h = [r for r in g if any(e>0 for e in r)]

# do
h = [*filter(max,g)]
```

### Upscaling A Grid

When upscaling a grid by a factor, a nested list comprehension with floor division is faster than a nested for loop.


```python
g = [
    [0, 0, 3],
    [0, 2, 0]
]
f = 3

# instead of
h = []
for i in range(len(g)):
    r = []
    for j in range(len(g[0])):
        r.extend([g[i][j]] * f)
    for _ in range(f):
        h.append(r[:])

# do
h = [[g[i//f][j//f] for j in range(len(g[0]) * f)] for i in range(len(g) * f)]
```
