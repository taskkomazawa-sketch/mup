@echo off

echo ==========================
echo MUP Bootstrap
echo ==========================

python -m venv .venv

call .venv\Scripts\activate

python -m pip install --upgrade pip

python -m pip install -r requirements.txt

pause