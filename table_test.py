from table import customTable
print(customTable(['+','-','+','+','+','-','+','+','+','-','+','+','|'],align='center',linespacing=1,exp=True) \
    .new_column('column 1').table.new_column('column 2').table.insert('row 1','col 2').get())