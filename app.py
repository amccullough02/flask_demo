from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

todo_list = [{"task": "Get Revenge on Jason", "done": False}]

@app.route('/')
def index():
    return render_template("index.html", todos=todo_list)

# Add CRUD methods and a check method to mark item as done.

@app.route('/add', methods=["POST"])
def add():
    todo = request.form['todo']
    todo_list.append({"task": todo, "done": False})
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)