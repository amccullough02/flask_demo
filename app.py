from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

todo_list = [{"todo": "Get Revenge on Jason", "done": False}]

@app.route('/')
def index():
    return render_template("index.html", todos=todo_list)

# Add CRUD methods and a check method to mark item as done.

if __name__ == '__main__':
    app.run(debug=True)