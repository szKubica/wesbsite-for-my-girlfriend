from django.shortcuts import render
from django.core.mail import send_mail
import smtplib

def home(request):
    return render(request, 'glowna.html', {})


def o_szkole(request):
    return render(request, 'o_szkole.html', {})


def cennik(request):
    return render(request, 'cennik.html', {})


def kontakt(request):
    if request.method == 'POST':
        imie = request.POST['imie']
        szkola = request.POST['szkola']
        email = request.POST['email']
        wiadomosc = request.POST['wiadomosc']
        wiadomosc_mail = '{} ze szkoły {} wysłał wiadomosc: {}'.format(imie, szkola, wiadomosc)

        send_mail('Wiadomość z formularza', wiadomosc_mail, email, ['']) #DO TABLICY WPISAC ADRES DO KTOREGO TRAFIAC BEDA MAILE

        return render(request, 'kontakt.html', {'imie' : imie})
    else:
        return render(request, 'kontakt.html', {})


def nauczyciele(request):
    return render(request, 'nauczyciele.html', {})
# Create your views here.
