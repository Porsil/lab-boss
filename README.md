# <h1 align="center">**LAB BOSS**</h1>

![Responsive Mockup](readme_assets/responsiveness.png)

## Introduction

Lab Boss is a laboratory planning tool and can be used by any laboratory team to make managing the workload easy and stress free. Lab Boss contains two apps, a batch tracker app and a scheduler app.

The batch tracker app allows the laboratory to track batches through the laboratory, easily seeing what batches require testing, when they are due and if they are a priority for the business.

The scheduler app allows the laboratory to schedule the workload by quickly and easily assigning an analytical test to an analyst on a particular day.

[View the live project here](https://lab-boss.herokuapp.com/)

## Table of Contents
  * [User Experience (UX)](#user-experience-ux)
  * [Data Model](#data-model)
  * [Agile Methodology](#agile-methodology)
  * [Design](#design)
  * [Security](#security)
  * [Features](#features)
  * [Languages and Libraries](#languages-and-libraries)
  * [Testing](#testing)
  * [Deployment](#deployment)
  * [Credits](#credits)

## User Experience (UX)

Lab Boss is a easy to use planning tool designed for use by a laboratory. There are two apps, a tracking tool that tracks batches through the laboratory and a scheduling tool that allows workload to be assigned to the team.

### User Stories

#### EPIC | User Admin
- As a Site User I can create an account so I can use the site.
- As a Site User I can log in or log out of my account so that I can keep my account secure.
- As a Site User I can only see any content without being logged in so that data is secure.
- As a Site User I can only see any content after my account has been authorised by an admin user so that control is maintained over the data.
- As a Site User I can only perform tasks appropriate to my role so that control is maintained over the data.
- As a Site User I receive success messages on completion of a task so that I am aware the changes I made were successful. 

#### EPIC | User Navigation
- As a Site User I can intuitively navigate around the site so that I can find content and understand where I am on the site.
- As a Site User I can view the contact information so that I can contact the site owner if required.

#### EPIC | Batch Tracker Use
- As a Site User I can see the batches that require testing so that the workload can be scheduled efficiently.
- As a Site User I can see which batches are priority so that they can be scheduled accordingly.
- As a Site User I can filter on fields for batches so that I can find a particular batch easily.
- As a Site User I can add a new batch onto the site through an easy-to-use interface so that the laboratory workload is up to date.

#### EPIC | Batch Tracker Management
- As a Senior Analyst I can approve batches so that that the laboratory workload is up to date.
- As a Senior Analyst I can edit or batches so that comments or changes can be made if required.
- As a Senior Analyst I can add, edit or delete materials so that changes can be made when required.

#### EPIC | Scheduler Use
- As a Site User I can view my workload cards so that I understand my work activities.
- As a Site User I can filter on fields for test_date, analyst or test so that I can find particular cards easily.
- As a Site User I can complete workload cards so that I can record my work as complete.
- As a Site User I can un-complete workload cards so that cards can be sent back to 'To Do' status if required.
- As a Site User I can create a new workload card through an easy-to-use interface so that work can be assigned.
- As a Site User I can edit testing cards so that the workload can be changed if required.

#### EPIC | Scheduler Management
- As a Senior Analyst I can delete testing cards so that the workload can be changed if required.
- As a Senior Analyst I can view, add, edit or delete analysts so that changes can be made when required.
- As a Senior Analyst I can add, edit or delete tests so that changes can be made when required.

[Table Of Contents](#table-of-contents)

## Data Model

Django’s Class-Based Generic Views  and Object-Oriented Programming princliples were used throughout this project.

Custom models were generated for this project:

Tracker app:
- The material model is used to create a custom list of the different materials or products the laboratory tests.
- The batch model is used to create details of a specific batch that has been received in the laboratory for testing. It uses the material model as a foreign key as a particular batch can only have 1 material.

Scheduler:
- The analyst model is used to create a custom list of analyst who perform testing in the laboratory. The user model was not used as not all users would be performing testing e.g. managers.
- The test model is used to create a custom list of testing that is performed in the laboratory.
- The workload model used both the analyst and test model and foreign keys to produce workload cards. These are designed to inform the analysts what tests they are performing on a certain day. 

Django AllAuth was used for the user authentication system.

The diagram below details the Database Entity Relationship Diagram:

![Database ERD](readme_assets/database_erd.png)

[Table Of Contents](#table-of-contents)

## Agile Methodology

An agile approach was implemented for the project using GitHub projects where the Epics were added as Milestones and allocated the User Stories as Issues. Each User Story Issue was given acceptance criteria and tasks to assist in the completion of each Issue.

The project board was also used to track development tasks and backlog issues (PBIs).

The project board can be viewed [here](https://github.com/users/Porsil/projects/6)

[Table Of Contents](#table-of-contents)

## Design

The site was designed to have a simple and professional look. The site was designed to have a clean and clinical look as the site would be used inside a laboratory setting.

### Fonts

Manrope was used as the font for the body of the site and Russo One was used for the headings. In case the fonts do not import into the website correctly, Sans Serif was used as the backup font.

### Colour Scheme

The colours for the site were taken from the logo using the Google Chrome Eye Dropper extension:

![Colour Palette](readme_assets/colour_palette.png)

### Imagery

To keep the site looking professional, only one image was used on the pages that did not contain much text. The image used is of test tubes containing a blue liquid to keep in theme of the site.

### Wireframes

<details>

<summary>Home</summary>

![Home](readme_assets/home.png)

</details>

<details>

<summary>Batch Tracker</summary>

![Tracker](readme_assets/tracker.png)

</details>

<details>

<summary>Scheduler</summary>

![Scheduler](readme_assets/scheduler.png)

</details>

<details>

<summary>Add Batch</summary>

![Home](readme_assets/new_batch.png)

</details>

<details>

<summary>Materials</summary>

![Home](readme_assets/materials.png)

</details>

<details>

<summary>Add/Edit Material</summary>

![Home](readme_assets/new_material.png)

</details>

<details>

<summary>Analysts</summary>

![Home](readme_assets/analysts.png)

</details>

<details>

<summary>Tests</summary>

![Home](readme_assets/tests.png)

</details>

<details>

<summary>Add/Edit Test</summary>

![Home](readme_assets/new_test.png)

</details>

<details>

<summary>Contact Us</summary>

![Home](readme_assets/contact_us.png)

</details>

[Table Of Contents](#table-of-contents)

## Security

### User Access and Authentication

Two User group's were set up using the Django Administration Panel, Analyst and Senior Analyst, these groups were assigned permissions appropriate to the role.

The site makes use of these Admin User Groups along with Django's Admin LoginRequiredMixin and PermissionRequiredMixin to ensure user's can only see and use features appropriate to their role.

New user's are not able to see or access the site feature's until they have been assigned to a role by a senior analyst, and are informed of this upon registration.

If the user attemps to access a feature not apropriate to their role, they are shown a HTTP 403 Forbidden Error.

### Secret Keys

To prevent unwanted connections the DATABASR_URL, SECRET_KEY and CLOUDINARY_URL are stored in the env.py, which is listed in the .gitignore file. This was done before the initial commit to GitHub.

### Forms

To prevent attack, Cross-Site Request Forgery (CSRF) tokens are used on all forms in the site.

[Table Of Contents](#table-of-contents)

## Features



[Table Of Contents](#table-of-contents)

## Languages and Libraries

### Languages Used

- HTML
- CSS
- JavaScript
- Python

### Frameworks, Libraries & Programs Used

- [Django](https://www.djangoproject.com/) was used as the main python framework.
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) was used to for account management.
- [Django-filer](https://django-filter.readthedocs.io/en/stable/) was used to create the filters on the site.
- [PostgreSQL](https://www.postgresql.org/) was used to host the database.
- [Cloudinary](https://cloudinary.com/) used to host images and static files.
- [Heroku](https://dashboard.heroku.com/login) was used to deploy the site.
- [Gitpod](https://gitpod.io/) was used for version control and agile methodology.
- [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) was used as a frontend toolkit to aid in the sites styling and responsiveness.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used to create the Django Forms.
- [Google Fonts](https://fonts.google.com/) was used to import the fonts used on the site.
- [Font Awesome](https://fontawesome.com/) was used for the approve, toggle, edit and delete icons used accross the site.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) was used through the project for inspecting and testing the site.
- [Balsamiq](https://balsamiq.com/) was used to create the wireframe for the website.
- [Lucidchart](https://www.lucidchart.com/pages/) was used to create the database entity relationship diagram.
- Microsoft Word was used to create the logo image.
- [Photoroom](https://www.photoroom.com/background-remover/) was used to remove the background from the logo image.
- [Ezgif](https://ezgif.com) was used to convert images to webp format.

[Table Of Contents](#table-of-contents)

## Testing

Testing details and results can be found [here](/TESTING.md).

[Table Of Contents](#table-of-contents)

## Deployment

To deploy this app to Heroku from its GitHub repository:

### File setup prior to deployment:
- Ensure all secret keys are stored in an env.py file and this is listed in the .gitignore file. Any keys that have been previously commited to GitHub should be changed for security purposes.
- Ensure requirements.txt file is up to date by using 'pip3 freeze --local > requirements.txt' in the command terminal.
- Ensure a Procfile is present and contains the code 'web: gunicorn labboss.wsgi'.
- Ensure in settings.py DEBUG = False
- Ensure the code is commited and pushed to GitHub.

### Create a Heroku App:
- Log in to [Heroku](https://dashboard.heroku.com/apps). If required, create an account.
- Click the 'New' button in the top right and select 'Create new app' from the drop-down menu.
- Enter a name for the app in the 'App name' field, this must be an unique and should be meaningful to the app's content.
- Select your region in the 'Choose a region' field.
- Click on the 'Create app' button.

### Add Heroku Config Vars:
- In Heroku click on the 'Settings' tab and scroll down to the 'Config Vars' section. Add the following Config Vars:
  - CLOUDINARY_URL
  - DATABASE_URL
  - SECRET_KEY
  - PORT: 8000

### Deploy in Heroku
- In Heroku click on the 'Deploy' tab and scroll down to the 'Deployment Method' section. Select 'GitHub' and confirm you wish to deploy using GitHub. Enter your GitHub password if prompted.
- Scroll to the 'Connect to GitHub' section and search for your repository.
- Click 'Connect' when found.
- To deploy:
  - Option 1 - To automatically redeploy your app every time you push changes to GitHub: In the 'Automatic deploys' section add the 'main' branch to 'Choose a branch to deploy' field and click 'Enable Automatic Deploys'.
  - Option 2 - To manually deploy your site: In the 'Manual Deploy' section add the 'main' branch to 'Choose a branch to deploy' field and click 'Deploy Branch'.
- The app is now live, click 'View' to view the deployed site.

## Forking the repository
- Open the [Lab Boss](https://github.com/Porsil/lab-boss) repository.
- Click the 'Fork' button in the top right.
- This creates a copy of the repository.

## Cloning the repository
- Open the [Lab Boss](https://github.com/Porsil/lab-boss) repository.
- Click the green '<> Code' button. Select the prefered cloning option from the list then copy the link provided.
- Change the current working directory to the location where you want the cloned directory.
- Type 'git clone' and paste the URL you copied earlier.
- Press 'Enter' to create your local clone.

[Table Of Contents](#table-of-contents)

## Credits

- The code to import the fonts was taken from [Google Fonts](https://fonts.google.com/).
- The code to add the icons used was taken from [Font Awesome](https://fontawesome.com/).
- The code to create the zebra stripes in the batch tracker table was adapred from [W3Schools](https://www.w3schools.com/html/html_table_styling.asp).
- The code to change the date format used on the site was taken from this [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#date).
- The following Geeks for Geeks sites were used to aid in creating all class based [Create Views](https://www.geeksforgeeks.org/createview-class-based-views-django/), [Update Views](https://www.geeksforgeeks.org/updateview-class-based-views-django/) and [Delete Views](https://www.geeksforgeeks.org/deleteview-class-based-views-django/).
- The code to stop the footer overlaying with the page content was adapted from this [CodeHim page](https://www.codehim.com/bootstrap/bootstrap-5-footer-always-at-bottom/).
- The code to create a message on the delete views was taken from this [Stackoverflow page](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown).
- The code to allow filters and pagination to work together was taken from this [CaktusGroup page](https://www.caktusgroup.com/blog/2018/10/18/filtering-and-pagination-django/).
- Various documentation sites were used throughout the project including [Django Docs](), [Django Filter Docs](), [Django Authentication](https://docs.djangoproject.com/en/4.1/topics/auth/default/), [Django Messages](https://docs.djangoproject.com/en/4.1/ref/contrib/messages/) and [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/).
- Various code was taken from the [Code Institute - Blog Walkthrough Project](https://github.com/Code-Institute-Solutions/Django3blog).

[Table Of Contents](#table-of-contents)
