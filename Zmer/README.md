# Typewriter.at Bot Generator

Ein kleines Automatisierungstool für die österreichische Tipptrainer-Webseite [Typewriter.at](https://www.typewriter.at). 

Dieses Tool generiert maßgeschneiderten JavaScript-Code, der in die Entwicklerkonsole des Browsers eingefügt werden kann, um dort Lektionen automatisch "abzutippen". Das Besondere daran ist die **Kalibrierungs-Funktion (Tipp-Leistungstest)**: Das Python-Skript misst zunächst die reale Tippgeschwindigkeit und die echten Fehler des Nutzers, um daraus ein Javascript zu generieren, das das menschliche Verhalten nahezu perfekt imitiert und so Anti-Cheat-Maßnahmen umgeht.

![Screenshot](.github/screenshot.png) (Füge hier nach dem Upload ein Bild deines Tools ein)

## Features

- **🎯 Tipp-Leistungstest:** Ermittelt automatisch deine individuelle minimale und maximale Anschlagsgeschwindigkeit sowie deine Fehlerquote.
- **⚡ JavaScript Generator:** Erzeugt den passenden Code auf Knopfdruck.
- **🛡️ Realistisches Tippen:** Baut simulierte Fehler ein, die danach "verbessert" werden, um komplett natürlich zu wirken.
- **📋 One-Click Copy:** Einfacher Button, um den fertigen Code direkt in die Zwischenablage zu kopieren.
- **❓ Integrierte Hilfe:** Schritt-für-Schritt Anleitung direkt im Programm.

## Voraussetzungen

Um das Generator-Tool lokal auszuführen, benötigst du **Python 3.x**. 
Es werden keine externen Bibliotheken benötigt (das Interface nutzt das in Python integrierte `tkinter`).

## Ausführung

Lade das Repository herunter oder klone es und führe die Python-Datei aus:

```bash
python typewriter_generator.py
```

## Nutzung (Schritt für Schritt)

1. **Kalibrierung (Empfohlen):** Starte das Tool und klicke auf "🎯 Tipp-Leistungstest". Tippe den vorgegebenen Text ab. Das Tool berechnet deine echten Werte und trägt sie ein.
2. **Generieren:** Klicke auf "⚡ Code Generieren".
3. **Kopieren:** Klicke auf "📋 Code Kopieren".
4. **Auf Typewriter.at anwenden:**
   - Öffne eine Übung auf Typewriter.at (im Browser).
   - Öffne die Entwicklerkonsole (Taste `F12`).
   - Gehe zum Reiter "Konsole" (Console).
   - Füge den Code in das Eingabefeld ein (`Strg` + `V`) und drücke `Enter`.
   - Zurücklehnen und zuschauen, wie der Bot die Arbeit erledigt! 😎

## Wichtige rechtliche Hinweise & Disclaimer

Dieses Tool wurde ausschließlich zu **Lern- und Bildungszwecken** im Bereich der Programmierung (Python GUI + JavaScript DOM Interaktion) erstellt. 
**Die Nutzung auf der echten Website erfolgt auf eigene Gefahr.** Der Entwickler übernimmt keine Haftung für eventuell gesperrte Accounts oder andere Konsequenzen, die durch die Nutzung dieses Scripts auf der Plattform Typewriter.at entstehen. Bitte beachte die Nutzungsbedingungen der Webseite.

## Lizenz

MIT License
