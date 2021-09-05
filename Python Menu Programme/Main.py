import os
from MenuItem import MenuItem

listOfMenuItems = []
possible_inputs_main = ["1", "2", "3", "Q"]
possible_inputs_one = ["N", "B", "R", "Q"]
possible_inputs_two = ["1", "2", "3", "4", "5", "6"]
possible_inputs_return = ["R", "Q"]

#Keep Screen Tidy
def clearScreen():
	if os.name == "nt":
		os.system("cls")
	elif os.name == "mac"  or  os.name == "posix":
		os.system("clear")

#Disp Main Menu
def display_main_menu():
    print("Main Menu")
    print("----------")
    print("1. Display all menu items available")
    print("2. Display full details from menu list")
    print("3. Search based on Name or Category substring")
    print("Enter 'Q' to quit programme")
    print("----------")

#Nav Main Menu
def main_menu():
    clearScreen()
    display_main_menu()
    usr_input_main = input("Please enter your selection: ")
    while usr_input_main not in possible_inputs_main:
        print ("Invalid Input. Please Try Again.")
        usr_input_main = input("Please enter your selection: ")

    if usr_input_main == "1": #Option 1
        option_one()
    elif usr_input_main == "2": #Option 2
        option_two()
    elif usr_input_main == "3": #Option 3
        option_three()

    elif usr_input_main.upper() == "Q": #Quit the Programme
        print("You have closed the Programme. Goodbye")
        exit()

#Disp Index
def display_index(index, max_index):
    item_index = index+1
    print("----------")
    print("Showing Item", item_index, "of", max_index)
    print("----------")

#Disp NavKeys
def display_navkeys():
    print("----------")
    print("Enter 'N' to view the Next item")
    print("Enter 'B' to go Back to the previous item")
    print("Enter 'R' to Return to the main menu")
    print("Enter 'Q' to Quit programme")
    print("----------")

#Nav Opt One
def sub_menu_one(index, usr_input_one):
    max_index= len(listOfMenuItems)
    while usr_input_one.upper() not in possible_inputs_one:
        print ("Invalid Input. Please Try Again.")
        usr_input_one = input("Please enter your selection: ")

    if usr_input_one.upper() == "N": #Next
        index= index + 1
        if index == max_index or index < 0 :
            index = 0
        display_index(index, max_index)
        PrintMenuItemDetails (listOfMenuItems[index])
        display_navkeys()
        usr_input_one = input("Please enter your selection: ")
        sub_menu_one(index, usr_input_one)

    elif usr_input_one.upper() == "B": #Back
        index= index - 1
        if index == max_index or index < 0 :
            index = max_index-1
        display_index(index, max_index)
        PrintMenuItemDetails (listOfMenuItems[index])
        display_navkeys()
        usr_input_one = input("Please enter your selection: ")
        sub_menu_one(index, usr_input_one)
            
    elif usr_input_one.upper() == "R": #Return Main
        main_menu()

    elif usr_input_one.upper() == "Q": #Quit
        print("You have closed the Programme. Goodbye")
        exit()

#Disp Opt Two
def display_option_two():
    print("----------")
    print("1. Tonkastu Ramen") 
    print("2. Hawaiian Pizza")
    print("3. Roasted Chicken Rice")
    print("4. Roasted Pork Rice")
    print("5. Wanton Noodles")
    print("6. Mutton Bryani")
    print("Enter 'R' to Return to the main menu")
    print("Enter 'Q' to Quit programme")
    print("----------")

#Nav Opt Two
def sub_menu_two():
    usr_input_return = input("Enter 'R' to Re-select item or Enter 'Q' to Quit programme: ")
    while usr_input_return.upper() not in possible_inputs_return:
        print ("Invalid Input. Please Try Again.")
        usr_input_return = input("Please enter your selection: ")

    if usr_input_return.upper() == "R": #Return Opt Two
        option_two()

    elif usr_input_return.upper() == "Q": #Quit
        print("You have closed the Programme. Goodbye")
        exit()

#Disp Opt Three
def display_option_three():
    print("----------")
    print("Enter a 'Name' or 'Category' to find matching Items")
    print("Enter 'R' to Return to the main menu")
    print("Enter 'Q' to Quit programme")
    print("----------")

#Nav Opt Three
def sub_menu_three():
    usr_input_return = input("Enter 'R' to Re-select item or Enter 'Q' to Quit programme: ")
    while usr_input_return.upper() not in possible_inputs_return:
        print ("Invalid Input. Please Try Again.")
        usr_input_return = input("Please enter your selection: ")

    if usr_input_return.upper() == "R": #Return Opt Two
        option_three()

    elif usr_input_return.upper() == "Q": #Quit
        print("You have closed the Programme. Goodbye")
        exit()

#Required-Done
def read_file(filename):
    with open (filename, "r") as file:
        Input_text = file.readlines()
        for x in range (1, len(Input_text)):
            EachItem = Input_text[x].split(",")
            Name = EachItem[0] 
            Category = EachItem[1]
            Description = EachItem[2]
            Price = float(EachItem[3])
            MenuObject = MenuItem(Name, Category, Description, Price)
            listOfMenuItems.append(MenuObject)
    return listOfMenuItems

#Required-Done
def PrintMenuItemDetails(MenuItem):
    print("----------")
    print("Name:", MenuItem.getName())
    print("Category:", MenuItem.getCategory())
    print("Description:", MenuItem.getDescription())
    print("Price: $", MenuItem.getPrice())
    print("----------")
    print("\n")
    
#Required-Done
def SearchBasedOnNameOrCategory (searchString, listOfMenuItems):
    searchResult = []
    searchString_lower = searchString.lower()
    
    for x in listOfMenuItems:
        if searchString_lower in x.getName().lower() or searchString_lower in x.getCategory().lower():
            searchResult.append(x)
            index = 0
            max_index= len(searchResult)
            display_index(index, max_index)
            PrintMenuItemDetails(x)

    print("No more results to display.")
    return searchResult

#1.Display all menu items available
#Required-Done
def option_one():
    read_file("input.txt")
    index = 0
    max_index= len(listOfMenuItems)
    display_index(index, max_index)
    PrintMenuItemDetails (listOfMenuItems[index])
    display_navkeys()
    usr_input_one = input("Please enter your selection: ")
    sub_menu_one (index, usr_input_one)

#2.Display full details from menu list
#Required-Done
def option_two():
    display_option_two()
    usr_input_two = input("Please enter your selection to view more details: ")

    if usr_input_two.upper() == "R": #Return Main
        main_menu()

    elif usr_input_two.upper() == "Q": #Quit
        print("You have closed the Programme. Goodbye")
        exit()

    else :    
        while usr_input_two not in possible_inputs_two:
            print ("Invalid Input. Please Try Again.")
            usr_input_two = input("Please enter your selection: ")

    read_file("input.txt")
    index = (int(usr_input_two)-1)
    max_index= len(possible_inputs_two)
    display_index(index, max_index)
    PrintMenuItemDetails (listOfMenuItems[index])
    sub_menu_two()

#3.Search based on Name or Category substring
#Required-Done
def option_three():
    read_file("input.txt")
    display_option_three()
    usr_input_three = input ("Please enter your selection: ")
    
    if usr_input_three.upper() == "R": #Return Main
        main_menu()

    elif usr_input_three.upper() == "Q": #Quit
        print("You have closed the Programme. Goodbye")
        exit()
    else :
        SearchBasedOnNameOrCategory (usr_input_three, listOfMenuItems) 
        sub_menu_three()
        
main_menu()