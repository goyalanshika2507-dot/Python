s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))#prints all items present in set but will not repeat the numbers
s1.update(s2)#it will add all numbers to s1
print(s1,s2)
print(s1.intersection(s2))#print common elements
#symmetric- it gives the elements which are not common
#difference- it only give elememnts from set1 which are not common to set2

#inbuilt methods
#isdisjoint- no intersection
#issuperset- is the value of set2 present in set1
#issubset- is the value of set1 present in set2
s1.remove(s2)#remove an item
s1.pop(s2)#remove last item
#s1.del(s2)#it is not a method it is a keyword
s1.clear(s2)#clear all items in set and print empty set
