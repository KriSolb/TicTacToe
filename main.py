list_field: list = ["",
                    "1", "2", "3",
                    "4", "5", "6",
                    "7", "8", "9"
                    ]

int_active_player = 1
run = True


def print_field():
    print(list_field[1] + " | " + list_field[2] + " | " + list_field[3])
    print(list_field[4] + " | " + list_field[5] + " | " + list_field[6])
    print(list_field[7] + " | " + list_field[8] + " | " + list_field[9])
    print("")

def move(player):
    global run
    while True:
        field = input("Player " + str(player) + " enter your move: ")

        if field == "q":
            run = False
            return

        field = int(field)

        if 1 <= field <= 9:
            if list_field[field] != "X" and list_field[field] != "O":
                if player == 1:
                    list_field[field] = "X"
                    break
                elif player == 2:
                    list_field[field] = "O"
                    break
                else:
                    print("Player failure")
            else:
                print("Already used")
        else:
            print("Wrong number")

def change_player():
    global int_active_player
    if int_active_player == 1:
        int_active_player = 2
    else:
        int_active_player = 1

def winner():
    if list_field[1] == list_field[2] == list_field[3]:
        return True
    if list_field[4] == list_field[5] == list_field[6]:
        return True
    if list_field[7] == list_field[8] == list_field[9]:
        return True

    if list_field[1] == list_field[4] == list_field[7]:
        return True
    if list_field[2] == list_field[5] == list_field[8]:
        return True
    if list_field[3] == list_field[6] == list_field[9]:
        return True

    if list_field[1] == list_field[5] == list_field[9]:
        return True
    if list_field[3] == list_field[5] == list_field[7]:
        return True

def draw():
    if list_field[1] != "1" and list_field[2] != "2" and list_field[3] != "3" and \
       list_field[4] != "4" and list_field[5] != "5" and list_field[6] != "6" and \
       list_field[7] != "7" and list_field[8] != "8" and list_field[9] != "9":
        return True

while run:
    print_field()
    move(int_active_player)

    if winner():
        print("Player " + str(int_active_player) + " won!")
        print_field()
        run = False
        break

    if draw():
        print("Draw!")
        print_field()
        run = False
        break

    change_player()




