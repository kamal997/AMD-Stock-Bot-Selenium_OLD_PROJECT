# AMD-Stock-Bot

Ein Python-Skript, das mit Selenium erstellt wurde, um den Lagerbestand eines AMD-Produkts zu überwachen und Benachrichtigungen auszulösen, wenn das Produkt verfügbar ist. Zusätzlich kann es eine Discord-Benachrichtigung senden, indem es einen Anruf in Discord startet.

## Voraussetzungen

Stellen Sie sicher, dass die folgenden Komponenten auf Ihrem System installiert sind:

- Python 3.x
- Selenium
- Google Chrome und der passende ChromeDriver

## Installation

1. **Repository klonen:**
   ```bash
   git clone https://github.com/kamal997/AMD-Stock-Bot-Selenium_OLD_PROJECT.git
   ```

2. **Erforderliche Python-Bibliotheken installieren:**
   ```bash
   pip install selenium
   ```

3. **ChromeDriver herunterladen:**
   Laden Sie die passende Version des [ChromeDrivers](https://chromedriver.chromium.org/downloads) herunter und platzieren Sie die Datei in Ihrem Projektverzeichnis.
   
4. **ChromeDriver-Pfad anpassen:**
   Aktualisieren Sie den Pfad in der Zeile, in der `webdriver.Chrome` im Skript aufgerufen wird, falls notwendig.

## Nutzung

1. **Persönliche Daten eintragen:**
   Öffnen Sie die Datei und ersetzen Sie die folgenden Platzhalter mit Ihren persönlichen Daten:
   - `your_email@example.com`: Ihre Discord-Login-E-Mail.
   - `password`: Ihr Discord-Passwort.

2. **Skript starten:**
   ```bash
   python main.py
   ```

3. **Funktionsweise:**
   - Das Skript überprüft regelmäßig die Verfügbarkeit des AMD-Produkts.
   - Wenn das Produkt auf Lager ist, wird eine Benachrichtigung über Discord gesendet.
   - Wenn das Produkt nicht auf Lager ist, wird eine andere Website zur Bestätigung besucht, bevor der Prozess erneut gestartet wird.

## Funktionsweise

1. Das Skript meldet sich bei Discord an.
2. Es ruft die AMD-Produktseite auf und prüft den Lagerstatus:
   - **Auf Lager:** Eine Benachrichtigung wird über Discord gesendet.
   - **Nicht auf Lager:** Das Skript besucht eine alternative Website, wartet und wiederholt den Vorgang.
3. Der gesamte Prozess wird in einer Endlosschleife ausgeführt.

## Sicherheitshinweise

- Vermeiden Sie die Verwendung Ihres echten Discord-Passworts im Skript. Nutzen Sie stattdessen **Umgebungsvariablen** oder andere sichere Methoden zur Passwortverwaltung.
- Verwenden Sie dieses Skript nur für den persönlichen Gebrauch und beachten Sie die Nutzungsbedingungen der überwachten Websites.

## Haftungsausschluss

Dieses Skript dient ausschließlich Bildungszwecken. Der Entwickler übernimmt keine Verantwortung für die Verwendung des Skripts oder für Verstöße gegen die Nutzungsbedingungen von Websites.


## 🚀 **Lizenz**

Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).
