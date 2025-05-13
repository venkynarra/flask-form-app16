from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        occupation = request.form["occupation"]

        # Print values to terminal
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Email:", email)
        print("Date:", date)
        print("Occupation:", occupation)

        # Render template with data
        return render_template("index.html",
                               first_name=first_name,
                               last_name=last_name,
                               email=email,
                               date=date,
                               occupation=occupation)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
