# lrs-biblioteca

Site feito para um projeto integrador do SENAI, o principal objetivo é criar um sistema bibliotecário online.

Para instalação, seguir os passos abaixo:

Instalar dependências:

    pip install -r requirements.txt

Caso apareça o erro " ERROR: Could not build wheels for pycairo, which is required to install pyproject.toml-based projects " execute esses 3 comandos e depois execute o pip install novamente:

    sudo apt update

    sudo apt full-upgrade

    sudo apt install libcairo2-dev

Para ativar o servidor:

    python manage.py migrate

    python manage.py runserver
