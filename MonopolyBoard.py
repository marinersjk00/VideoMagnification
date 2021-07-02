import random


    

board = ["GO", "Mediterranean Ave", "Community Chest", "Baltic Ave", "Income tax", "Reading Railroad", "Oriental Ave", "Chance", "Vermont Ave", "Connecticut Ave", "Jail",
         "St. Charles Place", "Electric Company", "States Ave", "Virginia Ave", "Pennsylvania Railroad", "St. James Place", "Community Chest", "Tennessee Ave", "New York Ave", "Free Parking",
         "Kentucky Ave", "Chance", "Indiana Ave", "Illinois Ave", "B & O Railroad", "Atlantic Ave", "Ventnor Ave", "Water Works", "Marvin Gardens", "Go to Jail!",
         "Pacific Ave", "North Carolina Ave", "Community Chest", "Pacific Ave", "Short Line", "Chance", "Park Place", "Luxury Tax", "Boardwalk"]

locationPos = 0;

boardLocation = board[0];

temp = 'a'
while temp != 'q':

    print("Currently on: " + str(board[locationPos]))
    print("Rolling...");

    die_one = random.randint(1,6);
    die_two = random.randint(1,6);

    roll_total = die_one + die_two;
    
    print("You rolled a " + str(roll_total) + "!");

    if (locationPos + roll_total) < 40:
        locationPos += roll_total
    elif (locationPos + roll_total) >= 40:
        print("You passed GO! You get $200!");
        locationPos = (locationPos + roll_total - 40)
        
    boardLocation = board[locationPos]
    print("You advanced to: " + str(board[locationPos]))

    if die_one == die_two:
        print("Doubles! Roll again!")
        die_one = random.randint(1,6);
        die_two = random.randint(1,6);

        roll_total = die_one + die_two;
        
        print("You rolled a " + str(roll_total) + "!");

        if (locationPos + roll_total) < 40:
            locationPos += roll_total
        elif (locationPos + roll_total) >= 40:
            locationPos = (locationPos + roll_total - 40);
            print("You passed GO! You get $200!");
            
        boardLocation = board[locationPos]
        print("You advanced to: " + str(board[locationPos]))
    temp = input("q to quit");
