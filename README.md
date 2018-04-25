# Book-A-Meal
Book-A-Meal is an application that allows customers to make food orders and helps the food vendor know what the customers want to eat.

##Runing the tests

To run the tests for tis application you should have Pyhton3 installed in your machine.If you do not have have it yet you can install python3 by running the following commands on linux
'''
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.6
'''
If you are using windows you can download python installer from their [official website](https://www.python.org/downloads/windows/)

Once you have python installed, you may need to install nose by runniing the command '''$ pip install nose'''.

Now you can clone this repository to your local machine, cd into the folder created, create a virtual environment, activate it then install
flask and flask_restful installed. You can do this by by running 

'''
$ pip install flask
$ pip install flask_restful
'''

Now you can run the tests by running this command on your terminal

'''
$ nosetests tests
'''

The tests should fail and you should see somthing  like the screenshot shown bellow

![screenshot](https://raw.githubusercontent.com/petermwash/Book-A-Meal/chore-tests/tests-img.png))
