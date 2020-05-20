# covid-tracker
This is an cross platform app made by using Ionic 4 framework and Flask micro-framework. Generally Flask is used with Angular,
which is used to make dynamic websites. 
Flask is a microframework that can be used to make REST APIS and can be sent requests to using the methods such as GET, POST, etc..

Read the documentation of Flask : https://flask.palletsprojects.com/en/1.1.x/

As Flask is more used with Angular to make dynamic websites, Flask can help the websites to be more self-sustainable as it makes the use of python scripts. You can write your custom python scripts and get data to display on the website.

However Angular and Ionic share some similarities, although Ionic uses Angular.
Ionic framework is used to create cross platform mobile applications. To read the ionic documentation: https://ionicframework.com/docs

Flask can also be used with Ionic so that you can pass requests from your mobile app to the Flask REST API.

This project makes the use of exactly that.
In the repo here you will get all the python scripts which are imported and used in the RestService.py script. This Service API makes a considerable use of Flask.

The python scripts get the data of a weather forecast and COVID 19 status of different parameters such as number of cases, recovered and deaths on Earth.
It also has a method to send an email with 2 graphs displaying the Total active cases in India, deaths and recovered. The second graph has is a bar graph displaying the state-wise data of active cases.


Prerequisits:
1) You need to have Typescript, Angular, Ionic, Node Js (npm) installed in your machine.
2) To run the python scripts in the you need python3, matplotlib, Flask, numpy, pandas, requests, BeautifulSoup installed in your machine.

To run the project
Clone/Download the files.

1) Make a new ionic project in your machine, use Angular framework and blank layout.
Follow the commands here to make a new Ionic project: https://ionicframework.com/docs/cli/commands/start

2) Replace the src folder of your created Ionic project with the one which you downloaded from the repository.

3) To run the Flask API, navigate using the terminal or command prompt to the folder where you have all the python scripts saved.
All the python scripts must be in the same directory (folder).
First follow the simple instructions in the sendtest.py file to pass some parameters for the email service to work.
Follow the instructions (see strings wit underscore _ ) in line 7, 17, 21, 28, 29.
Also see in the india.py

4) Run the execute the python script named RestService.py.

5) Your server should be hosted on http://127.0.0.1:5000/. Use your browser to go on that link and check for an output.

6) Then run the Ionic app. Make sure you have done the step 2. To run the ionic app, open another terminal or command prompt, navigate into your ionic app folder and type 'ionic serve' to start the ionic app on your local host.

7) Now on the first page you should have a good weather forecast of Mumbai for the next 10 days and on the next page you should get the updates of COVID 19. 

8) By entering the email id you can send the email from your email which is in the sendtest.py script. 
MAKE SURE TO ENTER YOUR EMAIL AND PASSWORD TO SEND THE MAIL WITH THE GRAPHS.

9) Also make another where you will store these 2 graphs and pass that path into india.py

And now you are good to go.
