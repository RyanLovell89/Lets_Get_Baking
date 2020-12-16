# Let's Get Baking

My project is an online recipe book for cakes. The users can view all the recipes that have been added to the website by the recipe book page
or sign up to the website and add their own to share with everyone else. Logged in users can view all the recipes they have added via the
profile page, there they can edit their recipes or even delete them if they wish.

# UX

This website is aimed at anyone who likes baking. Users of the website can visit the recipe book page without needing to sign up or log in 
and view all recipes that have been added to website. On the recipe book page users find everything they need to make the cake, list of 
ingredients, step by step guide, baking time and preparation time. If the user would like to add their own recipe to the recipe book that 
can be done by logging in and going over to the add recipe page or signing up if the user is new.

* As a user that wishes just to view recipes on the website. The user can visit the recipe book page where all the recipes are available
without needing to sign up or log in.
* As a new user that wishes to sign up. A new user can visit the sign up page and create a profile by entering a username and password.
* As a returning user that wishes to log in. A returning user can visit the log in page and log in by entering the username and password they
created the profile with.
* As a logged in user that wishes to add a recipe to the recipe book. Logged in users can add recipes to recipe book by visiting the add recipe
page. There they can add a recipe by filling out the add recipe form and submitting it by the add recipe button.
* As a logged in user that wishes to view all the recipes that I have added. Logged in users can visit their profile page see all that only they
have added to the recipe book.
* As a user that wishes to search for recipes. Any users can search for recipes on recipe book page by using the recipe search bar.
* As a logged in user that wishes to make changes to my recipe I added. Logged in users may edit recipes they have added by visting their
profile page selecting the recipe they wish to edit and clicking the edit button.
* As a logged in user i wish to delete a recipe I have added. A loggedin user may delete a recipe they have added by visiting their profile
page, selecting the recipe they wish to delete and clicking on the delete button.

Balsamiq Wireframes have been added to the project and are stored in a seperate directory in pdf format. Some changes were made from the
orignal ideas.

# Features

* Home page - the first place a user visits on the website. Has information about the site.
* Recipe Book page - the recipe book page shows all the recipes on the website. The recipes are compress just showing the recipe name and
description untill a user click on the recipe, it then opens up the rest of the information ie, baking time, preparation time, ingredients,
and step by step guide for making the recipe. There is also a search bar user can use to search for recipes.
* Add Recipe page - the add recipe page allows users to add recipes to the recipe book by filling out the form and submitting it. Users can
also reset the form and start again if any errors are made.
* Edit Recipe page - the edit recipe page allows users to edit a recipe they have already added, the user make the changes they wish by editing
the form and submitting with the edit recipe button. If the user does not wish to make any changes then they can click the cancel button and
no changes will be made.
* Profile page - here users can view all the recipe they have added to the recipe book. Also from this page users may edit and delete recipes
they have added.
* Log In page - here returning users may log in to the website.
* Sign Up page - here new users may sign up to the website.
* Log Out - logs the user out of the website.

## Existing Features

* Mobile nav bar - the nav bar is a mobile friendly and will collapse down to a bars icon on tablets and mobile only displaying the logo. When a
user clicks the bars icon the links for the other pages appear in a down list. Different nav bar links appear whether a user is logged in or.
A user that is not logged in will have the links; home, recipe book, login and sign up available to them. A logged in user will have the links;
home, recipe book, add recipe, profile and log out available to them.
* Background Image - Every page has the same back ground image of baking table filled with food and equipment. Gives the user a visual of
what the website is about.
* Footer - the footer stores contact information for the website. Also has links to social media sites which would lead to more information about
the website. The site will take the user to the attached website but just the home page of the site. The site opens a new window so they are
not taken away from the website.
* Signing Up - Users of the website can sign up by visiting the sign up page. On the page is a form for user to fill out, they need to provide
a username which needs to be longer than 4 letters and no longer than 12 and a password of the same. Capital letters and numbers maybe be used
in password. Users will told if the username and password is too short or long, also if the username is already taken a flash message will pop
up telling the user the "Username Already Taken". When the user signs up successfully they will redirected to their profile and a flash message 
will pop up telling them "Sign Up Successful". The sign up feature uses generate password hash, the passwords created by the user is not viewable 
on the mongo database.
* Logging In - Users of the website that have already singed up can log in by the log in page. On the page is a form for the user to fill out
username and password are required to log in. Users will use the username and password they signed up to the website with to log in. If the
username and password do not match a message pop up and tell the user "Username and/or password incorrect". When has logged in successfully
they will be redirected to their profile and flash message will pop up "Welcome (username will appear)".
* Logging Out - When a user of the website wishes to log out they can click the log out link in the nav bar. This will log the user out
redirecting them to back the log in page. A flash message will also pop up letting user know "You have logged out".
* Adding recipes - Logged in users of the website can added recipes by visiting the add recipe page. On the page users have a form to fill out,
users are required to fill out the recipe name (minlength of 5 and maxlength of 40), recipe description (minlength of 5 and maxlength of 300),
baking time (minlength of 1 and maxlength of 20), preparation time (minlength of 1 and maxlength of 20), the first ingredient and weight/amount 
input (minlength of 1 and maxlength of 50) and the first step of the cooking instruction (minlength of 5 and maxlength of 500). Every other
input is optional to user. Users can reset the form if they wish to start again by clicking the reset button, this will clear the all text in
the form. Once the user has filled out the form they can click on the add recipe button and they will be redirected to their profile page
where they will be able to see the recipe they just add and flash message will pop up "Your Recipe Has Been Added". It will also appear on the
recipe book page for everyone to see.
* User Profile - Logged in users may visit their profile page which is unique to them. The users profile page has the username in card panel
displaying to them and lists all the recipes the user has added in collapsible. If no recipes appear a user is yet to add any recipes 
to the website.
* Edit Recipes - Logged in users may edit their own recipes from their profile page. Users will select the recipe they wish to edit by viewing
it in full on the collapsed recipe card panel and clicking the edit button at the bottom of the recipe. The user will be redirected to the edit
recipe page, this page is very similar to add recipe page but the form will already be populated by the recipe the user is editing. Here the user
can make the changes to recipe, the same rules apply as to the add recipe page users will have to fill out the same required input fields. Once
the user has made the changes they will click the edit recipe button and will be redirected to their profile and flash message will pop up
"Your Recipe Has Been Edited". If user has clicked the edit recipe button button but does not wish to make any changes they can click the 
cancel button and the user will be redirected back to their profile and the recipe will not have changed.
* Delete Recipes - Logged in users may deleted a recipe they do not wish to share anymore from their profile page. Users will select the recipe
they wish to delete by viewing it in full from the collapsible card panel and clicking the delete button, the user will then be redirected back
to their profile page and flash message will pop up "Your Recipe Has Been Deleted". The recipe will no longer appear on the users profile page
or in recipe book.
* Searching - Any user of the website can search for recipes on the recipe book page. This is done typing keywords into the search bar, the user
can search with the following keywords; recipe name, recipe description and added by. So if a user was searching for a sponge cake
the user could type the word sponge into the search bar and if recipe existed in the recipe book it would display any recipe name or recipe
description that contained the word sponge. If the recipe is not in the recipe book then a flash message would pop up "No Results Found". The user
can also search for added by, meaning the user can by username, exmaple would if a user liked a cake made by a pacific user and want try other
making other cakes by the user they can type that users username into the search and see all the recipes added by the user. If the user wished
to reset the search criteria then all they need to do it click the reset button and it will reset to displaying all recipes in the recipe book.

## Features Left To Implement

* Image File Upload - Add a file upload so users can take pictures of cakes to share with the recipes.
* Buttons for ingredients/weights and steps - Have buttons on the add recipe form that allow users to add and remove more input fields to the
ingredients and cooking instruction parts of the form as it is limited at the moment.
* Recipe of day - Have the home page display a recipe for day and change it every day.

# Technologies Used

* [HTML](https://en.wikipedia.org/wiki/HTML) - one of the main programming languages used to create content for the website.
* [CSS](https://en.wikipedia.org/wiki/CSS) - one of the main programming language used to style the website.
* [JAVASCRIPT](https://en.wikipedia.org/wiki/JavaScript) - only used in the nav bar for side bar navigation and in the collapsible to pop
    the recipe out.
* [PYTHON](https://en.wikipedia.org/wiki/Python_(programming_language)) - one of the main programming languages used to create the website.
* [FLASK](https://en.wikipedia.org/wiki/Flask_(web_framework)) - main framework used to create the website.
* [MONGO-DB](https://en.wikipedia.org/wiki/MongoDB) - the database used to store all of the users and recipes for the website.
* [GOOGLE-MATERIALIZE](https://materializecss.com/about.html) - one of the main programming language used to style the website.
* [FONT-AWESOME](https://fontawesome.com/) - used for the icons across many pages of the website.
* [BALSAMIQ](https://balsamiq.com/) - used to create the wireframes for the website (desktop version).
* [JINJA](https://en.wikipedia.org/wiki/Jinja_(template_engine)) - used for website templating and iteration across database.
* [WERKZEUG](https://werkzeug.palletsprojects.com/en/1.0.x/) - used for password sercuity.
* [STACK](https://stackoverflow.com/) - used for general help.
* [W3SCHOOL](https://www.w3schools.com/html/default.asp) - used for general help.
* [GITHUB](https://github.com/) - used to host the website repository.
* [GITPOD](https://gitpod.com/) - used to write the code for the website.
* [HEROKU](https://heroku.com) -used to host the live website.


# Testing

* Chrome Developer Tool - Lots of testing for the layout, responsiveness and css styling of the website was carried out with this tool.
* [HTML-Vaildator](https://validator.w3.org/) - was used to check HTML code throughtout the creation of this project.
* [CSS-Vaildator](https://jigsaw.w3.org/css-validator/) - was used to CSS code throughtout the creation of this project.
* [Python-Code-Checker](https://extendsclass.com/python-tester.html) - was used to check for any major syntax errors.

As part of testing the website Chrome Developer Tool was used to check the responsiveness of the website across the different screen sizes
such as well;

* Iphone 6/7/8 and the plus versions
* Iphone X
* Ipad and Ipad Pro
* Mobile S-320px, M-375px, L-425px
* Tablet-768px
* Laptop-1024px
* Laptop L-1440px
* 4K-2560px

* The nav bar links were tested to make sure the links took the user to correct pages, this was done by clicking each, ie clicking recipe book link
took the user to recipe book page of the website. This was also done for the tablet and mobile side bar nav links.

* Social media links in the footer were tested by clicking the links and making sure the correct page opened for each site, it only takes
the user to the home page of that site.

* The side nav bar for tablet and mobile was tested by changing the screen size using the Chrome Developer Tool and making sure the links collapsed
into the bars icon and were correctly viewable when the user clicks on the bars icon.

* recipe book display

* The search bar on the recipe book page was tested by adding multiple recipes to recipe book and searching for keywords in each recipe to check 
the correct results appeared. The index for the search are recipe name, recipe description and added by. So I would test recipe name by 
typing in a recipe name I knew existed in the recipe book and check what result came up. Recipe description I would type in a keyword from 
the recipe description I knew was in the recipe description and check what result came up. Added by I would type the names of users I knew
had added recipes to the recipe and check the results that came up. The Reset button was tested by performing a search and then clicking the
reset button to make sure it reset the page back to displaying all recipes.

* The sign up form was tested by creating users accounts and checking they were going the mongo database and the user was being redirected
to the profile page and the correct username flash message popped up. I tested that the same username couldn't be used more than once by 
trying to create account I had already created one with, this also tested that the correct flash message popped up notiying the user that 
username had already been taken. Also tested the requirement lengths of the input fields by trying to sign up using too few and too may letters. 

* The log in form was tested by logging in with usernames I had creating from testing the sign up form making sure the user that signed in git
redirected to their profile page and the the correct flash message pop up was the correct username for the user that signed in. Also tested 
entering correct username and wrong password to make sure the correct flash message popped up letting the user know the the username and/or 
password was incorrect, tested with username that hadn't signed up to make sure the same flash message appeared.

* The add recipe form was tested by adding filling out every part of the form and submitting then checking it was getting posted to mongo database.
I would then test with filling out fewer fields and making sure I got the same result, when the form was submited I would check to see if user 
was redirected to their profile page and the correct flash messaged popped up telling the user that their recipe had been added. For testing 
the reset button out I would fill out the form and then press the reset button making sure it cleared the form and users redirected back 
to the same page just with a clear form. I also tested submitting a form without having required length of letters and the required 
input areas filled in to see if it would submit.

* The edit recipe form was tested from the profile page, I had to make sure the edit button redirected the user to the edit recipe page 
and populated the fields of the form with the recipe the user had selected. This was tested by adding recipes and then going to the profile page 
of that user and clicking edit button. The function its self had to find the matching recipe from its unique id as to make sure the correct 
recipe was being edited. Once I had tested that the input fields were populating correctly I need to test the edit recipe button up dated the recipe 
correctly, this was done changing the information in the in the input fields and clicking the edd recipe button and checking the data had 
changed on the mongo database. I tested the cancel button by clicking the edit button and going the edit recipe page once there I could click the 
cancel button and make sure it would take the user back to their profile page and made no changes to the recipes by checking the recipe on the 
profile page and mongo database.

* The profile name display was tested by logging in to the test accounts created and making sure the correct username was appearing when the user 
was redirected to the page. The user only recipe display was tested by logging into the test accounts and creating recipes and checking the 
page only displayed the recipes made by the users and not showing all the recipe in the recipe book.

* The delete recipe function was tested by logging in the test accounts, creating recipes then going the users profile page clicking on recipe 
the user wished to delete then clicking the delete button at the bottom of the collapsible, this would then redirect the user back to their 
profile page with a flash message pop up saying the recipe has been deleted and recipe not being there anymore. I would double check this function 
worked by checking the mongo database after to check the recipe had been removed from there.

* The log out function was tested by logging into a test account I had made and clicking log out. Making sure the user was redirected back
to the log in page and the correct flash message appeared letting the use know they had been logged out. I would use the Chrome Developer 
Tool to make sure session cookies had gone.

# Deployemt

This project was built using Gitpod and deployed using Heroku.

The deployment to Heroku was set up early on into the project. First I made the Heroku app chosing the name then selecting the region. Second 
I made a requirements.txt file so Heroku could understand what is needed to be installed to run my app. Then I created a Procfile to tell Heroku 
what kind of application is being deployed and what build pack is required to run it. The deploy method used is a straight connection to git hub, 
this was achieved by going to the deploy tab when logged into heroku, then going to deployment method and connecting to my github account. 
Next was to link the github repository I wanted to connect this was done by searching for the repository I wanted to connect, 
ie Let's_Get_Baking and clicking connect. After that set up automatic deploys this was done by selecting the branch, ie the master.

The config vars on the app used are;
* IP 0.0.0.0
* MONGO_DBNAME get_baking
* MONGO_URI mongodb+srv://root:Liverpool89@myfirstcluster.ds3fz.mongodb.net/get_baking?retryWrites=true&w=majority
* PORT 5000
* SECRET_KEY NOfnm~L&DBdceQ6C=PA,'KS&Rbmfr0

These can also be found in the env.py file.

Heroku link to [Lets-Get-Baking](https://lets-get-baking.herokuapp.com/)

Github repository link to [Lets-Get-Baking](https://github.com/RyanLovell89/Lets_Get_Baking)

# Credits

## Content

* The paragraphs were written by myself. The recipes came from family members.

## Media

The back ground image came from [Google-Images](https://www.google.com/search?hl=en-GB&tbs=simg:CAQSvAIJxQmNMIpXpFoasAILELCMpwgaYgpgCAMSKLwWjx24F-gbsxypHKARuxa0HLYWnSe8Kagn7DSqJ8IpwSnCNcwp7TQaMG8vlvRr2owOi8Rlkvu1afk0vFr5bo7asAMG7YZ7_10jl4a8nk_1aMxkB_1KsyMwiG-pSAEDAsQjq7-CBoKCggIARIED49PYgwLEJ3twQkaqAEKFwoDY3Vw2qWI9gMMCgovbS8wN3B0ajNuCiIKD2xlYXZlbmluZyBhZ2VudNqliPYDCwoJL20vMDFjNDV5CiEKDWNhcnZpbmcgc3Bvb27apYj2AwwKCi9tLzBoOGxyOTEKJwoTb3JnYW5pYyBicmVhZCBmbG91ctqliPYDDAoKL20vMDc3N3h2dgodCgphdHRhIGZsb3Vy2qWI9gMLCgkvbS8wYndqdjkM&sxsrf=ALeKk03xx8KuESLX_YP7oQ_FmEhtmZShsg:1608052150589&q=baking+a+cake&tbm=isch&sa=X&ved=2ahUKEwio8NyJvdDtAhVCiFwKHUdUDHgQwg4oAHoECBAQMQ&biw=960&bih=936#imgrc=UVzNtatJxo_wLM)

## Acknowledgements 

* I took the project idea from the code institute project suggestions.

**This website is solely or educational purposes.**