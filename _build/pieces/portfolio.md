<!-- style-gate: allow (sources quoted verbatim) -->
---
slug: portfolio
kind: layer
status: v1, passed by Jona 2026-10-23; Wave 1
evidence: every figure and quote opened at source by the lead on 2026-10-23; rows in ~/cutover/evidence/layer-portfolio.md
published: 23 October 2026
answers: Answers: what are we running as a whole, and who can stop it?
template_name: The Board, in the portfolio workbook
cover: /delivery/portfolio/portfolio-cover.png
template_shot: /delivery/portfolio/frqz-portfolio-board.png
template_text: The Board is a tab in FRQZ's portfolio workbook, Starter and Full. The brief for an assistant is [a text file](/delivery/portfolio/frqz-portfolio-agent-brief.txt) beside it.
templates: Starter | /delivery/portfolio-map/frqz-portfolio-starter.xlsx | /delivery/portfolio-map/frqz-portfolio-starter-example.xlsx | Seven tabs ;; Full | /delivery/portfolio-map/frqz-portfolio-full.xlsx | /delivery/portfolio-map/frqz-portfolio-full-example.xlsx | Nine tabs
files: /delivery/portfolio/frqz-portfolio-agent-brief.txt
desc: What a portfolio is, who runs it and what its board should read. How the US government's IT Dashboard put more than 700 investments on one page and kept a failing one at moderately low risk, with a portfolio dashboard to download.
---

# Moderately low risk

September 2012 · US Department of Agriculture

In June 2009 the White House budget office, the Office of Management and Budget, put the performance of the US government's major IT investments on a public website. By 2013 the IT Dashboard covered more than 700 major investments at 27 agencies.[1] Each one had a colour for cost and a colour for schedule, worked out from the dates and money the agency reported. Each also had a risk rating from the agency's chief information officer, from 1 for high risk to 5 for low, "based on the CIO's best judgment".[1] The budget office used the Dashboard to pick out investments at risk and call them in to meetings that could halt them.[1]

One of them was Farm Program Modernization, at the Department of Agriculture. From May to July 2012 the number of high and very high risks in its own briefings went up every month, until it had three that were each judged 70 percent likely to happen. In September a senior oversight committee found it off-track and unable to resolve its issues. On the Dashboard it stayed at moderately low risk until November, when it moved to medium. In December it was rated high.[1]

The Government Accountability Office found that case when it checked 80 investments at eight agencies in 2013. Most ratings matched the documents behind them: 53 did, 20 partly did and 7 didn't.[1] The same audit found ratings that hadn't moved at all. The Department of Veterans Affairs didn't update its ratings for 19 months, because it couldn't send them automatically: it had decided to build its own way of sending them instead of buying one. And each year, while the budget was being put together, the budget office stopped updating the public Dashboard. It went without an update for 15 of the 24 months before the audit.[1]

Some of the work left the page altogether. The Department of Energy moved several of its supercomputer investments out of its IT reporting by calling them facilities, which took $368 million off, almost a quarter of its IT spending in 2012. The Department of Commerce took the ground systems for its satellites off, another $447 million. A member of the budget office's staff told the auditors it "could not stop agencies from making such recategorizations".[1]

In 2016 GAO tried again with 95 investments still being built, scoring each one from its own risk register. Its score showed more risk than the chief information officer's rating 60 times, the same 22 times and less 13 times. Twenty-three of the investments were green on the Dashboard and red on GAO's score.[2] GAO's scores were a judgement too, and three agencies said their ratings were right. GAO's view was that many of the ratings "minimized the potential severity and impact of high risk scores".[2]

The Dashboard put a whole portfolio on one page, and a reader could see every investment on it. From the page alone they couldn't tell how old a colour was, or whether it had been worked out from the numbers or chosen by a person.

## What a portfolio is

A portfolio is all the work an organisation has under way that draws on the same money and the same people, kept as one list by someone who can stop things on it. It holds programs and projects, and it keeps going after they end. New work keeps arriving and old work keeps closing, so its reviews come round on a cycle instead of at the end of a stage.[4]

The list itself has its own page, the [portfolio map](/delivery/portfolio-map/).

## Who runs it

The UK government's standard for project delivery, GovS 002, names two people. The portfolio director answers "for the direction and governance of the portfolio", getting the benefits it was set up for at a risk the organisation can accept. The portfolio manager plans and runs the portfolio as a whole, watches spend against the budget and the benefits as they come in, and makes sure information reaches the people deciding.[3]

Most portfolios also have a board or steering group, chaired by the director, where its decisions get made. In a company of 40 the director might be the chief executive, and the board might be the leadership meeting on a Monday morning.

## What it decides

The portfolio decides what starts and what stops. GovS 002 lists the decisions as approving portfolio plans, starting a programme or project, authorising the start of a project's next stage or a programme's next tranche, and "pausing, terminating or closing work".[3]

Everything below that is delegated. A program decides how its projects fit together and a project decides how its work gets done, inside the money and priority the portfolio gives them. The report the board reads comes back up from them.

## What the board reads

GovS 002 sets out what that report covers. Portfolio performance "shall be reported against the portfolio plan, including, but not limited to, finances, benefits, costs, outcomes, milestones and risks." Commentary should "explain variances", and the report should show "both achievement to date and a forecast for future performance".[3]

What went wrong on the Dashboard is why I'd build the page this way:

- **Keep the worked-out figures apart from the judged ones.** A rating someone chose goes beside the colour worked out from dates and money, with the name of the person who chose it, and it never changes that colour.
- **Date every row.** Each row carries the day its owner last checked it, and the page counts the rows checked too long ago.
- **Show what left.** Anything that came off the list since the last review is listed, with how it left and the money on it.
- **Say what isn't there.** If benefits or risks aren't tracked yet, the page says so in words instead of leaving a blank that reads as fine.
- **Put the date of the last review at the top**, beside today's date, so you can see how long the page has gone without one.

## Test the page before the board reads it

1. **Is anything old?** Count the rows still running that nobody has checked in the last five weeks. On the Dashboard, Veterans Affairs didn't update its ratings for 19 months.[1]
2. **Has anything passed its own date?** A row whose latest forecast is already behind it is out of date, whatever colour it shows.
3. **Is any owner calmer than the numbers?** Where the dates and money say red or amber and the owner's view is milder, put both in front of the board and ask the owner why. GAO's 2016 count found 23 investments rated green that it scored red.[2]
4. **What left since last time?** Read the list of rows that closed or moved out, and check each one went because someone decided it should.

## When an agent does part of it

An agent can do most of the preparation. Before each review it can recount the Board tab's figures from the register and say where they differ, and run the Board's three checks and the workbook's own, listing each failure with its row. It can list every row that left since the copy saved at the last review, including any name that has gone and might have been renamed, and the rows nobody has checked lately, with any tracker or finance activity on them since. It can also draft the commentary from the owners' variance notes. The UK's major projects authority describes a tool of its own for part of this: an Early Warning System that uses the data it already holds on the government's major projects to flag the ones at risk of being rated red.[5]

It reads the workbook, the copy saved at the last review, and the tracker and finance exports if you have them. It writes nothing in the workbook: it returns one table, and every line names the cell or file it came from.

It never types Last checked or an owner's view, and it doesn't decide whether the owner or the numbers are right. Where an owner's view is milder than the numbers, it writes the owner one question and gives the figures.

Check its work the same way each time: take the reddest row, the row checked longest ago and one row that left, and redo them from the cells. The mistakes to look for are an owner's view repeated back as the status, a renamed project reported as one stopped and one started, a blank owner filled in from a name in the tracker, and a cause in the commentary that isn't in any variance note.

The director signs the commentary and the page. The brief for the agent comes with the download and names no particular assistant.

## The dashboard

The Board is a tab in the portfolio workbook from the [portfolio map](/delivery/portfolio-map/), and it reads the register you already keep there. On one page it counts the rows in each health colour and lists the rows to discuss, Red and Amber first, with each owner's view beside the numbers. Then it leaves room for the director's two lines of commentary and a signature. Its three checks look for rows nobody has checked in 35 days and forecast dates that have already passed, and flag any row where the owner's view is milder than the numbers. A second page lists what left since the last review. The Starter and the Full workbook both have it, blank and filled in for the same made-up company.

{{TEMPLATE}}

## Its parts

{{PARTS}}

## Sources

1. U.S. Government Accountability Office. *IT Dashboard: Agencies Are Managing Investment Risk, but Related Ratings Need to Be More Accurate and Available*, GAO-14-64, December 2013. Highlights; pages 4, 6, 11 and 18 to 22. https://www.gao.gov/products/gao-14-64
2. U.S. Government Accountability Office. *IT Dashboard: Agencies Need to Fully Consider Risks When Rating Their Major Investments*, GAO-16-494, June 2016. Highlights; pages 15, 19 and 22. https://www.gao.gov/products/gao-16-494
3. Cabinet Office. *Government Functional Standard GovS 002: Project delivery*, version 2.1, 1 September 2025. Clauses 4.3, 4.4.5, 4.4.6 and 5.3.7. https://projectdelivery.gov.uk/library-products/government-functional-standard-govs-002-project-delivery/
4. Infrastructure and Projects Authority. *Assurance Workbook: Portfolios and portfolio management*, version 1.0, 15 July 2021. Page 13. https://assets.publishing.service.gov.uk/media/60ef0da7e90e0764d3614478/2021-07-15-version-1-Assurance-workbook-portfolios-and-portfolio-management__1_.pdf
5. National Infrastructure and Service Transformation Authority. *NISTA Major Projects Annual Report 2025-26*, 13 July 2026. Section 8. https://www.gov.uk/government/publications/nista-major-projects-annual-report-2025-26/nista-major-projects-annual-report-2025-26
