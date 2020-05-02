from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, {
                            column: value
                            for column, value in self._to_dict().items()
                            })

    def json(self):
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
            }

class MyModel(BaseModel, db.Model):
    __tablename__ = 'table'

    id = db.Column(db.Integer, primary_key = True)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
