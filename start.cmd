
@echo off
echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Compiling translations...
pybabel compile -d translations

echo Starting the Flask app...
python run.py
pause
