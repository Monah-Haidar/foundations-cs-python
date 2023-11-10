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
# A dictionary is used to represent each tab using the title and url provided considering the url as a key and the title as a value. 
# The tab list is also provided as a parameter to append the opened tab. 
# Running Time: __
def openTab(url, title, tab_dict):
    tab_dict[title]= [url]

    print(f"Website title {title} and website url {url} have been added successfully!")
    
    return tab_dict

# Function to close a tab
# The function takes the index provided by the user and the tab list as a parameter. 
# The funciton checks if the user provided an empty string or a valid index and closes the tab.
# Running Time: __
def closeTab(index, tab_dict):
    if index == "":
        tab_dict.popitem()
    else:
        del tab_dict[index]

    return tab_dict

# Function to close a tab
# Running Time: __
def displayTabContent(index, lst):
    # Setting up Selenium for webscraping
    # Source: https://www.selenium.dev/documentation/webdriver/getting_started/first_script/
    # Source: https://pythonbasics.org/selenium-get-html/
    from selenium import webdriver
    import time
  
    
    # Start a session
    driver = webdriver.Chrome()
    
    # Navigate to a webpage using the .get() method
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Requesting the HTML source code of the website
    html = driver.page_source
    
    # Wait for the website to load
    time.sleep(2)
    
    # Print html source code
    print(html)

    # End session
    driver.quit()






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
    tab_dict = {}
    
    while user_input != 9:
        
        if user_input == 1:
            website_title = input("Enter the website title: ")
            website_url = input("Enter the website url: ")
            
            openTab(website_url, website_title, tab_dict)
            print(tab_dict)
        
        elif user_input == 2:
            print(tab_dict)
            tab_index = input("Please enter the index of the tab you wish to close or leave it empty to close the last tab: ")
            while not (tab_index == "" or tab_index.isnumeric()):
                tab_index = input("Please enter the index of the tab you wish to close or leave it empty to close the last tab: ")
                
            closeTab(tab_index, tab_dict)
            print(tab_dict)
        
        elif user_input == 3:
            print(tab_dict)
            tab_index = input("Please enter the index of the tab you wish to display it's content': ")
            while not (tab_index == "" or tab_index.isnumeric()):
                tab_index = input("Please enter the index of the tab you wish to display it's content': ")
        
            displayTabContent(tab_index, tab_dict)
            print(tab_dict)
        
        
        
        
        displayMenu()
        user_input = int(input("Please choose a number from the menu above: "))
        print(f"\nYou chose {user_input}\n")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
main()





















