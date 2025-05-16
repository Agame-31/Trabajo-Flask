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
                max-width: 300px;
                margin: 10px;
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
            .info {
                background: #fff;
                color: #222;
                border-radius: 8px;
                padding: 18px;
                margin-bottom: 20px;
                text-align: center;
                width: 90%;
                max-width: 600px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.07);
            }
            .enlace {
                display: inline-block;
                margin-top: 10px;
                color: #4176c5;
                text-decoration: none;
                font-weight: bold;
            }
            .enlace:hover {
                text-decoration: underline;
            }
            .imagenes {
                display: flex;
                justify-content: center;
                gap: 20px;
                flex-wrap: wrap;
            }
        </style>
    </head>
    <body>
        <div class="header">
            MI PRIMERA PAGINA WEB
        </div>
        <div class="container">
            <div class="info">
                <h1>Bienvenido a mi página</h1>
                <p>Esta es una página web de ejemplo creada con Flask. Aquí puedes ver imágenes, enlaces y más contenido organizado con HTML.</p>
                <a class="enlace" href="https://www.cesde.edu.co/" target="_blank">Visita el Instituto CESDE</a>
            </div>
            <div class="imagenes">
                <img src="https://static.wikia.nocookie.net/southpark/images/5/5d/Butters_crying.png" alt="Imagen 1">
                <img src="https://static.wikia.nocookie.net/southpark/images/5/5d/Butters_crying.png" alt="Imagen 2">
            </div>
        </div>
        <div class="footer">
            INSTITUTO CESDE
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()