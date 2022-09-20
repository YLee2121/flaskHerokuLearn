from flask import Flask, render_template, request, flash 

app = Flask(__name__)
app.secret_key = "bingbo"

@app.route('/hello')
def index():
    flash("what is your name?")
    return render_template("index.html")

@app.route('/greet', methods=['POST', 'GET'])
def greet():
    flash('hi ' + str(request.form['name_input']) + " good to see ya")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

