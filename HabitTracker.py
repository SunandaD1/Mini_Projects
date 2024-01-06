'''Daily tasks to complete, using python dictionnaries. Key-- habit,
value-- description, less of a to do list because they are mostly the same
everyday-- more to track daily tasks and feel accomplished doing them '''


x = {
    "drink water":8,
    "hours exercised":1.5,
    "meals eaten":3,
    "emails sent":10,
    "hours of homework": 4,
    "hours to sleep":8,
    "journal pages to complete":2
} 


print(x)

def habits(x):

    changeKey=input("Do you want to update an existing habit? Write yes or no: ")
    if changeKey.lower() == "yes":
        keyNum=input("Which habit? Enter the name: ")
        if keyNum in x:
            updated_value = input("Enter the updated value for the habit: ")
            x[keyNum] = updated_value
        else:
            print("Sorry, this habit does not exist.")

    addHabit=input("Do you want to add a habit? Write yes or no: ")
    if addHabit.lower() == "yes":
        newKey = input("What is the habit?: ")
        newValue = input("What is the description?: ")
        x[newKey] = newValue
    return x


result = habits(x)


print (result)

