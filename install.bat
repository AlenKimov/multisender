@echo off
python -V
@echo Creating virtual environment...
python -m venv .venv
call .venv\Scripts\activate.bat
@echo Installing libraries...
pip install -r requirements.txt
python scripts\create_start_bat.py
@echo To start the script run "start.bat"
pause
:: start.bat