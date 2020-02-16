from flask import Flask,render_template,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ahmedslounge.db'
app.config['SECRET_KEY']='ÇOK GİZLİ BİLGİ'
db=SQLAlchemy(app)
csrf=CSRFProtect(app)
migrate=Migrate(app,db)
login=LoginManager(app)
login.login_view="kullanici.kullaniciLogin"

from mod_anasayfa.yonetici import mod_menu
from mod_anasayfa.yonetici import mod_slayt
from mod_anasayfa.yonetici import mod_yemek
from mod_anasayfa.yonetici import mod_yemek2
from mod_kullanici.yonetici import mod_kullanici



import mod_anasayfa.yonetici


app.register_blueprint(mod_menu, url_prefix='/menu')
app.register_blueprint(mod_yemek, url_prefix='/yemek')
app.register_blueprint(mod_yemek2, url_prefix='/yemek2')
app.register_blueprint(mod_slayt, url_prefix='/slayt')
app.register_blueprint(mod_kullanici, url_prefix='/giris')

@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    app.run(debug=True)
