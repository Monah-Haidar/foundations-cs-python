# Display Menu
def menu():                           # O(1)
    print("""
          1. Add Matrices
          2. Check Rotation
          3. Invert Dictionary
          4. Convert Matrix to Dictionary
          5. Check Palindrome
          6. Search for an Element & Merge Sort
          7. Exit
          """)
          
              
# Funciton to create matrix 1
def createMat1(rows, columns):       # O(N^2)
    mat1 = []
    for i in range(rows):
        # declare an empty row
        lst = []
        for j in range(columns):
            elem = int(input(f"Enter elements of the {i+1} row of the first matrix: "))
            lst.append(elem)
        mat1.append(lst)    
    return mat1


# Funciton to create matrix 2
def createMat2(rows, columns):       # O(N^2)
    mat2 = []
    for i in range(rows):
      # declare an empty row
      lst = []
      for j in range(columns):
          elem = int(input(f"Enter elements of the {i+1} row of the second matrix: "))
          lst.append(elem)
      mat2.append(lst)
    return mat2
    
    
    
    

def main():
    # Ask the user for their name and welcome them
    name = input("Please Enter Your Name: ")
    print(f"Hello {name}")
    
    # Print the menu
    print(menu())
    
    # Ask user to choose a number from the menu
    user_input = input("Please choose a number from the above menu: ")
    print("You chose:", user_input)

    
    if user_input == 1:
        # Ask user to enter rows and columns
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))
       
        mat1 = createMat1(rows, columns)
        mat2 = createMat2(rows, columns)
        mat3 = []
        
        for i in range(rows):
            # initialize each row of mat3 in order to assign values in the 2nd for loop
            mat3.append([0] * columns)
            for j in range(columns):
                mat3[i][j] = mat1[i][j] + mat2[i][j]
 
        print(mat3)
















main()