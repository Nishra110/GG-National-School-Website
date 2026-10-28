from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/class/<int:class_number>")
def class_details(class_number):
    return render_template(
        "class_details.html",
        class_number=class_number)


@app.route("/teacher/<teacher_id>")
def teacher_details(teacher_id):
    return render_template("teacher_details.html", teacher_id=teacher_id)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/classes")
def classes():
    return render_template("classes.html")

@app.route("/teachers")
def teachers():
    return render_template("teachers.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/admission")
def admission():
    return render_template("admission.html")


if __name__ == "__main__":
    app.run(debug=True)

