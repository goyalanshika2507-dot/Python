countries=("spain","italy","india","england","germany")
temp=list(countries)
temp.append("russia") #add item
temp.pop(3)  #remove item
temp[2]="finland"  #change item
countries=tuple(temp)
print(countries)

#methods in tuple
#tup.count()#it returns the number of times trhe given element appears in the tuple
#tup.index() #returns the first occurence of the given element
