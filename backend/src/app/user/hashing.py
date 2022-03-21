from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['argon2'], deprecated='auto')


def verify_password(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)


def get_password_hash(password):
    return pwd_context.hash(password)
