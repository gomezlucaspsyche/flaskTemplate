flaskenv = open(".flaskenv","wt")
config = ("FLASK_APP=main.py \nFLASK_ENV=development")
flaskenv.write(config)
flaskenv.close()