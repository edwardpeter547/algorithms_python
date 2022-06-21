class Node:
    # An object for storing a single node of a linked list
    data = None
    # 
    next_node = None
    
    def __init__(self, data):
        self.data = data
        
    
    
    def __repr__(self): 
        return f"<Node data: %s" %self.data
    
 
   
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    
    def is_empty(self):
        return self.head == None    
    
    
    def size(self):
        
        current = self.head
        count = 0
        
        while current != None:
            count += 1
            current = current.next_node
            
        return count
    
    def add_node(self, data):
        new_node = Node(data)
        new_node.next_node = self.head #type: ignore
        self.head = new_node
        
    
    def __repr__(self):
        
        nodes = []
        current = self.head
        
        
        while current:
            
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            
            elif current.next_node == None:
                nodes.append(f"[Tail: {current.data}]")
            
            else:
                nodes.append(f"[{current.data}]")
                
            current = current.next_node
        
        return str('-->'.join(nodes))
    
    
    def find(self, data):
        
        
        if self.is_empty():
            return None
        
        current = self.head
        
        while current:
            
            if current.data == data:
                return current
            else:
                current = current.next_node           
                
        return None
    
    
    def insert(self, index, data):
        
        if index == 0:
            self.add_node(data)
            
        
        if index > 0:  
            new_node = Node(data)
            position = index   
            current = self.head
            
            while position > 1 :
                current = current.next_node #type: ignore
                position -= 1
                
            prev_node = current
            next_node = current.next_node #type: ignore
            
            prev_node.next_node =  new_node   #type: ignore
            new_node.next_node = next_node     
            
    
    def remove(self, key):
        
        current = self.head
        previous = None
        found = False
        
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node  #type: ignore
            else:
                previous = current
                current = current.next_node
        
          
            