# Daten des Spielfeldes
field = ["",
         "1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

# Definierte Variablen.
active_player = "X"
run = True


# Spielfeld erzeugen
def print_field():
    print(field[1] + "|" + field[2] + "|" + field[3])
    print(field[4] + "|" + field[5] + "|" + field[6])
    print(field[7] + "|" + field[8] + "|" + field[9])


# Spielzug umsetzen - Endlosschleife - Spieler können nur Zahlen zwischen 1-9 eingeben.
# Spieler dürfen sich nicht gegenseitig erneut die exakten Felder belegen.
def next_move():
    while True:
        player_move = input("Bitte gebe eine Zahl zwischen 1-9 ein: ")
        player_move = int(player_move)
        if player_move >= 1 and player_move <= 9:
            if field[player_move] == "X" or field[player_move] == "Y":
                print("Die Felder sind bereits belegt. Bitte wähle ein anderes Feld...")
            else:
                return player_move  # Die Funktion endet hier.
        else:
            print("Die Zahl liegt nicht in dem von mir definerten Rahmenbereich")


# Spielerwechsel - Hier definiere ich den zweiten Spieler namens "Y"
def change_player():
    global active_player
    if active_player == "X":
        active_player = "Y"
    else:
        active_player = "X"


# Gewinner-Ermittlung implementieren - prüfen, ob die jeweiligen Felder mit dem selben Spielersymbol hinterlegt sind.
def check_win():
    # Zeile prüfen:
    if field[1] == field[2] == field[3]:
        return field[1]  # Irgend ein Element an den Funktionsaufrufer schicken, damit dieser weiß, welches Spieler-
    # symbol auf dieses Spielerfeld liegt.

    if field[4] == field[5] == field[6]:
        return field[5]

    if field[7] == field[8] == field[9]:
        return field[9]

    # Spalte prüfen:
    if field[1] == field[4] == field[7]:
        return field[1]
    if field[2] == field[5] == field[8]:
        return field[8]
    if field[3] == field[6] == field[9]:
        return field[9]

    # Diagonale
    if field[1] == field[5] == field[9]:
        return field[9]
    if field[3] == field[5] == field[7]:
        return field[5]


# Funktionsaufrufe - Endlosschleife: Damit die Funktionen nicht nach einem Aufruf beendet werden.
# Spieler-Symbol: Ich weise, die von den Spielern auserwählten Felder, das Symbol des Spielers zu.
# Falls jemand das Spiel gewinnt, soll das Programm beendet werden - True verpacke ich in einer Variable, damit die
# Schleife variable wird. - If-Anweisung einbauen mit einer weiteren Variable.
while run:
    print_field()
    player_move = next_move()
    field[player_move] = active_player
    winner = check_win()
    if winner:  # Wenn in dieser Variable nur irgend einen Wert beinhaltet, wird diese Variable wie ein True gewertet.
        print("Der Spieler " + winner + " hat gewonnen!")
        run = False  # Spiel wird beendet, wenn die Schleife auf False ist und somit nicht mehr läuft.
    change_player()
