from flask import Flask, render_template, request
from .models import User, DB

# def create_app():
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
DB.init_app(app)

@app.route("/")
def home_view():
    return render_template('base.html')

@app.route("/user_submitted", methods=['GET',"POST"])
def user_submitted():
    if User.query.filter_by(id='0').count() > 0:
        id = User.query.all()[-1].id + 1
    else:
        id = 0
    goal = request.values['goal']
    pledged = request.values['pledged']
    backers = request.values['backers']
    usd_pledged_real = request.values['usd_pledged_real']
    usd_goal_real = request.values['usd_goal_real']

    record = User(id=id,
                  goal=goal,
                  pledged=pledged,
                  backers=backers,
                  usd_pledged_real=usd_pledged_real,
                  usd_goal_real=usd_goal_real
                  )
    DB.session.add(record)
    DB.session.commit()
    output='I am output'
    # pred = predict_user()
    # if pred == '[[0.]]':
    #     output = 'Your kickstarter will fail! Good Luck!'
    # else:
    #     output = 'Your destined for success. Go forth!'
    return render_template("user.html", output=output)
                           # project_name=project_name,
                           # category=category,
                           # main_category=main_category,
                           # currency=currency,
                           # deadline=deadline,
                           # goal=goal,
                           # launched=launched,
                           # pledged=pledged,
                           # backers=backers,
                           # country=country,
                           # usd_pledged=usd_pledged,
                           # usd_pledged_real=usd_pledged_real,
                           # usd_goal_real=usd_goal_real)

@app.route("/reset")
def reset():
    DB.drop_all()
    DB.create_all()
    return render_template("reset.html")

# return app