import json
import os
import textwrap

jsondatei = "learnote.json"

zu_lernen = []

def laden():
    global zu_lernen
    if os.path.exists(jsondatei):
        datei = open(jsondatei, "r")
        zu_lernen = json.load(datei)
        datei.close()

    else:
        print("Das hat leider nicht geklappt. Eine leere Liste wird nun ausgegeben.")


def speichern():
    global zu_lernen
    datei = open(jsondatei, "w")
    json.dump(zu_lernen, datei)
    datei.close()


def hinzufuegen():
    global zu_lernen
    titel = input("Titel: ")
    beschreibung = input("Beschreibung: ")

    einzelne_themen = {
        "titel": titel,
        "beschreibung": beschreibung,
    }

    zu_lernen.append(einzelne_themen)
    speichern()
    print("Gespeichert!")


def loeschen():
    global zu_lernen

    anzeigen()

    nummer = int(input("Welcher Eintrag soll gelöscht werden: \n"))

    zu_lernen.pop(nummer - 1)
    speichern()
    print("+" * 50)
    print("\nErfolgreich gelöscht!\n")
    print("+" * 50)

def anzeigen():
        print("+++GESPEICHERTE THEMEN")
        nummerierung = 1
        for thema in zu_lernen:
            print(f"{nummerierung}. {thema['titel']}")
            print(textwrap.fill(f"{thema['beschreibung']}", width=60))
            nummerierung += 1


def bearbeiten():
    global zu_lernen

    anzeigen()

    user_input = int(input("Welchen Eintrag möchtest du bearbeiten? ")) -1

    zu_lernen[user_input]["titel"] = input("Neuer Titel: ")
    zu_lernen[user_input]["beschreibung"] = input("Neuer Beschreibung: ")

    speichern()

    print("\nEintrag wurde aktualisiert.")


laden()

while True:
    print("1. Thema hinzufügen")
    print("2. Themen anzeigen")
    print("3. Thema löschen")
    print("4. Themen bearbeiten")
    print("5. Beenden")

    auswahl = input("Deine Wahl: ")

    if auswahl == "1":
        hinzufuegen()
    elif auswahl == "2":
        anzeigen()
        break
    elif auswahl == "3":
        loeschen()
    elif auswahl == "4":
        bearbeiten()
    elif auswahl == "5":
        print("Alles klar! Bis zum nächsten mal!")
        break
    else:
        print("Ungültige Eingabe! Bitte 1 - 3 wählen.")