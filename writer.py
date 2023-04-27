#grab the text file to write on.


#create a UI
print("Welcome to the typewriting system!")

#start a loop, make a while condition.

user_stop = False

while user_stop == False:
    #call the input.
    print("Selection: \n(1) Write a new line\n(2) Read the current list\n(3) close the program")
    selection = int(input("Please type the number of your selection: "))

    #if decision is 3, stop the program:
    if selection == 3:
        print("Closing the program, goodbye!")
        break

    #if selection is 1:
    if selection == 1:
        #start a while loop for the editor:
        my_file = open("mystory.txt", 'r')
        #count the number of lines
        line_count = 0
        for line in my_file:
            line_count = line_count + 1
        my_file.close()
        #if no lines found, write a new line.
        if line_count == 0:

            first_line = str(input("Type in your first line: "))
            #write down first line then close.
            my_file = open("mystory.txt", 'w')
            my_file.write(first_line + '\n')
            my_file.close()


