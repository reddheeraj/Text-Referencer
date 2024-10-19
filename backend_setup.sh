export FLASK_APP=./backend/app.py
python -m venv text_ref

source ./text_ref/bin/activate

pip install -r requirements.txt

flask run
