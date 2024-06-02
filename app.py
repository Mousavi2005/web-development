from flask import Flask, render_template

Projects = [
    {
    'pname' : 'p1',
    'pID' : '1'
    }, 
    {
        'pname' : 'p2',
        'pID' : '2'
    }
]



app = Flask(__name__)
@app.route("/")

def hi():
    return render_template("home.html", projects = Projects)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
