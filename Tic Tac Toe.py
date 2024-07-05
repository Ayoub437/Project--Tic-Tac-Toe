# Daten des Spielfeldes
field = ["",
         "1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

# Spielfeld erzeugen
def print_field():
    print(field[1] + "|" + field[2] + "|" + field[3])
    print(field[4] + "|" + field[5] + "|" + field[6])
    print(field[7] + "|" + field[8] + "|" + field[9])


# Spielzug umsetzen - Endlosschleife - Spieler können nur Zahlen zwischen 1-9 eingeben.
def next_move():
    while True:
        player_move = input("Bitte gebe eine Zahl zwischen 1-9 ein: ")
        player_move = int(player_move)
        if player_move >= 1 and player_move <= 9:
            return player_move
        else:
            print("Die Zahl liegt nicht in dem von mir definerten Rahmenbereich")


# Funktionsaufrufe - Endlosschleife: Damit die Funktionen nicht nach einem Aufruf beendet werden.
while True:
    print_field()
    next_move()
