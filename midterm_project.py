from selenium import webdriver
import time
import json
import os
import os.path
from os import path
import validators




# Function to display the menu
# Time Complexity of whole function: O(1)
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
# Time Complexity of whole function: O(1)
def openTab(url, title, tab_dict):
    
    # Validate user input
    while not ((validators.url(url) == True) and (title.isalpha())):   # O(1)
        print("Please enter website title or url correctly")
        title = input("Enter the website title: ")
        url = input("Enter the website url: ")
    
    tab_dict[title]= url   # O(1)
    
    return tab_dict

# Function to close a tab
# The function takes the index provided by the user and the tab dictionary as a parameter. 
# The funciton checks if the user provided an empty string or a valid index and closes the tab.
# Time Complexity of whole function: O(N)
def closeTab(index, tab_dict):

    # Validate user input
    while not ((index.isalpha()) or (index == "")):     # O(1)
        print("Please enter characters or leave it empty to close the last tab")
        index = input("Please enter the index of the tab you wish to close or leave it empty to close the last tab: ")
    
    # Time complexity for the 2 conditional statements above is O(N)
    # string is empty
    if not index:
        tab_dict.popitem()      # O(1)
    else:
        # Making a copy of dicitionary
        copy_of_tab_dict = tab_dict.copy()

        # Iterating over the copy and deleting from the original dictionary
        # We do that because it gives a runtime error when deleting from a dictionary while also iterating over it
        for key,value in copy_of_tab_dict.items():      # O(N)   since we are iterating over N elements in the dictionary
            if key == index:
                del tab_dict[index]
    
    return tab_dict
            



# Function to display the content of a tab
# Time Complexity of whole function: O(N)  - Time mainly depends on the number of times we are iterating over the dictionary
def switchTab(index, tab_dict):
    # Setting up Selenium for webscraping
    # Source: https://www.selenium.dev/documentation/webdriver/getting_started/first_script/
    # Source: https://pythonbasics.org/selenium-get-html/
  
    if not index:      # O(1)     # index is empty string
        # Source:https://stackoverflow.com/questions/2212433/counting-the-number-of-distinct-keys-in-a-dictionary-in-python
        # list(____.keys()) returns the dictionary keys in a list. That way i can access the last key in the dictionary and display its content
        key_lst = list(tab_dict.keys())
        elem = key_lst[-1]
        url = tab_dict[elem]
    else:
        for key,value in tab_dict.items():    # O(N)
            if key == index:
                url = tab_dict[key]
  
    
    # Start a session
    driver = webdriver.Chrome()
    
    # Navigate to a webpage using the .get() method
    driver.get(url)

    # Requesting the HTML source code of the website
    html = driver.page_source
    
    # Wait for the website to load
    time.sleep(2)
    
    # Print html source code
    print(html.encode('utf-8'))     # We use the .encode() method to display characters that aren't compatible with the default character encoding

    # End session
    driver.quit()


# Displaying all titles in the dictionary using depth-order traversal 
# depth-order traversal is a type of tree traversal that prints the parent node before its children according to depth
# Time Complexity of whole function: O(N)  - Time mainly depends on the number of times we are iterating over the dictionary
def displayAllTabs(tab_dict, depth = 0):
    
    for key, value in tab_dict.items():     # O(N)      # iterate over dictionary
        if isinstance(value, dict):         # O(1)      # check if the value is another dictionary
            print("\t" * depth + key)                   # if true, print the parent key with the respective indentation (hierarchy) according to the depth variable 
            displayAllTabs(value, depth + 1)            # call the function recursively until you reach no nested dicitonaries
        else:                               # O(1)
            print("\t" * depth + key)                   # Print the keys of the dictionaries according to their depth level
   

# This function enables users to create nested tab by choosing the index
# We are looping to find the desired index and inserting a dictionary on that specific index
# We added the 'parent_url' key in the newly added nested dictionary not to lose the url of the parent website
# Time Complexity of whole function: O(N)   - Time mainly depends on the number of times we are iterating over the dictionary
def openNestedTab(index, title, url, tab_dict):
    
    # Validate user input
    while not ((validators.url(url) == True) and (title.isalpha()) and (index.isalpha())):    # O(1)
        print("tab index or website title or url are wrong")
        index = input("Please enter the index of the tab you wish to nest: ")
        title = input("Enter the website title: ")
        url = input("Enter the website url: ")
    
    
    # Time complexity of the below is O(N) since they are not nested so we don't multiply
    # Making a copy of dicitionary
    copy_of_tab_dict = tab_dict.copy()     # O(N)
    
    for key, value in copy_of_tab_dict.items():   # O(N)
        if key == index:      # O(1)
            tab_dict[index] = {       # O(1)
                "parent_url" : value,
                title : url,
                }
            
    return tab_dict


# Delete of dictionary fields recursively
# Time Complexity of whole function: O(N)  - Time mainly depends on the size of the dictionary we deleting consisting of N elements 
def clearAllTabs(tab_dict):
    
    # Making a copy of dicitionary
    copy_of_tab_dict = tab_dict.copy()      # O(N)
    
    for key, value in copy_of_tab_dict.items():     # O(N)
        if isinstance(value, dict):       # O(1)
            del tab_dict[key]
            clearAllTabs(value)
        else:                             # O(1)
            del tab_dict[key]

    return tab_dict


# Function to save open tabs information in a json file
# Time Complexity of whole function: O(N)  - Time mainly depends on the size of the dictionary we are saving which is N elements
def saveTabs(p, tab_dict):
    
    if p == "":   # O(1)
        # Get current working directory
        directory = os.getcwd()
        new_path = f"{directory}\\savedOpenTabs.json"  # since the user didn't enter a path then we should automatically store the content in the current working directory and give the file a name by default
        with open(new_path, "w") as f:    # O(N)
            json.dump(tab_dict, f)
    else:
        
        # Validate user input
        if not path.exists(p):    # O(1)
            print("File path wrong...")
            p = input("Please enter a file path to load tabs: ")
        
        file_path = p
        
        with open(file_path, "w") as f:   # O(N)  # used to work with text files. takes 2 parameters - the path and the mod as to which we need to write(w), read(r), append(a), or create(x)
            json.dump(tab_dict, f)     # We are using the write mode because we should overwrite the content of the file if it exists and if it doesn't exist we should create it
        

# Function to load tabs information
# Time Complexity of whole function: O(N^2) 
def importTabs(p, tab_dict):
    
    # Validate user input
    while not path.exists(p):  # O(1)
        print("File path wrong...")
        p = input("Please enter a file path to load tabs: ")
    
    file_path = p    # O(1)
    
    # Time compelxity of the below is O(N^2) since the for loop is nested withing the file open
    # Open json file
    with open(file_path) as f:    # O(N)
        data = json.load(f)      # Load data from json file

        print("Loading Dictionary: ")
        
        for key, value in data.items():      # O(N)     
                tab_dict[key] = value     
        
    return tab_dict







def main():
    # Prompt the user to enter their name and greet them
    # Time Complexity: O(1)
    user_name = input("Enter your name: ")
    while not user_name.isalpha():
        print("Please enter your name correctly")
        user_name = input("Enter your name: ")
    print(f"Welcome to our Advanced Browser {user_name}")
    
    # Display Menu
    # Time Complexity: O(1)
    displayMenu()
    
    # Take user choice 
    # Time Complexity: O(1)
    user_input = int(input("Please choose a number from the menu above: "))
    
    
    
    # Dictionary to store tabs
    tab_dict = {}

    
    while user_input != 9:
        
        if user_input == 1:
            website_title = input("Enter the website title: ")
            website_url = input("Enter the website url: ")
            
            print(openTab(website_url, website_title, tab_dict))
            
        
        elif user_input == 2:
            print(tab_dict)
            
            if tab_dict == {}:
                print("No open tabs")
                
            else:
                tab_index = input("Please enter the index of the tab you wish to close or leave it empty to close the last tab: ")
            
                print(closeTab(tab_index, tab_dict))
        
        elif user_input == 3:
            print(tab_dict)
            
            if tab_dict == {}:
                print("No open tabs")
                
            else:
                tab_index = input("Please enter the index of the tab you wish to display it's content: ")
            
                while not ((tab_index.isalpha()) or (tab_index == "")):
                    print("Please enter characters or leave it empty to close the last tab")
                    tab_index = input("Please enter the index of the tab you wish to display it's content: ")
            
                switchTab(tab_index, tab_dict)
            
        elif user_input == 4:
            
            if tab_dict == {}:
                print("No open tabs")
                
            else:
                displayAllTabs(tab_dict)
        
        elif user_input == 5:
            print(tab_dict)
            
            if tab_dict == {}:
                print("No open tabs")
                
            else:
            
                tab_index = input("Please enter the index of the tab you wish to nest: ")
                website_title = input("Enter the website title: ")
                website_url = input("Enter the website url: ")
            
                print(openNestedTab(tab_index, website_title, website_url, tab_dict))
            
        
        elif user_input == 6:
            print(clearAllTabs(tab_dict))
        
        elif user_input == 7:
            file_path = input("Please enter a file path to save the current state of open tabs: ")
            
            saveTabs(file_path, tab_dict)
        
        elif user_input == 8:
            file_path = input("Please enter a file path to load tabs: ")
                
            print(importTabs(file_path, tab_dict))
        
        elif user_input != 9:
            print("Your choice is invalid. Please try again")
        
        
        
        displayMenu()
        user_input = int(input("Please choose a number from the menu above: "))
        
        
        
        
    
        
main()





















