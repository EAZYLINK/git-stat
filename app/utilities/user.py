from werkzeug.security import check_password_hash, generate_password_hash

def hash_password(password: str):
    password_hash = generate_password_hash(password, method='pbkdf2:sha256')
    return password_hash

def check_password(password_hash, password):
    return check_password_hash(password_hash, password)