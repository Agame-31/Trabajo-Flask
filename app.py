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
            .header, .footer {
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
                padding: 16px 0 10px 0;
                font-size: 1.1em;
                border-radius: 12px 12px 0 0;
                position: static;
                margin-top: 30px;
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
            }
            .info-box {
                background: #fff;
                color: #e3eaf7;
                border-radius: 8px;
                padding: 28px 24px;
                text-align: center;
                width: 400px;
                max-width: 100%;
                box-shadow: 0 2px 8px rgba(0,0,0,0.07);
                font-size: 1.2em;
                color: #e3eaf7;
                background: #4176c5;
                border: 0;
            }
            .info-box p {
                color: #fff;
                margin: 0;
                font-size: 1.1em;
                line-height: 1.5em;
            }
            .image-box img {
                width: 350px;
                max-width: 100%;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                background: #fff;
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
            </div>
            <div class="image-box">
                <img src="https://static.wikia.nocookie.net/southpark/images/5/5d/Butters_crying.png" alt="Butters llorando">
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