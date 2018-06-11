# TodoListApis

Son 4 APIS diferentes:
+ 1.- Registrar usuario
+ 2.- Loggear usuario
+ 3.- Agregar tarea - listar tareas
+ 4.- Actualizar estado de una tarea

Todo se realizó bajo Django2.0 rest-framework, existe un model para agregar las tareas. Se aplicó TokenAuthentication y todo se realizó bajo entorno virtual. Además se realizó bajo python3.

Para iniciar:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

```

Las urls no están redirigidas entre si, por lo que existen 4 tipos de url:

+ 1.- http://localhost:8000/api/users/register/
+ 2.- http://localhost:8000/api/users/login/
+ 3.- http://localhost:8000/api/users/list/
+ 4.- http://localhost:8000/api/users/edit/id ---> id será de la tarea a cambiar status.


