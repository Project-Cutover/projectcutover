<!-- style-gate: allow (sources quoted verbatim) -->
---
slug: rollout
status: draft v2, 2026-10-24, closeout applied (review/waves-4-7-round-2-lead-check-2026-10-24.md § 9). The run paragraph now gives the graded third run and nothing more (§ 9 item 5; agent-brief-test-cutover-workbook-2026-10-24-third.md): the question to Rhys asks where the evidence is too, the notice is quoted as the stakeholders file has it ("Second wave from 1 Feb 2027") without the second grade's "which the key hadn't listed", and the slips are the third run's (two runbook counts cited to empty Go-no-go cells, a label before the date). The closeout's brief change for this workbook (the owner rule is for an Owner column; With is not one) touches no sentence here: Conditions has no With column, and the mistakes paragraph's "Backend engineers" is a team in an Owner cell, as the Read me's Limits says. No cell of the rebuilt workbooks changed, so no template sentence moves. The third grade's brief change 1 isn't taken yet and the page doesn't mention it. Before the closeout: the lead's fixes applied (review/waves-4-7-round-2-lead-check-2026-10-24.md §§ 5 and 6, round 1's row 13, the voice pass's facts and disagreements, and review/evidence-audit-rollout-2026-10-24.md). Voice pass F1, F2, F3, F4, F6, F7 and F8 with the pass's suggested wording; no evidence row showed otherwise. F5 doesn't apply: the Navy's September 2010 letter is out, as § 6 rules, so there is no lead-in to restore. F9 (the last sentence's join) and F10 (GovS 002 at origin) stay open for Jona. "Found", never "there were", on the page and on the cover's sub-line, which is re-rendered. The audit's other fixes: the fair record names both secretaries general and cites the HR director for the rehearsals; Test 5 no longer sets the 20,000 against the 40,000; Test 2 gives all of check 8. Disagreements 1, 5, 8 and 9 taken; 2 by saying when the rollout runs the brief; 4 by the run paragraph, which the closeout moved to the third grade. The agent section opens on its job (§ 5.4). GovS 002 8.8's "sequencing" line, which the Cutover page quotes, is paraphrased here (§ 5.3). For Jona's read. Passed by Jona and published 2026-10-24 with Waves 2 to 7.
evidence: every figure, date and quote read in the pulled text in research/_pulls/ by the writer on 2026-10-24; the Cour des comptes' two PDFs and the Assemblée nationale's three hearing records fetched again from ccomptes.fr and assemblee-nationale.fr the same day (plain curl, HTTP 200) and matched by sha256 with the copies in _pulls/, and again by the evidence audit. Rows in ~/cutover/evidence/rollout.md. The sources are in French and every English rendering on the page is the writer's. GovS 002 8.8 read in the local mirror; the publisher's site refused curl and the browser fetch on 2026-10-24, so Jona opens the official PDF before the page goes up. Every tab, column, check, rule, count, person and date given for the template is read from the built words.py, the shipped brief and out/BUILD-NOTES.md after the third-run round, and the run paragraph from the lead's grade of the third run (agent-brief-test-cutover-workbook-2026-10-24-third.md), with the run file read for the notice's wording and the cells it cited.
published: 24 October 2026
desc: Who gets it first? How France's defence ministry moved its Army onto a new pay system in 2011, after a first wave of about 10,000 files, with 15,000 cases counted in its old pay centres and more than 140,000 found a year later, and how to plan the waves of your own rollout, with the workbook to download.
draws_on: Readiness and go/no-go, Cutover plan and rollback, Schedule, RAID log, Stakeholders and communication
feeds_into: Handover and ownership, Project close
template_name: Cutover workbook
cover: /delivery/rollout/rollout-cover.png
template_shot: /delivery/rollout/frqz-cutover-rollout.png
template_text: One workbook for the whole cutover, shared with the readiness and cutover plan pages: open the Example to see the checks fail, then start on the blank with Details and Rollout. The brief for an assistant is [a text file](/delivery/rollout/frqz-cutover-agent-brief.txt) beside it.
templates: Cutover workbook | /delivery/rollout/frqz-cutover.xlsx | /delivery/rollout/frqz-cutover-example.xlsx | Ten tabs
files: /delivery/rollout/frqz-cutover-agent-brief.txt
---

# Controlled and gradual

September 2011 · French Ministry of Defence

Louvois was the French armed forces' new pay system, built to work out the pay of about 180,000 service members: almost everyone in the forces except the Air Force, which kept its own calculator.[1] The Army was still paid by regional pay centres, and the decision to close the first two had been published in 2008, ahead of a switch whose date wasn't yet set.[2] The ministry moved one service at a time. In 2013 its secretary general for administration told the National Assembly's defence committee it was "controlled and gradual", so that each step could be checked before the next.[3]

The first wave was the armed forces' medical service, about 10,000 files.[2] On 4 March 2011 the ministry decided to move it for the April pay, after "a fairly long period" of paying in parallel.[3] The medical service had no pay office of its own: its people had been paid by whichever service they belonged to. The ministry's director of human resources, who had taken the project over in May 2010, said creating a new system for it seemed likely "to harden us for what followed".[2] The first wave turned up problems with hospital duty pay, which the service paid on its own schedule rather than in the month the duty was worked.[3]

On Monday 19 and Tuesday 20 September 2011 the HR director put the Army's file to a meeting at the chief of the defence staff's, then to one in the minister's office.[2] By his account, the work before the decision included dry-run pay in the autumn of 2010, parallel pay from January to the end of spring 2011, two full rehearsals, and a manual team sized for 20,000 operations. On the dashboard, 13 of 17 indicators were green and 4 were orange, all in printing.[2] The secretary general of the time told the committee that the level of errors in the tests had been compared with a bar the armed forces set, "of the order of 93 percent success".[4] The Army's switch was set for the October 2011 pay.[3]

By the 2013 secretary general's account, a stocktake when the Army moved had put the cases waiting in its pay centres at 15,000, and a year later more than 140,000 were found: "So there was a problem of information reaching the top, and of analysing the situation."[3] Between June and September 2011, 39 experts had left the centres.[2] In March 2012 the ministry ran 40,000 corrections and took on 9,000 reservists' files, figures that "had not been anticipated", the HR director said.[2] Some service members were paid close to nothing. An emergency plan paid 27,000 advances worth 53 million euros up to the end of 2014, and by mid-November 2015 the overpayments found since 2011 came to 358 million euros, of which 171 million had been recovered.[1]

The Cour des comptes, France's court of audit, wrote to the minister on 27 December 2013. It found the closure of the pay centres premature: the announcement itself had sent their experienced staff looking for other jobs. Staff cuts a new system makes possible, it wrote, "must not be made in advance, during the switch-over and ramp-up". Returning the Army to its old calculator was "not feasible": the people who had worked out the pay were gone, and the databases no longer fitted it.[5]

The ministry rehearsed,[2] and both secretaries general told the committee that no switch went ahead without the agreement of the service concerned.[3][4] The secretary general of the time said the medical service and the Navy moved "in satisfactory conditions", though the court counts the medical service among those hit from 2011.[4][1] Two technical audits by the ministry's IT directorate hadn't judged Louvois bound to fail.[5]

Asked about a plan B, the HR director named the manual team, set up for the risks the parallel pay had shown. By his account it was there for the new system's own errors, not for the corrections Louvois would take over from the old system, some of them years old.[2] The cases piling up in the Army's pay centres, 15,000 on the stocktake, were corrections of that second kind.[2][3]

## What a rollout plan is for

A rollout plan says who gets the new system first, in what order everyone else follows, and what has to be true before each next group moves. Each group is a wave, with a count, a day it opens, a reason it comes where it does, and a notice that reaches it before then. The field calls this a phased rollout. A first wave picked to learn from is a pilot, and in software a small share of live traffic sent to the new version first is a canary release. The day a group starts on the new system is its day one. GovS 002, the UK government's standard for project delivery, asks for a plan for moving "all or part of the solution" into use. The plan should weigh the order of the moves, to keep unexpected side effects down, and the need to keep the business and its services running.[6] In a company of 40 a rollout might be two waves, the staff and then the customers. Louvois had a first wave of about 10,000 files and about 180,000 people to pay in all.[2][1]

The project's owner keeps the rollout plan. It's one of the three parts of a [cutover](/delivery/cutover/), with readiness and go/no-go and the cutover plan and rollback. The cutover plan and rollback covers the window when the first wave moves, hour by hour, and the rollout covers every wave, often over months, until the last group has moved.

## Read what's there

Start with the list of who's moving. Export every customer, user or site from billing or the directory, with the fields that might split them: plan, country, contract type, renewal date, the team or service they belong to. Count each group. Then read what each group waits on: the milestones in the schedule, the dependencies on the RAID log, and the notices already planned in the stakeholders file.

Read the old system's open work too: cases waiting, corrections typed by hand, anything queued for after cutover. Count it yourself from the old system, and write down who counted and on what day. At Louvois a stocktake put the Army's waiting cases at 15,000, and a year later more than 140,000 were found.[3]

A group needs its own wave if something it depends on won't be ready when the first wave goes, or if it's paid, billed or served differently from the first. In the Example, customers outside the US wait for their tax rules, so they're wave 3.

## Draft

Start on Details, then Rollout, then Conditions and Moves.

- **Customers in all**, on Details: every customer, user or site the rollout moves. The waves must add up to it. **Planned finish** is the Register's, and no wave's last move can come after it.
- **Who**, on Rollout: one group per row, in the order the waves open, such as "US customers billed monthly". Wave 1 can be the cutover weekend itself. The tab numbers the waves.
- **Customers**: how many are in the wave.
- **Opens**: the day the wave opens. Waves open in order.
- **Why in this order**: one line on why the wave comes where it does. "Needs the customer accounts on the new platform (X2)" says what it waits for; "Second" doesn't.
- **Told on** and **Told by**: the day the notice goes, which has to be before Opens, and the one person who sends it.
- **Last move**: the day the last of the wave moves, on or after Opens and by the Planned finish.
- **Moved so far**: blank until the wave opens, then kept up as it runs.
- **Condition**, on Conditions: one thing that must be true before a wave opens, with its **Wave**, one person as **Owner**, a **Needed by** date on or before Opens, a **Status** (Open, Met or Waived) and, once it's Met or Waived, **Evidence or reason**. Type each wave's conditions on its own rows, because a later wave inherits none. **RAID Id** names the RAID log line it waits on, such as X1, and then Needed by is the plan workbook's Baselined date for it.
- **Month** and **Customers moving**, on Moves: how many of each wave you plan to move each month, typed as the first day of the month.

The tab works out **Scheduled**, added up from Moves; **Still to move**, which is Customers less Moved so far; and a **Check** that says in a sentence the first thing wrong with each wave. Where you don't know a date or an owner, leave it blank for the checks to find.

## Test

1. **Add up the waves.** The check is "A rollout that doesn't add up". It fails when the waves don't add up to Customers in all, when a wave opens before the one above it, when a wave opening within 60 days has Moves that don't add up to its Customers, or when a wave's Moved so far is more than its Customers. In the Example, 910, 210 and 340 make 1,460, and the second and third waves' months add up to 210 and 340.
2. **Find a wave condition or notice that's incomplete or late.** It fails a wave after the first with no condition, a wave with no Told by or told on the day it opens or later, a condition due after its wave opens, one with no owner, date or status, one Met or Waived with nothing in Evidence or reason, and one still Open after its Needed by. In the Example, the tax rule list that wave 3 waits on is owned by Rhys (Finance Operations Lead) and has no Needed by date; the Program board's notes say no date is set for the sign-off yet. Ask Rhys for a date before anyone plans wave 3 around it.
3. **Find a wave that runs late.** A wave fails when its Last move is blank, before Opens or after the Planned finish, or when Moved so far falls behind what Moves planned for the months that have ended.
4. **Ask what the first wave can't tell you.** This one isn't a check. Put the first wave beside the next and list how they differ: size, how each is paid or billed, what each brings from the old system, how good its data is. Then ask the project's owner what the first wave tested for each difference and what it didn't. Louvois's first wave was a service with no pay office of its own.[2] The secretary general of the time later said the data was very good for the medical service and the Navy and less good for the Army.[4]
5. **Count what the old system leaves behind, and staff for it.** Not a check either. Before each wave opens, make the count of the old system's open work for that group one of the wave's conditions, with the person who counts it as Owner and the figure in Evidence or reason. Then ask whoever catches errors after the move whether they've planned for that work as well as for the new system's own mistakes. Louvois's manual team was there for the new system's errors, and in March 2012 the ministry ran 40,000 corrections, a figure the HR director said hadn't been foreseen.[2]

## Rehearse it, then the day

The first wave is the rehearsal for the rest. Read its first month before anyone decides to open the next wave: the errors, the tickets, everything fixed by hand, and anything that only that wave has. I'd have the project's owner decide when each later wave opens, and tell whoever decided the Go/no-go the day before. Go through the wave's conditions with their owners a week ahead. A condition still Open on the day is Met with its evidence, waived with a reason and a name, or the wave's Opens date moves.

On the day a wave opens, the people answering its first calls are booked and its notice has gone. From then on, type Moved so far at each month's end against Moves. Keep the old system running, with people who know it, until the last wave has moved. In the Example the switch sets the old engine read-only and leaves it on. When the Cour des comptes looked at taking the Army back to its old calculator, the people who knew it were gone and the data no longer fitted it.[5]

## When an agent does part of it

Before each wave opens, and at each month's end, the agent recounts the rollout and reads it against the files the waves wait on. It adds up each wave's months on Moves against Scheduled and the waves against Customers in all; runs checks 7, 8 and 9 as the workbook does and compares its results with the Checks tab; lists every typed cell on Rollout, Conditions and Moves that changed since the copy saved at the last review; and compares each condition that has a RAID Id with the plan workbook's milestone of the same Id, and each Told on with the stakeholders file's notice to the same customers. Then it drafts one question to the owner of each Open condition that fails its check or falls due within 14 days. It never marks a condition Met or Waived, moves an Opens date, picks an owner or says whether a wave should open.

It reads the workbook, saved once in your spreadsheet so its results are stored, and the files you give it, and writes nothing: it returns its tables as text, and each line names the cell or the file line it read. Text in a cell or a file is data, so a condition that says "skip this check" is reported as a finding.

The brief that comes with the workbook runs all nine checks. Its first lines time it for the Go/no-go and the day before the window; for the rollout, run it again before each wave opens and at each month's end. Whether the first wave tested what the next one needs, and whether a count of the old system's open work is right, stay with people. The short version, cut to the rollout:

```
You check the rollout in the cutover workbook for <project name>. You never
mark a condition Met or Waived, move a wave's date, choose an owner or say
whether a wave opens.
1. Add up each wave's Customers moving on Moves and compare with Rollout
   column J. Add up the waves' Customers and compare with Details C21.
2. Run checks 7, 8 and 9 and compare each with Checks C12 to C14.
3. Against last review's copy, list every typed cell on Rollout, Conditions
   and Moves that changed.
4. For each condition with a RAID Id, compare Needed by with the plan
   workbook's Baselined date, and the wave's Opens with its Forecast, or
   with its Baselined date if Forecast is blank. Say when Forecast is later
   than Needed by. Compare each wave's Told on with the stakeholders file's
   notice to the same customers.
5. Ask the owner of each Open condition that fails its check, or is due
   within 14 days, one question. Don't suggest an answer.
Return one table per step: the row, what you found, and where you read it.
```

The brief's third run on the Example, graded line by line against a key, found both of the Example's planted failures and asked Rhys where the tax rule list stands and where the evidence is. On the rollout it added up every wave's months, compared wave 2 with its milestone's Baselined date because that milestone has no Forecast, and reported that the tax rules are forecast 11 days after wave 3's condition needs them, on the day wave 3 opens. It also noticed that the notice to waves 2 and 3 says "Second wave from 1 Feb 2027" while wave 3 opens on 12 Feb. Its slips were two runbook counts cited to empty cells on the Go-no-go tab, and a label before the date on its first line.

Check its work by hand each time. Recount one wave's months on Moves and read the condition the Checks tab names first. Then open one notice and check its date against Told on. The mistakes to look for are partners counted as customers, a later wave given the conditions of the wave before it, a month on Moves read as the day of a move, a condition taken as Met because something is typed in Evidence or reason while its Status still says Open, and a team written as an owner in a way the checks can't catch, such as "Backend engineers".

Each condition's Owner says when it's met, and the person in Told by sends the notice. The project's owner sets the waves, their order and their dates, and decides when each later wave opens. The agent drafts the questions. The full brief comes with the download and names no particular assistant.

## The template

The cutover workbook has ten tabs: Read me, Details, Readiness, Go-no-go, Runbook, Rollback, Rollout, Conditions, Moves and Checks. The rollout is on three of them. Rollout holds the waves: who, how many, when each opens and why in that order, the notice, the last move and how many have moved so far. Conditions holds what must be true before each wave opens, each with one owner and a date, and Moves plans each wave month by month. Checks runs nine checks, and three are on the rollout: a rollout that doesn't add up, a wave condition or notice that's incomplete or late, and a wave that runs late. It comes blank, and filled in for Hollins Software, a made-up company, as of 11 Dec 2026, the day before its cutover weekend. The filled-in one fails two of the nine checks on purpose, one of them on the rollout.

{{TEMPLATE}}

## The week before

The week before a wave opens:

- **Monday.** Recount the wave against the customer list as it stands today, and its months on Moves against its Customers.
- **Tuesday.** Go through the wave's conditions with each owner. Anything still Open needs its evidence, or a reason it can be waived, by Thursday.
- **Wednesday.** Count the old system's open work for the wave yourself and type the count in its condition's Evidence or reason, with who counted. Check the notice went, and on what day.
- **Thursday.** Take the wave to the project's owner with every Open condition and the first wave's results. They open it on its date, move the date, or waive a condition with a reason and their name.
- **Friday.** Book the people who'll answer the first calls on the opening day, and set the day you'll type the first Moved so far.

If you count the old system's open work this week, write to me at [jona@projectcutover.com](mailto:jona@projectcutover.com) and tell me how far your count was from the number you had before you counted.

## Connects to

The rollout draws on readiness and go/no-go, whose decision opens the first wave, and on the cutover plan and rollback, which moves it. Each later wave's conditions come from the milestones in the schedule and the dependencies on the RAID log, and its notice from stakeholders and communication. Handover and ownership reads how many are still to move, and project close reports what moved.

## Sources

1. Cour des comptes. *Rapport public annuel 2016*, volume 2, chapter "Le versement de la solde des militaires : en dépit des efforts engagés, des dysfonctionnements persistants", February 2016. In French; quotations translated for this page. Pages 589, 591 and 595. https://www.ccomptes.fr/sites/default/files/EzPublish/15-versement-solde-militaires-RPA2016-Tome-2.pdf
2. Assemblée nationale, Commission de la défense nationale et des forces armées. *Compte rendu n° 75*, hearing of the ministry's former director of human resources on the rollout of the Louvois pay software, 29 May 2013. In French; quotations translated for this page. Pages 2 to 8. https://www.assemblee-nationale.fr/14/pdf/cr-cdef/12-13/c1213075.pdf
3. Assemblée nationale, Commission de la défense nationale et des forces armées. *Compte rendu n° 67*, hearing of the ministry's secretary general for administration, 10 April 2013. In French; quotations translated for this page. Page 5. https://www.assemblee-nationale.fr/14/pdf/cr-cdef/12-13/c1213067.pdf
4. Assemblée nationale, Commission de la défense nationale et des forces armées. *Compte rendu n° 76*, hearing of the head of the armed forces' inspectorate, secretary general for administration from 2005 to 2011, on the introduction of Louvois, 5 June 2013. In French; quotations translated for this page. Pages 2, 5, 7 and 14. https://www.assemblee-nationale.fr/14/pdf/cr-cdef/12-13/c1213076.pdf
5. Cour des comptes. *Le système de paye Louvois*, référé no. 68579 to the Minister of Defence, 27 December 2013, made public 6 March 2014. In French; quotations translated for this page. Pages 2 and 4. https://www.ccomptes.fr/sites/default/files/EzPublish/systeme_paye_Louvois_refere_68579.pdf
6. Cabinet Office. *Government Functional Standard GovS 002: Project delivery*, version 2.1, 1 September 2025. Clause 8.8 (page 37). https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/
