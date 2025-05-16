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
            html, body {
                height: 100%;
                margin: 0;
                padding: 0;
            }
            body {
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                background: #d3d3d3;
                font-family: Arial, sans-serif;
            }
            .header {
                background: #4176c5;
                color: #fff;
                text-align: center;
                padding: 24px 0 12px 0;
                font-size: 1.3em;
                border-radius: 0 0 12px 12px;
                letter-spacing: 1px;
                margin-bottom: 0;
            }
            .footer {
                background: #4176c5;
                color: #fff;
                text-align: center;
                padding: 16px 0 10px 0;
                font-size: 1.1em;
                border-radius: 12px 12px 0 0;
                margin-top: 0;
                flex-shrink: 0;
            }
            .main-container {
                background: #4176c5;
                border-radius: 0.5em;
                max-width: 900px;
                margin: 40px auto;
                padding: 40px 30px 40px 30px;
                display: flex;
                flex-direction: row;
                align-items: center;
                justify-content: center;
                gap: 40px;
                flex: 1 0 auto;
            }
            .info-box {
                background: #4176c5;
                border-radius: 8px;
                padding: 28px 24px;
                text-align: center;
                width: 400px;
                max-width: 100%;
                box-shadow: 0 2px 8px rgba(0,0,0,0.07);
                font-size: 1.2em;
                color: #fff;
                border: 0;
                display: flex;
                flex-direction: column;
                gap: 24px;
                justify-content: center;
                align-items: center;
            }
            .info-box p {
                color: #fff;
                margin: 0;
                font-size: 1.1em;
                line-height: 1.5em;
            }
            .image-box {
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 16px;
            }
            .image-box img {
                width: 220px;
                max-width: 100%;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                background: #fff;
            }
            .link-box {
                margin-top: 10px;
            }
            .link-box a {
                color: #fff;
                background: #285ca8;
                padding: 8px 18px;
                border-radius: 6px;
                text-decoration: none;
                font-weight: bold;
                transition: background 0.2s;
            }
            .link-box a:hover {
                background: #1d4177;
            }
            @media (max-width: 900px) {
                .main-container {
                    flex-direction: column;
                    gap: 20px;
                }
                .info-box, .image-box img {
                    width: 100%;
                }
            }
        </style>
    </head>
    <body>
        <div class="header">
            MI PRIMERA PAGINA WEB
        </div>
        <div class="main-container">
            <div class="info-box">
                <p>
                La Tecnología de la Información (TI) es un campo fundamental en la sociedad moderna, ya que permite gestionar, procesar, almacenar y transmitir información mediante el uso de sistemas computacionales y redes de comunicación. A través del desarrollo y la implementación de herramientas tecnológicas, las TI facilitan la automatización de procesos, la toma de decisiones y la interconexión entre personas, empresas y gobiernos.
                </p>
                <div class="link-box">
                    <a href="https://www.cesde.edu.pe/" target="_blank">Visitar CESDE</a>
                </div>
            </div>
            <div class="image-box">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/300px-PNG_transparency_demonstration_1.png" alt="Imagen de ejemplo">
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