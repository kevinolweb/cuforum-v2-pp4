# CU Forum
![Project Preview](/additional/main-image-1.jpg)

The CU Forum is an online communication for platform for credit union staff and volunteers across all of Ireland to communicate with each other and share knowledge. The site is designed to be a social media site for credit unions to facilitate information sharing and communication across different credit unions throughout the country. One can login and create posts for other members to view, like and comment on fellow members posts. 


The tool is deployed here [https://cuforumv2.herokuapp.com/]

# UX

## The Strategy Plane
* The site is aimed at credit union staff and volunteers which vary in age from 20 years old to 80 years old. The site as such needs to be easy to navigate for all to encourage engagement. These people are busy professionals and would like a simplified experience that allows them to connect with their peers in other credit unions


## The Scope Plane
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


## The Structure Plane

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


## The Skeleton Plane

### Database Design
Before begining the project I used Excel to help me visualise the database layout and how the different keys would connect with each other. This helped me when in development as I already had the models ready to develop and knew how they connected making for faster deployment.

### Wireframing
I used Balsamiq to help me organise my thoughts on what I would develop and how the end outcome would look. I find the simplicity of the tool quite nifty for bring the project down to its basic component parts and prevent you becoming excessively bogged down on colours etc.

Homepage Variants
![Home Preview](/additional/Homepage B.png)
![Home Preview](/additional/Homepage.png)

Discussion Page
![Home Preview](/additional/Discussion Page.png)

Create a Topic
![Home Preview](/additional/Create a Dicussion.png)

Login Page
![Home Preview](/additional/Login Homepage.png)
![Home Preview](/additional/Login.png)

Register Page

![Home Preview](/additional/Register.png)

My Profile
![Home Preview](/additional/My profile.png)

## The Surface Plane

### Design
I went with a soft blue for the colour scheme to give the UX a user friendly look. I complimented it with a bright purple for the categories section so this finter woption would stand out and bring vibracy to the page.
![Home Preview](/additional/main-image-color.jpg)


## Testing
I tested all of the HTML, CSS and Python code to ensure all is working as it should prior to deployment. A series of both manual and automated tests were used to achieve this.

### Automated tests
Django Unit tests were used on aspects of the application in order to test functionality

#### Models
Automated test on Topic model to ensure topic trending is set to false.
![Models Test 1](/additional/models.png)

Automated test to ensure the topic title conforms to within 250 characters.
![Models Test 2](/additional/models2.png)

#### Forms
Two automated tests were created to test to ensure that a topic cannot be created with a title and to ensure a user cannot set another user as a creator of a topic.
![Forms Test](/additional/forms-test.png)

#### Views
A series of automated tests were run on the front facing side of the website to ensure it is displaying correctly to all visitors and no pages are down or displaying 404’s.


##### Homepage 
An automated test was run on the homepage to ensure it is loading for visitors with a status 200.

![Views Test 1](/additional/views-test-1.png)

##### Sign in Page
An automated test was run on the sign in page to ensure it loads for all visitors and users.

![Views Test 2](/additional/views-test-2.png)

#### Dashboard Page (non-logged in users)
An automated test was run to ensure the dashboard page redirects and does not load for non logged in users. As the view utilises the  login_required decorated similar to other authenticated views, I felt it was important to test this functionality does not display a request 200 and load the dashboard view which is for logged in users only.

![Views Test 3](/additional/views-test-3.png)


### Manual Testing
#### Unauthenticated users
1. Non logged in users cannot create a topic
2. Non logged in users cannot access the dashboard
3. Non logged in users cannot delete a topic
4. Non logged in users cannot contribute to the site other than through signing up as a member
5. Non logged in users do not see links to the dashboard or to “create a topic” on the homepage page navigation

#### Authenticated users
1. Users who sign up cannot access the admin panel - they remain staff so can access the topic dashboard etc once the register for the site but not admin area
2. Users who are signed in cannot delete topics that another user created
3. Users who are signed in cannot edit another persons topic
4. Users can delete their own topic
5. Users can edit their own topic
6. Users are able to successfully sign in and be redirected to the dashboard
7. Users are able to logout and are taken to the logout page and back to the homepage once they have confirmed they are signing out


## Technologies Used
* HTML
* CSS
* Python
* Django


## Deployment
* The code was deployed through Heroku server and can be viewed here[https://cuforumv2.herokuapp.com/].
* The database used is Elephant SQL
* All media files are stored through Cloudinary

## Credits 
* The Code Institute projects were used to assist my learning of Django and building applications requiring CRUD functionality.

