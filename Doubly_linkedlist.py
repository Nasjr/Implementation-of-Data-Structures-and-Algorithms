class Node():
    def __init__(self,data=None,prev=None,next=None) :
        self.data = data
        self.next = next
        self.prev = prev
class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None
    def insert_at_start(self,data):
        # Create a node it's next pointer is the current start
        if self.head == None:

            node=Node(data,self.head,self.head)
            # The current start is now this node 
            self.head = node
        else:
            node=Node(data,None,self.head)
            self.head.prev = node
            self.head = node
    def print_forward(self):
        # This method prints list in forward direction. Uses node.next
        if self.head == None:
            print("Empty linked list nothing to print")
            return
        itr = self.head
        llforward=''
        while itr:
            llforward+= str(itr.data) + '-->'
            itr = itr.next
        print(llforward)
    
    def get_tail(self):
        if self.head == None:
            print("Empty Linked list")
            return
        itr = self.head
        count=0
        while itr.next:
            count+=1
            itr = itr.next
        return itr
    def get_len(self):
        if self.head == None:
            print("Empty Linked list")
            return
        itr = self.head
        count = 0 
        while itr:
            count+=1
            itr = itr.next
        return count
    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data,self.head,self.head)
            return
        last_elem = self.get_tail()
        last_elem.next = Node(data,self.get_tail(),None) 
    def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.    
        if self.head == None:
            print("Empty linked list nothing to print")
            return
        itr = self.get_tail()
        llbackword = ''
        while itr != None:
            llbackword += str(itr.data) +'-->'
            itr = itr.prev
        print(llbackword)
    def insert_at(self,index,data):
        if index == 0:
            self.insert_at_start(data)
        if index < 0 or index > self.get_len():
            raise Exception("Invalid Index")
        itr = self.head
        count = 0
        while itr:
            if index-1 == count :
                itr.next = Node(data,itr,itr.next)
            itr= itr.next
            count+=1
        return
    def remove_at(self,index,data):
        if self.head == None:
            print("Cannot remove from empty linked list")
        if index < 0 or index > self.get_len():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            self.head.next.prev = None
        

        itr = self.head
        count = 0
        while itr:
            if index == count :
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
                
            count+=1
            itr = itr.next
        return
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

dll=DoublyLinkedList()
dll.insert_at_end(30)
dll.insert_at_end(20)
dll.insert_at_end(4)
dll.insert_at_end(2)
dll.insert_at_end(10)
dll.insert_at_end(10)
dll.remove_at(3,10)
dll.print_forward()