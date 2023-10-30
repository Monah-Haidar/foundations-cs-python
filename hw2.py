def menu():
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
def createMat1(rows, columns):
    mat1 = []
    for i in range(rows):
        lst = []
        for j in range(columns):
            elem = int(input(f"Enter elements of the {i+1} row of the first matrix: "))
            lst.append(elem)
        mat1.append(lst)    
    return mat1

# Funciton to create matrix 2
def createMat2(rows, columns):
    mat2 = []
    for i in range(rows):
      lst = []
      for j in range(columns):
          elem = int(input(f"Enter elements of the {i+1} row of the second matrix: "))
          lst.append(elem)
      mat2.append(lst)
    return mat2
    
    
    

def main():
    # name = input("Please Enter Your Name: ")
    # print(f"Hello {name}")
    
    # print(menu())
    
    # user_input = input("Please choose a number from the above menu: ")
    # print("You chose:", user_input)

    user_input = 1 
    
    if user_input == 1:
        # Ask user to enter rows and columns
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))
       
        mat1 = createMat1(rows, columns)
        mat2 = createMat2(rows, columns)
     

 
        
















main()