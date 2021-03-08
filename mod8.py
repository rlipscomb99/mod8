Python 3.8.7 (v3.8.7:6503f05dd5, Dec 21 2020, 12:45:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=a
>>> print id(a), id(b)
SyntaxError: invalid syntax
>>> print (a), (b)
5
(None, 5)
>>> print (b)
5
>>> c=b
>>> b=3
>>> print a,b,v
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(a,b,v)?
>>> print (a,b,c)
5 3 5
>>> b=a
>>> b=5
>>> print (a,b)
5 5
>>> import re
>>> re.compile(r'A', re.I)
re.compile('A', re.IGNORECASE)
>>> p=re.compile(r'A', re.I)
>>> p.match("A mind is a terrible thing to waste.")
<re.Match object; span=(0, 1), match='A'>
>>> p.match("abcd")
<re.Match object; span=(0, 1), match='a'>
>>> p.match("Hello,Alice!")
>>> p=re.compile(r'[1-9][0-9]*')
>>> p.search("My office number is 205A.")
<re.Match object; span=(20, 23), match='205'>
>>> p.search("11:00 to 12:15 is our class time.")
<re.Match object; span=(0, 2), match='11'>
>>> p.search("Python regular expressions are neat!")
>>> open ('airline-saftey.csv','r')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    open ('airline-saftey.csv','r')
FileNotFoundError: [Errno 2] No such file or directory: 'airline-saftey.csv'
>>> open ('/Users/rebeccalipscomb/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Python/airline-safety.csv','r')
<_io.TextIOWrapper name='/Users/rebeccalipscomb/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Python/airline-safety.csv' mode='r' encoding='UTF-8'>
>>> import copy
>>> print (reader.read())
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print (reader.read())
NameError: name 'reader' is not defined
>>> import reader
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    import reader
ModuleNotFoundError: No module named 'reader'
>>> print(reader.read(5))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(reader.read(5))
NameError: name 'reader' is not defined
>>> names={"Air Canada"}
>>> names2=names
>>> names2.add("Air France")
>>> names2.add("Korean Air")
>>> import itertools
>>> for i in chain ([1,2,3],['a','b','c']):
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> print(i)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(i)
NameError: name 'i' is not defined
>>> for i in chain ([1,2,3],['a','b','c']):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    for i in chain ([1,2,3],['a','b','c']):
NameError: name 'chain' is not defined
>>> for i in itertools.repeat("hi",5):
	print (i)

	
hi
hi
hi
hi
hi
>>> for i in itertools.cycle([5,6,7,8]):
	print (i)
	counter=0
	counter=counter+2
	if counter > 10
	
SyntaxError: invalid syntax
>>> if counter>10:
	break
SyntaxError: 'break' outside loop
>>> for i in itertools.cycle([5,6,7,8]):
	print (i)
	counter=0
	counter=counter+1
	if counter > 10:
		break

	
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8

5
6
7
8
5
6
7
8
5
6

7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
n6
7
8
5
6
n7
8
5
6
n7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
b7
8
r5
e6
7
8
5
a6
7
8k
5
6
7

8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7

8
5
6
7
8
5
6

7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8

6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
6
7
8
5
Traceback (most recent call last):
  File "<pyshell#55>", line 2, in <module>
    print (i)
KeyboardInterrupt
>>> itertools.count(start=0, step=2)
count(0, 2)
>>> for i in itertools.count(0,5):
	print (i)
	if i > 50:
		break

	
0
5
10
15
20
25
30
35
40
45
50
55
>>> count(1,10)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    count(1,10)
NameError: name 'count' is not defined
>>> 