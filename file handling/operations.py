import os 
filename = "data.txt" 
while True: 
   print("\nFile Operations Menu") 
   print("1. Read") 
   print("2. Write") 
   print("3. Append") 
   print("4. Delete") 
   print("5. Exit") 
   choice = input("Enter your choice (1-5): ") 
   if choice == '1': 
     if os.path.exists(filename): 
       with open(filename, 'r') as f: 
         print("\nFile Content:\n") 
         print(f.read()) 
     else:  
       print("File does not exist.") 
   elif choice == '2': 
     text = input("Enter text to write: ") 
with open(filename, 'w') as f: 
f.write(text) 
print("File written successfully.") 
elif choice == '3': 
text = input("Enter text to append: ") 
with open(filename, 'a') as f: 
f.write("\n" + text) 
print("Text appended successfully.") 
elif choice == '4': 
if os.path.exists(filename): 
os.remove(filename) 
print("File deleted successfully.") 
else: 
print("File not found.") 
elif choice == '5': 
print("Exiting program...") 
break 
else: 
print("Invalid choice. Please enter a number between 1 
and 5.") 
