# Kyutza Lopez
# Assignment 4.1
# COP 2500
# Nov 3, 2022

schedule = list()
dropped = []

print ("You aren't currently taking any courses.")


    # loops everything as long as the length of schedule doesn't reach 5
while (len(schedule) != 5):
    courses = input("What courses would you like to take? ")
    # exit loop
    if (len(schedule) == 5):
        print("Done!")
        break
        
    else:
        courses = courses.split(",")
        for index in range(len(courses)):
            courses[index] = courses[index].strip().title()
    # creates the updated schedule after each new input
            
        schedule = schedule + courses

        print("You are currently taking these courses:")
        for index in range(len(schedule)):
            print(str(index+1) + ": " + str(schedule[index])) 
    # str(index+1) creates the numbers for the list, str(schedule[index] print out the input as string

    # performs these functions if the legnth of the schedule reaches 6
    while (len(schedule) > 5):
        dropped = input("What courses would you like to drop? ")

        dropped = dropped.split (",")
       
        for index in range(len(dropped)):
            dropped[index] = dropped[index].strip().title()
            # creates a new list that will be deleted from the schedule
            # list made from dropped courses that will be detected from schedule
            dropped.append(dropped[index])

            if dropped[index] in schedule:
                schedule.remove(dropped[index])
            # detecting dropped courses from schedule, and removing them
      
        print("You are currently taking these courses:") # reprinting new schedule 
        for index in range(len(schedule)):
            print(str(index+1) + ": " + str(schedule[index])) 
