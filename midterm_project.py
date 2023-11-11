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

# Function to open a tab
# A dictionary is used to represent each tab using the title and url provided considering the title as a key and the url as a value. 
# Running Time: __
def openTab(url, title, tab_dict):
    tab_dict[title]= url
    
    return tab_dict

# Function to close a tab
# The function takes the index provided by the user and the tab dictionary as a parameter. 
# The funciton checks if the user provided an empty string or a valid index and closes the tab.
# Running Time: __
def closeTab(index, tab_dict):
    # string is empty
    if not index:
        tab_dict.popitem()
    else:
        # Making a copy of dicitionary
        copy_of_tab_dict = tab_dict.copy()

        # Iterating over the copy and deleting from the original dictionary
        # We do that because it gives a runtime error when deleting from a dictionary while also iterating over it
        for key,value in copy_of_tab_dict.items():
            if key == index:
                del tab_dict[index]
    
    return tab_dict
            



# Function to close a tab
# Running Time: __
def displayTabContent(index, tab_dict):
    # Setting up Selenium for webscraping
    # Source: https://www.selenium.dev/documentation/webdriver/getting_started/first_script/
    # Source: https://pythonbasics.org/selenium-get-html/
    from selenium import webdriver
    import time
  
    if not index:
        # Source:https://stackoverflow.com/questions/2212433/counting-the-number-of-distinct-keys-in-a-dictionary-in-python
        # list(____.keys()) returns the dictionary keys in a list. That way i can access the last key in the dictionary and display its content
        key_lst = list(tab_dict.keys())
        elem = key_lst[-1]
        url = tab_dict[elem][0]
    else:
        for key,value in tab_dict.items():
            if key == index:
                url = tab_dict[key][0]
  
    
    # Start a session
    driver = webdriver.Chrome()
    
    # Navigate to a webpage using the .get() method
    driver.get(url)

    # Requesting the HTML source code of the website
    html = driver.page_source
    
    # Wait for the website to load
    time.sleep(2)
    
    # Print html source code
    print(html)

    # End session
    driver.quit()

    # Requesting the HTML source code of the website
    html = driver.page_source
    
    # Wait for the website to load
    time.sleep(2)
    
    # Print html source code
    print(html)

    # End session
    driver.quit()


# Printing all titles in the dictionary using pre-order traversal 
# Pre-order traversal is a type of tree traversal that prints the parent node before its children according to to depth
# Running Time: __
def printAllTabs(tab_dict, depth = 0):
    
    for key, value in tab_dict.items():         # iterate over dictionary

        if isinstance(value, dict):             # check if the value is another dictionary
            print("\t" * depth + key)           # if true, print the parent key with the respective indentation (hierarchy) according to the depth variable 
            printAllTabs(value, depth + 1)      # call the function recursively until you reach no nested dicitonaries
        else:
            print("\t" * depth + key)           # Print the keys of the dictionaries according to their depth level
   




def main():
    # Prompt the user to enter their name and greet them
    # Running Time: O(1)
    # user_name = input("Enter your name: ")
    # print(f"Welcome to our Advanced Browser {user_name}")
    
    # Display Menu
    # Running Time: O(1)
    displayMenu()
    
    # Take user choice 
    # Running Time: O(1)
    user_input = int(input("Please choose a number from the menu above: "))
    
    # Dictionary to store tabs
    # tab_dict = {
    #     'sef': 'https://www.activestate.com/',
    #     'net': 'https://www.selenium.dev/documentation/',
    #     }
    
    tab_dict = {
        "child4": "halawalla.com",
        "child1" : {
            "name" : "Emil",
            "year" : 2004
            },
        "child2" : {
            "name" : "Tobias",
            "year" : 2007
            },
        "child3" : {
            "name" : "Linus",
            "year" : 2011
            }
        
        } 
    
    while user_input != 9:
        
        if user_input == 1:
            website_title = input("Enter the website title: ")
            website_url = input("Enter the website url: ")
            
            print(openTab(website_url, website_title, tab_dict))
        
        elif user_input == 2:
            print(tab_dict)
            tab_index = input("Please enter the index of the tab you wish to close or leave it empty to close the last tab: ")
            
            print(closeTab(tab_index, tab_dict))
        
        elif user_input == 3:
            print(tab_dict)
            tab_index = input("Please enter the index of the tab you wish to display it's content: ")
            
            displayTabContent(tab_index, tab_dict)
            
        elif user_input == 4:
            
            printAllTabs(tab_dict)
        
        
        
        
        
        
        
        displayMenu()
        user_input = int(input("Please choose a number from the menu above: "))
        
        
        
        
        
        
        
        
        
        
        
main()





















