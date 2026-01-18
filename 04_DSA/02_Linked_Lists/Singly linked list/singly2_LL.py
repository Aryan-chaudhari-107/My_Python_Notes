class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    
    def __init__(self):
        self.head = None

    def append(self, data):
        new_Node = Node(data)
        if self.head == None:
            self.head = new_Node
            return 
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next 
                
            currentNode.next = new_Node

    def display(self):
        if self.head == None:
            print("List is empty")
        else:
            currentNode = self.head
            while currentNode is not None:
                print(currentNode.data, end="->")
                currentNode = currentNode.next 
        
        print("None")    


    def insert_at(self, data, position):
        new_Node = Node(data)
        if position == 0:
            new_Node.next = self.head
            self.head = new_Node

        else:
            currentNode = self.head
            prevNode = None
            count = 0

            while currentNode is not None and count < position:
                prevNode = currentNode
                currentNode = currentNode.next
                count += 1

            new_Node.next = currentNode
            prevNode.next = new_Node    

        def delete_at(slef, data):
            temp = self.head
            if temp is not None:
                if temp.data == data:
                    self.head = self.head.next
                    del temp

            else:
                found = False
                prevNode = None
                while temp is not None:
                    if temp.data == data:
                        found = True
                        break
                    prevNode = temp
                    temp = temp.next 

                if found:
                    prevNode.next = temp.next 
                    del temp
                else:
                    print("Node Not Found")