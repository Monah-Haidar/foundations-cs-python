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
            
            
    
    
    
    
        displayMenu()
        user_input = int(input("Please choose a number from the menu above: "))
    
    
    
    
    
main()
    
    
    
    