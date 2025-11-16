# Learnote

Ein kleines CLI‑Programm zum Verwalten von Lernnotizen.  
Alle Daten werden als JSON‑Liste in einer Datei namens `learnote.json` gespeichert.

![Demo GIF](Assets/consolepycharm.gif)

---

## Inhaltsverzeichnis
1. [Installation](#installation)
2. [Benutzung](#benutzung)
3. [Datenstruktur](#datenstruktur)
4. [Fehlerbehandlung](#fehlerbehandlung)
5. [Lizenz](#lizenz)

---

## Installation

```bash
git clone https://github.com/BenjoKnista/learnote.git
cd learnote
```

Du brauchst lediglich Python 3 (empfohlen 3.10+).  
Alternativ kannst du die einzelne Datei `learnote.py` herunterladen und in ein beliebiges Verzeichnis legen.

---

## Benutzung

Starte das Programm:

```bash
python learnote.py
```

### Menü‑Optionen

| Option | Aktion |
|--------|--------|
| **1**  | Thema hinzufügen |
| **2**  | Alle Themen anzeigen (Programm beendet sich danach) |
| **3**  | Ein bestimmtes Thema löschen |
| **4**  | Programm beenden |

#### Beispiel: Thema hinzufügen
```
Titel: Mathe 101
Beschreibung: Grundlagen der Algebra
Gespeichert!
```

---

## Datenstruktur

Die Datei `learnote.json` hat das folgende Format:

```json
[
    {
        "titel": "Mathe 101",
        "beschreibung": "Grundlagen der Algebra"
    },
    {
        "titel": "Geschichte",
        "beschreibung": "Römisches Reich"
    }
]
```

---

## Fehlerbehandlung

- Wenn `learnote.json` nicht existiert, wird eine leere Liste erzeugt und du wirst informiert.

---

## Lizenz

Dieses Projekt steht unter der MIT‑Lizenz. Weitere Details findest du in der `LICENSE`‑Datei.

--- 

