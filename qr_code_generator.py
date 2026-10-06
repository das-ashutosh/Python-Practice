import qrcode
data = input("Enter text or URL: ")
qr = qrcode.make(data)
qr.save("my_qr_code.png")
print("QR code generated successfully!")
print("Saved as: my_qr_code.png")
