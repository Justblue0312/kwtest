from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm, RakeForm
from .models import Contact
from news.utils import get_keyword_rake, get_keyword_yake, get_word_tokenize, get_classify


def get_about(request):
    return render(request, 'others/about.html')


def get_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            contact_obj = Contact()
            contact_obj.email = from_email
            contact_obj.subject = subject
            contact_obj.message = message
            contact_obj.save()
            # try:
            #     send_mail(subject, message, from_email, ['trao@gmail.com.com'])
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            return redirect('sucess')
    return render(request, "others/contact.html", {'form': form})


def successView(request):
    return render(request, 'others/sucess.html')


def handle_yake_alg(request):
    return render(request, 'others/yake.html')


def handle_rake_alg(request):
    form = RakeForm()
    text = ''
    if request.method == "POST":
        if 'keyword' in request.POST:
            form = RakeForm(request.POST)
            if form.is_valid():
                para = form.save(commit=False)
                _, text = get_keyword_rake(request, para.paragraph)
                # text = get_word_tokenize(request, para.paragraph)
                # text = get_classify(request, para.paragraph)
                para.save()

            context = {
                'form': form,
                'text1': text[:5]
            }
            return render(request, 'others/result.html', context)
        elif 'tokenize' in request.POST:
            form = RakeForm(request.POST)
            if form.is_valid():
                para = form.save(commit=False)
                # _,text = get_keyword_rake(request, para.paragraph)
                text = get_word_tokenize(request, para.paragraph)
                # text = get_classify(request, para.paragraph)
                para.save()

            context = {
                'form': form,
                'text2': text
            }
            return render(request, 'others/result.html', context)
        elif 'classify' in request.POST:
            form = RakeForm(request.POST)
            if form.is_valid():
                para = form.save(commit=False)
                # _,text = get_keyword_rake(request, para.paragraph)
                # text = get_word_tokenize(request, para.paragraph)
                text = get_classify(request, para.paragraph)
                para.save()

            context = {
                'form': form,
                'text3': text
            }
            return render(request, 'others/result.html', context)
    else:
        form = RakeForm()
    context = {
        'form': form,
        'text': text
    }
    return render(request, 'others/rake.html', context)
