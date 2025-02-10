from app_main import db

class user(db.Model):
    userid=db.Column(db.String(255), primary_key=True, nullable=False)
    password_hash=db.Column(db.String(255), nullable=False)
    role=db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Userid: {self.userid} password_hash {self.password_hash} role: {self.role}"
    