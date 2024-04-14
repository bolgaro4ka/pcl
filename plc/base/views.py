from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import CodeForm
import subprocess
import random
import os
from .models import Compile
# Create your views here.

def set_lang(lang, form):
    if lang.name.lower() == 'node':
        form.fields['code'].widget.attrs['language'] = 'js'
    else:
        form.fields['code'].widget.attrs['language'] = lang.name.lower()
def indexPage(request):
    return render(request, 'index.html')

def mainPage(request):
    compilers = Compile.objects.all()
    return render(request, 'choose.html', {'compilers': compilers})
def compiler_normal_lang(request, short_name):
    error={}
    try:
        lang = Compile.objects.all().filter(short_name=short_name)[0]
    except IndexError:
        error['name'] = 'Такого компилятора не существует'
        error['description'] = f'Убедитесь что компилятор {short_name} существует!'
        return render(request, 'error.html', {'error':error})
        
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CodeForm(request.POST)
        set_lang(lang, form)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            stdinput = data['stdinput'].split('\r\n')
            print(stdinput)
            name = f'tmp-{random.randint(10000, 99999)}'+lang.ext
            code = data['code']
            for i in stdinput:
                code = code.replace(lang.input_command, i, 1)
            print(code)
            d = open(name, "w", encoding='utf-8')

            d.write(code)
            d.close()
            print(f'../{name}')
            result = subprocess.run(lang.starter+f' {name}', capture_output=True, text=True, errors='ignore')
            clear_res = result.stdout.strip()
            error_res = result.stderr.strip()
            os.remove(name)
            print(result)
            output = result
            # redirect to a new URL:
            return render(request, 'main.html', {"form": form, 'clear_res': clear_res, 'error_res': error_res, 'comp': lang, 'notSupportInput': lang.input_command == '!none!'})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CodeForm()
        set_lang(lang, form)

    return render(request, 'main.html', {"form": form, 'notSupportInput': lang.input_command == '!none!', 'clear_res': '', 'error_res': '', 'comp': lang})
    