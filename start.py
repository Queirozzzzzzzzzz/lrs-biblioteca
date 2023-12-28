import subprocess

# Roda o comando de migração
subprocess.run(['python', 'manage.py', 'migrate'])

# Roda o comando de inicializar servidor
subprocess.run(['python', 'manage.py', 'runserver'])