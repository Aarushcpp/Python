Modules

They are basically used to borrow someone else's code.Modules contain someone else's code.Basically when making new work assume you want a program which gives you geometric mean of 10 numbers we dont have to write each and 
everything program we can use someone else's code who has done this and documented it for our use.That code is written in modules and we can use that code that function without knowing it's implementation without writing it's code
we can simply use it.
2 types of modules
1.Built-In Modules-They are installed when we download Python.
2.External Modules-They can be imported in your program/pc using pip.
pip3 install pandas-Python Pandas library.
downloads packages/libraries from internet to python interpreter.

  
Module is like a code library which can be used to borrow code written by somebody else in our python program. There are two types of modules in python:

Built in Modules - These modules are ready to import and use and ships with the python interpreter. there is no need to install such modules explicitly.
External Modules - These modules are imported from a third party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of a same module with time.
The pip command

It can be used as a package manager pip to install a python module. Lets install a module called pandas using the following command

pip install pandas
Using a module in Python (Usage)

We use the import syntax to import a module in Python. Here is an example code:

import pandas
# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df) # This will display first few rows from the words.csv file
