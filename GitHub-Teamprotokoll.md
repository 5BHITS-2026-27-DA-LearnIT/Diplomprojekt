# Besprechungsprotokoll: Offene Team-Issues

**Projekt:** LearnIT – Diplomarbeit 5BHITS 2026/27
**Issues:** Repo `Diplomarbeit`, alle offenen Issues mit mehreren Zuständigen

Datum: ______________

Anwesend: [ ] Luca  [ ] Jakob  [ ] Jai  [ ] Betreuer: ______________

Ankreuzen: `[ ]` zu `[x]` ändern.

---

## #5 Auslieferung Frontend/API: gleiche Adresse oder getrennt?
*Zuständig: Jai, Luca, Jakob. Hängt mit #24 (Build/Deployment) zusammen.*

- [ ] **Gleiche Adresse:** nginx liefert das Frontend und `/api` unter einer Domain aus. Login über Session + CSRF, kein CORS nötig (Empfehlung).
- [ ] **Getrennte Adressen:** Login über Token, CORS muss eingerichtet werden.

Frontend wird ausgeliefert als:
- [ ] Statischer Build, den nginx ausliefert
- [ ] Eigener Container mit Node-Server

Notizen: ____________________________________________

---

## #2 API-Vertrag festlegen
*Zuständig: Luca (Lead), Jakob. Sollte laut Kapiteln am 15.11. stehen.*

Endpunkte für den Meilenstein (ankreuzen, was dazugehört):
- [ ] Login / Logout
- [ ] Aktueller Benutzer
- [ ] Liste der Lerninhalte
- [ ] Lernkarten eines Lerninhalts
- [ ] Fällige Karten
- [ ] Bewertung einer Karte abschicken
- [ ] Weitere: ______________

Fehlerformat:
- [ ] Standardformat von Django REST Framework (`{"detail": "..."}` bzw. Fehler pro Feld)
- [ ] Eigenes einheitliches Format: ______________

Wo wird der Vertrag abgelegt?
- [ ] Automatisch erzeugtes OpenAPI-Schema (#15), Jakob erzeugt daraus die TypeScript-Typen (#23)
- [ ] Zusätzlich eine kurze Doku im Repo

Notizen: ____________________________________________

---

## #3 Algorithmus für Lernkarten
*Zuständig: Luca, Jai, Abstimmung mit Jakob. Legt fest, wie viele Bewertungsbuttons das Frontend hat.*

- [ ] **SM-2** für den Meilenstein (Bewertung 0–5), FSRS später prüfen (Empfehlung)
- [ ] **FSRS** gleich von Anfang an (4 Stufen), Version: ______________

Buttons im Frontend:
- [ ] Alle 6 Stufen (0–5) als einzelne Buttons
- [ ] Weniger Buttons, die auf SM-2-Werte abgebildet werden: ______________

Notizen: ____________________________________________

---

## #4 Offene Punkte der Datenbankstruktur
*Zuständig: Jai (Lead), Luca, Jakob. Danach: ER-Diagramm (#30, Jai) und Modelle (#11, Luca) anpassen.*

Bekommen Testaufgaben auch einen Wiederholungsstatus?
- [ ] Ja
- [ ] Nein, nur Lernkarten

Lernergebnis:
- [ ] Ein gemeinsames Modell für Lernkarte und Testaufgabe
- [ ] Zwei getrennte Modelle

Gamification-Daten (Punkte, Level, Abzeichen, Streak):
- [ ] Werden im Backend gespeichert
- [ ] Werden aus vorhandenen Daten berechnet
- [ ] Vorerst keine Gamification

Was passiert, wenn ein Benutzer gelöscht wird?
- [ ] Seine Daten werden mitgelöscht
- [ ] Seine Daten werden anonymisiert
- [ ] Erst nach Rücksprache mit Betreuern (#7)

Notizen: ____________________________________________

---

## #6 Ranglisten ja/nein (Datenschutz)
*Zuständig: Jakob, Luca*

- [ ] Keine Ranglisten (zumindest am Anfang)
- [ ] Ranglisten nur mit Zustimmung der Schüler
- [ ] Ranglisten ohne Namen (anonym)

Notizen: ____________________________________________

---

## #7 Datenschutz-Fragen an Betreuer
*Zuständig: Luca (Hauptverantwortlicher), alle*

Fragen, die mitgenommen werden:
- [ ] Wer ist Verantwortlicher im Sinne der DSGVO?
- [ ] Auf welcher Rechtsgrundlage werden die Daten verarbeitet?
- [ ] Wie lange werden die Daten aufbewahrt?
- [ ] Löschen oder Anonymisieren von Benutzern (aus #4)
- [ ] Ranglisten erlaubt? (aus #6)

Termin mit Johannes Fischer / Franz Schweiberer:
- [ ] Vereinbart am: ______________
- [ ] Noch offen, macht: ______________

Antworten: ____________________________________________

---

## #8 Einheitliche Begriffe im Dokument
*Zuständig: alle*

- [ ] „Benutzer“ / „Schüler“
- [ ] „Benutzer:innen“ / „Lernende“
- [ ] Andere Variante: ______________

Notizen: ____________________________________________

---

## #1 Meilenstein 29.11.2026 „Startfähiges System“
*Zuständig: alle. Nur Statuscheck, die Entscheidungen oben sind Voraussetzung.*

- [ ] Wird bis 29.11. erreicht
- [ ] Wird nicht erreicht, neuer Termin: ______________

Was fehlt noch: ____________________________________________

---

## Aufgaben nach der Besprechung

| Aufgabe | Zuständig | Bis |
|---|---|---|
| Entscheidungen als Kommentar in die Issues schreiben und Issues schließen | | |
| | | |
| | | |
