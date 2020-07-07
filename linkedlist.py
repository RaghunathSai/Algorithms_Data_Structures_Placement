class Node:   #Each node consists of data and the link to next node
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList: #is the sinle linked list
    def __init__(self,count):
        self.head = None
        self.count = 0
    
    def insert_begin(self,data): #inserts the node at the beggining of the list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.count +=1
        
    def append(self,data):   #inserts the node at the end of the list
        new_node = Node(data)
        new_node.next = None
        if self.head == None:  #empty list
            self.head = new_node
          
        else:
            curr_node = self.head 
            while(curr_node.next):
              curr_node = curr_node.next
            curr_node.next = new_node
        self.count +=1
    
    def insert_before(self,data1,data2):   #inserts the node before a particular node data value
        new_node = Node(data2)
        new_node.next = None
        curr_node = self.head
        pre_node = self.head
        flag = 0
        while(curr_node):
            if(curr_node.data == data1):
                if(pre_node == self.head):
                    new_node.next = curr_node
                    self.head = new_node
                else:
                    new_node.next = curr_node
                    pre_node.next = new_node 
                print("Node with data {} is inserted".format(new_node.data))
                flag = 1
                self.count +=1
                break
            else:
                pre_node = curr_node
                curr_node = curr_node.next
        if(flag == 0):
            print("Node not found ")
        
    def delete_data(self,data):   #deletes a particular node from the list
        curr_node = self.head
        pre_node = self.head
        flag = 0
        while(curr_node):
            if(curr_node.data == data):
                if(pre_node == self.head):
                    self.head = curr_node.next
                else:
                    pre_node.next = curr_node.next 
                print("Node with data {} is deleted".format(curr_node.data))
                flag = 1
                self.count -=1
                break
            else:
                pre_node = curr_node
                curr_node = curr_node.next
        if(flag == 0):
            print("Node not found ")
           
    def printlist(self):   #prints the entire values in the list
        if self.head == None:
            print("Empty Node")
        else:
             curr_node = self.head
             while(curr_node):
               print(curr_node.data,end = " ")
               curr_node = curr_node.next
        print()
        print("Total no.of elements in the linked list are : {}".format(self.count))
        
if __name__ == '__main__':
    llist = LinkedList(0)
    llist.append(5)
    llist.append(6)
    llist.insert_begin(1)
    llist.printlist()
    llist.delete_data(1)
    llist.printlist()
    llist.insert_before(5,7)
    llist.printlist()
    

        
    
    
 




