from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os, dotenv, smtplib, ssl

dotenv.load_dotenv()

port = 465
sender_email = 'sender.paulofilho@gmail.com'
sender_password = os.getenv('EMAIL_PASSWORD')
receiver_email = 'paulomacieltorresfilho@gmail.com'

context = ssl.create_default_context()

content = """\
<html>

<head>
    <style>
        * {
            margin: 0;
            padding: 0;
            font-family: 'Courier New'
        }

        body {
            width: 100%;
        }

        .header {
            text-align: center;
            width: 100%;
            height: 80px;
            line-height: 80px;
            background-color: blue;
            color: white;
            margin-bottom: 30px;
        }

        .section {
            margin-bottom: 30px;
            width: 100%;
        }

        h2 {
            padding-left: 60px;
            margin-bottom: 15px;
        }

        table {
            margin: 0 auto;
            width: 100%;
            border-collapse: collapse;
        }

        td {
            border-bottom: 1px solid #cecece;
            padding: 8px;
        }
    </style>
</head>

<body>
    <div class="header">
        <h1>Novos Anúncios</h1>
    </div>
    <div class="section">
        <h2>OLX</h2>
        <table>

            <tr class="list-items">
                <td><a href="">Nome do anúncio</a></td>
                <td>Valor</td>
                <td>Local</td>
            </tr>
            <tr class="list-items">
                <td><a href="">Nome do anúncio</a></td>
                <td>Valor</td>
                <td>Local</td>
            </tr>
            <tr class="list-items">
                <td><a href="">Nome do anúncio</a></td>
                <td>Valor</td>
                <td>Brasília - DF</td>
            </tr>
        </table>
    </div>
    <div class="section">
        <h2>Mercado Livre</h2>
        <table>

            <tr class="list-items">
                <td><a href="">Nome do anúncio</a></td>
                <td>Valor</td>
                <td>Local</td>
            </tr>
            <tr class="list-items">
                <td><a href="">Nome do anúncio</a></td>
                <td>Valor</td>
                <td>Local</td>
            </tr>
            <tr class="list-items">
                <td><a href="">Nome do anúncio</a></td>
                <td>Valor</td>
                <td>Brasília - DF</td>
            </tr>
        </table>
    </div>
    <div class="section">
        <h2>WebMotors</h2>
        <table>

            <tr class="list-items">
                <td><a href="">Nome do anúncio</a></td>
                <td>Valor</td>
                <td>Local</td>
            </tr>
            <tr class="list-items">
                <td><a href="">Nome do anúncio</a></td>
                <td>Valor</td>
                <td>Local</td>
            </tr>
            <tr class="list-items">
                <td><a href="">Nome do anúncio</a></td>
                <td>Valor</td>
                <td>Brasília - DF</td>
            </tr>
        </table>
    </div>
    <div class="section">
        <h2>Facebook Marketplace</h2>
        <table>

            <tr class="list-items">
                <td><a href="">Nome do anúncio</a></td>
                <td>Valor</td>
                <td>Local</td>
            </tr>
            <tr class="list-items">
                <td><a href="">Nome do anúncio</a></td>
                <td>Valor</td>
                <td>Local</td>
            </tr>
            <tr class="list-items">
                <td><a href="">Nome do anúncio</a></td>
                <td>Valor</td>
                <td>Brasília - DF</td>
            </tr>
        </table>
    </div>
</body>

</html>
"""

message = MIMEMultipart('alternative')
message['Subject'] = "Teste com HTML"
message['From'] = sender_email
message['To'] = receiver_email

message.attach(MIMEText(content, 'html', 'utf-8'))


with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
