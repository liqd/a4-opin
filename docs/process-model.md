# Projects - How do they work?

Opin allows users to create organisations and projects inside those organisations. Those projects are
participatory processes, build up by participation modules and phases.

## Purpose of this document

In this document we try to describe exactly what a projects is. It should be understanable by developers, non-technical stuff and user with good knowledge of the platform.

## Data model of a project

Each project has some meta data, that will always be present. It needs to have a name, a
description, information if it is private and at least one moderator. It can have an image and, a
background image. If it is private it also might have participants.

In euth a project is made up by a collection of particiaption modules. Each participation module has
phases that can be activated or deactivated. For our example there exists only one participation
module called 'idea collection'. It offers the following phases:

  1. Add ideas:
   - participants can add ideas
   - participants can updated, delete thier own ideas
   - participants can comment ideas
  2. Rate ideas:
   - participatns can comment ideas
   - participatns can vote ideas
  3. Comment ideas:
   - participatns can comment ideas
  4. Universal:
   - participants can add ideas
   - participants can updated, delete thier own ideas
   - participants can comment ideas
   - participants can vote ideas


(The last one is for compatibility with the old platform)

When a participation module is added to a project all phases will be added. The intiator can then disable
phases that she doesn't need. She can also set a title, set a desription, add start date, and
add end date for each phase.

Start and end dates of a phase should never overlap with another phase of all participation modules
in the same project. If a project is not in draft mode all dates should be set, but they might be
changed by the moderators. The active phase is the phase which starts earlier than the current date
and ends later.

To make this less theoretical, lets give the representation of an example project:

- project
   - Name: Build a new tree house.
   - Information:
      We want a new tree house in our garden and invite all neighbours and family members to design that tree house.

      In order to be cheap and sustainable the tree house should be build from recycleable
      materials.

      First we collect cool ideas for elements that a tree house should have (like rope ladder, fountain,
      bucket shower).

      Than you can add your proposal by drawing a concept study. Through rate and jury
      decision the best one will be selected and than realized.
   - Moderators: Tina, Sam
   - Participation modules:
       - Idea Collection:
         - Phases:
             1. Add ideas:
               -Title: Best tree house element
               - Description:
                  Give us your facourite tree house element and say why it is the best.
               - Start: 1st june 2016
               - End: 5th june 2016
             2. Rate ideas:
               - Title: Vote elements
               - Description:
                 Vote your favourite tree house element.
               - Start: 6th june 2016
               - End: 10th june 2016
             3. Comment ideas: **Disabled**
             4. Universal: **Disabled**
       - Idea Collection:
         - Phases:
             1. Add ideas[**active**]:
               - Title: Propose your tree house vision
               - Description:
                   Use the provided image of the tree and add a draft of your envisioned tree house
                   to it. Please keep in mind that we only have 100 € of savings.
               - Start: 14th june 2016, 8:00 h
               - End: *not set*
             2. Rate ideas:
               - Title: Rate the submitted drawings
               - Description:
                 Vote up all the tree house designs you like, so Tina and Sam can make a good
                 decision what to build.
               - Start: *not set*
               - End: *not set*
             3. Comment ideas: **Disabled**
             4. Universal: **Disabled**

For each project two phases are added automatically:

 - information: In this phase only the information text of the project is displayed
 - result: In this phase a result text provided by the moderator is displayed
