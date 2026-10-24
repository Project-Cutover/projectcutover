"""Every word on projectcutover.com outside the pieces. Source: the copywriter's v2,
~/cutover/writing/standard/drafts/copywriter-site-copy-v2.md (2026-10-22). Change words there first, then here."""

SUBSTACK = 'https://jonavenzor.substack.com/subscribe'
SKIP = 'Skip to the content'
SUBSCRIBE = 'Subscribe'

NAV = [('delivery', 'Delivery', '/delivery/'), ('about', 'About', '/about/')]
SHOW_VIDEOS = False  # the Videos page is built and linked only once a video is up

FOOT = {
    'credit': 'Project Cutover is brought to you by FRQZ.',
    'read_h': 'Read',
    'read': [('Delivery', '/delivery/'), ('About', '/about/'), ('Newsletter', '/newsletter/')],
    'contact_h': 'Contact',
    'contact': [('jona@projectcutover.com', 'mailto:jona@projectcutover.com'), ('Subscribe on Substack', SUBSTACK)],
    'copyright': '© 2026 Project Cutover',
}


def comp(name, what, q, aka):
    import re
    return {'name': name, 'slug': re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-'), 'what': what, 'q': q, 'aka': aka}


LAYERS = [
    {'name': 'Portfolio', 'short': 'Everything under way across the organization, and how it decides what starts next.', 'comps': [
        comp('Portfolio map', 'Every program and project under way, with an owner and a stage against each.',
             'Answers: what are we running, and who owns each one?', 'project inventory, portfolio register'),
        comp('Intake and scoring', "How a new request gets in, and how it's ranked against the work already running.",
             'Answers: should we take this on, and ahead of what?', 'demand management, project intake, prioritization criteria'),
        comp('Capacity', 'How many people are free for new work, counted before anything new starts.',
             "Answers: who's free to do it?", 'capacity planning, resource management')]},
    {'name': 'Program', 'short': 'A group of projects run together because they serve one goal.', 'comps': [
        comp('Program charter and benefits', 'What the program is meant to deliver, and how anyone will know it did once the projects have closed.',
             'Answers: what is this program for, and how will we know it worked?', 'program mandate, program brief, benefits register, benefits realization plan'),
        comp('Roadmap and dependencies', 'When each project lands, and which ones are waiting on another.',
             "Answers: what's waiting on what?", 'program roadmap, integrated master schedule, dependency map'),
        comp('Program meetings', 'The meetings a program holds, and what each one is allowed to decide.',
             'Answers: where does this get decided?', 'governance cadence, steering committee, program board')]},
    {'name': 'Project', 'short': 'One piece of work with a sponsor and an end date.', 'comps': [
        comp('Project charter', "What the project is for, who sponsors it, what it can spend and what's out of scope.",
             'Answers: why are we doing this, and where does it stop?', 'project initiation document (PID), project brief, terms of reference'),
        comp('Acceptance and sign-off', 'One page the sponsor signs, saying what live means for this project and how someone could test it.',
             "Answers: how will we know we're done?", 'what finished looks like, acceptance criteria, success criteria, definition of done'),
        comp('RACI', "For each decision, who does the work, who answers for it, who's asked first and who's told after. The letters stand for responsible, accountable, consulted and informed.",
             'Answers: who decides this?', 'responsibility assignment matrix, RASCI'),
        comp('Stakeholders and communication', 'Everyone the project affects, and what each of them needs to hear and when.',
             'Answers: who needs to know?', 'stakeholder register, stakeholder map, communications plan'),
        comp('RAID log', 'Risks, assumptions, issues and dependencies, each with an owner and a date to look at it again.',
             "Answers: what could go wrong, and who's watching it?", 'risk register, issue log')]},
    {'name': 'Plan', 'short': 'How the work is broken down and scheduled, and what happens when the plan changes.', 'comps': [
        comp('Work breakdown', 'The whole job, split into pieces small enough for one person to own.',
             "Answers: what's all the work?", 'work breakdown structure (WBS), work packages'),
        comp('Schedule', 'The order the work happens in, and the chain of tasks that sets the end date.',
             'Answers: when will it be done?', 'project schedule, Gantt chart, critical path'),
        comp('Estimates', 'How long each piece should take, and where the number came from.',
             'Answers: how sure are we of that date?', 'effort estimate, three-point estimate, basis of estimate'),
        comp('Baseline and change control', 'The plan everyone agreed to, and how a change to it gets asked for and approved.',
             'Answers: who agreed to that change?', 'scope baseline, change request, change control board (CCB)')]},
    {'name': 'Run', 'short': 'The build itself, and the records kept while it happens.', 'comps': [
        comp('Status report', 'Where the project stands this week, with any slip shown in the week it happens.',
             'Answers: where are we this week?', 'status update, RAG report, highlight report'),
        comp('Decision log', 'Every decision that changes the project, with who made it and when.',
             'Answers: when did we decide that, and who did?', 'decision register, action and decision log'),
        comp('Test evidence', 'What was tested, what passed and who checked it, kept where someone can find it later.',
             'Answers: can you show it works?', 'test summary report, test exit report, UAT sign-off, traceability matrix')]},
    {'name': 'Cutover', 'short': 'The days around go-live, when the new system takes over from the old one.', 'comps': [
        comp('Readiness and go/no-go', 'The criteria that decide whether go-live happens, agreed weeks ahead, and the one person who makes the call.',
             'Answers: are we ready to go live?', 'go/no-go criteria, operational readiness review, launch readiness'),
        comp('Cutover plan and rollback', 'Every task in the cutover window in order, each with an owner, and every change with a way to undo it.',
             'Answers: what happens during cutover, and how do we back out?', 'cutover runbook, implementation plan, backout plan, fallback plan'),
        comp('Rollout', 'Who gets the new system first, and what has to be true before it reaches everyone else.',
             'Answers: who gets it first?', 'phased rollout, pilot, canary release, day one')]},
    {'name': 'Handover', 'short': "When the project ends and a team that didn't build the system takes it on.", 'comps': [
        comp('Handover and ownership', 'The team that will run the system, named before go-live, and what the project leaves them.',
             "Answers: who owns it once the project's gone?", 'transition to operations, handover to business as usual (BAU), hypercare exit'),
        comp('Project close', "What was delivered against what was promised, and who owns what's still open.",
             'Answers: did we deliver what we said we would?', 'closure report, post-implementation review, lessons learned')]},
]
for _l in LAYERS:
    _l['long'] = _l['short']

WHO = ('Jona Venzor has run software implementations and cutovers for about ten years, in hospitality, banking, gaming '
       'and cloud hosting. The largest ran to thousands of tasks across more than 100 people.')

HOME = {
    'title': 'Project Cutover',
    'desc': 'How to run software delivery, from the portfolio to the handover. Each piece opens on a real failure from a public report and comes with a workbook to start from.',
    'headline': 'How to run software delivery, from the portfolio to the handover',
    'stand': 'Each piece opens on a real failure from a public report and comes with a workbook to start from.',
    'cta': 'Subscribe',
    'cta_href': '/newsletter/',
    'first': ('Read the first piece', '/delivery/portfolio-map/'),
    'layers_h': 'Delivery',
    'layers_p': '',
    'layers_link': 'What each one is for',
    'who_h': "Who's behind it",
    'who_p': WHO,
    'who_link': ('About', '/about/'),
}

SIGNUP = {
    'h': 'Subscribe',
    'p': 'New pieces go out on Substack. It\'s free.',
    'btn': 'Subscribe on Substack',
}

DELIVERY = {
    'title': 'Delivery · Project Cutover',
    'desc': 'Software delivery from the portfolio to the handover: what each part is for and what the field calls it.',
    'h1': 'Delivery',
    'sub': 'From the portfolio to the handover.',
    'stand': 'A portfolio holds programs, and a program holds projects. Each project is planned and run, then cut over and handed to the team that keeps it.',
    'map_label': 'Delivery, drawn as layers: a portfolio holds programs, a program holds projects, and each project is planned, run, cut over and handed over',
    'toc_label': 'Layers',
    'aka_label': 'Also called:',
}

WATCH = {
    'title': 'Videos · Project Cutover',
    'desc': 'A video for each piece on Project Cutover: the same case and the same document, talked through in 10 to 14 minutes.',
    'h1': 'Videos',
    'stand': ('Each piece on this site gets a video: the same case and the same document, talked through in 10 to 14 minutes. '
              'They go up on the Project Cutover channel on YouTube.'),
    'episodes': [],  # newest first: {'title', 'minutes', 'component', 'piece', 'url'}
}

ABOUT = {
    'title': 'About · Project Cutover',
    'desc': 'Who writes Project Cutover, and how to get in touch.',
    'h1': 'About',
    'body': ('Project Cutover is about how software delivery gets run, from the portfolio to the handover.\n\n'
             f"## Who's behind it\n\n{WHO}\n\n"
             '## Get in touch\n\nWrite to [jona@projectcutover.com](mailto:jona@projectcutover.com).'),
    'button': ('Subscribe on Substack', SUBSTACK),
}

NEWSLETTER = {
    'title': 'Newsletter · Project Cutover',
    'desc': 'Subscribe to Project Cutover on Substack. It\'s free.',
    'h1': 'Newsletter',
    'body': "New pieces go out on Substack. It's free.",
    'button': ('Subscribe on Substack', SUBSTACK),
}

NOTFOUND = {
    'title': 'Page not found · Project Cutover',
    'desc': 'There is no page at this address.',
    'h1': 'Page not found',
    'body': "There's no page at this address. Every piece is listed in [Delivery](/delivery/).",
    'button': ('Home', '/'),
}

PIECE = {
    'on_page': 'On this page',
    'meta': '{date} · {minutes} min read',
    'close_h': 'New pieces go out on Substack.',
    'close_btn': 'Subscribe on Substack',
    'dl_label': 'The template',
    'dl_btn': 'Download the {label}',
    'dl_example': 'Or the filled-in example',
    'dl_alt': 'The first tab of the template, filled in',
    'connects_h': 'Connects to',
    'draws_on': 'Draws on:',
    'feeds_into': 'Feeds into:',
    'sources_h': 'Sources',
    'prev': 'Previous:',
    'next': 'Next:',
}
