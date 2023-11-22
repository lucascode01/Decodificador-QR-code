#Gerador de Qr Code

import qrcode

data = 'TopG'

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
img = qr.make_image(fill_color="green", back_color="white")

# Salva a imagem
img.save('C:/Users/lucas/OneDrive/Documents/new/myqrcode3.png')
