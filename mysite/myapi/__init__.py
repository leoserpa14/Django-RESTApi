# Packages installed: django, djangorestframework, djoser (autenticação e login)
# adicionar em INSTALED_APPS em settings.py


# Se eu quiser criar um novo modelo tenho que atualizar: admin.py, models.py, serializers.py, myapi/urls.py, views.py, 
# acho que mysite/urls.py é opcional. Depois ainda tenho que rodar 'python manage.py makemigrations' e 'python manage.py migrate'.
# 'python manage.py runserver' pra poder acessar o localhost pelo browser.


# Aparentemente, para criar uma conta pra login, para receber um token para o API, é com 
# o seguinte comando:
# curl -X POST -d "{"username":"leonardo","password":Kkk12345"}" -H "Content-Type:application/json" http://127.0.0.1:8000/api/auth/token/login/
# porém essa merda desse comando não está funcionando, então eu fui até 127.0.0.1:8000/api/auth/token/login e cliquei em HTML form e botei meu
# user: leonardo e senha: kkk12345 e recebi meu auth_token: "2e99dbb4333ccedcabdb21cce7d42e045e66e3a6"

# Agora para receber dados com esse token, usar o comando:
# curl -X GET http://127.0.0.1:8000/heroes/ -H "Authorization: Token 2e99dbb4333ccedcabdb21cce7d42e045e66e3a6"


# OBS: Aparentemente o problema com o 'python manage.py migrate' que travava era por causa do Postgres.
# Quando eu mudo esse projeto para o postgres como database, da o mesmo problema. Com o SQLite3 não tava dando nada de errado
