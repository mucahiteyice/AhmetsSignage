from flask import Blueprint,render_template,redirect,url_for
from .model import *
from .formlar import LoginFormu
from flask_login import login_user,logout_user
mod_kullanici = Blueprint('kullanici',__name__)

@mod_kullanici.route('/login',methods=['post','get'])
def kullaniciLogin():
    loginForm=LoginFormu()
    if loginForm.validate_on_submit():
        kullanicilar=kullanici.query.filter(kullanici.kullaniciadi==loginForm.KullaniciAdi.data).one_or_none()
        if kullanicilar is None:
            return render_template('login.html',form=loginForm,hata="Kullanıcı veya Şifre Hatalı")
        if kullanicilar.sifreDogrula(loginForm.sifre.data):
            login_user(kullanicilar)
            return redirect(url_for('yemek1.yemeklerr1'))
        else:
            return render_template('login.html',form=loginForm,hata="Kullanıcı veya Şifre Hatalı")
    return render_template('login.html',form=loginForm,hata="")


@mod_kullanici.route('/cikis')
def cikis():
    logout_user()
    return redirect(url_for('kullanici.kullaniciLogin'))

