






def main():
    # Prompt the user to enter their name and greet them
    # Time Complexity: O(1)
    user_name = input("Enter your name: ")
    
    while not user_name.isalpha():
        print("Please enter your name correctly")
        user_name = input("Enter your name: ")
    print(f"Welcome {user_name}")
    

    
    
    
    
main()
    
    
    
    