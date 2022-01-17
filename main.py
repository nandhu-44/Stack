# Stack Implementations!
# Push Stack
def push(stack):
    item=int(input("enter the item"))
    stack.append(item)
    top=len(stack)-1
#  Pop Stack
def pop(stack):
    if (stack)==[]:
        print('underflow')
    else:
     x=stack.pop()
     print('poped element is',x)
     if len(stack)==0:
              top=None
     else:
      top=len(stack)-1
# Peek(Top) Stack     
def peek(stack):
    if stack==[]:
       print('underflow')
    else:
     top=len(stack)-1
     print('peek is',stack[top])
# Display Stack    
def display(stack):
    if stack==[]:
       print('underflow')
    else:
        top=len[stack]-1
       for x in range(top-1,-1):
       print(stack[x])
      
stack=[]
top=None
print('Stack Operations!\n1 Push\n2 Pop\n3 Peek\n4 Display \n5 Exit\n')
While True:


  ch=int(input('enter your choice'))
  if ch==1:
       push(stack)
  elif ch==2:
       pop(stack)
  elif ch==3:
       peek(stack)
  elif ch==4:
       display(stack)
  elif ch==5:
          break;
  else:
     print('Please provide a valid choice!')
