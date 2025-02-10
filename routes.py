from conn_db import user
from flask import request,render_template

def all_routes(app,db):

    @app.route('/',methods=['GET','POST'])
    def home():
        if request.method=='POST':
            username=request.form['username']
            from hashing import hashof
            hashed=hashof(request.form['password'])
            c_user=user.query.filter(user.userid==username).all()
            if len(c_user)!=0:
                if c_user[0].password_hash==hashed:
                    if c_user[0].role=='admin':
                        c_user=user.query.all()
                    return render_template('table.html',current=c_user)
            return render_template('home.html')
        else:
            return render_template('home.html')