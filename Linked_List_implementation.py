#Singly Linked List Structure
class Node:
    def __init__(self,value):
        self.data = value
        self.add = None
       
       
class LinkedList():
    
    # Head/Root node
    def __init__(self):
        self.start = None
    
    #Linked List element creation
    def create_list(self):
        n = int(input("enter no of nodes :  "))
        if n==0:
            return
        for i in range(n):
            data = int (input("Enter the element to be inserted : "))
            self.insert_end(data)
            
    #   Display of the Linked List
    def display(self):
        if self.start = None:
            print("Empty List")
            return
        else:
            print("List is : ")
            p = self.start
            while p != None: 
                print(p.data, " ", end=" ")
                p = p.add
            print()
    
    # Counting the nodes of Lindked List
    def count_node(self):
        p = self.start
        count = 0
        while p != None:
            count+=1
            p = p.add
        print("Number of nodes in the list = ", count)
    
    # For searching an element in the Linked List
    def search(self,x):
        pos = 1
        p=self.start
        while p != None:
            if p.data == x:
                print(x, "is at position ", pos)
                return True
            pos+=1
            p = p.add
        else:
            print(x, " is not found")
            return False
    
    # For inserting an element at the beginning
    def insertion_begin(self,data):
        temp = Node(data)
        temp.add = self.start
        self.start = temp
    
    # For inserting an element at the end    
    def insert_end(self,data):
        temp = Node(data)
        if self.start = None:
            self.start = temp
            return
        
        p = self.start
        while p.add != None:
            p = p.add
        p.add = temp
    
    # For inserting an element at the K position                
    def insert_pos(self,data,k):
        if k==1:
            temp = Node(data)
            temp.add = self.start
            self.start = temp
            return
        p = self.start
        i = 1
        while i <k-1 and p != None:
            p = p.add
            i+=1
        
        if p = None:
            print("You can insert upto position ", i)
        else:
            temp = Node(data)
            temp.add = p.add
            p.add = temp
    
    # For deleting an element by taking element's value        
    def deletion(self,x):
        if self.start = None:
            print("List is empty")
            return
        
        # if head node is only there
        if self.start.data == x:
            self.start = self.start.add
            return
        
        p = self.start
        while p.add != None:
            if p.add.data==x:
                break
            p = p.add
            
        if p.add = None:
            print("Element ", x , "not in the list")
        else:
            p.add = p.add.add

list = LinkedList()
list.create_list()

while True:
    print("1. Display List")
    print("2. Count the nodes")
    print("3. Search for an element")
    print("4. Insertion at beginning")
    print("5. Insertion at end")
    print("6. Insertion at a position")
    print("7. Delete the node by given element value")
    print("8. Exit")
    
    option = int (input("Enter your choice :: "))
    
    if option == 1:
        list.display()
    elif option == 2:
        list.count_node()
    elif option == 3:
        data = int(input("Enter the element you want to search "))
        list.search(data)
    elif option == 4:
        data = int(input("Enter the element you want to insert "))
        list.insertion_begin(data)
    elif option == 5:
        data = int(input("Enter the element you want to insert "))
        list.insert_end(data)
    elif option == 6:
        data = int(input("Enter the element you want to insert "))
        x = int(input("Enter the element after which you want to insert "))
        list.insert_pos(data,x)
    elif option == 7:
        data = int(input("Enter the element you want to delete "))
        list.deletion(data)
    elif option == 8:
        break
    else:
        print("Wrong option entered")
    print()
