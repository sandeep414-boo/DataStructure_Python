class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
        self.tail=None

    def push(self,value):
        newnode=node(value)
        if self.top is None:
            self.top=newnode
        else:
            self.top.next=newnode
            self.top=newnode

    def pop(self):
        if self.top is None:
            return ("Stack is empty")
        else:
            popnode=self.top
            self.top=self.top.next
            return popnode.data
    
    def peek(self):
        if self.top is None:
            return "empty"
        else:
            n1=self.top
            return n1.data
    def display(self):
        if self.top is None:
            print("Empty")
        else:
            p=self.tail
            

op=1
st=stack()
while(op):
    
    print("select the option")
    print("1.PUSH")
    print("2.POP")
    print("3.TOP")
    print("0.exit")
    op=int(input())
    
    if op==1:
        print("enter the value")
        value=int(input())
        st.push(value)
    elif op==2:
        print(st.pop())
    elif op==3:
        re=st.Top()
        print(re)
    else:
        quit()
        
