import os

from peewee import *

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../database.db')
db = SqliteDatabase(filename)  # Database system here


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    phonenumber = CharField(unique=True)
    authcode = IntegerField()

    time = DateTimeField()  # Last interaction
    count = IntegerField()  # Number of interactions

    claim_last = DateTimeField()

    trust_address = CharField(null=True)
    trust_phonenumber = CharField(null=True)

    rec_word = CharField()


tables = [User]


if __name__ == "__main__":
    db.create_tables(tables)

