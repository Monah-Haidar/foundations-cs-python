def displayMenu():
    print("""
          1. Singly Linked List
          2. Check if Palindrome
          3. Priority Queue
          4. Evaluate an Infix Expression
          5. Graph
          6. Exit
          """)


def displayLinkedListMenu():
    print("""
          a. Add Node
          b. Display Nodes
          c. Search for & Delete Node
          d. Return to main menu
          """)

class Node:
    def __init__(self, info):
        self.info = info
        self.next  = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def addNode(self, data, index):
        new_node = Node(data)
        
        if index == 0:
            # Insertion happens at the begining of the linked list
            if self.head is None:
                # List is empty
                self.head = new_node
                self.size += 1
                
            else:
                # List is not empty
                new_node.next = self.head    # new node points to head
                self.head = new_node         # head became the new node
                self.size += 1
                
        elif index == (self.size - 1):
            # Insert node end of linked list
            
            # set current node to head
            current_node = self.head
            
            # iterate over linked list to find the last node
            while current_node.next:
                current_node = current_node.next
                
            # Current node is the last node , current node .next points to None 
            # Therefore, current_node.next points to the newly added node which in turn will point to None
            current_node.next = new_node
            
            self.size += 1
        
        else:
            # Add search for indexed node and add it in its place 
            
            # variable that keeps track of node index
            pos = 0 
    
            while not (current_node == None and pos+1 == index):
                # increment pos and current_node until we reach the node before the specified index or we reach end of list (current_node == None)
                pos+=1
                current_node = current_node.next
                
            if current_node != None:
                # Add node
                new_node.next = current_node.next    # assign the pointer of the new node to the pointer of the current node (the node we want to insert the new node in) 
                current_node.next = new_node         # assign the pointer the current node to the newly added node
                self.size +=1
                
            else:
                print("Index not available")
    
    
    def displayNodes(self):
        # Iterate of the nodes of the linked list and display their values
        if self.size == 0:
            print("List is empty")
        else:
            current_node = self.head
            while current_node.next != None:
                print(current_node.info)
                # Increment current_node because its a while loop
                current_node = current_node.next

    # def deleteNode(self):





def main():
    # Prompt the user to enter their name and greet them
    # Time Complexity: O(1)
    # user_name = input("Enter your name: ")
    
    # while not user_name.isalpha():
    #     print("Please enter your name correctly")
    #     user_name = input("Enter your name: ")
    # print(f"Welcome {user_name}")
    
    # Display Menu
    # Time Complexity: O(1)
    displayMenu()
    
    # Take user choice 
    # Time Complexity: O(1)
    user_input = int(input("Please choose a number from the menu above: "))
    
    while user_input != 6:
        if user_input == 1:
            displayLinkedListMenu()
            user_choice = input("Please choose an option from the menu above: ")
            while not (user_choice.isalpha() and len(user_choice) == 1):
                user_choice = input("Please enter a character: ")
            
            if user_choice == "a":
                n = input("Enter a numerical value to add to the linked list: ")
                i = input("Enter the index you wish to insert the node in: ")
                while not (n.isnumeric() and i.isnumeric()):
                    n = input("Enter a number: ")
                    i = input("Enter a corrent index: ")
                
                ll = LinkedList()
                ll.addNode(n, i)
            
            elif user_choice == "b":
                ll = LinkedList()
                ll.displayNodes()
                
                
                
            elif user_choice == "c":
                ll = LinkedList()
                # deleteNode()
            
            elif user_choice == "d":
                print()
                # Return to main menu
    
    
    
        displayMenu()
        user_input = int(input("Please choose a number from the menu above: "))
    
    
    
    
    
main()
    
    
    
    