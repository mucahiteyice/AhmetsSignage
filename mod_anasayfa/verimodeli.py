from app import db

class yemekler1(db.Model):
    no=db.Column(db.Integer,primary_key=True)
    yemekİsmi=db.Column(db.String(50))
    yemekisim=db.Column(db.String(50))
    yemekFiyati=db.Column(db.String(50))
    yemekicerik=db.Column(db.String(50))
    yemekİcerik=db.Column(db.String(50))
    yemekid1=db.Column(db.String(50))

class yemekler2(db.Model):
    yemekno=db.Column(db.Integer,primary_key=True)
    yemekİsmi2=db.Column(db.String(50))
    yemekismi2=db.Column(db.String(50))
    yemekFiyati2=db.Column(db.String(50))
    yemekicerik2=db.Column(db.String(255))
    yemekİcerik2=db.Column(db.String(50))
    yemekid2 = db.Column(db.String(50))
class slayt(db.Model):
    slaytno = db.Column(db.Integer, primary_key=True)
    slaytfiyati = db.Column(db.String(50))
    slaytfotosu = db.Column(db.String(255))
    slaytbas = db.Column(db.String(255))
    slayttipi=db.Column(db.String(255))
    slaytid=db.Column(db.String(255))


class menuler(db.Model):
    menuno=db.Column(db.Integer, primary_key=True)
    menuresmi=db.Column(db.String(255))
    menuadi=db.Column(db.String(255))
    menufiyati=db.Column(db.String(255))
    menutipi=db.Column(db.String(255))
    menuid=db.Column(db.String(50))


