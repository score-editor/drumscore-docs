**Hinweis:** Diese Datenschutzerklärung ist eine Übersetzung zur Information. Im Konfliktfall ist die englische Fassung maßgeblich.

# Datenschutzerklärung für DrumScore Editor

**WICHTIGER HINWEIS:** Dies ist eine KI-generierte Referenzübersetzung und MUSS von einem professionellen Übersetzer oder zweisprachigen Juristen überprüft werden, bevor sie rechtlich verwendet wird. Im Konfliktfall ist die englische Fassung maßgeblich.

**Datum des Inkrafttretens:** 17. November 2025  
**Version:** 1.0

Alan White („wir", „uns" oder „unser") betreibt DrumScore Editor („die Software"). Diese Datenschutzerklärung erläutert, wie wir Informationen sammeln, verwenden und schützen, wenn Sie die Software nutzen.

---

## 1. Von Uns Erfasste Informationen

### 1.1 Lokal Gespeicherte Informationen

Die Software speichert die folgenden Informationen **ausschließlich lokal auf Ihrem Gerät**:

- **Benutzereinstellungen:** Anwendungseinstellungen, Theme-Auswahl, Spracheinstellungen, Anzeigeoptionen
- **Lizenzinformationen:** Ihr Lizenzschlüssel (verschlüsselt), Name des Lizenznehmers und E-Mail-Adresse
- **Musikpartituren:** Alle Kompositionen und Arrangements, die Sie erstellen
- **Zuletzt Verwendete Dateien:** Pfade zu kürzlich geöffneten Dateien
- **Fensterpositionen:** Größe und Position der Anwendungsfenster

**Diese Daten verlassen niemals Ihren Computer**, es sei denn, Sie entscheiden sich ausdrücklich dafür, Dateien zu teilen oder die unten beschriebenen optionalen Funktionen zu aktivieren.

### 1.2 Anonyme Nutzungsanalysen (Optional)

Ab Version [X.X] enthält die Software optionale anonyme Nutzungsanalysen. Wenn aktiviert, erfassen wir:

**Was wir erfassen:**
- Verwendete Funktionen und deren Nutzungshäufigkeit
- Softwareversion und Betriebssystem
- Sitzungsdauer
- Absturzberichte und Fehlerprotokolle
- Allgemeine Workflow-Muster (z. B. „Benutzer hat Volta erstellt", „Benutzer hat in PDF exportiert")

**Was wir NICHT erfassen:**
- Ihren Namen, E-Mail oder Lizenzinformationen
- Ihre musikalischen Kompositionen oder Partiturinhalte
- Dateinamen, Pfade oder Dateimetadaten
- IP-Adressen oder Gerätekennungen
- Personenbezogene Daten jeglicher Art

**Anonyme Kennung:** Wir generieren eine zufällige anonyme ID (UUID), die lokal gespeichert wird, um uns zu helfen, Nutzungsmuster zu verstehen, ohne Sie persönlich zu identifizieren.

**Deaktivierung:** Sie können die Analysedatenerfassung jederzeit in Einstellungen → Datenschutz deaktivieren. Diese Einstellung wird sofort respektiert.

### 1.3 Update-Prüfung (Optional)

Die Software kann regelmäßig nach verfügbaren Updates suchen. Wenn aktiviert, übermittelt die Update-Prüfung:

- Ihre aktuelle Softwareversion
- Betriebssystemtyp und -version

**Bei Update-Prüfungen werden keine personenbezogenen Daten übermittelt.**

**Deaktivierung:** Sie können die automatische Update-Prüfung in Einstellungen → Updates deaktivieren.

---

## 2. Wie Wir Informationen Verwenden

### 2.1 Lokale Daten
Lokal gespeicherte Einstellungen und Dateien werden ausschließlich verwendet, um:
- Die Kernfunktionalität der Software bereitzustellen
- Ihre Einstellungen zwischen Sitzungen zu speichern
- Ihre Lizenz offline zu validieren
- Von Ihnen konfigurierte Funktionen zu aktivieren

### 2.2 Anonyme Analysen
Anonyme Nutzungsdaten werden verwendet, um:
- Zu verstehen, welche Funktionen am wertvollsten sind
- Verbesserungsbereiche zu identifizieren
- Entwicklungsbemühungen zu priorisieren
- Fehler zu erkennen und zu beheben
- Die allgemeine Benutzererfahrung zu verbessern

### 2.3 Update-Informationen
Update-Prüfungsdaten werden ausschließlich verwendet, um:
- Sie über verfügbare Updates zu informieren
- Kompatibilität mit Ihrem Betriebssystem sicherzustellen
- Das Update-Bereitstellungssystem zu verbessern

---

## 3. Datenspeicherung und Sicherheit

### 3.1 Lokale Speicherung
Ihre Einstellungen, Partituren und Lizenzinformationen werden unter Verwendung der Java Preferences API und Dateisystemspeicherung auf Ihrem Computer gespeichert. Lizenzschlüssel werden mit branchenüblicher Verschlüsselung (PBEWithMD5AndDES) verschlüsselt.

### 3.2 Analysedaten
Wenn Sie Analysen aktivieren, werden anonyme Daten über HTTPS an unseren sicheren Server übertragen und zur Analyse gespeichert. Diese Daten können nicht mit Ihnen persönlich in Verbindung gebracht werden.

### 3.3 Keine Cloud-Speicherung
Wir speichern Ihre musikalischen Kompositionen oder persönlichen Daten nicht in einem Cloud-Dienst. Ihre Arbeit verbleibt auf Ihrem Gerät, es sei denn, Sie entscheiden sich, sie zu exportieren oder zu teilen.

---

## 4. Datenweitergabe und Dritte

### 4.1 Kein Verkauf von Daten
Wir verkaufen, vermieten oder handeln keine von der Software erfassten Informationen.

### 4.2 Drittanbieterdienste
Die Software integriert sich nicht mit Drittanbieter-Analysediensten, Werbenetzwerken oder Datenbrokern.

### 4.3 Gesetzliche Anforderungen
Wir können Informationen offenlegen, wenn dies gesetzlich vorgeschrieben ist, durch gerichtliche Anordnung oder zum Schutz unserer Rechte. Da wir jedoch minimale Daten erfassen und die meisten lokal gespeichert werden, gibt es sehr wenig, was wir offenlegen könnten.

---

## 5. Ihre Rechte und Wahlmöglichkeiten

### 5.1 Zugriff auf Ihre Daten
Alle Ihre Daten werden lokal auf Ihrem Gerät gespeichert. Sie haben vollständigen Zugriff auf:
- Ihre Musikpartituren (in Ihrem Dateisystem)
- Ihre Einstellungen (über das Menü Einstellungen)
- Ihre Lizenzinformationen (über den Lizenzdialog)

### 5.2 Löschen Ihrer Daten
Sie können jederzeit alle Daten löschen:
- **Partituren:** Löschen Sie Dateien aus Ihrem Dateisystem
- **Einstellungen:** Setzen Sie auf Standardwerte im Menü Einstellungen zurück
- **Lizenz:** Entfernen Sie die Lizenz mit dem Befehl: `DrumScoreEditor removeLicense`
- **Analysen:** Deaktivieren Sie in den Einstellungen (vergangene Daten können ohnehin nicht mit Ihnen verknüpft werden)

### 5.3 Deaktivierung von Analysen und Updates
Sowohl anonyme Analysen als auch Update-Prüfungen sind **Opt-out**:
1. Öffnen Sie Einstellungen → Datenschutz
2. Deaktivieren Sie „Anonyme Nutzungsstatistiken senden"
3. Deaktivieren Sie „Automatisch nach Updates suchen"

Änderungen werden sofort wirksam.

---

## 6. Datenschutz für Kinder

Die Software richtet sich nicht an Kinder unter 13 Jahren. Wir sammeln wissentlich keine Informationen von Kindern. Wenn wir erfahren, dass wir Informationen von einem Kind unter 13 Jahren gesammelt haben, werden wir diese umgehend löschen.

---

## 7. Internationale Nutzer

Die Software wird in Schottland (Vereinigtes Königreich) entwickelt, aber international genutzt. Durch die Nutzung der Software:
- Verbleiben lokal gespeicherte Daten auf Ihrem Gerät in Ihrer Rechtsordnung
- Werden anonyme Analysen (falls aktiviert) an Server im Vereinigten Königreich/EU übertragen
- Stimmen Sie der Verarbeitung anonymer Daten gemäß den Datenschutzstandards des Vereinigten Königreichs/der EU zu

### 7.1 DSGVO-Rechte (EU-Nutzer)
Wenn Sie sich in der Europäischen Union befinden, haben Sie Rechte gemäß der DSGVO:
- **Recht auf Auskunft:** Sie können auf alle lokal gespeicherten Daten zugreifen
- **Recht auf Löschung:** Sie können alle Daten jederzeit löschen
- **Widerspruchsrecht:** Sie können Analysen widersprechen
- **Recht auf Datenübertragbarkeit:** Ihre Partituren liegen im offenen MusicXML-Format vor

Da wir minimale anonyme Daten erfassen und die meisten Daten lokal gespeichert werden, werden diese Rechte weitgehend bereits durch das Design der Software erfüllt.

---

## 8. Datenaufbewahrung

### 8.1 Lokale Daten
Auf Ihrem Gerät gespeicherte Daten bleiben bestehen, bis Sie sie löschen. Wir haben keinen Zugriff auf diese Daten und keine Kontrolle darüber.

### 8.2 Anonyme Analysen
Falls erfasst, werden anonyme Analysedaten 24 Monate lang aufbewahrt und danach automatisch gelöscht.

### 8.3 Update-Prüfungsprotokolle
Update-Prüfungsprotokolle werden zu Fehlerbehebungszwecken 90 Tage lang aufbewahrt und dann automatisch gelöscht.

---

## 9. Sicherheit

### 9.1 Lokale Sicherheit
Die Sicherheit Ihres Geräts liegt in Ihrer Verantwortung. Wir empfehlen:
- Verwendung starker Gerätepasswörter
- Aktuellhalten Ihres Betriebssystems
- Verwendung von Antivirensoftware
- Regelmäßige Sicherung Ihrer Partituren

### 9.2 Übertragungssicherheit
Alle von der Software übertragenen Daten (Update-Prüfungen, Analysen) verwenden HTTPS-Verschlüsselung.

### 9.3 Lizenzschlüssel-Verschlüsselung
Lizenzschlüssel werden in verschlüsseltem Format auf Ihrem Gerät gespeichert.

---

## 10. Änderungen an Dieser Datenschutzerklärung

### 10.1 Sprache
Diese Datenschutzerklärung ist ursprünglich in englischer Sprache verfasst. Übersetzungen werden der Bequemlichkeit halber bereitgestellt, aber im Falle eines Konflikts oder einer Abweichung zwischen der englischen Version und einer Übersetzung hat die englische Version Vorrang und ist maßgeblich.

### 10.2 Aktualisierungen
Wir können diese Datenschutzerklärung von Zeit zu Zeit aktualisieren. Änderungen werden unter drumscore.scot/privacy mit einem aktualisierten „Datum des Inkrafttretens" veröffentlicht.

**Wesentliche Änderungen** (solche, die sich darauf auswirken, wie wir Daten erfassen oder verwenden) werden in den Software-Versionshinweisen hervorgehoben.

**Die fortgesetzte Nutzung** der Software nach Veröffentlichung von Änderungen stellt die Annahme der aktualisierten Datenschutzerklärung dar.

---

## 11. Kontakt

Wenn Sie Fragen zu dieser Datenschutzerklärung oder zur Handhabung Ihrer Daten haben:

**E-Mail:** alan@drumscore.scot  
**Website:** https://drumscore.scot  
**Adresse:** [Ihre Geschäftsadresse, falls nach lokalem Recht erforderlich]

---

## 12. Zusammenfassung

**In Einfachem Deutsch:**

- ✅ Ihre Partituren und Daten bleiben auf Ihrem Computer
- ✅ Wir sammeln minimale, anonyme Nutzungsstatistiken (wenn Sie es erlauben)
- ✅ Sie können alles jederzeit deaktivieren
- ✅ Wir verkaufen Ihre Daten nicht
- ✅ Wir verwenden keine Drittanbieter-Tracker
- ✅ Ihr Lizenzschlüssel ist verschlüsselt
- ✅ Keine Cloud-Speicherung Ihrer Arbeit

**Fragen?** Kontaktieren Sie uns unter alan@drumscore.scot

---

**Durch die Nutzung von DrumScore Editor bestätigen Sie, dass Sie diese Datenschutzerklärung gelesen und verstanden haben.**