#!/bin/bash

startPythonServer(){
    python3 manage.py runserver 0.0.0.0:8000
}

startNPM(){
    npm start   
}

echo $'\n'
echo "[1] - Start only server (python)"
echo "[2] - Start server and NPM"
echo "[3] - Start only NPM"

echo $'\n'

action=''
echo -n "Select an action [default Start only server (python)]: "
read action

if [ "$action" == "1" ]; then
    startPythonServer
elif [ "$action" == "2" ]; then
    startPythonServer
    startNPM
elif [ "$action" == "3" ]; then
    startNPM
else
    startPythonServer
fi