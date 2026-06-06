import qrcode

url = input("Enter the URL to generate QR code: ").strip()
file_path = "D:\\Coding\\QR Code\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)


print("QR code generated and saved to", file_path)