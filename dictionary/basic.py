# syntax-
# len()#len(dict_name)
# get()#dict.get(key,[default])
# items()#dict_name.items()
# keys()#dict_name.keys()
# values()#dict_name.values()
# fromkeys()#dict.fromkeys(<key sequence>,[<value>])
# setdefault()#dict_name.setdefaullt(<key>,<value>)
# update()#dict_name.update(dict_name2)
# pop()#dict_name.pop(<key>)
# popitem()#dict_name.popitem()
# clear()#dict_name.clear()
# sorted()#sorted(dict_name)
# sum()#sum(dict_name)


def dictionary():
    d={1:'a',2:'B',3:'c'}
    print(len(d))
    print(d.get(1))
    print(d.keys())
    print(d.values())
    #d2=dict.fromkeys([1,2,3,4,5],5)
    d2=dict.fromkeys([1,2,3,4,5],[5,1,2,4,5])#by this the keys i.e 1,2,3,4,5 will seperately store the common value i.e [5,1,2,4,5]
    print(d2)
    d.setdefault(1,'A')
    print(d)
    d3={1:'A',2:'B',3:'c'}
    d.update(d3)# whatever in d3 will be copied in d
    print(d)
    print(d3)
    #same
    d3=d2.copy()
    d4={}
    print("copy",d3)
    print(d3.pop(5))
    print(d.popitem())
    d4.clear()
    print(d4)
    sorted(d)
    print(d)
    print(max(d))
    print(min(d))
    print(sum(d))
dictionary()
