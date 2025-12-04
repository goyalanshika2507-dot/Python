a=input("enter string")
vowels="aeiouAEIOU"
space=" "
symbols="!@#$%^&*()_+:<>?{}|[];',./'"
vowels_count=0
consonants_count=0
space_count=0
symbol_count=0
for ch in a:
    if ch in vowels:
        vowels_count+=1
    elif ch in space:
        space_count+=1
    elif ch in symbols:
        symbol_count+=1
    else:
        consonants_count+=1
print("total vowels",vowels_count)
print("total consonants",consonants_count)
print("space",space_count)
print("symbols",symbol_count)
