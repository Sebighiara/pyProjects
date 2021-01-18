print ("My \"To do\" list \n")

#this function prints all the options that can be realised on the list 
def options():
    print ("1) View My \"To Do\" list")
    print ("2) Add activities to the list")
    print ("3) Mark activities as done")
    print ("4) Delete an activity from the list")
    print ("5) Delete the list")
    print ("6) Close app\n")
    pass

#update the content of the file to a list
def updateList(list):
    with open ("ToDoListFile.txt", "r") as file:
        list = file.readlines()
    return list

#storing to "fileName" the name of the file where the "to do" list is also stored
fileName = "ToDoListFile.txt"

#initialized empty list where will be stored the activities from the file
activities = []

activities = updateList(activities)

closeList = False

#while certain operations on the list are stil performed
#the program will not be closed
while closeList == False:
    
    options() #options are printed
    
    #the client types an option that will be stored to "option" variable
    option = input("Choose an option: ")
    if option == "1":
        print ("The content of your list is: \n")
        #if the client wants to see the list, the program reads from the
        #file and print on the screen
        with open (fileName, "r") as myToDo:
            print (myToDo.read())
        print (activities)
    elif option == "2":
        addActivities = True
        #the client can add as many activities as he wants, not only one
        while addActivities == True or addActivities == "yes":
            addActivity = input ("\nType what you want to add to your list: ")
            addActivity += "\n" #every activity has to be on a new line
            with open (fileName, "a") as myToDo:
                myToDo.write(addActivity)#activity is added to the list
            activities = updateList(activities)
            addActivities = input ("Do you want to add something else? ")
    elif option == "3":
        wantToMark = True
        #the program allows the client to mark as many activities as he wants 
        while wantToMark == True or wantToMark == "yes":
            markAsDone = input ("\nType exactly what you want to mark as done: ")
            with open (fileName, "w") as myToDo:
                #searching the activity in the list
                for activity in activities:
                    #once found, the activity is marked and overwritten in the file
                    if activity[: -1] == markAsDone: #[: -1] is used beacuse the elements of "activities" list ends in "\n"
                        markAsDone += "*\n"
                        myToDo.write(markAsDone)
                    #else the activity is just overwritten again
                    else:
                        myToDo.write(activity)
            activities = updateList(activities)
            wantToMark = input ("Do you want to mark something else? ")
    elif option == "4":
        wantToDelete = True
        #also the client can delete one or more activities
        while wantToDelete == True or wantToDelete == "yes":
            delActivity = input ("\nType exactly what you want to delete: ")
            with open (fileName, "w") as myToDo:
                #searching for the activity the client wants to delete
                for activity in activities:
                    #are overwritten those who doesn't coincide 
                    if activity[:-1] != delActivity and activity[:-1] != delActivity + "*":
                        myToDo.write(activity)
            activities = updateList(activities)
            wantToDelete = input ("Do you want to delete something else? ")
    elif option == "5":
        #asking for confirmation
        delete = input ("are you sure you want to delete the list?: ")
        if delete == "yes":
            with open (fileName, "w") as myToDo:
                myToDo.write("")#the file is empty
        activities = []#also the list will be deleted
    #option for closing the application
    elif option == "6":
        closeList = True 
    


