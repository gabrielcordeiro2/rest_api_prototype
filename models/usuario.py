from sql_alchemy import banco
import hmac

class UserModel(banco.Model):
    __tablename__ = 'usuarios'

    user_id = banco.Column(banco.Integer, primary_key = True)
    login = banco.Column(banco.String(40))
    senha = banco.Column(banco.String(40))


    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login
        }

    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()
        if user:
            return user
        return None

    @classmethod
    def find_by_login(cls, login):
        user = cls.query.filter_by(login=login).first()
        if user:
            return user
        return None

    def save_user(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()

class AuthModel:
    def safe_str_cmp(a: str, b: str) -> bool:

        if isinstance(a, str):
            a = a.encode("utf-8")

        if isinstance(b, str):
            b = b.encode("utf-8")

        return hmac.compare_digest(a, b)
