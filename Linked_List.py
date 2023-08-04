class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList():
    def __init__(self):
        self.head = None
    def insert_at_start(self,data):
        # Create a node it's next pointer is the current start
        node=Node(data,self.head)
        # The current start is now this node 
        self.head = node
    def print_ll(self):
        if self.head == None:
            print("Cannot print empty linked list")
            return
        itr = self.head
        llstr = ""
        while itr != None:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)
    def insert_at_end(self,data):
        # Case ll is empty 
        if self.head == None :
            self.head = Node(data,None)
            return
        # Case it is not empty traverse untill the last itr
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    def get_len(self):
        count=0
        if self.head == None :
           print("Linked list is empty")
           return
        itr = self.head
        while itr:
            itr=itr.next
            count+=1
        return count
    def insert_at(self,index,data):
        if index < 0 or index > self.get_len():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_start(data)
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
        


    def remove_at(self,index,data):
        if index < 0 or index > self.get_len():
            raise Exception("Invalid index")
        if self.get_len() == 0:
            print("Cannot remove from empty list")
            return
        if index == 0:
            self.head = self.head.next

        itr=self.head
        count=0
        while itr:
            if count == index - 1 :
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1

    def insert_values(self,list_values):
        self.head = None
        for val in list_values:
            self.insert_at_end(val)
    def insert_after_value(self,value,data):
        if self.head == None:
            print("No values in the linked list to insert after")
            return
        itr = self.head
        while itr:
            if value == itr.data:
                print(itr.data)
                itr.next = Node(data,itr.next)
                return
            itr = itr.next
        print("Value was not found")
    def remove_by_value(self,value):
        if self.head == None:
            print("Cannot Remove from empty linked list")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        itr = self.head
        while itr:
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next

                

ll=LinkedList()
ll.insert_values([1,2,3,4,5,6])
ll.print_ll()
ll.insert_after_value(7,7)
ll.print_ll()


        