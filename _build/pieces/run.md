<!-- style-gate: allow (sources quoted verbatim) -->
---
slug: run
kind: layer
status: draft v2 (2026-10-24), the lead's fixes applied (review/waves-4-7-round-2-lead-check-2026-10-24.md §§ 5 and 6; the evidence audit of 2026-10-24). Voice pass F1, F3 and F6 to F8 applied with the pass's suggested wording; F2 with its alternative ("withdrew its award to its supplier"), which the evidence row and the audit (P4) support; F4 and F5 by taking the 37 talks off the page, as the ruling allows; F9's sentence (the director's two roles) cut for the 1,000-word limit, with the 7.9 half of the last GovS sentence; F10 still open. Disagreements 1, 2 and 4 as suggested, 3 by § 5.5, 5 by the new cover (v2), 6 by § 6. 987 words, the story about 590. For Jona's read. Passed by Jona and published 2026-10-24 with Waves 2 to 7.
evidence: every figure, date and quote read in the pulled text in research/_pulls/ by the writer on 2026-10-23, and every quote string-matched again on its page by the evidence audit of 2026-10-24; the committees' PDF fetched again from parlament.ch on both days (plain curl, HTTP 200) and matched by sha256 with the copy in _pulls/. Rows in ~/cutover/evidence/run.md. The source is in German and every English rendering on the page is the writer's. GovS 002 read in the local mirror (Figure 5 read as an image on 2026-10-24); the publisher's page and PDF refuse curl and a headless browser (403), so Jona opens the official PDF before the page goes up.
published: 24 October 2026
answers: Answers: while it's being built, where does it stand, and who can show it?
cover: /delivery/run/run-cover.png
desc: The stretch from Plan baselined to Build complete, who runs it and what it decides. How Switzerland's tax IT project INSIEME kept writing monthly reports through 2009 while no project body at the top of the administration held a minuted meeting, and the stage's three parts.
---

# No minuted meetings

December 2008 · Swiss Federal Tax Administration

In 2001 Switzerland's Federal Tax Administration started INSIEME, a project to replace its old IT systems with one system for every kind of tax.[1] In 2007, after an outside audit found that it would far exceed the time and money planned unless it changed substantially, the administration withdrew its award to its supplier and relaunched the project with the federal IT office as the builder.[1] It ran until September 2012, when the head of the finance department stopped it. It had cost 115.9 million francs, and the department called that clearly out of proportion to its progress.[1]

To oversee the relaunch, the administration set up a steering committee of 14 to 18 people at the end of April 2008. It was to watch the project's cost, dates and deliverables through the reports of the overall project head and the quality and risk controllers, and step in where needed.[1] On 3 June 2008 it decided that a special project for a new value added tax law would come first, and gave it resources from inside the project.[1] The Finance Committees and the Control Committees of the Swiss parliament, which later investigated INSIEME, found that decision did much to send the project off course, though they didn't put the whole responsibility on the steering committee.[1] By the minutes parliament's committees were given, the steering committee met four times, the last at the end of 2008.[1]

Its successor, an overall project committee, was formed in December 2009. For the year in between, parliament's committees found no minuted meeting of any project body at the top of the administration. The administration's IT board took up INSIEME at three of its meetings in that time.[1] Meanwhile the monthly controlling reports went on, as they had since mid-2007, with quality and risk reports beside them.[1] In the second half of 2009 the finance department's head of IT saw serious problems in the project. The department's leadership didn't give them the weight they needed and took no action.[1]

Parliament's committees couldn't find out what the finance department's general secretariat knew of the project in that time. There were no minutes of project committee meetings for that year, and no standard reports reached the secretariat before mid-2010.[1] In May 2013, given the state of the files, the committees gave up on a full review of them and worked from hearings and from documents they asked for one by one.[1]

From 2010 management and quarterly reports were added to the monthly ones. "Evidently the shortage was not so much in their quantity," the committees wrote, "as in their quality, completeness and coherence."[1] Of twenty project designs they analysed, two could be shown in writing to have followed HERMES, the method federal projects had been required to use since 1995.[1]

They found that the tax administration's director had pushed to improve the reporting, though he couldn't make it meet his requirements.[1] They didn't blame only the people who wrote the reports. The head of IT's finding showed, they wrote, that "a critical assessment of the project would have been possible" with the information there was. The people who receive reports, they added, have to keep asking until they get what they need.[1] From October 2011 a new project head had the key documents written down, dated and signed by the people responsible for them.[1]

The steering committee was set up to watch the project through its reports. The monthly reports were still being written through 2009, and the steering committee hadn't held a minuted meeting since the end of 2008.

## What Run is

Run is the stretch of a project where the system gets built and tested. It runs from Plan baselined to Build complete, two gates on the [project's gate map](/delivery/project/). The field calls it execution, or the build phase. In a company of 40 Run might be ten weeks of a weekly note from the engineering lead, a short list of decisions and one folder of test runs. Its main document is the [status report](/delivery/status-report/).

GovS 002, the UK government's standard for project delivery, has no stage called Run. It keeps planning and control going "throughout the life cycle" and puts the decisions at gates between stages.[2]

## Who runs it

The project manager runs it. GovS 002 makes planning and control "the responsibility of the relevant manager", which for a project is the project manager.[2] The project manager answers to the senior responsible owner, whom most companies call the sponsor, and the sponsor makes the decisions about the project's future.[2]

In a company of 40 the project manager is often the engineering lead, who writes the weekly report, keeps the decision log and makes sure each test result is filed and checked by someone who didn't build it. Whoever the report goes to, usually the sponsor, reads it and has to ask when a line in it doesn't add up.

## What it decides

Run decides the day-to-day: what gets built next, which defect holds up what, whether a test result stands, and when a problem goes up. GovS 002 asks for each manager to be given tolerances on cost, schedule, scope and more, "within which no escalation is required to the next level of management".[2] Beyond them a decision goes to the sponsor, and beyond the sponsor's authority to the body above.[2] A change to the baselined plan goes through Baseline and change control.

Whether the build is complete is decided at the gate, by the person the gate map names, on criteria agreed before Run started and changed since only through a logged decision. The three parts below are what that person reads. The test evidence lists the runs behind each criterion in [acceptance and sign-off](/delivery/acceptance-and-sign-off/), each with who checked it and the file its result is kept in. GovS 002 asks for reports that are "factual and realistic" and dated.[2]

## Its parts

{{PARTS}}

## Sources

1. The Finance Committees and the Control Committees of the Swiss parliament (the Federal Assembly). *Informatikprojekt INSIEME der Eidgenössischen Steuerverwaltung (ESTV)*, report of 21 November 2014. In German; quotations translated for this page. Pages 6378, 6379, 6381, 6387, 6427, 6428, 6432, 6433, 6434, 6496, 6497, 6499, 6503 and 6523. https://www.parlament.ch/centers/documents/de/bericht-insieme-fk-gpk-2014-11-21-d.pdf
2. Cabinet Office. *Government Functional Standard GovS 002: Project delivery*, version 2.1, 1 September 2025. Clauses 4.4.8, 4.4.9, 6.3 (with Figure 5), 6.4.4, 7.1 and 7.5. https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/
