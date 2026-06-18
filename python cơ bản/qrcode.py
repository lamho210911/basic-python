#cách để tải module qr code là pip install qrcode[pil]

import qrcode

image = qrcode.make("https://youtube.com/@tmsangdev")
image.save("qrcode.png", "PNG")
#nếu muốn xoá module qrcode thì dùng lệch pip uninstall qrcode









