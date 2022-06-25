from django.shortcuts import render
from django.core.mail import send_mail

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

        wiadomosc_mail = '{} ze szkoły {} : {}'.format(imie, szkola, wiadomosc)

        #wysylanie maila
        #send_mail('Wiadomość z formularza', wiadomosc_mail, email, ['szymbarc@gmail.com'])

        return render(request, 'kontakt.html', {'imie' : imie})
    else:
        return render(request, 'kontakt.html', {})


def nauczyciele(request):
    return render(request, 'nauczyciele.html', {})
# Create your views here.
