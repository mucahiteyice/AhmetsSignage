from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField,SubmitField,TextAreaField
from wtforms.validators import DataRequired
class yemekekler1ekle(FlaskForm):
    yemekkodu=StringField(label='Yemek Kodu',validators=[DataRequired(message='Yemek Kodu Boş Geçilemez.')])
    yemekismi=  StringField(label='Yemek İsmi',validators=[DataRequired(message='Yemek İsmi Boş Geçilemez.')])
    yemekicerik= TextAreaField(label='Yemek İçeriği',validators=[DataRequired(message='Yemek İçeriği Bos Geçilemez')])
    yemekfiyati = StringField(label='Yemek Fiyatı', validators=[DataRequired(message='Yemek Fiyatı Bos Geçilemez')])
    ekle=SubmitField(label='Kaydet')

class yemekekler2ekle(FlaskForm):
    yemekkodu2=StringField(label='Yemek Kodu',validators=[DataRequired(message='Yemek Kodu Boş Geçilemez.')])
    yemekismi2=  StringField(label='Yemek İsmi',validators=[DataRequired(message='Yemek İsmi Boş Geçilemez.')])
    yemekicerik2= TextAreaField(label='Yemek İçeriği',validators=[DataRequired(message='Yemek İçeriği Bos Geçilemez')])
    yemekfiyati2 = StringField(label='Yemek Fiyatı', validators=[DataRequired(message='Yemek Fiyatı Bos Geçilemez')])
    ekle2=SubmitField(label='Kaydet')

class SlaytEkle(FlaskForm):
    slayttid= StringField(label='Slayt İdsi',validators=[DataRequired(message='Slayt İd Boş Geçilemez.')])
    slaytbaslik=  StringField(label='Slayt Başlığı',validators=[DataRequired(message='Slayt Başlığı Boş Geçilemez.')])
    slaytfiyati= TextAreaField(label='Slayt Fiyatı',validators=[DataRequired(message='Slayt İçeriği Bos Geçilemez')])
    slayttipi = StringField(label='Slayt Linki')
    slaytresmi = StringField(label='Slayt  Resmi', validators=[DataRequired(message='Slayt Resmi Bos Geçilemez')])
    ekle=SubmitField(label='Kaydet')

class MenuEkle(FlaskForm):
    menulerid=StringField(label='Menu İd',validators=[DataRequired(message='Menu İd si Boş Geçilemez.')])
    menuleradi=StringField(label='Menu Başlığı',validators=[DataRequired(message='Menu Adı Boş Geçilemez.')])
    menulerfiyati=StringField(label='Menu Fiyatı',validators=[DataRequired(message='Menu Fiyatı Boş Geçilemez.')])
    menulerresmi = StringField(label='Slayt  Resmi', validators=[DataRequired(message='Menu Resmi Bos Geçilemez')])
    ekle = SubmitField(label='Kaydet')