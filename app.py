from flask import Flask, request, jsonify, render_template
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_qrcode', methods=['POST'])
def gerar_qrcode():
    try:
        # Obtém os dados da solicitação POST
        data = request.json['data']

        # Cria um objeto QRCode com algumas opções de personalização
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(data)
        qr.make(fit=True)

        # Cria uma imagem QRCode personalizada
        img = qr.make_image(fill_color="red", back_color="black")

        # Salva a imagem
        img.save('static/myqrcode.png')

        return jsonify({'status': 'success', 'message': 'QR Code gerado com sucesso!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
