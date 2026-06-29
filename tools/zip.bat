@echo off
cd /d %~dp0..
powershell -ExecutionPolicy Bypass -File tools\zip.ps1
pause