# ***pyTableMaker***
**The library / module for python to allow programmers to create, edit and show tables without gui conveniently.**  
[![Run on Repl.it](https://repl.it/badge/github/windowsboy111/pyTableMaker)](https://repl.it/github/windowsboy111/pyTableMaker)

> Check out changelog at CHANGELOG.md  
> run example.py to check out how it performs!

---

# Info
There are 2 *editions* of pyTableMaker:
1. the one on github
2. the one on pypi

These 2 editions have difference between when importing, but other than that, there's not much difference.

Syntax of importing for **github edition**:
```py
import table
myTable = table.modernTable()
```
Syntax of importing for **pypi edition**:
```py
import pyTablemaker
myTable = pyTableMaker.modernTable()
```
Pretty simple, right?

---

# Usage
## Types of table
### modernTable
- double line, probably the most perfect-looking table
- formed with ╔ ═ ╗ ╦ ╠ ╣ ╬ ╚ ╝ ╩ ║
### classicTable
- for consoles with ASCII support only
- formed with + | -
### onelineTable
- similar to *modernTable* but with one line only, self explainatory
- formed with ┌ ─ ┐ ┬ ├ ┤ ┼ └ ┘ ┴ │
### customTable
- this is the base class of all other table classes (aka other are abstract)
- you can customize your table how it is formed using this class, self explainatory again
## creating a table
```py
t = modernTable(align='right',exp=True,linespacing=1) # please don't do linespacing it's ugly unless you need to
```
### parameters
- align="left" : str {"left","center","right"} (align the text for each column)
- exp=False : bool                             (Express mode allows you to stack up methods, see below ￬ )
- linespacing=0 : int                          (add a row on top and below a item / value)
### return
- table object
## express mode
You can turn on express mode when you initialize / declare the table. ￪ see above  
After turning on, you can stack up methods, and calling them once. all methods will return `self` in express mode except `get()`.
```py
t2 = classicTable(exp=True).new_column('id').table.new_column('name').table.new_column('price').table.new_column('note').rename('remarks').table\
    .new_column('description').table\
    .insert(0,'coke',          'A popular drink in brown color',   3.5,   'Need more, ppl keep buying, keep running out!')\
    .insert(1,'chips',         None,                               0xffff,"It comes from the space lol idk.")\
    .insert(2,'tea',           'Hot green tea i guess.',           5,     None)\
    .insert(3,'Cup noodles',   None,                               40,    'Need many cuz Corona Virus.')\
    .show(2) # you can specify how many rows to get as a argument. (0 is ignored) see below ￬
#   ~^~~~~~~  just a side note that there's a show() method so you don't need to do print(t.get()) ￬ see below.
```
## append a column
```py
col = t.new_column(name)
```
### parameters
- name : str
### return
- column object linked to the table object
## delete a column
```py
col.delete()
```
## rename a column
```py
col.rename(newColumnName)
```
### parameters
- newColumnName : str
## move a column
You can only move a column to the end (the most right hand side) of a table.
```py
col.moveToEnd()
```
## insert a row
```py
t.insert(v1,v2,v3)
t.insert(values)
```
### parameters
- v1, v2, v3... : any
- values : tuple
## print the table
```py
t.show(rowCount)
```
### parameters
- rowCount=0 : int (how many rows you want, default is 0 which shows all)
## get the table in string form
**IMPORTANT: t.get() method will always return the string form of the table even express mode is turned on!**
```py
result = t.get(rowCount)
```
### parameters
- rowCount=0 : int (how many rows you want, default is 0 which returns all)
### return
- result : str  
note: you can print the string form of table using `t.show()`. see above ￪
## number of rows in a table
```py
t.row
```