# Exercise 1 - Tried to add as much information to each line as I could to better understand what was actually happening. 
# Though it looks very close to the code that we practiced above, I still felt that this exercise was helpful
# so that I could start grasping what was actually happening on each line along with what was going on as a whole.

class Node:                                            # Create Node class to hold all methods that we'll call later within our LinkedList class
    def __init__(self,value):                      
        self.value = value
        self.next = None
        
class LinkedList:                                      # Create LinkedList class which will hold all methods (__init__, pushOn, insertAfter, append, traverse)
    def __init__(self):
        self.head_node = None                          # Initial header or starting node is set to none. Will be replaced later on
    
    def pushOn(self,new_value):                        # PushOn will add node to the front of the LinkedList vs append (coming later) will add to the end of the LinkedList
        new_node = Node(new_value)                     # Pull node class and create new node value 
        new_node.next = self.head_node
        self.head_node = new_node
        
    def insertAfter(self, previous_node, new_value):   # This will create a Node in a certain space within the Linked List which will place it after a specified value
        if previous_node is None:                      # Does the previous node exist?
            return                                     # If not, nothing happens
        new_node = Node(new_value)                     # If it does, a new node will be created
        new_node.next = previous_node.next             # Previous node points to new node
        previous_node.next = new_node
    
    def append(self,new_value):                        # Append will add node to the back or end of the Linked List
        new_node = Node(new_value)                     # Pull node class and create new node value
        if self.head_node is None:                     # Is the list empty?
            self.head_node = new_node                  # If yes, use this new_node value as the official "head"
        last = self.head_node
        while last.next:                               # loop until we find a none value for next pointer
            last = last.next
        last.next = new_node                           # Change current last node value to point at new node
        
    def traverse(self):
        temp = self.head_node
        while temp is not None:                        # keep looping thru the links until you reach a none value
            print(temp.value)
            temp=temp.next
            
        
weekdays_links = LinkedList()

weekdays_links.pushOn("Mon")                           # Pushing "Mon" Node onto the front/beginning of the Linked List
weekdays_links.append("Tue")                           # Appending "Tue" Node on to the Linked List
weekdays_links.insertAfter(weekdays_links.head_node.next, "Wed") # Inserting "Wed" node after the node that is after the head node
weekdays_links.traverse()                              # Traversing through the entire Linked List until there is no value (After "Wed"))

# Exercise 2 - Ran into trouble lower in the BST (See Notes)

class BST:                                                  # Create BST (Binary Search Tree) class that identifies the left and right values as None to start
    def __init__ (self,value):
        self.value = value                                  # Value given
        self.left = None                                    # Left starts as None
        self.right = None                                   # Right starts as None
        
    def insert(self, value):                                
        if value < self.value:
            if self.left is None:                           # If the left is empty or None
                self.left = BST(value)                      # We will insert the value that is less than the original value on that left side
            else:
                self.left.insert(value)                     # Otherwise we will look at the existing value and check if it's less than that. If it is, we add it to the left of that value
        else:                                               # If this is greater than, we'll head down the right side
            if self.right is None:                          # If the right is empty or None
                self.right = BST(value)                     # We will insert the value that is more than the original value on that right side
            else:
                self.right.insert(value)                    # Otherwise we will look at the existing value and check if it's greater than that. If it is, we add it to the right of that value
        return self
    
    def contains(self,value):                                
        if value < self.value:                              # if the value that is passed is is less than current value...
            if self.left is None:                           # if the value is none. We'll say that it is not in there, or False
                return False
            else:
                return self.left.contains(value)            # we will continue to check each node to see if the passed in value is greater than or less than the current value
        elif value > self.value:                            
            if self.right is None:                          # Like above, if there is nothing there, we will return false (does not exist)
                return False
            else:
                return self.right.contains(value)
        else:
            return True                                     # if it ends up being there after doing checks on each individual node, we will print that it is there, or True.
        
    def getMinValue(self):                                  # This function is built to find the value that is most left, or smallest in terms of value
        if self.left is None:                               # If there is nothing left of that
            return self.value                               # return that value as the min
        else:
            return self.left.getMinValue()                  # otherwise, keep doing that on each individual node until there is nothing to the left
    
    def getMaxValue(self):                                  # This function is built to find the value that is most right, or largest in terms of value
        if self.right is None:                              # If there is nothing right of that
            return self.value                               # return that value as the max
        else:
            return self.right.getMaxValue()                 # otherwise, keep doing that on each individual node until there is nothing to the right
        
    def remove(self, value, parent=None):                   # function to remove a value from the tree while not taking out the entire section of the tree
        if value < self.value:                              # If the vlue is less than the value we're looking at
            if self.left is not None:                       # 
                self.left.remove(value, self)               # 
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value,self)
                
        ##### HERE IS THE POINT WHERE I BEGAN TO GET PRETTY CONFUSED AT WHAT WE WERE ACTUALLY DOING WITH THE CODE #####  
        ##### Conceptually, I get that this is checking every node and then if it removes a value it is
        ##### going to update the pointer to be pointing at the correct or new parent value. I'm just not
        ##### entirely sure exactly where those are happening below in the code. I see that when the node is removed,
        ##### that we are then reassigning a parent value to the node that would be below that if it had a value below it.
        ##### The rest of the code I can actually tell what it's doing, this is where I was running into an issue (Below)
        ##### from a syntax standpoint. Wanted to make sure I got this in at the beginning of class on Tuesday for submission.
    
                
#        else:
#            if self.left is not None and self.right is not None:
#                self.value = self.right.getMinValue()
#                self.right.remove(self.value, self)
#            elif parent is None:                            
#                if self.left is not None:
#                    self.value = self.left.value
#                    self.left = self.right.left
#                    self.right = self.left.left
#                elif self.right is not None:
#                    self.value = self.right.value
#                    self.left = self.right.left
#                    self.right = self.right.right
#                else:
#                    self.value = None
#            elif parent.left == self:
#                parent.left = self.left if self.left is not None else self.right
#            elif parent.right == self:
#                parent.right = self.left if self.left is not None else self.right
#        return self
    
    
#bst_example = BST(39)
#bst_example.insert(40)
#bst_example.insert(50)
#print(bst_example.getMaxValue())
#print(bst_example.contains(40))
#bst_example.remove(40)
#print(bst_example.contains(40))
    