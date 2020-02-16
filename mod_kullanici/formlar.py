from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired
class LoginFormu(FlaskForm):
    KullaniciAdi=  StringField(label='Kullanıcı Adınız',validators=[DataRequired(message='Kullanıcı Adı Boş Geçilemez.')])
    sifre= PasswordField(label='Sifreniz',validators=[DataRequired(message='Şifre Boş Geçilemez.')])
    BeniHatirla=BooleanField(label='Beni Hatırla')
    Gonder=SubmitField(label='Giris')
