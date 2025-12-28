# n=int(input("enter number"))
# count=0
# i=1
# while n>=i:
#     if n%i==0:
#         count=count+1
#     i=i+1
# if count==2:
#    print("prime number")
# else:
#     print("not a prime number") 
 #pen the input file in read mode
file1 = open("input.txt", "r")

text = file1.read()
file1.close()

# Convert text to lowercase and split into words
words = text.lower().split()

# Dictionary to store word frequency
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Open output file in write mode
file2 = open("output.txt", "w")

for word, count in word_count.items():
    file2.write(word + " : " + str(count) + "\n")

file2.close()

print("Word frequency written to output.txt")