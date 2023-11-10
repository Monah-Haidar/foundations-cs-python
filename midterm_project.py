

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
def addTab(title, url, lst):
    tab_dict = {}
    tab_dict[url]= [title]
    lst.append(tab_dict)

    print(f"Website title {title} and website url {url} have been added successfully!")
    
    return lst

# Function to close a tab
# Running Time: __
def closeTab(index, lst):
    if index == "":
        lst.pop()
    else:
        lst.pop(int(index))

    return lst


def displayTabContent(index, lst):
    print()







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
    print(f"\nYou chose {user_input}\n")
    
    # List to maintain to order of tabs
    tab_list = []
    
    while user_input != 9:
        
        if user_input == 1:
            website_title = input("Enter the website title: ")
            website_url = input("Enter the website url: ")
            addTab(website_title, website_url, tab_list)
            print(tab_list)
        
        elif user_input == 2:
            print(tab_list)
            tab_index = input("Please enter the index of the tab you wish to close or leave it empty to close the last tab: ")
            while not (tab_index == "" or tab_index.isnumeric()):
                tab_index = input("Please enter the index of the tab you wish to close or leave it empty to close the last tab: ")
                
            closeTab(tab_index, tab_list)
            print(tab_list)
        
        elif user_input == 3:
            print(tab_list)
            tab_index = input("Please enter the index of the tab you wish to display it's content': ")
            while not (tab_index == "" or tab_index.isnumeric()):
                tab_index = input("Please enter the index of the tab you wish to display it's content': ")
        
            displayTabContent(tab_index, tab_list)
            print(tab_list)
        
        
        
        
        displayMenu()
        user_input = int(input("Please choose a number from the menu above: "))
        print(f"\nYou chose {user_input}\n")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
main()





















