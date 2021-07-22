<h1 align="center">Praca inżynierska SYLKOS</h1>

<p> krok 0 - pobranie projektu i otworzenie go w visual studio code w głównym katalogu.</p>

$  git clone https://github.com/wojkos9/SYLKOS.git

<p> krok 1 - instalacja django i aplikacji <p>
<p align="justify"> po upewnieniu się, że mamy zainstalowanego pythona kolejno wykonać poniższe polecenia (najlepiej w folderze głównym). Zależnie od wersji pythona polecenia należy wpisać pip lub pip3 (jeśli jedno nie działa warto wypróbować drugie i później analogicznie z poleceniami zaczynającymi się od python - zależnie od wersji może działać python3). </p>

<code>pip install django</code>
<code>pip install djangorestframework</code>
<code>pip install markdown</code>
<code>pip install django-filter</code>
<code>pip install django-rest-authtoken</code>
<code>pip install django-allauth</code>
<code>pip install django-crispy-forms </code>
<code>pip install django-rest-auth</code>
<code>pip install django-webpack5-loader</code>
<code>pip install django-registration</code>

<p> krok 2 - należy przez terminal wejść do folderu frontend i zainstalować wszystkie paczki. Aby to zrobic najpierw trzeba mieć już pobrany Node.js </p> 

<code>cd frontend </code>
<code>npm install vue</code>
<code>npm install @vue/cli</code>
<code>npm install</code>
<code>
npm install --save-dev webpack-bundle-tracker@0.4.3</code>
<code>npm run build</code>

<p>krok 3 - wracamy do głównego folderu i uruchomiamy projekt</p>

<code>cd ..</code>
<code>python manage.py makemigrations</code>
<code>python manage.py migrate</code>
<code>python manage.py runserver</code>





// .gitignore: db.sqlite3, frontend/package-lock.json frontend/package.json, frontend/webpack-stats.json?
