#!/bin/sh 
if [ $# -lt 2 ] ; then
    if [ "$1" == "run"]; then 
    echo 'Launching localhost server';
    # cd israsoc_website 
    # python manage.py runserver
    else
    echo ""
    fi 

    # elif [ "$1" == "venv"]; then 
    # echo 'Activate virtual environment';
    # ./israsoc_venv/Scripts/activate 
    # else
    # echo ""
    # fi
    else
    echo ""
else
    echo 'Please enter a valid argument'
fi
