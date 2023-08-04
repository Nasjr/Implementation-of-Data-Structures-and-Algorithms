import ctypes
class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.arr = self.make_arr(self.capacity)
    def make_arr(self,capacity:int):
        return (capacity * ctypes.py_object)()
    def __len__(self):
        #Length of arr
        return self.n
    def __getitem__(self,k):
        #Return item at K index
        if k < 0 and k > self.n:
            return IndexError('K is out of bounds !')
        return self.arr[k]
    def append(self,elem):
        if self.n == self.capacity:
            self.resize(self.capacity*2)
        self.arr[self.n] = elem
        self.n+=1
    def resize(self,new_capacity):
        tmp_arr= self.make_arr(new_capacity)
        for i in range(self.n):
            tmp_arr[i] = self.arr[i]
        self.arr = tmp_arr
        self.capacity = new_capacity
    def insert_At(self,pos,elem):
        if pos < 0 or pos > self.n:
            print('index not correct')
            return
        if self.n == self.capacity:
            self.resize(self.capacity*2)
        
        for i in range(self.n-1,pos-1,-1):
            #Shift the array from left to right to the index
            self.arr[i] = self.arr[i+1]
        #insert element
        self.arr[pos] = elem
        self.n+=1
    def delete(self):
        if self.n == 0:
            print('Cannot delete from an empty array')
        self.arr[self.n-1] = 0
        self.n -= 1
    def remove_At(self,pos):
        if self.n == 0:
             print('Cannot remove from an empty array')
        if pos < 0 or pos >= self.n:
            return IndexError("Index out of bound....deletion not possible")
        if pos == self.n:
            self.arr[pos] = 0
            self.n-=1
            return
        self.arr[pos] = 0
        for i in range(pos,self.n-1):
            self.arr[i] = self.arr[i+1]
        self.arr[self.n-1] = 0
        self.n-=1
    

arr=DynamicArray()
arr.append(10)
arr.append(20)
arr.append(3)
arr.capacity=2


