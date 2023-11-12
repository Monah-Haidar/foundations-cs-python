from selenium import webdriver
import time
import json
import os
import os.path
from os import path
import validators




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
    
    # Validate user input
    while not ((validators.url(url) == True) and (title.isalpha())):
        print("Please enter website title or url correctly")
        title = input("Enter the website title: ")
        url = input("Enter the website url: ")
    
    tab_dict[title]= url
    
    return tab_dict

# Function to close a tab
# The function takes the index provided by the user and the tab dictionary as a parameter. 
# The funciton checks if the user provided an empty string or a valid index and closes the tab.
# Running Time: __
def closeTab(index, tab_dict):

    # Validate user input
    while not ((index.isalpha()) or (index == "")):
        print("Please enter characters or leave it empty to close the last tab")
        index = input("Please enter the index of the tab you wish to close or leave it empty to close the last tab: ")
    
    
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
            



# Function to display the content of a tab
# Running Time: __
def switchTab(index, tab_dict):
    # Setting up Selenium for webscraping
    # Source: https://www.selenium.dev/documentation/webdriver/getting_started/first_script/
    # Source: https://pythonbasics.org/selenium-get-html/
  
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


# Displaying all titles in the dictionary using depth-order traversal 
# depth-order traversal is a type of tree traversal that prints the parent node before its children according to depth
# Running Time: __
def displayAllTabs(tab_dict, depth = 0):
    
    for key, value in tab_dict.items():         # iterate over dictionary
        if isinstance(value, dict):             # check if the value is another dictionary
            print("\t" * depth + key)           # if true, print the parent key with the respective indentation (hierarchy) according to the depth variable 
            displayAllTabs(value, depth + 1)    # call the function recursively until you reach no nested dicitonaries
        else:
            print("\t" * depth + key)           # Print the keys of the dictionaries according to their depth level
   

# This function enables users to create nested tab by choosing the index
# We are looping to find the desired index and inserting a dictionary on that specific index
# We added the 'parent_url' key in the newly added nested dictionary not to lose the url of the parent website
# Running Time: __
def openNestedTab(index, title, url, tab_dict):
    
    # Validate user input
    while not ((validators.url(url) == True) and (title.isalpha()) and (index.isalpha())):
        print("tab index or website title or url are wrong")
        index = input("Please enter the index of the tab you wish to nest: ")
        title = input("Enter the website title: ")
        url = input("Enter the website url: ")
    
    # Making a copy of dicitionary
    copy_of_tab_dict = tab_dict.copy()
    
    for key, value in copy_of_tab_dict.items():
        if key == index:
            tab_dict[index] = {
                "parent_url" : value,
                title : url,
                }
            
    return tab_dict


# Delete of dictionary fields recursively
# Running Time: __
def clearAllTabs(tab_dict):
    
    # Making a copy of dicitionary
    copy_of_tab_dict = tab_dict.copy()
    
    for key, value in copy_of_tab_dict.items():
        if isinstance(value, dict):
            del tab_dict[key]
            clearAllTabs(value)
        else:
            del tab_dict[key]

    return tab_dict


# Function to save open tabs information in a json file
# Running Time: __ 
def saveTabs(p, tab_dict):
    
    if p == "":
        # Get current working directory
        directory = os.getcwd()
        new_path = f"{directory}\\savedOpenTabs.json"  # since the user didn't enter a path then we should automatically store the content in the current working directory and give the file a name by default
        with open(new_path, "w") as f:
            json.dump(tab_dict, f)
    else:
        
        # Validate user input
        if not path.exists(p):
            print("File path wrong...")
            p = input("Please enter a file path to load tabs: ")
        
        file_path = p
        
        with open(file_path, "w") as f:     # used to work with text files. takes 2 parameters - the path and the mod as to which we need to write(w), read(r), append(a), or create(x)
            json.dump(tab_dict, f)     # We are using the write mode because we should overwrite the content of the file if it exists and if it doesn't exist we should create it
        

# Function to load tabs information
# Running Time: __ 
def importTabs(p, tab_dict):
    
    # Validate user input
    while not path.exists(p):
        print("File path wrong...")
        p = input("Please enter a file path to load tabs: ")
    
    file_path = p
    
    # Open json file
    with open(file_path) as f:
        data = json.load(f)      # Load data from json file

        print("Loading Dictionary: ")
        
        for key, value in data.items():         
                tab_dict[key] = value     
        
    return tab_dict







def main():
    # Prompt the user to enter their name and greet them
    # Running Time: O(1)
    user_name = input("Enter your name: ")
    while not user_name.isalpha():
        print("Please enter your name correctly")
        user_name = input("Enter your name: ")
    print(f"Welcome to our Advanced Browser {user_name}")
    
    # Display Menu
    # Running Time: O(1)
    displayMenu()
    
    # Take user choice 
    # Running Time: O(1)
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





















