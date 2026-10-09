from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
	return "Welcome to Azure App Service and test"
if __name__=="__main__":
	app.run()
