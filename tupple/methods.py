countries=("spain","italy","india","england","germany")
temp=list(countries)
temp.append("russia") #add item
temp.pop(3)  #remove item
temp[2]="finland"  #change item
countries=tuple(temp)
print(countries)

#methods in tuple
#count()#it returns the number of times the given element appears in the tuple or to find the frequency
#index() #returns the first occurence of the given element
#len()#total counting of elements
#min()&max() to find min and max value
#index(item) index of existing elements at first occurence
#tuple() use to create tuples from different types of values
     # we can create empty tupple(),create tuple from list([1,2,3]),create tupple from string as- tuple("xyz"), create from key of dictionary-tuple({1:"m",2:"n"})
