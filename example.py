from table import *
t = modernTable()                       # init new table t
col1 = t.new_column('col1')             # add column named "col1" to t
col2 = t.new_column('col2')             # add column named "col2" to t
col3 = t.new_column('col3')             # add column named "col3" to t
col1.delete()                           # self-explainatory
col2.rename('wow')                      # rename column and move it to the end
col2.moveToEnd()                        # self-explainatory
t.insert('a',1.1235)                    # insert new row with value (1,     'a', 1.1235)
t.insert('bc',3.14159)                  # insert new row with value (2,     'bc',3.14159)
t.insert('d',9.00001)                   # insert new row with value (11110, 'd', 9.00001)
print(t.get())                          # get table t in String and print outg
print(t.data)                           # get the raw dictionary of the table.
print(t.row)                            # number of rows



t = classicTable()
id = t.new_column('id')
name = t.new_column('name')
price = t.new_column('price')
remarks = t.new_column('note')

remarks.rename('remarks')
description = t.new_column('desctription')
price.moveToEnd()
remarks.moveToEnd()

t.insert(0,'coke',          'A popular drink in brown color',   3.5,   'Need more, ppl keep buying, keep running out!') # in my country a can of coke is 3 dollars
t.insert(1,'chips',         None,                               0xffff,"It's come from the space lol idk.") # jk
t.insert(2,'tea',           'Hot green tea i guess.',           5,     None)
t.insert(3,'Cup noodles',   None,                               40,    'Need many cuz Corona Virus.')
print(t.get())