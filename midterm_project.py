

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

# Function to add a tab
# Running Time: __
def addTab(title, url):
    tab_dict = {}
    tab_dict[url]= [title]

    print(f"Website title {title} and website url {url} have been added successfully!")







def main():
    # Prompt the user to enter their name and greet them
    # Running Time: O(1)
    user_name = input("Enter your name: ")
    print(f"Welcome to our Advanced Browser {user_name}")
    
    # Display Menu
    # Running Time: O(1)
    displayMenu()
    
    # Take user choice 
    # Running Time: O(1)
    user_input = int(input("Please choose a number from the menu above: "))
    print(f"\nYou chose {user_input}")
    
    
    if user_input == 1:
        print()
        website_title = input("Enter the website title: ")
        website_url = input("Enter the website url: ")
        
        addTab(website_title, website_url)
    
    
main()





















