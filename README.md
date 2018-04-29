# Book-A-Meal
[![Build Status](https://travis-ci.org/petermwash/Book-A-Meal.svg?branch=ft-api)](https://travis-ci.org/petermwash/Book-A-Meal)
[![Coverage Status](https://coveralls.io/repos/github/petermwash/Book-A-Meal/badge.svg)](https://coveralls.io/github/petermwash/Book-A-Meal)


Book-A-Meal is an application that allows customers to make food orders and helps the food vendor know what the customers want to eat.


## Runing the API

To run the api for this application you should have Pyhton3 installed in your machine.If you do not have have it yet you can install python3 by running the following commands on linux

 
>$ sudo apt-get install software-properties-common 
>$ sudo add-apt-repository ppa:deadsnakes/ppa 
>$ sudo apt-get update $ sudo apt-get install python3.6 


If you are using windows you can download python installer from their official website

Once you have python installed, you will need to install postman by [this instructions](https://www.google.com/url?q=https%3A%2F%2Fitrendbuzz.com%2Finstall-postman-native-app-on-ubuntu%2F&sa=D&sntz=1&usg=AFQjCNHww20936CFPZKMxkqjrk3TbBnshQ).

Now you can clone this repository to your local machine, cd into the folder created, create a virtual environment, activate it then install flask and flask_restful. You can do this by by running 

>$ pip install flask $ pip install flask_restful 

Install the dependencies by running the command bellow


>$ pipenv install -r requirements.txt


Now run the application by

>$ export FLASK_APP=run.py
>$ flask run


You will a message as the one shown bellow

![screenshot](https://raw.githubusercontent.com/petermwash/Book-A-Meal/ft-api/run.png)

copy the URL and paste it on postman. Now you can test the various api endpoints by select the appropiate method on poatman.


## Runing the tests

To run the tests for tis application you should have Pyhton3 installed in your machine.If you do not have have it yet you can install python3 by running the following commands on linux

>$ sudo apt-get install software-properties-common
>$ sudo add-apt-repository ppa:deadsnakes/ppa
>$ sudo apt-get update
>$ sudo apt-get install python3.6

If you are using windows you can download python installer from their [official website](https://www.python.org/downloads/windows/)

Once you have python installed, you may need to install nose by runniing the command '''$ pip install nose'''.

Now you can clone this repository to your local machine, cd into the folder created, create a virtual environment, activate it then install
flask and flask_restful installed. You can do this by by running 

>$ pip install flask
>$ pip install flask_restful

Now you can run the tests by running this command on your terminal

>$ nosetests tests


The tests should fail and you should see somthing  like the screenshot shown bellow

![screenshot](https://raw.githubusercontent.com/petermwash/Book-A-Meal/chore-tests/tests-img.png))

## Github pages

To view my user interface pages of the App on the github pages, click on the "Templates" link below.


[Templates](https://petermwash.github.io/Book-A-Meal/)


>Since the pages have no authentication yet, use the "Admin section" and "Customer section" links on the sign in page to be able to browse through the pages on the adimn section and customer section respectively. See the screeshot bellow on the circled part.

![alt text](https://raw.githubusercontent.com/petermwash/Book-A-Meal/master/eg-img.png))

![screenshot](https://raw.githubusercontent.com/petermwash/Book-A-Meal/chore-tests/tests-img.png)
