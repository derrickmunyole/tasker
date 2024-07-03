import hashlib


def login(username, password):
    # Verify credentials and return user object if valid
    pass


def verify_password(stored_password_hash, provided_password):
    # Hash provided password and compare with stored hash
    return stored_password_hash == hashlib.sha256(provided_password.encode()).hexdigest()


def logout(user):
    # Handle logout (e.g., clear session)
    pass
