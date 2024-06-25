from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template("index.html")

# Add CRUD methods and a check method to mark item as done.

if __name__ == '__main__':
    app.run(debug=True)