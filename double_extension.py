import requests

# die Liste aus dem repo enthält extensions für php und asp
response = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/web-extensions.txt")

# splitline() ist Methode des Zeichentyp Strings, teilt inhalt in eine Liste von Zeilen auf
extensions = response.text.splitlines()
# Schleife, welche die liste ausgibt
for i in extensions:
    print(i)

# Umgang mit Dateien erstellt eine Datei, und öffnet diese, das "w" bedeutet im Modus beschreiben
# anschließend am ende einer with-Anweisung wird die Datei automatisch geschlossen
with open("wordlist.txt", "w") as file:
    special_chars = ['%20', '%0a', '%00', '%0d0a', '/', '.\\', '.', '…', ':']

    for char in special_chars:
        for ext in extensions:
            # das f steht für formatieren des strings und ermöglicht, es ermöglicht die 
            # Auswertung innerhalb des String in {}-Klammern 
            # file bezieht sich auf das file-Objekt, welches durch die open()-Funktion erstellt wurde
            # in diesem Fall wordlist.txt
            file.write(f"shell{char}{ext}.jpg\n")
            file.write(f"shell{ext}{char}.jpg\n")
            file.write(f"shell.jpg{char}{ext}\n")
            file.write(f"shell.jpg{ext}{char}\n")