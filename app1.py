from flask import Flask, render_template
import flask
# print(flask.__version__)
# 
app = Flask(__name__) # Flask app instance


# Creating flask routes
@app.route('/')
# Create function
def hello_world():
    return 'Hello , I am Adam'


@app.route('/adam')
# Create function
def adam():
    return render_template('profile.html')

if __name__=="__main__":
    app.run(debug=True)