# --USING QRCODE
# import qrcode as qr

# img = qr.make("Hello, Python!!")
# img.save("pythonqr.png")

# --------------------------------------------------------------------

# --USING SEGNO
import segno

qr = segno.make_qr("Hello, PYTHON!!")
qr.save(
    "segno_qrcode.png",
    scale = 5,
    border = 2,
    light = "lightgreen",
    dark = "green",
    data_dark = "darkgreen",
    
) 
