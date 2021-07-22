<h1 align="center">Praca inżynierska SYLKOS</h1>

<p><b> krok 0</b> - pobranie projektu i otworzenie go w visual studio code w głównym katalogu.</p>

$  git clone https://github.com/wojkos9/SYLKOS.git

<p><b> krok 1</b> - instalacja django i aplikacji <p>
<p align="justify"> po upewnieniu się, że mamy zainstalowanego pythona kolejno wykonać poniższe polecenia (najlepiej w folderze głównym). Zależnie od wersji pythona polecenia należy wpisać pip lub pip3 (jeśli jedno nie działa warto wypróbować drugie i później analogicznie z poleceniami zaczynającymi się od python - zależnie od wersji może działać python3). </p>

<code>pip install django</code><br>
<code>pip install djangorestframework</code><br>
<code>pip install markdown</code><br>
<code>pip install django-filter</code><br>
<code>pip install django-rest-authtoken</code><br>
<code>pip install django-allauth</code><br>
<code>pip install django-crispy-forms </code><br>
<code>pip install django-rest-auth</code><br>
<code>pip install django-webpack5-loader</code><br>
<code>pip install django-registration</code><br>

<p><b> krok 2</b> - należy przez terminal wejść do folderu frontend i zainstalować wszystkie paczki. Aby to zrobic najpierw trzeba mieć już pobrany Node.js </p> 

<code>cd frontend </code><br>
<code>npm install vue</code><br>
<code>npm install @vue/cli</code><br>
<code>npm install</code><br>
<code>npm install --save-dev webpack-bundle-tracker@0.4.3</code><br>
<code>npm run build</code><br>

<p><b>krok 3</b> - wracamy do głównego folderu i uruchomiamy projekt</p>

<code>cd ..</code><br>
<code>python manage.py makemigrations</code><br>
<code>python manage.py migrate</code><br>
<code>python manage.py runserver</code><br>





// .gitignore: db.sqlite3, frontend/package-lock.json frontend/package.json, frontend/webpack-stats.json?
