# Generative AI

<p align="center">
  <img width="460" height="300" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Claude_Monet%2C_Impression%2C_soleil_levant.jpg/617px-Claude_Monet%2C_Impression%2C_soleil_levant.jpg" alt="Claude Monet, Soleil Levant" />
</p>

## Install

### Windows

```
python -m venv venv
venv\Scripts\activate.bat
pip -r requirements.txt
```

## Deployment

### Windows

```
set FLASK_ENV=development
set FLASK_APP=app.py
flask run --host=0.0.0.0
```

## Run

Open http://127.0.0.1:5000 in a browser.
