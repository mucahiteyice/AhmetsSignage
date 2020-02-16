from flask import Blueprint, render_template, url_for, redirect, request, abort, jsonify
from .verimodeli import *
from .formlar import yemekekler1ekle,yemekekler2ekle,SlaytEkle,MenuEkle
from flask_login import login_required



mod_yemek=Blueprint('yemek1', __name__)
mod_yemek2=Blueprint('yemek21', __name__)
mod_slayt=Blueprint('slayts', __name__)
mod_menu=Blueprint('menuler', __name__)
from app import app

@app.route('/')
@mod_yemek.route('/anasayfa')
@mod_yemek.route('/')
def solyemekler():
    yemekilk=yemekler1.query.all()
    yemekiki=yemekler2.query.all()
    menu=menuler.query.all()
    BuyukSlayt=slayt.query.all()
    return render_template('anasayfa.html', title='Anasayfam',
                           veri=yemekilk,
                           veri1=yemekiki,
                           veri2=menu,
                           veri3=BuyukSlayt
                           )

@mod_yemek.route('/liste')
@login_required
def yemeklerr1():
    yemeklerim1=yemekler1.query.all()
    return render_template('YemekListeler/Liste.html',
                           veri=yemeklerim1
                           )

@mod_yemek2.route('/liste')
@login_required
def yemeklerr2():
    yemeklerim2=yemekler2.query.all()
    return render_template('YemeklerListeler2/Liste.html',
                           veri=yemeklerim2
                           )

@mod_menu.route('/liste')
@login_required
def menuList():
    menulerim=menuler.query.all()
    return render_template('MenuListeler/Liste.html',
                           veri=menulerim
                           )

@mod_slayt.route('/liste')
@login_required
def slaytList():
    slaytlarim=slayt.query.all()
    return render_template('BuyukSlaytListeler/Liste.html',
                           veri=slaytlarim
                           )

@mod_yemek.route('/ekle', methods=["GET", "POST"])
@login_required
def ekleyemek1():
    form = yemekekler1ekle()
    if form.validate_on_submit():
        yeniYemek1 = yemekler1()
        yeniYemek1.yemekid1=form.yemekkodu.data
        yeniYemek1.yemekisim= form.yemekismi.data
        yeniYemek1.yemekicerik = form.yemekicerik.data
        yeniYemek1.yemekFiyati = form.yemekfiyati.data
        db.session.add(yeniYemek1)
        db.session.commit()
        return redirect(url_for('yemek1.yemeklerr1'))
    return render_template('YemekListeler/YemekEkle.html', form=form,sayfa_baslik="Yeni Yemek Ekle")

@mod_yemek2.route('/ekle', methods=["GET", "POST"])
@login_required
def ekleyemek2():
    form = yemekekler2ekle()
    if form.validate_on_submit():
        yeniYemek2 = yemekler2()
        yeniYemek2.yemekid2=form.yemekkodu2.data
        yeniYemek2.yemekismi2= form.yemekismi2.data
        yeniYemek2.yemekicerik2 = form.yemekicerik2.data
        yeniYemek2.yemekFiyati2 = form.yemekfiyati2.data
        db.session.add(yeniYemek2)
        db.session.commit()
        return redirect(url_for('yemek21.yemeklerr2'))
    return render_template('YemeklerListeler2/YemekEkle2.html', form=form,sayfa_baslik="Yeni Yemek Ekle")

@mod_slayt.route('/ekle', methods=["GET", "POST"])
@login_required
def ekleslayt():
    form = SlaytEkle()
    if form.validate_on_submit():
        yeniSlayt = slayt()
        yeniSlayt.slaytid=form.slayttid.data
        yeniSlayt.slaytbas= form.slaytbaslik.data
        yeniSlayt.slaytfotosu = form.slaytresmi.data
        yeniSlayt.slaytfiyati = form.slaytfiyati.data
        db.session.add(yeniSlayt)
        db.session.commit()
        return redirect(url_for('slayts.slaytList'))
    return render_template('BuyukSlaytListeler/SlaytEkle.html', form=form,sayfa_baslik="Yeni Slayt Ekle")


@mod_menu.route('/ekle', methods=["GET", "POST"])
@login_required
def eklemenu():
    form = MenuEkle()
    if form.validate_on_submit():
        yeniMenu = menuler()
        yeniMenu.menuid=form.menulerid.data
        yeniMenu.menuadi= form.menuleradi.data
        yeniMenu.menufiyati = form.menulerfiyati.data
        yeniMenu.menuresmi = form.menulerresmi.data
        db.session.add(yeniMenu)
        db.session.commit()
        return redirect(url_for('menuler.menuList'))
    return render_template('MenuListeler/MenuEkle.html', form=form,sayfa_baslik="Yeni Menu Ekle")


@mod_yemek.route("/sil", methods=['POST'])
@login_required
def yemeksil1():
    yemekNoo = request.form["no"]

    silinecekyemek1 = yemekler1.query.filter(yemekler1.no == yemekNoo).one_or_none()

    if silinecekyemek1 is None:
        abort(404)

    db.session.delete(silinecekyemek1)
    db.session.commit()

    return jsonify({'sonuc': 'TAMAM'})

@mod_yemek2.route("/sil", methods=['POST'])
@login_required
def yemeksil2():
    yemekNo2 = request.form["yemekno"]

    silinecekyemek2 = yemekler2.query.filter(yemekler2.yemekno == yemekNo2).one_or_none()

    if silinecekyemek2 is None:
        abort(404)

    db.session.delete(silinecekyemek2)
    db.session.commit()

    return jsonify({'sonuc': 'TAMAM'})

@mod_menu.route("/sil", methods=['POST'])
@login_required
def menusil():
    menuNo1 = request.form["menuno"]

    silinecekmenu = menuler.query.filter(menuler.menuno == menuNo1).one_or_none()

    if silinecekmenu is None:
        abort(404)

    db.session.delete(silinecekmenu)
    db.session.commit()

    return jsonify({'sonuc': 'TAMAM'})

@mod_slayt.route("/sil", methods=['POST'])
@login_required
def slaytsil():
    slaytNo1 = request.form["slaytno"]

    silinecekslayt = slayt.query.filter(slayt.slaytno == slaytNo1).one_or_none()

    if silinecekslayt is None:
        abort(404)

    db.session.delete(silinecekslayt)
    db.session.commit()

    return jsonify({'sonuc': 'TAMAM'})

@mod_yemek.route("/duzenle/<int:id>",methods=["GET", "POST"])
@login_required
def yemekduzenle1(id):
   duzenlenecekyemek = yemekler1.query.filter(yemekler1.no == id).one_or_none()
   if duzenlenecekyemek is None:
       abort(404)
   form=yemekekler1ekle()
   if form.validate_on_submit():
       duzenlenecekyemek.yemekid1 = form.yemekkodu.data
       duzenlenecekyemek.yemekisim = form.yemekismi.data
       duzenlenecekyemek.yemekicerik = form.yemekicerik.data
       duzenlenecekyemek.yemekFiyati = form.yemekfiyati.data
       db.session.commit()
       return redirect(url_for('yemek1.yemeklerr1'))
   form.yemekkodu.data = duzenlenecekyemek.yemekid1
   form.yemekismi.data = duzenlenecekyemek.yemekisim
   form.yemekicerik.data = duzenlenecekyemek.yemekicerik
   form.yemekfiyati.data = duzenlenecekyemek.yemekFiyati
   return render_template('YemekListeler/YemekEkle.html', form=form,sayfa_baslik="{} Yemeğini Düzenle".format(duzenlenecekyemek.yemekisim))


@mod_yemek2.route("/duzenle/<int:id>",methods=["GET", "POST"])
@login_required
def yemekduzenle2(id):
   duzenlenecekyemek2 = yemekler2.query.filter(yemekler2.yemekno == id).one_or_none()
   if duzenlenecekyemek2 is None:
       abort(404)
   form=yemekekler2ekle()
   if form.validate_on_submit():
       duzenlenecekyemek2.yemekid2 = form.yemekkodu2.data
       duzenlenecekyemek2.yemekismi2 = form.yemekismi2.data
       duzenlenecekyemek2.yemekicerik2 = form.yemekicerik2.data
       duzenlenecekyemek2.yemekFiyati2 = form.yemekfiyati2.data
       db.session.commit()
       return redirect(url_for('yemek21.yemeklerr2'))
   form.yemekkodu2.data = duzenlenecekyemek2.yemekid2
   form.yemekismi2.data = duzenlenecekyemek2.yemekismi2
   form.yemekicerik2.data = duzenlenecekyemek2.yemekicerik2
   form.yemekfiyati2.data = duzenlenecekyemek2.yemekFiyati2
   return render_template('YemeklerListeler2/YemekEkle2.html', form=form,sayfa_baslik="{} Yemeğini Düzenle".format(duzenlenecekyemek2.yemekismi2))



@mod_slayt.route("/duzenle/<int:id>",methods=["GET", "POST"])
@login_required
def slaytduzenle(id):
   duzenlenecekyslayt = slayt.query.filter(slayt.slaytno == id).one_or_none()
   if duzenlenecekyslayt is None:
       abort(404)
   form=SlaytEkle()
   if form.validate_on_submit():
       duzenlenecekyslayt.slaytid = form.slayttid.data
       duzenlenecekyslayt.slaytbas = form.slaytbaslik.data
       duzenlenecekyslayt.slaytfotosu = form.slaytresmi.data
       duzenlenecekyslayt.slaytfiyati = form.slaytfiyati.data
       db.session.commit()
       return redirect(url_for('slayts.slaytList'))
   form.slayttid.data = duzenlenecekyslayt.slaytid
   form.slaytbaslik.data = duzenlenecekyslayt.slaytbas
   form.slaytresmi.data = duzenlenecekyslayt.slaytfotosu
   form.slaytfiyati.data = duzenlenecekyslayt.slaytfiyati
   return render_template('BuyukSlaytListeler/SlaytEkle.html', form=form,sayfa_baslik="{} Slaytını Düzenle".format(duzenlenecekyslayt.slaytbas))



@mod_menu.route("/duzenle/<int:id>",methods=["GET", "POST"])
@login_required
def menuduzenle(id):
   duzenlenecekmenu = menuler.query.filter(menuler.menuno == id).one_or_none()
   if duzenlenecekmenu is None:
       abort(404)
   form=MenuEkle()
   if form.validate_on_submit():
       duzenlenecekmenu.menuid = form.menulerid.data
       duzenlenecekmenu.menuadi = form.menuleradi.data
       duzenlenecekmenu.menufiyati = form.menulerfiyati.data
       duzenlenecekmenu.menuresmi = form.menulerresmi.data
       db.session.commit()
       return redirect(url_for('menuler.menuList'))
   form.menulerid.data = duzenlenecekmenu.menuid
   form.menuleradi.data = duzenlenecekmenu.menuadi
   form.menulerfiyati.data = duzenlenecekmenu.menufiyati
   form.menulerresmi.data = duzenlenecekmenu.menuresmi
   return render_template('MenuListeler/MenuEkle.html', form=form,sayfa_baslik="{} Menüsünü Düzenle".format(duzenlenecekmenu.menuadi))



