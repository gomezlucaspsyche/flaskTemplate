#Creating .flaskenv configurations...
flaskenv = open(".flaskenv","wt")
config = ("FLASK_APP=main.py \nFLASK_ENV=development")
flaskenv.write(config)
flaskenv.close()

#Now i have to add a command to:
#python3 -m venv venv 
#virtualenv venv
#source venv/bin/activate
#pip install flask
#pip3 install flask

#i need to make a Json file that install dependencies
#then when all the dependencies are installed both in pip and pip3
#flask run

#create a log

#git repository remote add option