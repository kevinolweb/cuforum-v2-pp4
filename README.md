# CU Forum
![Project Preview](/additional/main-image-1.jpg)

The CU Forum is an online communication for platform for credit union staff and volunteers across all of Ireland to communicate with each other and share knowledge. The site is designed to be a social media site for credit unions to facilitate information sharing and communication across different credit unions throughout the country. One can login and create posts for other members to view, like and comment on fellow members posts. 


The tool is deployed here [https://cuforumv2.herokuapp.com/]

## UX

### The Strategy Pane
* The site is aimed at credit union staff and volunteers which vary in age from 20 years old to 80 years old. The site as such needs to be easy to navigate for all to encourage engagement. These people are busy professionals and would like a simplified experience that allows them to connect with their peers in other credit unions


### The Scope Pane
* The site will require a login for people to engage and interact with the community
* An authenticated user can create conversation topics for other members to see as well as leave comments on other peoples topics.
* The site will require CRUD functionality
* The site needs a framework to handle easy authentication and restrict access to certain pages and elements based on the user id i.e I should not be able to edit other peoples comments
* The site needs to be responsive and load quickly across all formats

## Agile Methodology, User Stories & Epics

### User Stories
As a registered user my goals are to:
1. Join a forum which is easy to navigate and engage with fellow members
2. Join/register for a community where I can engage my peers in conversation topics related to work and like fellow members contributions 
3. I want registration to be managed by an admin so nobody can join without authorization and I know they are other credit union personnel
4. Over time I want a personalised experience where I am mainly only exposed to information that I am interested in or people I follow
5. I want the interface to show newly created topics first so I can easily see whats relevant and trending in the community
6. I want to post topics to get other users inputs and experience but also have the ability to delete my own topic if I make a mistake or disclose the wrong information
7. I want to like and unlike other peoples posts while also having the ability to comment and remove my own comments
8. I want to be able to update my own profile if my details or preferences change
9. I want to be able to reset my password at any time

### Kanban
I used the Kanban feature baord on Github to help plan my project successfully. I divided the project into a series of steps that needed to be completed. Once I started a task I marked it as in progress and done when finished. This helped me to clearly stay on task and not get lost in scope creep.
![Kanban Preview](/additional/main-image-4-kanban.jpg)

The Kanban board can be viewed here.[https://github.com/users/kevinolweb/projects/1/views/1]

### Development Plan
Development Plan
I identified a lof of requirements which I wanted to implement for the project. At it core I needed the project to be a CRUD application which would allow users to create conversation topics and make comments. I placed this need as the main must have as well as facilitation login. There were extra features I also wanted if time would allow. These features included a very personalised experience with information tailored to your role in the credit union, editing, liking and deleting comments, managing your own personal profile and updating your preferences etc.


## The Structure Pane

### Features
![Dashboard Preview](/additional/main-image-2.jpg)

* Role based User Authentication
Only logged in users can engage in the forum and all pages are blocked off to non logged in users. You cannot edit only peoples contributions and can only comment.
* Mobile and Pleasing Design
* Soft colours are used to make the application appear easy to use and invite people to interact

![Dashboard Preview](/additional/main-image-3-disctopic.jpg)
* Create discussion topics within the forum
* Comment on other peoples topics
* Filter community discussions by category so you only see what interests you
* Easy registration process
* Testimonial area on the homepage 
This feature allows the admin to easily highlight their testimonials of credit unions using the platform and visually add an image via the website admin panel.
* Easily update and delete topics you create
* Easy site navigation with main dashboard storing whats happening recently
* Access all the latest activities/discussion topics from a convenient dashboard which you are brought to when you login.


## The Skeleton Pane

## Database Design
Before begining the project I used Excel to help me visualise the database layout and how the different keys would connect with each other. This helped me when in development as I already had the models ready to develop and knew how they connected making for faster deployment.

## Wireframing
I used Balsamiq to help me organise my thoughts on what I would develop and how the end outcome would look. I find the simplicity of the tool quite nifty for bring the project down to its basic component parts and prevent you becoming excessively bogged down on colours etc.

Homepage Variants
![Dashboard Preview](/additional/main-image-3-disctopic.jpg)


### Advanced Error Checking
![Age error display](/assets/images/age-error-display.png)
* The tool checks that the user cannot be under or over a certain age in order to submit their salary data. And that it is a number.
![Salary error display](/assets/images/number-error.png)
* The tool checks that the user inputted a number and the salary is between a certain reasonable range of €10,000 - €100,000.

### Salary Information Collection Storage
* The tool stores data inputted by the user such as name, age and salary in a Google Worksheet for future data interrogation.

### Salary Comparison
![Salary Comparison](/assets/images/comparison.png)
* The tool takes your salary and checks it against the cumulative average salary across all industries stored in the Google Worksheet.
* The tool tells you how much more/less you earn compared to the national average salary in the year previous.


### Display Salary Data from Worksheet
![Display Industry Salaries](/assets/images/data-display.png)
* The tool displays average salaries across all industries which is stored in a Google Spreadsheet
* The user has the option of viewing this if they want by selecting 'y' or ending the survey by selecting 'n'.

## Technology
* The tool was developed using Python.

## Testing
1. I have put the code for the app through the pep8 editor and no major errors were uncovered.
2. Minor whitespacing issues and similar were discovered and will be addressed later as they do not affect code functionality.

## Deployment
* The code was deployed through Heroku and can be viewed here[[https://irish-salary-survey.herokuapp.com/].
* The Google Spreadsheet raw data is stored on a seperate private file.

## Credits 
* The Code Institute Love Sandwiches project was used to assist my learning of getting data from a spreadsheet and making calculations.

