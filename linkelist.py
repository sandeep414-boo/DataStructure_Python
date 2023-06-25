
class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None


        
    def insertAtBegin(self,value):
        newnode=node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode

            

            
    def insertAtEnd(self,value):
        newnode=node(value)
        if self.tail is None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode


            
    def insertAfterNode(self,value,data1):
        newnode=node(value)
        if self.head is None:
            print("the list is empty")
            self.head=newnode
            self.tail=newnode
        
        else:
            temp=self.head
            while temp.next is not None:
                if(temp.data==data1):
                    newnode.next=temp.next
                    temp.next=newnode
                    break
                #print(temp.data)
                temp=temp.next
            else:
                if temp.data==data1:
                    self.tail.next=newnode
                    self.tail=newnode
                else:
                    print("Give Node is not present")


                
    def insertBeforeNode(self,value,data1):
        newnode=node(value)
        if self.head is None:
            print("the list is empty")
            self.head=newnode
            self.tail=newnode
        elif self.head.data==data1:
            newnode.next=self.head
            self.head=newnode
            
        else:
            temp=self.head
            while temp.next is not None:
                if(temp.next.data==data1):
                    newnode.next=temp.next
                    temp.next=newnode
                    break
                #print(temp.data)
                temp=temp.next
            else:
                print('Given Node is not present')



    def insertAtPos(self,value,pos):
        newnode=node(value)
        count=1
        f=1

        if pos==0:
            if self.head is None:
                self.head=newnode
                self.tail=newnode
            else:
                newnode.next=self.head
                self.head=newnode
        else:
            temp=self.head
            while(temp.next is not None):
                if(pos==count):
                    newnode.next=temp.next
                    temp.next=newnode
                    f=0
                    break
                count+=1
                temp=temp.next
            else:
                self.tail.next=newnode
                self.tail=newnode
                
                    

    def deleteNode(self,value):
        if self.head is None:
            print("the List is Empty")
        elif self.head.data==value:
            self.head=self.head.next
            
        else:
            temp=self.head
            while temp.next.next is not None:
                if(temp.next.data==value):
                    p=temp.next
                    temp.next=p.next

                    break
                temp=temp.next
            else:
                if temp.next.data==value:
                    temp.next=None
                    self.tail=temp
                else:
                    print("Node is not Present")
                    
                    
                    
            
    
        
            
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print()
    def reverse(self):
        if self.head is None:
            print("Empty list")
        elif self.head.next is None:
            print(self.head.data)
        else:
            stack=[]
            temp=self.head
            while temp is not None:
                stack.append(temp.data)
                temp=temp.next
            temp=self.head
            while temp is not None:
                temp.data=stack.pop()
                temp=temp.next

            temp=self.head
            print("reverse list")
            while temp is not None:
                print(temp.data,end="->")
            
                temp=temp.next
    def reverse2(self):

        if self.head is None:
            print("empty")
        elif self.head.next is None:
            pass
        else:
            prev=None
            cur=self.head
            while(cur!=None):
                ne=cur.next
                cur.next=prev
                prev=cur
                cur=ne
            self.head=prev
            temp=self.head
            while temp is not None:
                print(temp.data,end="->")
                temp=temp.next
                
                
            
            
            
            



if __name__:
    list1=linkedlist()
    option=1
    while option:
        print("\nselect the option")
        print("1.insert at begining")
        print("2.display")
        print("3.insert at end")
        print("4.insert at after particular node")
        print("5.insert at before a particular node")
        print("6.insert at specified position")
        print("7.delete specified node")
        print("8.delete node at particular location")
        print("9.reverse a linked list")
        print("10.reverse without stack")
        
        print("0.exit")
        option=int(input())
        if option==1:
            print("enter the value")
            value=int(input())
            list1.insertAtBegin(value)
        elif option==3:
            print('Enter the value')
            value=int(input())
            list1.insertAtEnd(value)
        elif option==2:
            list1.display()
        elif option==4:
            print("enter the value")
            value=int(input())
            print("enter node")
            data1=int(input())
            list1.insertAfterNode(value,data1)
        elif option==5:
            print("enter the value")
            value=int(input())
            print("enter node")
            data1=int(input())
            list1.insertBeforeNode(value,data1)

        elif option==6:
            print("Enter the data")
            value=int(input())
            print("enter the position")
            pos=int(input())
            list1.insertAtPos(value,pos)
            
        elif option==7:
            print("Enter Node you want to delete")
            value=int(input())
            list1.deleteNode(value)
        elif option==8:
            pass
        elif option==9:
            list1.reverse()
        elif option==10:
            list1.reverse2()
            
        elif option==0:
            
            quit()














































eswwsCLASS
