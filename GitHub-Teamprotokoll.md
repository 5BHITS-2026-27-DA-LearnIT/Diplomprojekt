# Protokoll: Nutzung der GitHub-Teamfunktionen

**Projekt:** LearnIT – Diplomarbeit 5BHITS 2026/27
**Organisation:** `5BHITS-2026-27-DA-LearnIT`
**Repos:** `Diplomprojekt` (Code), `Diplomarbeit` (Issues, Kanban, Doku)

| | |
|---|---|
| Datum | ______________ |
| Ort / Form | ☐ Schule ☐ Online ☐ ______________ |
| Anwesend | ☐ Luca (Backend) ☐ Jakob (Frontend) ☐ Jai (Infrastruktur/DB) ☐ Betreuer: ______________ |
| Protokoll | ______________ |

> **Anleitung:** Pro Punkt genau eine Option ankreuzen (außer bei „mehrere möglich“).
> Die Zeile *Stand* zeigt, wie es am 27.11.2026 in GitHub eingestellt war.
> Auf GitHub lassen sich die Kästchen direkt anklicken.

---

## 1. Organisation und Mitglieder

**1.1 Rollen in der Organisation**
*Stand: 5 Mitglieder (JaiKumarDE, jakob-berger-c, JohannesFischerHTL, lucamoldovanHTL, SFranz1976)*
- [ ] Alle drei Schüler sind *Owner*
- [ ] Ein Schüler ist *Owner*, die anderen sind *Member*
- [ ] Betreuer sind ebenfalls *Owner*
- [ ] Betreuer sind *Member* mit Leserechten

**1.2 Basisberechtigung für alle Mitglieder**
*Stand: Read*
- [ ] Read (Schreibrechte nur über Teams)
- [ ] Write (alle dürfen überall pushen)
- [ ] No permission

**1.3 Teams anlegen** (mehrere möglich)
*Stand: keine Teams*
- [ ] Keine Teams, Rechte direkt pro Person
- [ ] Team `entwickler` (Luca, Jakob, Jai) mit Write/Maintain auf beide Repos
- [ ] Team `betreuer` mit Read (für Reviews und Einblick)
- [ ] Fachteams `backend`, `frontend`, `infrastruktur` (für Erwähnungen und Code Owners)

**1.4 Zwei-Faktor-Authentifizierung (2FA)**
*Stand: nicht verpflichtend*
- [ ] Für alle Mitglieder verpflichtend
- [ ] Freiwillig

---

## 2. Repositories

**2.1 Sichtbarkeit**
*Stand: Diplomprojekt ist öffentlich*
- [ ] Öffentlich (Actions-Minuten und Code-Scanning kostenlos)
- [ ] Privat

**2.2 Wiki**
*Stand: aktiviert*
- [ ] Nutzen
- [ ] Deaktivieren, Doku nur als Markdown im Repo `Diplomarbeit`

**2.3 Discussions** (Forum für Fragen und Ideen)
*Stand: deaktiviert*
- [ ] Aktivieren
- [ ] Nicht nutzen, Absprachen über Issues und Kommentare

---

## 3. Branches und Schutzregeln (Rulesets)

> ⚠️ **Hinweis:** Es gibt ein Ruleset „ruleset“ (aktiv, Löschen und Force-Push gesperrt, PR mit 1 Freigabe).
> Es ist aber **keinem Branch zugeordnet** (Zielbranches leer) und wirkt deshalb derzeit nicht.
> `main` ist aktuell ungeschützt.

**3.1 Schutz von `main`**
- [ ] Ruleset auf `main` (Default-Branch) anwenden
- [ ] Kein Schutz, alle pushen direkt auf `main`

**3.2 Änderungen an `main` nur über Pull Request**
- [ ] Ja, immer
- [ ] Nein, kleine Änderungen direkt

**3.3 Notwendige Freigaben (Approvals) pro PR**
*Stand im Ruleset: 1*
- [ ] 0 (PR nur zur Nachvollziehbarkeit)
- [ ] 1
- [ ] 2

**3.4 Zusätzliche Regeln** (mehrere möglich)
- [ ] Force-Push auf `main` verbieten
- [ ] Löschen von `main` verbieten
- [ ] Alle Review-Kommentare müssen erledigt sein
- [ ] Neue Pushes machen bestehende Freigaben ungültig
- [ ] Automatische Prüfungen (Actions) müssen grün sein
- [ ] Code-Owner-Review verpflichtend (siehe 4.4)

**3.5 Branch-Strategie**
- [ ] Feature-Branches von `main` (GitHub Flow)
- [ ] Zusätzlicher `develop`-Branch (Git Flow)

**3.6 Branch-Namen**
- [ ] `<issue-nr>-<kurzbeschreibung>` (z. B. `12-login-api`)
- [ ] `feature/…`, `fix/…`, `docs/…`
- [ ] Keine Vorgabe

---

## 4. Pull Requests und Code-Reviews

**4.1 Merge-Methode**
*Stand: Merge, Squash und Rebase erlaubt*
- [ ] Nur Squash-Merge (ein Commit pro PR)
- [ ] Nur Merge-Commit
- [ ] Alle erlaubt

**4.2 Branch nach dem Merge automatisch löschen**
*Stand: aus*
- [ ] Ja
- [ ] Nein

**4.3 Wer reviewt?**
- [ ] Jeder PR wird von einem anderen Teammitglied reviewt
- [ ] Reviewer je nach Bereich (Backend/Frontend/Infrastruktur)
- [ ] Betreuer bei größeren PRs als Reviewer

**4.4 CODEOWNERS-Datei** (automatische Reviewer-Zuweisung nach Ordner)
- [ ] Ja, z. B. `backend/` → Luca, `frontend/` → Jakob, `docker/` → Jai
- [ ] Nein

**4.5 PR-Vorlage** (`.github/pull_request_template.md`)
- [ ] Ja (Beschreibung, verknüpftes Issue, wie getestet)
- [ ] Nein

**4.6 Issues mit PRs verknüpfen**
- [ ] PR-Beschreibung enthält `Closes 5BHITS-2026-27-DA-LearnIT/Diplomarbeit#<nr>` (schließt das Issue beim Merge)
- [ ] Issue wird von Hand geschlossen

**4.7 Draft-PRs für unfertige Arbeit**
- [ ] Nutzen
- [ ] Nicht nutzen

---

## 5. Issues

**5.1 Wo liegen die Issues?**
*Stand: im Repo `Diplomarbeit`*
- [ ] Alle Issues zentral in `Diplomarbeit`
- [ ] Code-Issues in `Diplomprojekt`, Organisatorisches in `Diplomarbeit`

**5.2 Issue-Vorlagen** (`.github/ISSUE_TEMPLATE/`)
- [ ] Ja: Aufgabe, Fehler (Bug), Dokumentation
- [ ] Nein

**5.3 Labels** (mehrere möglich)
*Stand: nur Standard-Labels von GitHub*
- [ ] Bereich: `backend`, `frontend`, `infrastruktur`, `doku`
- [ ] Art: `bug`, `feature`, `aufgabe`
- [ ] Priorität: `prio:hoch`, `prio:mittel`, `prio:niedrig`
- [ ] Nicht benötigte Standard-Labels löschen

**5.4 Unteraufgaben (Sub-Issues)**
- [ ] Große Aufgaben in Sub-Issues aufteilen
- [ ] Nicht nutzen, stattdessen Checklisten im Issue

**5.5 Zuständigkeit**
- [ ] Jedes Issue hat genau eine zuständige Person (Assignee)
- [ ] Mehrere Assignees erlaubt

**5.6 Meilensteine**
*Stand: im Repo `Diplomarbeit` keine GitHub-Meilensteine angelegt. Geplant: 29.11.2026 „Startfähiges System“*
- [ ] Projekt-Meilensteine als GitHub-Milestones anlegen und Issues zuordnen
- [ ] Nur im Kanban-Board bzw. in der Doku führen

---

## 6. GitHub Projects (Kanban-Board)

*Stand: Org-Project „Kanban“ (Nr. 1) mit Standardfeldern (Status, Assignees, Labels, Milestone, Reviewers, Sub-Issues …)*

**6.1 Spalten (Status)** (mehrere möglich)
- [ ] Todo / In Progress / Done (Standard)
- [ ] Zusätzlich: Backlog
- [ ] Zusätzlich: In Review
- [ ] Zusätzlich: Blockiert

**6.2 Zusätzliche Felder** (mehrere möglich)
- [ ] Priorität
- [ ] Geschätzter Aufwand (Stunden)
- [ ] Iteration / Sprint (Dauer: ____ Wochen)
- [ ] Start- und Enddatum (für Roadmap-Ansicht)

**6.3 Ansichten** (mehrere möglich)
- [ ] Board (Kanban)
- [ ] Tabelle
- [ ] Roadmap (Zeitstrahl)
- [ ] Ansicht „Meine Aufgaben“ pro Person

**6.4 Automatische Workflows** (mehrere möglich)
- [ ] Neue Issues automatisch zum Board hinzufügen
- [ ] Geschlossene Issues automatisch auf „Done“
- [ ] Gemergte PRs automatisch auf „Done“
- [ ] PR geöffnet → „In Review“

**6.5 Insights / Diagramme** (Fortschritt für die Doku)
- [ ] Nutzen (z. B. Burn-up-Diagramm)
- [ ] Nicht nutzen

---

## 7. Automatisierung und Sicherheit

**7.1 GitHub Actions (CI)** (mehrere möglich)
- [ ] Backend-Tests (`manage.py test`) bei jedem PR
- [ ] Linter (z. B. Python: flake8/ruff, Frontend: ESLint)
- [ ] Frontend-Build (`npm run build`) bei jedem PR
- [ ] Docker-Image-Build prüfen
- [ ] Vorerst keine Actions

**7.2 Dependabot**
- [ ] Sicherheitswarnungen (Alerts) aktivieren
- [ ] Zusätzlich automatische Update-PRs
- [ ] Nicht nutzen

**7.3 Secret Scanning und Push Protection** (verhindert z. B. das Hochladen von Passwörtern)
- [ ] Aktivieren
- [ ] Nicht nutzen

**7.4 Code Scanning (CodeQL)**
- [ ] Aktivieren
- [ ] Nicht nutzen

---

## 8. Konventionen und Kommunikation

**8.1 Commit-Nachrichten**
- [ ] Mit Issue-Nummer: `#12 Login-API angelegt`
- [ ] Conventional Commits: `feat: …`, `fix: …`, `docs: …`
- [ ] Keine Vorgabe

**8.2 Sprache** in Issues, PRs und Commits
- [ ] Deutsch
- [ ] Englisch

**8.3 Erwähnungen**
- [ ] `@person` bzw. `@team` in Issues/PRs für Rückfragen nutzen
- [ ] Absprachen hauptsächlich außerhalb von GitHub (Kanal: ______________)

**8.4 Releases / Tags**
- [ ] Pro Meilenstein ein Release (z. B. `v0.1` = Startfähiges System)
- [ ] Keine Releases

---

## 9. Offene Punkte und Aufgaben

| Nr. | Aufgabe | Zuständig | Bis |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

---

## 10. Bestätigung

| Name | Unterschrift |
|---|---|
| Luca Moldovan | |
| Jakob | |
| Jai | |
| Betreuer | |
