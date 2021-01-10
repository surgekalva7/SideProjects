def getOTTotal(scores,round)->int:
    total =0
    if (round > 10):
        if (scores[11] == "10"):
            total += 10
            if (scores[12] == "10"):
                total += 20
            elif(len(scores[12]) >= 3):
                temp = scores[12].split(":")
                total += int(temp[0]) + int(temp[1])
            else:
                total+=int(scores[12])
        elif (len(scores[11]) >= 3):
            temp = scores[11].split(":")
            total += int(temp[0]) + int(temp[1])
        else:
            total += int(scores[11])
    return total

def getTotal(scores,round)->int:
    total = 0
    temp = []
    for i in range(1,11):
            temp = scores[i]
            temp_array = temp.split(":")
            if (len(temp_array) == 1 and temp_array[0] == "10"):
                total += 10
                if(i+1<=10):
                    if (len(scores[i + 1]) == 2):
                        total += 10
                        if(i+2<=10):
                            if (len(scores[i + 2]) == 2):
                                total += 10
                            else:
                                total += int(scores[i + 2][0])
                    else:
                        if (len(scores[i + 1]) > 1):
                            total += int(scores[i + 1][0]) + int(scores[i + 1][2])
            elif (len(temp_array) == 1 and temp_array[0] == "0"):
                total += 0
            elif (int(temp_array[0]) + int(temp_array[1]) == 10):
                if(i+1<=10):
                    temp2_array = scores[i + 1].split(":")
                    total += 10 + int(temp2_array[0])
                else:
                    total+=10
            else:
                total += int(temp_array[0]) + int(temp_array[1])




    return total

def getNames(number)->str:
    name = input("What is the name of player {}: ".format(number))
    while(len(name)>8 and not len(name)==0):
        name = input("What is the name of player {}, please make sure that it is under 8 characters: ".format(number))
    return name
def isValidBowl(num1,num2)->bool:
    state = False
    if(num1.isdigit() and num2.isdigit()):
        if(int(num1)>=0 and int(num2)>=0):
            if(int(num1)+int(num2)<=10):
                state = True
    return state

def bowl(playername,player_bowl,round)->str:
    value = ""
    bowl1 = "0"
    bowl2 = "0"
    bowl1 = input("Frame {}: How many pins did {}'s first bowl knock down: ".format(round,playername))
    while not (isValidBowl(bowl1,bowl2)):
        bowl1 = input("Frame {}: How many pins did {}'s first bowl knock down, please indicate the proper value: ".format(round,playername))
    if(bowl1 =="10"):
        value = "X"
        player_bowl[round]="{}".format(bowl1)
    else:
        bowl2 =  input("Frame {}: How many pins did {}'s second bowl knock down: ".format(round,playername))
        while not (isValidBowl(bowl1, bowl2)):
            bowl2 = input(
                "Frame {}: How many pins did {}'s second bowl knock down, please indicate the proper value: ".format(round,playername))
        if(int(bowl1)+int(bowl2)==10):
            value = "/"
        else:
            value = "{}".format(int(bowl1)+int(bowl2))
        player_bowl[round]="{}:{}".format(bowl1,bowl2)
    return value

def sparebowl(playername,player_bowl,round)->str:
    bowl2 = "0"
    bowl1 = input("Frame {}: How many pins did {}'s first bowl knock down: ".format(round,playername))
    while not (isValidBowl(bowl1, bowl2)):
        bowl1 = input(
            "Frame {}: How many pins did {}'s first bowl knock down, please indicate the proper value: ".format(round,playername))
    if(bowl1 == "10"):
        value = "X"
        player_bowl[round] = "{}".format(bowl1)
    else:
        value = "{}".format(int(bowl1) + int(bowl2))
        player_bowl[round] = "{}:{}".format(bowl1,bowl2)
    return value

def isValid(x)->bool:
    state = False
    if(x.isdigit()):
        temp = int(x)
        if(temp<11 and temp >=0):
            state = True
    return state

def displayScores(players,round,num,playersbowl):
    word = ("  Name  |")
    for r in range(round):
        word += ("  Round {}  |".format(r+1))
    word+=("  Total  |")
    print(word)
    print("-"*len(word))
    temp=""
    for x in range(num):
        name = players[x][0]
        name = name + ((8 - len(name)) * " ")
        temp = "{}|".format(name)
        for r in range(round):
            if(r>=9):
                temp += "     {}      |".format(players[x][r + 1])
            else:
                temp += "     {}     |".format(players[x][r + 1])
        num = 0
        if(round<=10):
            num = getTotal(playersbowl[x], round)
        else:
            num = getOTTotal(playersbowl[x], round)+getTotal(playersbowl[x], round)
        num = "    {}".format(num)+((5-len(str(num)))*" "+"|")
        temp += num
        print(temp)






def main():

    numberofplayers = input("How many people are playing? ")
    while not isValid(numberofplayers):
        numberofplayers = input("How many people are playing? Please input a valid number: ")
    num_players = int(numberofplayers)
    players = []
    players_bowls= []
    for i in range(num_players):
        players += [["0"]*14]
        players_bowls +=[["0"]*14]
        players[i][0] = getNames(i + 1)
        players_bowls[i][0] = players[i][0]
    round = 0
    displayScores(players, round, num_players, players_bowls)
    print("")
    while(round<=9):
        round=round+1
        for t in range(num_players):
            players[t][round]=bowl(players[t][0],players_bowls[t],round)
            displayScores(players, round, num_players, players_bowls)
            if(round==10 and players[t][10]=="X"):
                print("")
                print("")
                players[t][round+1] = bowl(players[t][0], players_bowls[t], round+1)
                displayScores(players, round + 1, num_players, players_bowls)
                if(players[t][11]=="X"):
                    print("")
                    print("")
                    players[t][round + 2] = sparebowl(players[t][0], players_bowls[t], round + 2)
                    displayScores(players, round + 2, num_players, players_bowls)
            elif(round==10 and players[t][10]=="/"):
                print("")
                print("")
                players[t][round + 1] = sparebowl(players[t][0], players_bowls[t], round + 1)
                displayScores(players, round + 1, num_players, players_bowls)

        print("")
        print("")
    displayScores(players, round + 2, num_players, players_bowls)
    print(players)



if __name__ == "__main__":
    main()