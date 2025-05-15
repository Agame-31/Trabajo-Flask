from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>¡Hola, esta es mi página web en producción con Python!</h1>"

if __name__ == '__main__':
    app.run()