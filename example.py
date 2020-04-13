from table import *
t1 = modernTable()                       # init new table t
col1 = t1.new_column('col1')             # add column named "col1" to t
col2 = t1.new_column('col2')             # add column named "col2" to t
col3 = t1.new_column('col3')             # add column named "col3" to t
col1.delete()                            # self-explainatory
col2.rename('wow')                       # rename column and move it to the end
col2.moveToEnd()                         # self-explainatory
t1.insert('a',1.1235)                    # insert new row with value (1,     'a', 1.1235)
t1.insert('bc',3.14159)                  # insert new row with value (2,     'bc',3.14159)
t1.insert('d',9.00001)                   # insert new row with value (11110, 'd', 9.00001)
print(t1.get())                          # get table t in String and print outg
print(t1.data)                           # get the raw dictionary of the table.
print(t1.row)                            # number of rows




t2 = classicTable()
id = t2.new_column('id')
name = t2.new_column('name')
price = t2.new_column('price')
note = t2.new_column('note')

note.rename('remarks')
description = t2.new_column('desctription')
price.moveToEnd()
note.moveToEnd()

print(t2)
print(str(repr(t2)))

t2.insert(0,'coke',          'A popular drink in brown color',   3.5,   'Need more, ppl keep buying, keep running out!') # in my country a can of coke is 3 dollars
t2.insert(1,'chips',         None,                               0xffff,"It's come from the space lol idk.") # jk
t2.insert(2,'tea',           'Hot green tea i guess.',           5,     None)
t2.insert(3,'Cup noodles',   None,                               40,    'Need many cuz Corona Virus.')
print(t2.get())




t3 = onelineTable()
time = t3.new_column('Time')
event = t3.new_column('Event')
remarks = t3.new_column('Remarks')

remarks.rename('Note')
t3.insert('11:00','Brunch','I ate a cookie and a cup noodle which costs 40 dollars to buy at home.')
t3.insert('13:00','Coding','That\'s my hobby, right?')
t3.insert('15:55','Do hw', 'Annoying mum asks me to do hw :(')
t3.insert('19:30','Dinner','Nice curry ;)')
print(t3.get())