<!-- style-gate: allow (sources quoted verbatim) -->
---
slug: project
kind: layer
status: draft v2 (2026-10-23), the lead's fixes applied, for Jona's read. Passed by Jona and published 2026-10-24 with Waves 2 to 7.
evidence: every figure, date and quote read in the pulled text in research/_pulls/ by the writer on 2026-10-23; both Victorian Auditor-General PDFs matched by sha256 with the copies on audit.vic.gov.au the same day. Rows in ~/cutover/evidence/project.md. The agent section's account of the brief's test is the lead's graded second run (pass). GovS 002 read in the local mirror; Jona to open the official PDF before the page goes up.
published: 24 October 2026
answers: Answers: what has to be true before this goes further, and who says so?
template_name: Gate map workbook
cover: /delivery/project/project-cover.png
template_shot: /delivery/project/frqz-gate-map.png
template_text: One size for any project: open the Example to see four of its five checks fail, then start on the blank. The brief for an assistant is [a text file](/delivery/project/frqz-gate-map-agent-brief.txt) beside it.
templates: Gate map | /delivery/project/frqz-gate-map.xlsx | /delivery/project/frqz-gate-map-example.xlsx | Three tabs
files: /delivery/project/frqz-gate-map-agent-brief.txt
desc: What a project is, who runs it and what its gates decide. How Victoria's Ultranet went to contract in 2009 after four of its five gate reviews rated it Red, with a gate map to download.
---

# Critical and urgent

May 2009 · Department of Education and Early Childhood Development, Victoria

In November 2006 the government of Victoria, in Australia, announced the Ultranet, an A$60.5 million project run by the state's education department: an online system for teaching, learning and assessment in every government school.[1] Since 2003 Victoria had used the Gateway Review Process, managed by its treasury department: short reviews by a team from outside a project at six points in its life, called Gates. A project wasn't meant to move on until the review at its gate had been completed. Each review ended in a confidential report to the project's senior responsible owner, rated Red, Amber or Green.[2]

The Ultranet had five Gateway reviews while it was being planned, between May 2007 and February 2009. Four were Red, which then meant "critical and urgent, action on recommendations should be taken immediately", and one was Amber.[1] The reviewers warned that the $60.5 million budget hadn't come from a full scoping of the project, and more than once they couldn't do a full assessment because the documents weren't complete.[1] In May 2008, after the first tender drew no suitable bid, the premier's department recommended stopping the project. The government cut it back to fit the budget instead, from 1,260 required functions to 131.[1]

In May 2009 the education department asked the government for approval to sign a contract. Its third business case arrived that month, after the second tender had started, although the treasury department's own framework puts the business case before the tender.[1] The premier's and treasury departments both advised against going ahead. The treasury department asked whether the education department was "breaching due process and major project protocols". It wanted outside scrutiny of how a fixed budget of $60.5 million would cover a preferred bid of $77.3 million, and of why the required implementation plan and risk management frameworks hadn't been provided.[1] The scrutiny didn't take place, and the education department gave no further advice on the issues raised. On 30 June 2009 it signed the Ultranet's master agreement for $64.6 million.[1]

In December 2012 the Victorian Auditor-General found "no trail of documentary evidence to explain whether or how" the education department had dealt with the "many critical issues" the premier's and treasury departments raised. After each of the five reviews the project "proceeded to the next phase with little evidence that issues identified were rectified", and more than 60 percent of the reviews' recommendations hadn't been adequately addressed.[1] By the audit's estimate the Ultranet had cost about $162 million by June 2012.[1] From July 2011 to May 2012, on average, 10 percent of students and 27 percent of teachers logged in each month.[1]

In May 2013 the Auditor-General audited the Gateway process across the state. Taking part had in practice been each department's choice, and 62 projects worth $4.3 billion weren't included between 2005 and 2012. Nearly 70 percent of the projects reviewed had completed two gates or fewer. The treasury department hadn't tracked what departments did about the recommendations, or put review results in front of the government when it looked at how its major projects stood.[2]

The same audit called the process "a valuable concept", and departments said the reviews were of high quality.[2] The education department's broadband project for the same schools, VicSmart, was planned from a clear analysis of needs and options and was delivering its benefits.[1] From late 2010 a high-value or high-risk project needed the Treasurer's own approval at decision points such as the final business case, and one given a Red-rated recommendation had to send the Treasurer a plan of action.[2]

Victoria's rule was that a project shouldn't go on until its gate review had been completed. The Ultranet's reviews were completed, five times, and the project went on after each one.

## What a project is

A project is one piece of work with a sponsor, a budget and an end date. It's done in stages, and before each stage someone decides whether it goes on. GovS 002, the UK government's standard for project delivery, calls it "a unique, temporary management environment, undertaken in stages".[3] It can sit in a portfolio on its own or inside a program. It ends when its work is done and the people who'll run what it built have taken over the risks and issues still open.[3]

The decisions between stages are gates, which the field also calls stage gates, phase gates or decision points. In a company of 40 a project might be four people for a quarter with two gates, Start and Go/no-go. What the project is for, and where it stops, are written down in its [project charter](/delivery/project-charter/).

## Who runs it

GovS 002 asks for two named people on every project.[3] The senior responsible owner owns the business case and answers for the project meeting its objectives and delivering its benefits. The project manager answers to the senior responsible owner for running the project day to day. Above them is a sponsoring body, a person or a group, which the senior responsible owner answers to and which makes the decisions beyond that person's own authority. For a project inside a program it can be the program manager.[3]

Most companies call the senior responsible owner the sponsor. In Victoria's Gateway reviews it was "the senior executive to whom the project director reports".[2] In a company of 40 the sponsor is often the CTO or a founder, and the project manager is an engineering lead who also writes code. The project manager is usually the Owner on the Register and in the gate map.

## What it decides

A project decides how its own work gets done, one stage at a time. GovS 002 puts a gate before every stage, where someone authorises the stage to start and commits the money and people for it. The decision at a gate can approve going on, send the work back to be revised, defer it, or end the project.[3] In the gate map those are the outcomes Go, Revise, Defer and Stop.

Anything beyond the senior responsible owner's authority goes up to the sponsoring body.[3] In practice that's more money than was agreed or an end date the program can't take. Starting a project at all is the [portfolio's](/delivery/portfolio/) call. The levels below it on the map (Plan, Run, Cutover and Handover) work between its gates, and what they produce is judged at the next one.

## The gates

GovS 002 asks for four things at every gate: the criteria for going on, who decides, who is consulted, and the kind of review held before the decision.[3] The review comes before significant decisions "such as contractual commitments and gates", and its recommendations should be "documented, agreed and acted on".[3]

A software project's gates are often Start, Plan baselined, Build complete, Readiness, Go/no-go, Handover accepted and Close, with go-live as a milestone between the Go/no-go and Handover accepted. The criteria for the Go/no-go have a page of their own, Readiness and go/no-go, and so do those for the team taking the system over, Handover and ownership.

Before each gate, run these. Each is a gate map check of the same name.

1. **Find a gate with no criteria.** A gate that's decided, or due within 60 days, with nothing written about what has to be true at it can only be passed. The check, "A gate with no criteria, or criteria with no gate", also finds a criterion filed under a name that isn't a gate, such as Go-live.
2. **Name one person to decide each gate.** Put one name in Decides and everyone asked first in Consulted. The check is "A gate without one person to decide it, or no one consulted". When someone consulted raises a problem, write it down as a criterion so it stays Open until it's answered. The auditor found no record of how the education department answered the premier's and treasury departments.[1]
3. **Book each review before its gate, with someone else running it.** The check, "A gate review that's missing, late or not independent", fails a review dated after its gate, a reviewer who owns the project or decides the gate, and a Go on a review that didn't pass. The Ultranet's last review before its contract, in February 2009, was Red, and it went to contract with little evidence its issues had been fixed.[1]
4. **Find a gate passed without its evidence.** The check of that name fails a gate decided Go while one of its criteria is Open, Waived with no reason, or Met with nothing in Evidence.
5. **Check that the dates hold together.** The check, "Gate dates that don't hold together", fails a gate dated before a gate above it, a date that has passed with no decision, and a Go/no-go dated after the project's Latest forecast. The Ultranet's third business case came after the tender it should have come before.[1]

## When an agent does part of it

The checking before each gate can go to an agent. It recounts the Criteria lines against Gates, reruns the five checks against the sheet's results, and lists every line Open, Waived with no reason or Met with nothing in Evidence on a gate already decided Go. Given the copy saved at the last gate review, it lists each gate whose date, decider or outcome has moved and each line whose Status changed; given the project charter, it sets each gate's date and decider beside the charter's. For each undecided gate due within the days set for booking reviews (30 to start), it writes one question to the owner of each Open criterion.

It reads the workbook, the old copy, the charter and any Evidence document, and writes nothing: it returns one table per step, each line naming the cell or file it read. Whether a criterion is really true, and whether a waiver's reason is good enough, are for a person.

```
You check the gate map for <project name>. You never mark a criterion Met, record a
decision, or choose who decides or who reviews.
1. Recount each gate's Met, Open and Waived lines on Criteria against the Gates columns.
2. Run the five checks and compare each with the result on Gates. Ask about any line
   whose gate isn't on Gates, such as Go-live. Don't move it.
3. For each gate decided Go, list every line Open, Waived with no reason or Met with no
   evidence, and every Evidence document you weren't given ("not seen").
4. Against last review's copy, list each gate whose Date, Decides or Outcome moved, and
   each line whose Status changed. Against the charter, set each gate's Date and Decides
   beside it: same or different.
5. For each undecided gate due within the days in Gates B11, ask the owner of each Open
   line one question: is it true now, and where is the evidence?
Return one table per step: the gate or line, what you found, and where you read it.
```

Run on the Example with an old copy and the charter, the brief matched its answer key on every line: the four failing checks, a Go-live question that named no gate, two Evidence documents "not seen", both changes since the old copy and eight questions to the right owners.

Check its work each time by redoing three things by hand: the first gate it says fails "A gate passed without its evidence", one gate it says is clear, and one of its questions against the criterion's row. The mistakes to look for are a line filed under Go-live read as the Go/no-go, a Waived line counted as Met, and an Evidence entry taken as proof.

The person in Decides makes the call at each gate and types Decided on and Outcome. A waiver is theirs to give too, and Reason records who gave it and why. Each criterion's owner says when it's Met, and the agent drafts the questions they're asked. The full brief comes with the download and names no assistant.

## The gate map

The gate map is one workbook per project, with three tabs: Read me, Gates and Criteria. Gates holds the project's settings, the five checks, and one gate per row in the order they come. Each gate has its Kind and Date, who Decides and who is Consulted, the Review before it with its Reviewer, Review date and Review result, and the Outcome once it's Decided on. Criteria holds one line per thing that must be true at a gate, with its Owner (says it's met), a Status of Open, Met or Waived, a Reason for any waiver and the Evidence for anything Met. The file works out each gate's counts and State, and the Check on every row of both tabs. It comes in one size, blank and filled in for Hollins Software, a made-up company. The filled-in one fails four of its five checks on purpose.

{{TEMPLATE}}

## Its parts

{{PARTS}}

## Sources

1. Victorian Auditor-General's Office. *Learning Technologies in Government Schools*, 2012-13:19, December 2012. Pages viii, ix, 6 and 20 to 25. https://www.audit.vic.gov.au/sites/default/files/20121212-Learning-Tech.pdf
2. Victorian Auditor-General's Office. *Planning, Delivery and Benefits Realisation of Major Asset Investment: The Gateway Review Process*, 2012-13:28, May 2013. Pages vii, viii, ix, xi, 1, 3, 5 and 30. https://www.audit.vic.gov.au/sites/default/files/20130508-Gateway-Review-Process.pdf
3. Cabinet Office. *Government Functional Standard GovS 002: Project delivery*, version 2.1, 1 September 2025. Clauses 3.3, 4.2.3, 4.4.7 to 4.4.9, 6.2, 6.3 and 6.4.8. https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/
