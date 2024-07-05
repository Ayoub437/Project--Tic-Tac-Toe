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
# Abbruchbedingung - Spieler können das Spiel beenden, bei der Eingabe des Wortes "q".
def next_move():
    global run
    while True:
        player_move = input("Bitte gebe eine Zahl zwischen 1-9 ein: ")
        if player_move == "q":
            run = False
            return player_move
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


# Unentschieden prüfen - Wenn jedes Feld nicht mit den Zahlen, sondern mit den Symbolen der Spieler belegt ist.
def check_draw():
    if field[1] != "1" and field[2] != "2" and field[3] != "3" and field[4] != "4" and field[5] != "5" \
     and field[6] != "6" and field[7] != "7" and field[8] != "8" and field[9] != "9":
        return True


# Funktionsaufrufe - Endlosschleife: Damit die Funktionen nicht nach einem Aufruf beendet werden.
# Spieler-Symbol: Ich weise, die von den Spielern auserwählten Felder, das Symbol des Spielers zu.
# Falls jemand das Spiel gewinnt, soll das Programm beendet werden - True verpacke ich in einer Variable, damit die
# Schleife variable wird. - If-Anweisung einbauen mit einer weiteren Variable.
while run:
    print_field()
    player_move = next_move()
    if player_move == None:
        field[player_move] = active_player   # Wert None wird in player_move gespeichert, wenn ein Spieler "q" eingibt.
        if check_draw():
            print("Das Spiel ist unentschieden ausgegangen!")
            run = False  # Die Schleife und somit das Spiel wird beendet, da dies keine Endlosschleife mehr ist.
        winner = check_win()
        if winner:  # Wenn in dieser Variable nur irgend einen Wert beinhaltet ist, wird diese Variable wie ein True
            # gewertet.
            print("Der Spieler " + winner + " hat gewonnen!")
            run = False  # Spiel wird beendet, wenn die Schleife auf False ist und somit nicht mehr läuft.
        change_player()
