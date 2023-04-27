#grab the text file to write on.

with open("mystory.txt") as my_file:
    #create a UI
    print("Welcome to the typewriting system!")

    #start a loop, make a while condition.

    user_stop = False

    while user_stop == False:
        #call the input.
        print("Selection: \n(1) Write a new line\n(2) Read the current list\n(3) close the program")
        selection = int(input("Please type the number of your selection: "))