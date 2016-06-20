# Processes - How do they work?

Opin allows users to create organizations and within those groups projects. Those projects are
participatory processes, build up by participation modules and phases. In this document we try to
describe exactly what a process is. It should be understanable by developers, project managers and
user with good knowledge of the platform.

## Data model of a process

Each process has some meta data, that will always be present. It needs to have a title, a
description, information if it is private and at least one moderator. It can have an image and, a
background image. If it is private it also might have participants.

In euth a process is made up by a collection of particiaption modules. Each participation module has
phases that can be activated or deactivated. For our example there exists only one participation
module called 'idea collection'. It offers the following phases:

  1. Add ideas:
   - particpants can add ideas
  2. Add and comment ideas:
   - participants can add ideas
   - participatns can comment ideas
  3. Offline idea workshop:
   - moderator can upload ideas from offline meeting
  4. Comment ideas:
   - participatns can comment ideas
  5. Rate and commment ideas:
   - participatns can comment ideas
   - participatns can vote ideas
  6. Rate ideas:
   - participants can rate ideas
  7. Offline rate:
   - moderator can upload rates from offline meeting
  8. Offline jury selection:
   - moderator can upload labels/statments from offline jury meeting

When a process module is added to a process all phases will be added. The intiator can then disable
all phases that she doesn't need. She can also set a title, set a desription, add start date, and
add end date for each phase.

Start and end dates of a phase should never overlap with another phase of all participation modules
in the same process. The might be ommited, in that case the processes needs to be manually switched
to that phase. If that happens the end date of the prvious phase and the start date of the new phase
will be set. The active phase is that phase that has a start date in past and a end date in the
future or no end date set.

To make this less theoretical, lets give the representation of an example process:

   Title: Build a new tree house.
   Description: We want a new tree house in our garden and invite all neighbours and family members
                to design that tree house.

                In order to be cheap and sustainable the tree house should be build from recycleable
                materials.

                First we collect cool ideas for elements that a tree house should have (like rope
                ladder, fountain, bucket shower).

                Than you can add your proposal by drawing a concept study. Through rate and jury
                decision the best one will be selected and than realized.
   Moderators: Tina, Sam
   Participation modules:
     a. Idea Collection:
      Phases:
        1. Add ideas:
           Title: Best tree house element
           Description: Give us your facourite tree house element and say why it is the best.
           Start: 1st june 2016
           End: 5th june 2016
        2. Add and comment ideas:
           -- Disabled --
        3. Offline idea workshop:
           -- Disabled --
        4. Comment ideas:
            -- Disabled --
        5. Rate and commment ideas:
            -- Disabled --
        6. Rate ideas:
           Title: Vote elements
           Description: Vote your favourite tree house element.
           Start: 6th june 2016
           End: 10th june 2016
        7. Offline rate:
            -- Disabled --
        8. Offline jury selection:
            -- Disabled --
     b. Idea Collection:
       Phases:
         1. Add ideas:
           -- Disabled --
         2. Add and comment ideas [active]:
           Title: Propose your tree house vision
           Description: Use the provided image of the tree and add a draft of your envisioned tree house
                        to it. Please keep in mind that we only have 100 € of savings.
           Start: 14th june 2016, 8:00 h
           End: -- not set --
         3. Offline idea workshop
           -- Disabled --
         4. Comment ideas:
           -- Disabled --
         5. Rate and comment ideas:
           -- Disabled --
         6. Rate ideas:
           Title: Rate the submitted drawings
            Description: Vote up all the tree house designs you like, so Tina and Sam can make a good
                          decision what to build.
            Start: -- not set --
            End: -- not set --
         7. Offline Rate:
            -- Disabled --
         8. Offlice jury selection:
            Title: Winner
            Description: Tina and Sam select the best among the 5 highest votet proposals. The
                          selection is based on rates, general vibes from the comment and budget.


## How to setup a process

TODO
