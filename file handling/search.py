#txt file
# f = open("data.txt", "w")
# f.write("10 20 30 40 50")
# f.close()

# f = open("data.txt", "r")
# data = f.read().split()
# f.close()

# x = input("Enter element to search: ")

# if x in data:
#     print("Element Found")
# else:
#     print("Element Not Found")


# #binary file
# import pickle

# f = open("data.dat", "wb")
# pickle.dump([10, 20, 30, 40, 50], f)
# f.close()

# f = open("data.dat", "rb")
# data = pickle.load(f)
# f.close()

# x = int(input("Enter element to search: "))

# if x in data:
#     print("Element Found")
# else:
#     print("Element Not Found")

#csv file
import csv

f = open("data.csv", "w", newline="")
w = csv.writer(f)
w.writerow(["10"])
w.writerow(["20"])
w.writerow(["30"])
w.writerow(["40"])
w.writerow(["50"])
f.close()

f = open("data.csv", "r")
r = csv.reader(f)

x = input("Enter element to search: ")
found = False

for row in r:
    if x == row[0]:
        print("element found")
    else:
        continue

f.close()

# if found:
#     print("Element Found")
# else:
#     print("Element Not Found")