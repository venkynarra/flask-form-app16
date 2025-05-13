from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy  # rhis library allow us to ineteract with database more efficiently.
from datetime import datetime

app = Flask(__name__)

app.config["SECRET_KEY"] = "myapplication123"  # security for application for not hacking
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db?check_same_thread=False&timeout=10"  # uri specifies we are using sqlite , data.db is database file name

db = SQLAlchemy(app)  # this will sql alchemy database instance.

# this is a database model
class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))

@app.route("/", methods=["GET", "POST"])
def index():
    # initialize variables for use in render_template
    first_name = last_name = email = date = occupation = None

    if request.method == "POST":
        try:
            first_name = request.form["first_name"]  # get the firstname from the form.
            last_name = request.form["last_name"]
            email = request.form["email"]
            date = request.form["date"]
            date_obj = datetime.strptime(date, "%Y-%m-%d")  # convert string to date object
            occupation = request.form["occupation"]

            # creating the form object with collected data
            form = Form(first_name=first_name, last_name=last_name, email=email,
                        date=date_obj, occupation=occupation)

            db.session.add(form)
            db.session.commit()  # kind of insert sql query
            flash("Your form was submitted successfully!", "success")  # flash message

            # Print values to terminal
            print("First Name:", first_name)
            print("Last Name:", last_name)
            print("Email:", email)
            print("Date:", date)
            print("Occupation:", occupation)

        except Exception as e:
            print("ERROR:", e)  # print exception in terminal
            db.session.rollback()  # rollback if any issue happens during insert
            flash("Database error: " + str(e), "danger")  # flash error message

        finally:
            db.session.close()  # always close session

    # render the page whether GET or POST, with data if submitted
    return render_template("index.html",
                           first_name=first_name,
                           last_name=last_name,
                           email=email,
                           date=date,
                           occupation=occupation)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # this will create a database, it also checks with the URI; if it is created, it is not created twice.
    app.run(debug=True, port=5001)
