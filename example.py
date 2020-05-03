from table import *
t1 = modernTable()                       # init new table t (in this situation the type is modernTable)
col1 = t1.new_column('col1')             # add column named "col1" to t
col2 = t1.new_column('col2')             # this method will return a column object
col3 = t1.new_column('col3')             # to get the table of the column, use col.table or col.getTable()
col1.delete()                            # self-explainatory
col2.rename('wow')                       # rename column and move it to the end
col2.moveToEnd()                         # self-explainatory
t1.insert('a',1.1235)                    # insert new row with values
t1.insert('bc',3.14159)                  # Specifying the type of values is not needed
t1.insert('d',9.00001)                   # all values will be converted to string
print(t1.get())                          # get table t in String and print out
print(t1.data)                           # get the raw dictionary of the table.
print(t1.row)                            # number of rows



# express mode (exp for short) is a mode that allows you to stack all the methods into a single statement.
# to enable express mode, add a kwargs called 'exp' and set it to True:
t2 = classicTable(align='right',exp=True)\
    .new_column('id').table\
    .new_column('name').getTable()\
    .new_column('price').table\
    .new_column('note').rename('remarks').table\
    .new_column('description').table\
    .insert(0,'coke',          'A popular drink in brown color',   3.5,   'Need more, ppl keep buying, keep running out!')\
    .insert(1,'chips',         None,                               0xffff,"It comes from the space lol idk.")\
    .insert(2,'tea',           'Hot green tea i guess.',           5,     None)\
    .insert(3,'Cup noodles',   None,                               40,    'Need many cuz Corona Virus.')\
    .show() # just a side note that there's a show() method so you don't need to do print(t.get())
print(t2)
print(repr(t2))



t3 = onelineTable(align='center')                   # by default align is 'left', you can specify it with 'right' or 'center'
time = t3.new_column('Time')
event = t3.new_column('Event')
remarks = t3.new_column('Remarks')

remarks.rename('Note')
t3.insert('11:00','Brunch','I ate a cookie and a cup noodle which costs 40 dollars to buy at home.')
t3.insert('13:00','Coding','That\'s my hobby, right?')
t3.insert('15:55','Do hw', 'Annoying mum asks me to do hw :(')
t3.insert('19:30','Dinner','Nice curry ;)')
print(t3.get())
print()
print(lib_info)                                     # info about the library ;)