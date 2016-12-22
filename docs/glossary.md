**Contet Management System (CMS)**:
The Opin Platform consists of the platform itself, meaning the part where users can add, edit, delete organisations, projects, modules, phases, ideas, comments, ratings, reports etc. as well as of descriptive webpages that give more information on the platform, such as imprint, help and how to's. As these webpages should be editable by a user a Content Management System (CMS) is used. For this project the Wagtail CMS used. Major advantage of this CMS is that it builds up upon the Webframework Django which is also used for the OPIN Platform. Because of that it is possible, that users who are logged in on the platform and also have rights to access the CMS-Administration interface, do not have to log in again. 

---
**Comment**:
A comment is the expressed opinion of a user. Users on Opin can comment on ideas, documents and paragraphs. 

---
**Creator**
User geneared content has to be created by an user (usally participant, but other roles possible). If an user has created content, she will assume the creator role for that content. Creators have special rights, because they can delete or modify their own content.

---
**Dashboard**:
The part of the opin interface, used by organisation owners, initators and moderators to manage projects on the platform. In the dashboard also users can edit their personal settings, such as username, email-adress, avatars. 

---
**Feature,Tool, or Method**:
A feature/method/tool is a formalized way to collaborate in order to reach a common goal. In one participation project, content may be transferred from one feature/method/tool to another or even worked on with different features/methods/tools at the same time (e.g. online and offline)

---
**Initiator**:
There are various roles on OPIN: Different people may do different actions. For example, Initiators. They manage users and groups, initiate participation projects, invite users to private processes, edit and delete projects, proposals and comments, receive emails on reported comments.

---
**Item**:  (for developers only)
Items are an abstraction for any kind of resource that have a link to a module. For example ideas and documents inherit the the item class that means the they have foreign key to a module. On database level there is a table for each items, ideas, documents. If a new model that inherits the Item model is created it will get its own table and each row in the table will automatically have a foreign key to the item in the Item table. The foreign key to the module will be in the items table. More on the topic can be found here: https://docs.djangoproject.com/el/1.10/topics/db/models/#multi-table-inheritance

---
**Language Switch**:
OPIN offers the user several languages. The selection of languages can be changed at the top menue bar next to the log-in. In a drop-down menue users can select a language. OPIN offers its editorial content in several languages. Comments and proposals and other content added by users are not translated.

---
**Moderator**:
Moderators are defined for each project, this means one user can be moderator of several projects at the same time. Moderators of a project update the project settings and - if the project is private - invite and add participants to the project. They also receive a message, if a comment within this project was reported and can decide if the comment needs to be deleted. Depending on the modules and phases within in the project, they have additional rights, e.g. create the document for a commenting text module.

---
**Module**:
A sub unit of a project that contains user generated elements of a specific kind. For example all ideas of an project might be in one module, while all texts might be in an other one. A project might also contain two modules with both containing ideas. A module always belongs to a phase.

---
**Organisation**:
An organisation is a group of people with the permission to create private or public projects. They have their own dedicated page to display themselves on, using images and texts explaning why and how they are using Opin.me.

---
**Organisation owner**:
A user role with in an organisation, that allows to alter the details of the organisation. In addition this role can also create and manage processes. *Currently this role is not implemented, its responsibilites are taken over by the initiator*

---
**Participant**:
Participants are defined for each project, this means one user can be participant of several projects at the same time. If a project is private a user needs to be invited or added to the project by a moderator in order to become participant. In public projects all users are free to participate and therefore participants of the project.

---
**Phase**:
A phase is characterized by a starting and an ending time and date. It is a part of the participation project and allow users to divide actions in their project. For example, in the first phase, users post ideas, in the second phase, users can comment on the ideas and rate them. Sometimes a participation project consists thus of two phases. In another scenario a participation project consists of one phase only: Then users can post an idea, add a comment and rate at the same time.

---
**Poll**:
A poll is a way to collect many opinions in a short time. It is similiar to a survey: Users are asked to indicate their opinion from a list of possibilities. The results are usually visible after finishing the poll.

---
**Popularity**:
Ideas can be sorted by Popularity - popularity is defined by the number of positive ratings.

---
**Process**:
In OPIN we decided not to use the term 'process' but instead use 'project' as this term is more user friendly. 

---
**Project**:
OPIN offers initiators to execute digital participation projects. A project is initiated in the dashboard by an organisation. Each project follows the structure of "Information-Participation-Result". In the information tab, initiators tell about their aims and answer the "w" questions to their participants (why, what, when, who). In the participation tab, initiators set up modules. In the result tab, initiators present the results of the module when finished. 

---
**(Proposal vs) idea**:
An idea is a contribution by a user in a e-participation project. It is an expression of opinion towards the concrete topic of the project. An idea can be just text or can be text and a picture or just a picture. Other users can comment on an idea, asking questions or providing additional input. It is possible to rate an idea and hereby express agreement or disagreement.

---
**Rating**:
Through rating ideas or comments users express their agreement or disagreement with its content. 

---
**Social media verknüpfungen**:
Users have the possibility to connect to OPIN through social media accounts, such as Facebook or Google+. These settings can be managed in the user profile in the section "account connections". 

---
**Tab**:
Tabs are user interface elements used to group content together. Having several tabs next to each other creates a Tab group, where one Tab at a time can be activated to show its content. On Opin, we use Tabs to group content on the project detail page together ("Information, "Participation", "Result").

---
**Templates or Blueprints**:
Blueprints are used to let initiators choose a set of premade phases with defined features (commenting, rating, adding proposals, etc.). These blueprints are used to establish a standard of projects.

---
**Timeline**:
A design element used to show the chronological process of a Project. It is shown on the project detail page and highlights the active phase. It groups all phases to their modules, displaying further information about every phase (name, start/end date, whether it's active).

---
**User**:
After a User has registered to the platform he/she can participate in public projects or private projects he/she is invited in through creating proposals/collecting ideas, commenting or rating proposals, as well as editing his/her own content. Users can also be made initiators of an organisation by the owner or another initiator of the organisation. They can also be added as moderators to projects. Within the content management system (CMS) they can be added to the moderators and/or the editors group. Users can also receive administrator rights. By that they achieve access to the administrator interface, which allows them to add organisations and add, update or delete all available resource types on the platform.

---
**User generated content**
All things that will can be created by participants in a process (eg. comments, rates, ideas, reports).

---
**WISYWIG**:
A kind of editor where the user can immediately see the styles (bold, italics, links, images, etc.) that are applied to text. In Opin we are using the CKEditor for user generated content.
