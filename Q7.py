myList = ['text', 'another text', '1', '2.980', '3']
output = [ a for a in myList if a.isnumeric() ]
print( output )