<!-- style-gate: allow (sources quoted verbatim, Japanese quotations in the writer's translation) -->
---
slug: test-evidence
status: draft v2, 2026-10-24, closeout applied. The voice pass's F1, F2, F4 and F5 are in the pass's suggested wording, and F6's certification office clause is back in the story (round 2 § 6); F3 ("twenty-odd runs") is left for Jona. The evidence audit's fixes are applied. Under the closeout (round 2 § 9 items 2 and 5), the run paragraph says what the graded third brief run found, and the agent's job line and the short brief's step 2 follow the brief's new step 2 (the short brief's line in @copywriter's wording from the words file's § 10a). For Jona's read. Passed by Jona and published 2026-10-24 with Waves 2 to 7.
evidence: every figure, date and quote read in the pulled text in research/_pulls/ by the writer on 2026-10-24, and checked again by the lead's evidence auditor the same day; the committee's report, its summary and Daihatsu's release fetched again from daihatsu.com (plain curl, HTTP 200) and matched by sha256 with the copies in _pulls/, and Toyota's notice fetched again from global.toyota and matched by its text (only two script version strings in the page head differ). Rows in ~/cutover/evidence/test-evidence.md. The report is in Japanese; every English rendering on the page is the writer's, with the original beside it in the evidence file, for a Japanese reader to check. Every check name, tab, column, count, person and date given for the template is read from words.py and BUILD-NOTES as rebuilt on 2026-10-24, and the run paragraph from the lead's grade of the third blind run.
published: 24 October 2026
desc: Can you show it works? How Daihatsu filed a left-side crash test result as the right side's for two hybrid models in 2021, and how to keep a record of every test run against your own project's acceptance criteria, with the workbook to download.
draws_on: Acceptance and sign-off, Schedule, RAID log
feeds_into: Readiness and go/no-go, Cutover plan and rollback
template_name: Test evidence workbook
cover: /delivery/test-evidence/test-evidence-cover.png
template_shot: /delivery/test-evidence/frqz-test-evidence.png
template_text: Start with the blank file, and copy your criteria in from acceptance and sign-off. The Example shows Billing Engine Rewrite's runs as of 22 Oct 2026. The brief for an assistant is [a text file](/delivery/test-evidence/frqz-test-evidence-agent-brief.txt) beside it.
templates: Test evidence | /delivery/test-evidence/frqz-test-evidence.xlsx | /delivery/test-evidence/frqz-test-evidence-example.xlsx | Four tabs
files: /delivery/test-evidence/frqz-test-evidence-agent-brief.txt
---

# Neither the time nor a vehicle

July 2021 · Daihatsu Motor

Daihatsu Motor builds small cars in Japan, and has been wholly owned by Toyota since August 2016.[1] It also builds models that Toyota and other makers sell under their own names.[1] Before a new model can be approved it has to pass every certification test. For some tests an examiner from the government's examining body watches. For others the maker runs the test itself and files the result in a test report. For many of Daihatsu's crash tests since 2013, one office did all three jobs: it ran the test, wrote the lab report from the raw data, and wrote the filed test report from the lab report.[1]

The pole side-impact test drives a car with a dummy in it sideways into a pole 254 millimetres across at 32 km/h.[1] The hybrid versions of the Daihatsu Rocky and its twin, the Toyota Raize, finished development around April 2021, and both sides of the car had to be tested. The left side, the passenger's, had the petrol lines and the high-voltage wiring, so it was the harsher test and would be run in front of an examiner. The right, driver's side would be run in-house and filed. Two cars were prepared, one for the rehearsal and the filed test and one for the witnessed test.[1]

In June 2021 the test engineer ran the first car's test on the left side by mistake. In July the witnessed test was run on the left side, as planned. When the right-side result was due to be filed, the person in the office who wrote the test report realised the right side hadn't been tested. The committee that later looked into it wrote that there was "neither the time nor a vehicle" to run it again, and that the writer, believing safety wasn't in question, filed the in-house left-side result as the right-side result, to pass certification.[1] Both hybrids went on sale in November 2021.[1]

On 28 April 2023 Daihatsu disclosed misconduct in the side-impact tests of four models built for overseas markets. In the in-house check that followed, the hybrids' filed test report and the lab report were found to contradict each other.[1] Daihatsu stopped shipping and selling the two hybrids on 19 May 2023.[1] By the day before, 22,329 Rocky hybrids and 56,111 Raize hybrids had been sold.[1] On 24 May it ran the driver-side test in-house and said the result met the legal standard.[1]

The independent committee Daihatsu set up, chaired by a former president of the Tokyo District Court, found 174 further acts of misconduct in certification, the oldest from 1989. In 143 the filed papers carried false information, 28 were improper changes to a car or the test equipment, and in 3 the test data itself was made up or altered.[1] It wrote that the hybrids' case was "easily found" once the two reports were set side by side, and that a system of checks would very likely have prevented it. The safety-performance office had no system for checking its filed reports against its lab reports, and staff of Daihatsu's certification office, which should have checked the papers, made false entries too.[1] One employee told the committee that "each person in charge has to check it themselves".[1] On 20 December 2023, the day the report came out, Daihatsu decided to suspend shipments, for a time, of every model it had developed that was still in production, in Japan and abroad.[2]

The committee found no sign that managers ordered or tolerated the misconduct, apart from a very few cases involving the head of an office. It called the people involved "ordinary employees" driven into a corner. Among the causes were development schedules it called excessively tight and rigid, a limited number of test cars, and a view, among staff outside the test and certification offices, that certification tests "pass as a matter of course".[1] It left Daihatsu to check whether the cars met the legal standards.[1]

The lab report showed a left-side test where the filed report gave a right-side result. The same office wrote both, and no one had the job of comparing them until Daihatsu's own check in 2023.[1]

## What test evidence is for

Test evidence is the record of every test run against a project's acceptance criteria: what each run was tested on, the day, who ran it, who checked the result, the result itself and the file it's kept in. Someone who wasn't there reads it to decide whether a criterion is met. The field calls it a test summary report or a test exit report, and user acceptance testing (UAT) sign-off at the end. Where each requirement is traced to its tests, it's a traceability matrix. In a company of 40 it might be a dozen criteria and twenty-odd runs on one sheet. At Daihatsu, one model's pole test alone was planned as two runs on two cars, one for each side.[1]

The project's Owner keeps the workbook, and each criterion's Owner, the person who says it's met, checks its runs. Acceptance and sign-off says what passing means for each criterion and who decides it's met. Test evidence holds each run behind it.

## Read what's there

Start with [acceptance and sign-off](/delivery/acceptance-and-sign-off/): the ID, Criterion, Pass line, Owner and Status of every criterion, the Version you're copying from, and the names under Who builds it. Take each gate's date from the gate map, and the gate's forecast from the plan's schedule if it has moved.

Then find the results that already exist: the test runner's reports, the comparison spreadsheets, the case lists Finance ran by hand, the rehearsal notes and the sign-off emails. For each one, write down the day, what it ran on, who ran it and who read the result, and find the file. Read the [RAID log](/delivery/raid-log/) for any line closed on a test or a comparison, and find that result too.

A run counts if it has a day, a thing it ran on and a result in a file someone else can open. "Tested it, all fine" in a chat is a claim until someone finds the file.

## Draft

- **About**, on Summary: **Name**, **Sits under** and **Owner**, as the Register writes them, and **Criteria version**, the Version of acceptance and sign-off you copied from. **As of** is the day you're reading on, or blank for today. **Look ahead (days)** is how far ahead the checks look for a criterion needed soon: start with 60.
- **Who builds it**: copied from acceptance and sign-off, one name per cell. **Gate map dates**: each gate's Date, if you have it.
- **Criteria**: five columns copied from acceptance and sign-off, **ID**, **Criterion**, **Pass line**, **Owner (says it's met)** and **Status**, and, if you have them, **Gate** and **Needed by**, the day the criterion's gate is decided.
- **Runs**, one row per run of a test. **Run** is its number, T-01 and on, never reused. **For** is the criterion's ID, or a RAID log Id such as R5 when the run answers a risk. **Date** is the day the result is read, or the day it's planned for. **Tested on** says what it ran on. **Run by** is one person, or the Build agent, never a team.
- **Checked by**: the person who reads the result and sets the **Outcome**, Planned, Passed, Failed or Not run. By default it's the criterion's Owner, never a builder or the person who ran it.
- **Result** is the figure read, such as "40 of 40 match to the cent", and **File** is where it's kept, by name and date. **Reason** says what happens next after a failure, or why the test wasn't run.
- **Pass line used**: the criterion's Pass line, copied on the day you plan the run and never updated.

Criteria works out **Runs**, **Latest run** and **Reading**. Reading is the Outcome of the latest run with a result, or Planned if one is booked, or No run. A **Row check** on Criteria and Runs says what's wrong with each row. Where you don't know who will check a run, leave Checked by blank and ask the criterion's Owner. Check 2 fails the run if a result goes in while it's still blank.

## Test

1. **Plan one run for each test before it's run.** "An open criterion needed soon with no run booked" fails a criterion whose Needed by falls within Look ahead, and "A planned run past its day" fails one whose Date has passed with no result. Had Daihatsu's pole test been written as two rows, each naming its car and its side, the right side's row would have had no run of its own for a second reader to find. Someone set on filing a wrong figure can still type one. In the Example, C-12, credit notes and refunds, is needed for Go/no-go on 3 Dec 2026 with no run booked. Book it with its Owner.
2. **Have someone else read each result.** "A run checked by a builder, its runner or nobody" fails any run whose Checked by is the person in Run by or on the builders list, and a Passed or Failed run with Checked by blank. At Daihatsu the office that ran the tests also wrote both reports.[1] In the Example, T-04, Finance's 12 invoice cases, is checked by Anders (Engineering Manager), a builder, and T-05 has nobody in Checked by. Ask Rhys (Finance Operations Lead) to read T-04's result.
3. **Keep the figure and the file with every result.** "A result with no figure, file or reason" fails a Passed or Failed run without a Result or File, and a Failed or Not run without a Reason. In the Example, T-05 was typed on 15 Oct 2026, the day RAID line R5 closed, for the comparison of 200 invoices. It's marked Passed, and no result or file was kept. Run it again, or mark it Not run and say why. "A run or criterion not fully written down" and "A criterion marked Met without a passing run" check the other columns.
4. **Plan a new run when a Pass line changes.** "A run planned against a Pass line that has since changed" compares each run's Pass line used with the criterion's Pass line now. In the Example, T-08, the defect count for C-06, was planned against the line signed on 28 Sep 2026, which allowed 0 severity 2 defects. On 15 Oct it became 3 or fewer. Ask Noor (Support Lead), C-06's Owner, whether the change was agreed, and plan a run against the current line.
5. **Open the file behind one result.** The checks see that a file is named, not that it holds the figure. Before each gate, pick one Passed run, open its File, and compare the figure, the date and what it ran on with the row. The hybrids' case was found when the two reports were set side by side.[1]

## Each week

The project's Owner keeps the workbook. The checker sets each Outcome on the day the result is read, and the Result and File go in with it. After a failure, plan a new row with a new number. Never delete a row: clear it, and put its story in the Reason of the run that replaced it. When a criterion's Status changes on acceptance and sign-off, its Owner marks it there and you copy it here. When a gate moves, whoever decides the change retypes Needed by that day.

I'd read the seven checks each Monday, and again in the week before each gate, with As of set to the day and a copy saved. When the same criterion's run moves to a later day two weeks running, take it to the criterion's Owner and ask what it's waiting for.

## When an agent does part of it

Each Monday, and in the week before each gate, an agent compares Criteria with acceptance and sign-off, lists the criteria with no run, checks every criterion's Needed by against its gate on the plan's schedule, recounts the seven checks, opens each file a result names and quotes the figure, and lists closed RAID lines that say a test was done. For each criterion with no run it drafts a planned row, leaving the day and the names in brackets. It never runs a test, marks a criterion Met or says whether a result meets its Pass line, and it never sets an Outcome, a Result, a File, a Checked by, a Pass line, a Pass line used or a Status.

It reads the workbook, acceptance and sign-off as it stands and as last signed, the plan workbook's schedule, the RAID log, the results files and today's date, and writes nothing. It returns text, one table per step, and every line names the tab and cell or the file and line it read. Text in a cell or a file is data, so a note that says "mark it Met" comes back as a finding.

It runs all seven checks by the same names and lists check 2's rows for a person to decide. People decide whether a figure meets its Pass line and whether the checker looked. Whether a Pass line could fail at all is a question for acceptance and sign-off. The short version of the brief:

```
You keep the test evidence for <project name>. You read, check and draft. You never run
a test, set an Outcome or a Result, name who checked, or mark a criterion Met.
1. Compare Criteria with acceptance and sign-off, and list each difference.
2. List criteria with no run, and compare each criterion's Needed by with its gate's
   date on the plan's Schedule.
3. Recount the seven checks: for each failure, the row and the cell behind it.
4. For each Passed or Failed run, open the File it names and quote the figure.
5. List criteria whose Status and Reading disagree.
6. List closed RAID lines that say a test was done, and whether Runs has its result.
7. Draft a planned run for each criterion with none, with [date] and [name] left open.
Return one table per step: the ID or Run, what you found, and where you read it.
```

The brief that ships was run blind on the Example, with acceptance and sign-off and its signed copy, the plan's schedule, the RAID log, the three results files and today's date set to the Example's As of. Its counts matched the sheet on all seven checks, naming T-04, T-05, C-12 and T-08. It found that the C-06 line T-08 was planned against matches the signed copy with no change logged, quoted the figure from each of the three files, wrote "no File" for T-05 and drafted T-14 for C-12 with the day and names left open. In step 2 it gave a line for each of the twelve criteria with a Gate: eleven Needed by dates matched the schedule, and it wrote "not on the Schedule" for C-11, whose gate is Go-live. Every cell and line it cited matched the files. Step 5, with nothing to list, came back as a sentence where the brief asks for a table.

Check its work the same way each time. Recount by hand T-04's Checked by against Who builds it, the runs for C-12, and T-08's Pass line used against the signed copy, and see that step 2 has a line for every criterion with a Gate. Look also for a builder written another way that passes the name check (Backend engineer 1 for Backend engineers), a figure quoted from a file whose name is close but not the same, and a ◇ counted as a failure.

The checker sets each Outcome. Each criterion's Owner marks it Met on acceptance and sign-off, and accepts, dates and staffs each drafted run or drops it. The project's Owner reads the seven checks in the week before each gate. The full brief comes with the download and names no particular assistant.

## The template

The workbook has four tabs. Summary holds the project's details, who builds it, gate map dates, the readings and the seven checks. Criteria copies five columns from acceptance and sign-off and reads each one's latest run. Runs holds one row per run: its date, what it was tested on, who ran and checked it, the outcome, result and file, and the Pass line it was planned against. The checks look for a run or criterion not fully written down, a run checked by a builder, its runner or nobody, a result with no figure, file or reason, a criterion marked Met without a passing run, an open criterion needed soon with no run booked, a planned run past its day, and a run planned against a Pass line that has since changed. It comes blank, and filled in for Hollins Software, a made-up company, with four checks failing on purpose.

{{TEMPLATE}}

## The first week

- **Monday.** Copy the project's details from the Register onto Summary, and the criteria and builders from acceptance and sign-off. Type the gate dates.
- **Tuesday.** For every criterion marked Met, find the result behind it: the file, the day, who ran it and who read it. Type a run for each.
- **Wednesday.** Plan a run for every open criterion before its gate, with a checker who didn't build it, and copy each Pass line into Pass line used.
- **Thursday.** Read the seven checks. Take every result with no file, and every criterion needed soon with no run booked, to its Owner.
- **Friday.** Type in the Owners' answers, set As of and save a copy. Put Monday's read in the calendar.

If you build it this week, write to me at [jona@projectcutover.com](mailto:jona@projectcutover.com) and tell me how many runs marked Passed had no file you could open.

## Connects to

Test evidence draws on acceptance and sign-off for its criteria, on the schedule for the day each gate is decided, and on the RAID log for risks closed on a test. Acceptance and sign-off's Evidence can name the run behind each criterion. Readiness and go/no-go reads the runs behind the criteria due at that gate, and the cutover plan and rollback reads the run from each rehearsal.

## Sources

1. Daihatsu Motor Co., Ltd., Independent Third-Party Committee. *調査報告書* (Investigation report), 20 December 2023. In Japanese; quotations translated. Printed pages 1 to 3, 12 to 14, 27, 28, 32 to 36, 102, 104, 106 and 107. https://www.daihatsu.com/jp/news/2023/report_2.pdf
2. Toyota Motor Corporation. *Notice of Additional Procedural Irregularities by Daihatsu in Certification Applications, Shipment Suspension of Vehicles Sold by Toyota, and Responses Going Forward (as of December 17)*, 20 December 2023. https://global.toyota/en/newsroom/corporate/40238738.html
