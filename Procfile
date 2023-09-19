release: python manage.py migrate --noinput
web: gunicorn pypro.wsgi --log-file -

#se eu não me engano essa parte aqui, diz respeito ao heroku, na verdade qualquer banco externo tem sua configuração diferente do sqlite3(que é nosso banco interno). Explicamos isso um pouco melhor nosso projeto url reduce.