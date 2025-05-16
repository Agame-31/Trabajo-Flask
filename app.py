from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mi Primera Pagina Web</title>
        <style>
            body {
                background: #d3d3d3;
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
            }
            .header {
                background: #4176c5;
                color: #fff;
                text-align: center;
                padding: 24px 0 12px 0;
                font-size: 1.3em;
                border-radius: 0 0 12px 12px;
                margin-bottom: 30px;
                letter-spacing: 1px;
            }
            .container {
                background: #4176c5;
                border-radius: 0.5em;
                max-width: 650px;
                margin: 40px auto;
                padding: 30px 30px;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .container img {
                width: 100%;
                max-width: 500px;
                margin-bottom: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            }
            .footer {
                background: #4176c5;
                color: #fff;
                text-align: center;
                padding: 16px 0 10px 0;
                font-size: 1.1em;
                border-radius: 12px 12px 0 0;
                position: fixed;
                width: 100%;
                bottom: 0;
                left: 0;
                letter-spacing: 1px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            MI PRIMERA PAGINA WEB
        </div>
        <div class="container">
            <img src="https://static.wikia.nocookie.net/southpark/images/5/5d/Butters_crying.png" alt="Imagen 1">
            <img src="https://static.wikia.nocookie.net/southpark/images/5/5d/Butters_crying.png" alt="Imagen 2">
        </div>
        <div class="footer">
            INSTITUTO CESDE
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()