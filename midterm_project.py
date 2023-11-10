

# Function to display the menu
# Running Time: O(1)
def displayMenu():
    print("""
          1. Open Tab
          2. Close Tab
          3. Switch Tab
          4. Display All Tabs
          5. Open Nested Tab
          6. Clear All Tabs
          7. Save Tabs
          8. Import Tabs
          9. Exit
          """)







def main():
    # Prompt the user to enter their name and greet them
    user_name = input("Enter your name: ")
    print(f"Welcome to our Advanced Browser {user_name}")
    
    # Display Menu
    displayMenu()
    
    # Take user choice 
    user_input = int(input("Please choose a number from the menu above: "))
    print(f"\nYou chose {user_input}")
    
    
    
    
    
    
main()