import bcrypt

from db.connection import create_connection
from db.operations import DatabaseOperations
from contextlib import closing


class User:
    db_operations = DatabaseOperations('tasker.db')

    def __init__(self, user_id, username, email, password_hash):
        self.id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash

    @classmethod
    def create(cls, username, email, password):
        # Hash password and create user in database
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        user = (username, email, password_hash,)
        with closing(create_connection('tasker.db')):
            user_id = cls.db_operations.create_user(user)
        return cls(user_id, username, email, password_hash)

    @classmethod
    def get_by_id(cls, user_id):
        # Retrieve user from database by ID
        user_data = cls.db_operations.get_user_by_id(user_id)
        if user_data:
            return cls(*user_data)
        return None
