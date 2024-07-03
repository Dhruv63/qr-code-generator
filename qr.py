import qrcode as qr
a=input("ENTER THE URL")
b=input("ENTER THE NAME OF QR")
img=qr.make(a)
img.save(b)