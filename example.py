from table import table
t = table()                     # init new table t
t.add_column('col1')            # add column named "col1" to t
t.add_column('col2')            # add column named "col2" to t
t.add_column('col3')            # add column named "col3" to t
t.insert(1,'a',1.1235)          # insert new row with value (1,     'a', 1.1235)
t.insert(2,'bc',3.14159)        # insert new row with value (2,     'bc',3.14159)
t.insert(11110,'d',9.00001)     # insert new row with value (11110, 'd', 9.00001)
print(t.get())                  # get table t in String and print out