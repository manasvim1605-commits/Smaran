
@echo off

title SMARAN Launcher

cd /d "C:\Users\Manasvi M. Mandhare\Desktop\Smaran"

echo Starting SMARAN...

start "SMARAN Server" /min cmd /k "python flask/app.py"

timeout /t 4 /nobreak >nul

echo Opening SMARAN in Google Chrome...

start "" chrome "http://127.0.0.1:5000/"

exit
