import qrcode

print("===== QR CODE GENERATOR =====")

text = input("Enter text or a website URL: ").strip()

if not text:
    print("Please enter some text or a URL.")
else:
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    image.save("my_qr_code.png")

    print("QR code created successfully!")
    print("Saved as: my_qr_code.png")
```
