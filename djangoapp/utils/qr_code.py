'''Module for generating QR codes'''
from io import BytesIO
import qrcode
from django.core.files import File


def generate_qr_code(data):
    ''' Generate a QR code for the class session. '''
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Gera a imagem PIL do QR code
    img = qr.make_image(fill='black', back_color='white')

    # Retorna a imagem gerada
    return img
