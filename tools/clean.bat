@echo off

cd /d %~dp0..

del /s /q *.pyc

for /d /r %%d in (__pycache__) do rd /s /q "%%d"

pause