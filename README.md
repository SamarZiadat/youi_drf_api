<h1  align="center">you.i API</h1>

This the readme for the you.i project's backend. For more information about the frontend, please visit [this link](https://github.com/SamarZiadat/youi_frontend).

'youi.i' is a professional networking platform designed and created for digital design professionals globally. The interactive platform is intended to be used by digital designers to platform their own work, advertise their own events and create posts about their career. It also allows designers to keep up to date with digital design related events, and to interact with, learn about, and be inspired by other designers and their work.

The you.i API provides a backend database to create, view, edit and delete user's career-related posts, professional event advertisements, comments and reviews. A user can publish a post, including written content, an image, and keyword tags. A user can advertise an event, including a title and description for the event, an event category (ie. panel, workshop etc.), a format (ie. in person, hybrid), an image, and keyword tags. Users can follow each other, show support for a post by liking it, show interest in an event by bookmarking it, comment on posts, and leave reviews on events. The API also includes search and filter logic to improve user experience, and make it easier for users to find events and posts tailored to their own interests.

View the live API [here](https://youi-backend-25262e22ef8b.herokuapp.com/).

## Table of Contents

- [The Strategy Plane](https://github.com/SamarZiadat/youi_drf_api#the-strategy-plane)
  - [Agile Project Management](https://github.com/SamarZiadat/youi_drf_api#agile-project-management)
  - [Developer User Stories](https://github.com/SamarZiadat/youi_drf_api#developer-user-stories)
- [The Structure Plane](https://github.com/SamarZiadat/youi_drf_api#the-structure-plane)
  - [Features](https://github.com/SamarZiadat/youi_drf_api#features)
- [The Skeleton Plane](https://github.com/SamarZiadat/youi_drf_api#the-skeleton-plane)
  - [Database Design](https://github.com/SamarZiadat/youi_drf_api#database-design)
- [Technologies](https://github.com/SamarZiadat/youi_drf_api#technologies)
- [Testing](https://github.com/SamarZiadat/youi_drf_api#testing)
- [Deployment](https://github.com/SamarZiadat/youi_drf_api#deployment)
- [Credits](https://github.com/SamarZiadat/youi_drf_api#heroku-credits)

## The Strategy Plane

### Agile Project Management

This project was managed using agile methodologies by delivering small features in incremental sprints. There were 4 sprints and 6 epics in total. A kanban board was created using github projects and was utilised as a project management tool to help visualise work, limit work-in-progress, and maximise efficiency/flow for both backend and frontend of this app. The Kanban board can be viewed [here](https://github.com/users/SamarZiadat/projects/2/views/2).

![Image of Kanban](https://res.cloudinary.com/ddsrnz9la/image/upload/v1695288072/kanban_ut6ueo.png)

![Image of Project Board](https://res.cloudinary.com/ddsrnz9la/image/upload/v1696005608/project_board_view_2_r40r11.png)

### Developer User Stories

**Profiles**

- As a developer/superuser I can view a list of all profiles so that I can see all the profiles that have been created
- As a developer/superuser I can view the details of one profile so that I can see individual profile data
- As a developer/superuser I can edit a profile when I am logged in so that update my personal information
- As a developer/superuser I can delete a profile that I own so that I can delete my user account from the API

**Posts**

- As a developer/superuser I can view a list of all posts so that I can see all posts at once
- As a developer/superuser I can view a single post so that I can see single post details, including comments
- As a developer/superuser I can create a new post so that this post will be displayed in the posts list
- As a developer/superuser I can edit a post that I created so that I can amend any missing or incorrect information on the post
- As a developer/superuser I can delete a post that I created so that I can delete post data from the API

**Posts**

- As a developer/superuser I can view a list of all events so that I can see all events at once
- As a developer/superuser I can view a single event so that I can see single event details, including reviews
- As a developer/superuser I can create a new event so that this event will be displayed in the events list
- As a developer/superuser I can edit an event that I created so that I can amend any missing or incorrect information on the event
- As a developer/superuser I can delete an event which I created so that I can delete event data from the API

**Comments**

- As a developer/superuser I can create a comment so that I can link a comment to a post
- As a developer/superuser I can view a list of all comments so that I can see all comments created in the API
- As a developer/superuser I can retrieve a single comment by ID so that I can edit or delete this comment
- As a developer/superuser I can edit a comment that I created so that I can amend any missing or incorrect information
- As a developer/superuser I can delete a comment which I created so that I can delete comment data from the API

**Reviews**

- As a developer/superuser I can create a review so that I can link a review and rating to an event
- As a developer/superuser I can view a list of all reviews so that I can see all reviews created in the API
- As a developer/superuser I can retrieve a single review by ID so that I can edit or delete this comment
- As a developer/superuser I can edit a review that I created so that I can amend any missing or incorrect information
- As a developer/superuser I can delete a review which I created so that I can delete review data from the API

**Likes**

- As a developer/superuser I can create a liked object linked to a single event so that I can show interest in an event
- As a developer/superuser I can delete a liked object which I created so that I can delete liked data from the API
- As a developer/superuser I can not delete a liked object which I did not create
- As a developer/superuser I can view a list of all likedobjects so that I can see all liked objects created in the API

**Bookmarks**

- As a developer/superuser I can create a bookmarked object linked to a single event so that I can show the audience interest of an event
- As a developer/superuser I can delete a bookmarked object which I created so that I can delete bookmarked data from the API
- As a developer/superuser I can not delete a bookmarked object which I did not create
- As a developer/superuser I can view a list of all bookmarked objects so that I can see all bookmarked objects created in the API

**Followers**

- As a developer/superuser I can create a follow so that I can follow another user
- As a developer/superuser I can view a list of follows so that I can see all the follows that have been created
- As a developer/superuser I can delete a follow so that I can unfollow another user profile

**Search and Filter**

- As a developer/superuser I can see a search field in the events and posts list so that I can search for a specific event or post
- As a developer/superuser I can filter the events list by category so that I can see only the events relating to one desired category
- As a developer/superuser I can view a list of events/posts by profiles I follow so that I can see only the events/posts relating to profiles that I like
- As a developer/superuser I can view a list of posts I have posted a like id to so that I can see only the posts I like
- As a developer/superuser I can view a list of events I have posted a bookmarked id to so that I can see only the events I am interested in attending
- As a developer/superuser I can view a list of events/posts relating to just one profile so that I can see only the events/posts created by a single user
- As a developer/superuser I can view a list of comments linked to a particular post so that I can see see the comments relating to one single post id
- As a developer/superuser I can view a list of reviews linked to a particular event so that I can see see the reviews relating to one single event id

## The Structure Plane

### Features

### Homepage

When you first enter the API site, you are directed to the Root Route homepage, with a message welcoming you to the API,

![Homepage](https://res.cloudinary.com/ddsrnz9la/image/upload/v1697807308/api_browser_n3v4v3.png)

### Profile Data

Within the Profile List section, a user can view a list of all profiles in the API.

![Profiles list](https://res.cloudinary.com/ddsrnz9la/image/upload/v1697807311/profile_ohknhu.png)

Create functionality is not enabled, as the process is done automatically through the user registration process.

Besides the fields created in the Profile model (as shown in the ERD Diagram), through the serializer, I also added the following fields to the JSON data:

- is_owner
- following_id
- posts_count
- events_count
- followers_count
- following_count

I have set up ordering for the profile list, and selected the following parameters to sort the profiles by:

- posts_count
- events_count
- followers_count
- following_count
- owner\_\_following_created_at
- owner\_\_followed_created_at

I have set up two field filters on the events list to filter as follows:

1.  Profiles that are following the logged in user
2.  Profiles that are being followed by the logged in user

If the user logs in, and views the detail of their own profile, additional Edit and Delete functionality becomes available. A pre-populated form is available to edit the profile model fields. A delete button is available to delete the profile from the API.

### Posts Data

Within the Posts List section, a user can view a list of all posts in the API.

![Posts list](https://res.cloudinary.com/ddsrnz9la/image/upload/v1697807313/posts_list_ssn5sn.png)

Besides the fields created in the Post model (as shown in the ERD Diagram), through the serializer, I also added the following fields to the JSON data:

- is_owner
- profile_id
- tags
- profile_image
- like_id
- likes_count
- comments_count

I have set up ordering for the posts list, and selected the following parameters to sort the posts by:

- likes_count
- comments_count
- likes_created_at

I have set up a search function whereby the full posts list can be searched on by the post owner or post tags.

I have set up five field filters on the events list to filter as follows:

1.  Posts whose owners the logged in user is following - this will be the front end 'Post Feed' page
2.  Posts which the logged in user has liked - ultimately, this was not used in the front end, but if desired it could be a 'Likes' page
3.  All posts posted by user - this will be used in the 'Profile' page

If the user logs in, a form becomes visible to create a new post.

Once logged in, if the user views the details of a single post which they created additional Edit and Delete functionality becomes available; a pre-populated form is available to edit, and a delete button is available to delete the post from the API.

### Events Data

Within the Events List section, a user can view a list of all events in the API.

![Events list](https://res.cloudinary.com/ddsrnz9la/image/upload/v1697807314/events_list_fh7dlg.png)

Besides the fields created in the Event model (as shown in the ERD Diagram), through the serializer, I also added the following fields to the JSON data:

- is_owner
- profile_id
- tags
- profile_image
- bookmark_id
- bookmarks_count
- reviews_count

I have set up ordering for the events list, and selected the following parameters to sort the events by:

- bookmarks_count
- reviews_count
- bookmarks_created_at

I have set up a search function whereby the full events list can be searched on by the event owner, title, event date, or event tags.

I have set up five field filters on the events list to filter as follows:

1.  Events whose owners the logged in user is following - this will be the front end 'Event Feed' page
2.  Events which the logged in user has bookmarked - this will be the front end 'Bookmarks' page
3.  All events posted by user - this will be used in the 'Profile' page
4.  All events in one category - this filter will be visible on all front end 'Events' pages
5.  All events by event_date - used to filter only events that are in the future

If the user logs in, a form becomes visible to create a new event.

Once logged in, if the user views the details of a single event which they created additional Edit and Delete functionality becomes available; a pre-populated form is available to edit, and a delete button is available to delete the event from the API.

### Comments Data

Within the Comments List section, a user can view a list of all comments in the API.

![Comments list](https://res.cloudinary.com/ddsrnz9la/image/upload/v1697807315/comments_list_e3mljq.png)

Besides the fields created in the Comment model (as shown in the ERD Diagram), through the serializer, I also added the following fields to the JSON data:

- is_owner
- profile_id
- profile_image

I also set up one field filter to filter the comments by the post they are commenting on.

If the user logs in, a form becomes to create a new comment. The post they want to comment on can be selected, and comment text must be entered to post the comment successfully.

Once logged in, if the user views the details of a single comment which they created additional Edit and Delete functionality becomes available. A pre-populated form is available to edit the comment, and a delete button is available to delete the comment from the API.

### Reviews Data

Within the Review List section, a user can view a list of all reviews in the API.

![Reviews list](https://res.cloudinary.com/ddsrnz9la/image/upload/v1697807312/reviews_list_ttrwxx.png)

Besides the fields created in the Review model (as shown in the ERD Diagram), through the serializer, I also added the following fields to the JSON data:

- is_owner
- profile_id
- profile_image

I also set up one field filter to filter the reviews by the event they are reviewing.

If the user logs in, a form becomes visible to create a new review. The event they want to review can be selected, and review text must be entered and a rating must be selected to post the review successfully.

If a user tries to review the same event twice, they see an error message saying that they have already reviewed the selected event, and the duplicate review is not created. If the user tries to review their own event, they see an error message saying that they can't review their own event, and the review is not created.

Once logged in, if the user views the details of a single review which they created additional Edit and Delete functionality becomes available. A pre-populated form is available to edit the comment and a delete button is available to delete the comment from the API.

### Likes Data

Within the Likes List section, a user can view a list of all likes made in the API.

![Likes list](https://res.cloudinary.com/ddsrnz9la/image/upload/v1697807310/likes_list_rhke4x.png)

If the user logs in, a form becomes visible to create a new like. The post they want to like can be selected in order to link the like with the post.

If a user tries to like the same post twice, they see an error message saying that they have already liked the selected post, and the duplicate like is not created. If a user tries to like a post that they created, they see an error message saying they can't like their own post, and that like is not created.

Once logged in, if the user views the details of a single like which they created additional Delete functionality becomes available. It is not possible to Edit a like.

### Bookmarks Data

Within the Bookmarks List section, a user can view a list of all the bookmarks made in the API.

![Bookmarks list](https://res.cloudinary.com/ddsrnz9la/image/upload/v1697807309/bookmarks_list_ftcvn2.png)

If the user logs in, a form becomes visible to create a new bookmark. The event they want to bookmark can be selected in order to link the bookmark with the event.

If a user tries to bookmark the same event twice, they see an error message saying that they have already bookmarked the selected event, and the duplicate bookmark is not created. If a user tries to bookmark an event that they created, they see an error message saying they can't bookmark their own event, and that bookmark is not created.

Once logged in, if the user views the details of a single bookmark which they created, additional Delete functionality becomes available. It is not possible to Edit a bookmark.

### Followers Data

Within the Follower List section, a user can view a list of all follower posts in the API.

![Followers list](https://res.cloudinary.com/ddsrnz9la/image/upload/v1697809133/followers_ilnynw.png)

If the user logs in, a form becomes visible to create a new follower post. The user they want to follow can be selected to link the follower post with another user profile.

If a user tries to follow the same profile twice, they see an error message saying that they are already following the selected profile, and the duplicate follow post is not created.

Once logged in, if the user views the details of a single follower post which they created additional Delete functionality becomes available. It is not possible to Edit a follower post.

## The Skeleton Plane

### Database Design

**Entity-Relationship diagram for DBMS**

I have created the following models for the You.I Backend API:

- Users (slightly customised from the Django standard User model)
- Profiles (automatically created on User creation and customised)
- Posts (a professional networking post publicised by a logged in user)
- Likes (to indicate if a user likes another user's professional networking post)
- Comments (to make a comment on a professional networking post)
- Events (a post for a future event publicised by a logged in user)
- Reviews (to rate and leave a review on a publicised event)
- Bookmarks (to indicate if a user is interested in a publicised event)
- Followers (For users to follow each other)

The relationships between all of these models is summarised in the followed entity relationship diagram:

![Entity relationship diagram](https://res.cloudinary.com/ddsrnz9la/image/upload/v1697808126/erd_nn2x92.png)

Notes on the ER diagram:

- The ER diagram provided shows the logical data model.
- The Users table in the ER diagrams is also a logical representation of the data captured during user registration and how it relates to the application data model. The Users table itself is not declared in a models.py file, but is handled by the django modules and this logical view does not reflect all columns and constraints etc. used by the physical data tables in the database.

## Technologies Used

### Languages

- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>) - Provides the functionality for the DRF backend framework.

### Frameworks & Software

- [Django Rest Framework](https://www.django-rest-framework.org/) - A framework for building web API's
- [PEP8 Validation](https://pypi.org/project/pep8/) - pep8 is a tool to check your Python code against some of the style conventions in PEP 8.
- [Github](https://github.com/) - Used to host the repository, store the commit history and manage the project board containing user stories.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform that the application is deployed to.
- [Cloudinary](https://cloudinary.com/) - A service that hosts image files in the project.

### Libraries

The libraries used in this project are located in the requirements.txt file and have been documented below

- [asgiref](https://pypi.org/project/asgiref/) - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI.
- [cloudinary](https://pypi.org/project/cloudinary/) - The Cloudinary Python SDK allows you to quickly and easily integrate your application with Cloudinary.
- [dj-database-url](https://pypi.org/project/dj-database-url/0.5.0/) - This simple Django utility allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
- [dj-rest-auth](https://pypi.org/project/dj-rest-auth/) - Drop-in API endpoints for handling authentication securely in Django Rest Framework.
- [Django](https://pypi.org/project/Django/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [django-allauth](https://pypi.org/project/django-allauth/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) - Django Cloudinary Storage is a Django package that facilitates integration with Cloudinary by implementing Django Storage API.
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) - A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.
- [django-filter](https://pypi.org/project/django-filter/) - Django-filter is a reusable Django application allowing users to declaratively add dynamic QuerySet filtering from URL parameters.
- [django-taggit](https://pypi.org/project/django-taggit/) - Django-taggit a simpler approach to tagging with Django.
- [django-rest-framework](https://pypi.org/project/djangorestframework/) - web-browsable Web APIs.
- [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/) - Simple JWT is a JSON Web Token authentication plugin for the Django REST Framework.
- [gunicorn](https://pypi.org/project/gunicorn/) - Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.
- [oauthlib](https://pypi.org/project/oauthlib/) - OAuthLib is a framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.
- [pillow](https://pypi.org/project/Pillow/8.2.0/) - The Python Imaging Library adds image processing capabilities to your Python interpreter.
- [psycopg2](https://pypi.org/project/psycopg2/) - Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
- [PyJWT](https://pypi.org/project/PyJWT/) - A Python implementation of RFC 7519.
- [python3-openid](https://pypi.org/project/python3-openid/) - OpenID support for modern servers and consumers.
- [pytz](https://pypi.org/project/pytz/) - This is a set of Python packages to support use of the OpenID decentralized identity system in your application, update to Python 3
- [requests-oauhlib](https://pypi.org/project/requests-oauthlib/) - P rovides first-class OAuth library support for Requests.
- [sqlparse](https://pypi.org/project/sqlparse/) - sqlparse is a non-validating SQL parser for Python.

## Deployment

The project was deployed to [Heroku](https://www.heroku.com/). To deploy, please follow the process below:

1.  To begin with we need to create a GitHub repository from the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) by following the link and then click 'Use this template'.
2.  Fill in the details for the new repository and then click 'Create Repository From Template'.
3.  When the repository has been created, click on the 'Gitpod' button to open it in the GitPod Editor.
4.  Now it's time to install Django and the supporting libraries that are needed, using the following commands:

- `pip3 install 'django<4' gunicorn`
- `pip3 install 'dj_database_url psycopg2`
- `pip3 install 'dj3-cloudinary-storage`

5.  When Django and the libraries are installed we need to create a requirements file.

- `pip3 freeze --local > requirements.txt` - This will create and add required libraries to requirements.txt

6.  Now it's time to create the project.

- `django-admin startproject YOUR_PROJECT_NAME .` - This will create the new project.

7.  When the project is created we can now create the applications. My project consists of the following apps; Profiles, Comments, Contact, Events, Followers, Going, Interested and Reviews.

- `python3 manage.py startapp APP_NAME` - This will create an application

8.  We now need to add the applications to settings.py in the INSTALLED_APPS list.
9.  Now it is time to do our first migration and run the server to test that everything works as expected. This is done by writing the commands below.

- `python3 manage.py makemigrations` - This will prepare the migrations
- `python3 manage.py migrate` - This will migrate the changes
- `python3 manage.py runserver` - This runs the server. To test it, click the open browser button that will be visible after the command is run.

9.  Now it is time to create our application on Heroku, attach a database, prepare our environment and settings.py file and setup the Cloudinary storage for our static and media files.

- Once signed into your [Heroku](https://www.heroku.com/) account, click on the button labeled 'New' to create a new app.

10. Choose a unique app name, choose your region and click 'Create app".

11. Next we need to connect an external PostgreSQL database to the app from [ElephantSQL](https://customer.elephantsql.com/login). Once logged into your ElephantSQL dashboard, you click 'Create New Instance' to create a new database. Give the database a:

- Name
- Tiny Turtle Free Plan
- Selected data center near you

and click 'Create Instance'. Return to your ElephantSQL Dashboard, and click into your new database instance. Copy the Database URL and head back to Heroku.

12. Back in your Heroku app settings, click on the 'Reveal Config Vars' button. Create a config variable called DATABASE_URL and paste in the URL you copied from ElephantSQL. This connects the database into the app.

13. Go back to GitPod and create a new env.py in the top level directory. Then add these rows.

- `import os` - This imports the os library
- `os.environ["DATABASE_URL"]` - This sets the environment variables.
- `os.environ["SECRET_KEY"]` - Here you can choose whatever secret key you want.

14. Back in the Heroku Config Vars settings, create another variable called SECRET_KEY and copy in the same secret key as you added into the env.py file. Don't forget to add this env.py file into the .gitignore file so that it isn't commited to GitHub for other users to find.

15. Now we have to connect to our environment and settings.py file. In the settings.py, add the following code:

`import os`

`import dj_database_url`

`if os.path.isfile("env.py"):`

`import env`

16. In the settings file, remove the insecure secret key and replace it with: `SECRET_KEY = os.environ.get('SECRET_KEY')`

17. Now we need to comment out the old database settings in the settings.py file (this is because we are going to use the postgres database instead of the sqlite3 database).

Instead, we add the link to the DATABASE_URL that we added to the environment file earlier.

18. Save all your fields and migrate the changes again.

`python3 manage.py migrate`

19. Now we can set up [Cloudinary](https://cloudinary.com/users/login?RelayState=%2Fconsole%2Fmedia_library%2Ffolders%2Fhome%3Fconsole_customer_external_id%3Dc-95a4cb26371c4a6bc47e19b0f130a1#gsc.tab=0) (where we will store our static files). First you need to create a Cloudinary account and from the Cloudinary dashboard copy the API Environment Variable.

20. Go back to the env.py file in Gitpod and add the Cloudinary url (it's very important that the url is correct):

`os.environ["CLOUDINARY_URL"] = "cloudinary://************************"`

21. Let's head back to Heroku and add the Cloudinary url in Config Vars. We also need to add a disable collectstatic variable to get our first deployment to Heroku to work.

22. Back in the settings.py file, we now need to add our Cloudinary Libraries we installed earlier to the INSTALLED_APPS list. Here it is important to get the order correct.

- cloudinary_storage
- django.contrib.staticfiles
- cloudinary

23. For Django to be able to understand how to use and where to store static files we need to add some extra rows to the settings.py file.

24. To be able to get the application to work through Heroku we also need to add our Heroku app and localhost to the ALLOWED_HOSTS list:

`ALLOWED_HOSTS = ['happening-api-kelz.herokuapp.com', 'localhost']`

25. Now we just need to create the basic file directory in Gitpod.

- Create a file called \*_Procfile_ and add the line `web: gunicorn PROJ_NAME.wsgi?` to it.

26. Now you can save all the files and prepare for the first commit and push to Github by writing the lines below.

- `git add .`
- `git commit -m "Deployment Commit`
- `git push`

27. Now it's time for deployment. Scroll to the top of the settings page in Heroku and click the 'Deploy' tab. For deployment method, select 'Github'. Search for the repository name you want to deploy and then click connect.

28. Scroll down to the manual deployment section and click 'Deploy Branch'. Hopefully the deployment is successful!

### How To Fork The Repository On GitHub

It is possible to make an independent copy of a GitHub Repository by forking the GitHub account. The copy can then be viewed and it is also possible to make changes in the copy without affecting the original repository. To fork the repository, follow these steps:

1.  After logging in to GitHub, locate the repository. On the top right side of the page there is a 'Fork' button. Click on the button to create a copy of the original repository.

### Cloning And Setting Up This Project

To clone and set up this project you need to follow the steps below.

1.  When you are in the repository, find the code tab and click it.
2.  To the left of the green GitPod button, press the 'code' menu. There you will find a link to the repository. Click on the clipboard icon to copy the URL.
3.  Use an IDE and open Git Bash. Change directory to the location where you want the cloned directory to be made.
4.  Type 'git clone', and then paste the URL that you copied from GitHub. Press enter and a local clone will be created.
5.  To be able to get the project to work you need to install the requirements. This can be done by using the command below:

- `pip3 install -r requirements.txt` - This command downloads and installs all required dependencies that is stated in the requirements file.

6.  The next step is to set up the environment file so that the project knows what variables that needs to be used for it to work. Environment variables are usually hidden due to sensitive information. It's very important that you don't push the env.py file to Github (this can be secured by adding env.py to the .gitignore-file). The variables that are declared in the env.py file needs to be added to the Heroku config vars. Don't forget to do necessary migrations before trying to run the server.

- `python3 manage.py migrate` - This will do the necessary migrations.
- `python3 manage.py runserver` - If everything i setup correctly the project is now live locally.

## Credits

- The default profile picture image was sourced from [Vecteezy](https://www.vecteezy.com/)
- I read about [Django Taggit](https://django-taggit.readthedocs.io/en/latest/api.html) before implementing this library into my events and posts apps
- I also read this [dev.to](https://dev.to/tikam02/how-to-implement-django-search-field-and-tags-keywords-286a) blog on how to use tag fields effectively in a keyword search bar

## Acknowledgments

- My mentor at Code Institute, Adeye Adegbenga, for code review, help and feedback. Very much appreciated!
