#Brian K Burnett Jr 08/29/2025

#The purpose of this program is to calculate the users cost per days spent in a hotel.
def main():
    #The input greets the user to the assistant and hotel.
    input("Hello User welcome to your SummerSet Hotel Reservation Maker press [ENTER] to proceed.")

    #This lets the user input the amount of days but only in numbers because of the integer(int) function.
    Days = int(input("How many days would you like to stay at SummerSet Hotel pick a number between 1 and 4?: "))

    if Days == 1:
        print("Before we start select the room you want to stay in.")

    elif Days == 2:
        print("Before we start select the room you want to stay in.")

    elif Days == 3:
        print("Before we start select the room you want to stay in.")

    #If the selected answer isn't in the list it'll quit the code
    elif Days != [1,2,3,4]:
        print("Invalid option.")
        exit()

    #Filler just to make it seem more realistic.
    #print("Before we start select the room you want to stay in.")

    #Presents the user with a selection of rooms and their costs.
    print("Single Room ($100 per day), Standard Room ($200 per day), Presidential Suite ($300 per day)")

    #Lets the user pick the room based on a number system.
    Room = int(input("Please select the room you want by choosing 1, 2, or 3: "))

    #The if, elif, and else statements give value to the numbers since I didn't know how to do the words.
    #Also, the else puts an error checker on it or whatever it's called when a user puts in a wrong number.
    if Room == 1:
        cost_day = 100

    elif Room == 2:
        cost_day = 200

    elif Room == 3:
        cost_day = 300

    elif Room != [1,2,3]:
        print("INVALID SELECTED ROOM")

    #The calculation part of the code
    totalcost = Days * cost_day

    #Shows the user the cost
    print(f"Your stay at SummerSet will cost {totalcost} for {Days} days, enjoy.\n")

    print("^...^    ")
    print(" / o,o \ ")
    print("|) ::: (|")
    print("===w=w===")

if __name__ == "__main__":
    main()