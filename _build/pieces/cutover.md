<!-- style-gate: allow (sources quoted verbatim) -->
---
slug: cutover
kind: layer
status: draft v2 (2026-10-24), the lead's fixes applied (review/waves-4-7-round-2-lead-check-2026-10-24.md §§ 5 and 6; review/evidence-audit-cutover-2026-10-24.md). Voice pass F1 to F7 taken with the pass's suggested wording; no evidence row showed otherwise. D1 the definition, with the stage as § 5.5 has it; D2 the first period of use (GovS 8.9) cut, as Handover's; D3 the one-workbook line; D4 "tracks", with the criteria from the gate map and the acceptance and sign-off file, as the Readiness ruling has them. The audit's other fixes: the whiteboards cut (5.163's "if at all then"); the chief executive's day in 7.90's word, "cope"; the description now names the Chief Secretary, whose letter it was. Cut to 1,000 words in all (§ 5.2): the workarounds quote, 4:40 am, the railway, the trials, the 45 systems, the week after, Annex D, the earlier gates line and the gate decision's deferral came out. For Jona's read. Passed by Jona and published 2026-10-24 with Waves 2 to 7.
evidence: every figure, date and quote read in the pulled text in research/_pulls/ by the writer on 2026-10-23; the seven Select Committee chapters and the Commission summary matched by sha256 with the copies on legco.gov.hk and info.gov.hk that day, and again by the evidence audit on 2026-10-24. Rows in ~/cutover/evidence/cutover.md. GovS 002 read in the majorprojects.org mirror (the publisher's site refuses curl and the browser fetch); Jona to open the official PDF before the page goes up.
published: 24 October 2026
answers: Answers: who can stop the switch, and until when?
cover: /delivery/cutover/cutover-cover.png
desc: The move from an old system to a new one, from the go/no-go through the switch to the rollout, and who decides each step. How Hong Kong's new airport opened on 6 July 1998, on a date the Chief Secretary had called irreversible.
---

# Irreversible

July 1998 · Airport Authority, Hong Kong

Hong Kong's new airport at Chek Lap Kok took seven years to build and cost about HK$155 billion, by the Chief Executive's account at the opening ceremony on 2 July.[1] The Airport Authority was to run it, and a government steering committee chaired by the Chief Secretary[1] was the "overall monitor" of whether it was ready.[2] The equipment, facilities and staff of the old airport, Kai Tak, were to move across on a Sunday night, for the new one to open the next morning.[2]

In January 1998, with the passenger terminal and the main cargo terminal running late, the steering committee moved the opening from April to Monday 6 July, when air traffic would be lighter and the roads quiet for the move the night before.[2] Two months earlier the Chief Secretary had written to the Authority's chairman that the date, "once announced, will be irreversible".[1]

The steering committee met on Saturday 4 July, two days out. The flight information display system tells everyone at an airport which flight lands when and at which gate. The Authority's readiness report said this one "was sufficiently stable". The chair's brief from the government's co-ordination office said the same system had been down 9 percent of the time in a test run from 14 to 27 June, and called that not satisfactory.[1] Members heard the switch to the standby had been tried on 2 July. They didn't seem to know that the standby's own procedure let the switch be considered only once someone had decided the main system would be down for more than three hours.[1]

Witnesses told the Legislative Council's Select Committee that on the Monday the system that assigns aircraft to parking stands began to malfunction at 2:00 am, and that at about 7:00 am the screen of expected arrivals froze.[1] The first emergency meeting was at 10:00 am, "to ascertain what the problems were". At 10:30 am the airport management director and the head of IT chose to restart the flight information system rather than switch to the standby. Neither the Authority's board nor the steering committee had known the standby had only limited functions.[1] From about noon to about 5 pm the apron was full, and again from 8 to 11 pm, and aircraft waited for a stand.[2] By about 7:45 pm an emergency coordination centre and the contingency measures were working "in a generally satisfactory manner".[1] At the cargo terminal, hundreds of trucks queued for up to 12 hours, and normal cargo handling didn't return until 24 August.[1]

The Commission of Inquiry on the New Airport counted 42 problems, three of them major: the flight information system, the cargo handling system and baggage. Some of the 39 smaller ones were isolated, and the effects of each "snowballed and spiralled" when they met each other and the trouble with the flight information and cargo handling systems.[2] The Select Committee found the Authority's contingency plans "patchy and disorganized".[1]

The Commission found the decision to open on 6 July "proper and wise". It also found that neither the Authority nor the cargo terminal's operator asked for a postponement, and that putting the opening off by about two months could have avoided the chaos.[2] The Select Committee held the steering committee's chair responsible for not making sure every sign of risk was weighed once the date was set.[1] It credited the overnight move, done without mishap, to the deputy chief executive's "organising abilities".[1]

On 4 July the 9 percent was in the chair's brief, and the standby's own procedure set out the three-hour rule. By the Select Committee's account, nobody involved knew of any way the date could be put off, "apart from severe inclement weather".[1]

## What a cutover is

A cutover is the move from an old system to a new one: the decision to go, the switch itself, and the hours after it while the old system can still be brought back. The field also calls it go-live or the cutover weekend. GovS 002, the UK government's standard for project delivery, calls it transition, "to establish the capability for a solution to work within its intended environment".[3]

On this map Cutover runs from Build complete through Readiness, the Go/no-go, the window and the rollout's waves, and the last waves can run on past Handover accepted. In a company of 40 the window might be one weekend with six people on a call. The main document is the cutover plan and rollback, kept with the go/no-go criteria and the rollout in one cutover workbook that the three parts below share.

## Who runs it

GovS 002 asks for each gate's decision makers to be named.[3] At the Go/no-go that's one person who makes the call. The cutover itself needs a second role, whoever runs the switch on the day and can stop it or roll it back while there's still time. One person can hold both.

In a company of 40 the CTO or a founder makes the Go/no-go call, and the engineering lead runs the cutover with the support lead on the line. At Chek Lap Kok the Authority's chief executive left it to his senior managers to cope. The Select Committee found no leadership at the Authority on the day.[1]

## What it decides

Three decisions sit at this stage and no other: whether to go on the date, whether to carry on or roll back while the switch is under way, and who gets the new system first and what has to be true before everyone else does. GovS 002's list for a transition plan includes sequencing "to minimise unexpected side effects", keeping the business running, the transfer of ownership and switching off what the new system replaces.[3]

Its gates are Readiness and the Go/no-go on the project's [gate map](/delivery/project/). The part called Readiness and go/no-go tracks their criteria, from the gate map and the acceptance and sign-off file, until the call.

## Its parts

{{PARTS}}

## Sources

1. Legislative Council of Hong Kong. *Report of the Legislative Council Select Committee to inquire into the circumstances leading to the problems surrounding the commencement of the operation of the new Hong Kong International Airport at Chek Lap Kok since 6 July 1998 and related issues*, laid on 27 January 1999. Chapter 1, paragraphs 1.1 and 1.2; chapter 3, paragraph 3.2 and Chart 3.2; chapter 4, paragraphs 4.146, 4.148, 4.149, 4.152 and 4.153; chapter 5, paragraphs 5.159, 5.163, 5.164, 5.167 and 5.173; chapter 7, paragraphs 7.21, 7.22, 7.25, 7.90 and 7.99. https://www.legco.gov.hk/yr98-99/english/sc/sc01/papers/report.htm
2. Commission of Inquiry on the New Airport. "Detailed summary of airport inquiry report", Hong Kong Government press release, 22 January 1999. Paragraphs 1 to 3, 5, 6, 8, 10, 12 and 27. https://www.info.gov.hk/gia/general/199901/22/0122063.htm
3. Cabinet Office. *Government Functional Standard GovS 002: Project delivery*, version 2.1, 1 September 2025. Clauses 6.3 and 8.8. https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/
