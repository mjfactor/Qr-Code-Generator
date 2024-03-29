import qrcode


def generate_qr_code(website_link):
    qr = qrcode.QRCode(version=1, box_size=7, border=5)
    qr.add_data(website_link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode.png')
    return img
