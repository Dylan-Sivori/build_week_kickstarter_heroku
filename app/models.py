from flask_sqlalchemy import SQLAlchemy

# Creating DB
DB = SQLAlchemy()

# Creating a user table
class User(DB.Model):
    """Stores values input by the user"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    goal = DB.Column(DB.Float, nullable=False)
    pledged = DB.Column(DB.Float, nullable=False)
    backers = DB.Column(DB.Integer, nullable=False)
    usd_pledged_real = DB.Column(DB.Float, nullable=False)
    usd_goal_real = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return 'Project Name {}'.format(self.project_name)
