from table import modernTable


t = modernTable(cellwrap=10, linespacing=1)
col = t.new_column('hi bro what\'s up? ha ha ha!')
col1 = t.new_column('ahhhhhhh :)')
t.insert('ahhhhhhhhhhhhh', "yes you get it right, finally!")
t.insert('a', 34567)
t.show()
