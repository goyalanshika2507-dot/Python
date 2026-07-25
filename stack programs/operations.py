stack=[]
def push():
    element=input("enter element to push:")
    stack.append(element)
    print("element pushed")
def pop():
    if not stack:
        print("stack is empty")
    else:
        print("popped element:",stack.pop())
def peek():
    if not stack:
        print("stack is empty")
    else:
        print("top element",stack[-1])
def display():
    print("stack elements",stack)
while True:
    print("\n1.push 2.pop 3.peek 4.display 5.exit")
    choice=int(input("enter the choice"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        peek()
    elif choice==4:
        display()
    elif choice==5:
        break
    else:
        print("invalid choice")
    