#!/bin/sh 
#!/usr/bin/python3

if [ $# -lt 2 ] ; then
    if [ "$1" = "run" ]; then 
        echo 'Launching localhost server';
        cd israsoc_website 
        python manage.py runserver
    elif [ "$1" = "venv" ]; then 
        echo 'Activating virtual environment';
        ./israsoc_venv/Scripts/activate 
    elif [ "$1" = "deactivate" ] ; then 
        echo 'Deactivating venv'; 
        deactivate 
    elif [ "$1" = "migration" ]; then 
        echo 'Making migrations ... ';
        cd israsoc_website
        python manage.py makemigrations
    elif [ "$1" = "migrate" ]; then 
        echo 'Migrate dbsqlite ';
        cd israsoc_website
        python manage.py migrate
    elif [ "$1" = "superuser" ]; then 
        echo 'Creating SuperUser';
        cd israsoc_website
        python manage.py createsuperuser
    else
        echo 'Please enter a valid argument'
    fi
else
    echo "Too many arguments provided"
fi

