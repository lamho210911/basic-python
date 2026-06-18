phone_book = open("phone_book.txt", "a" , encoding="utf-8")
phone_book.write("Sáng - 09812345xx")#sau khi ấn run cửa sổ terminal sẽ không hiện gì mà hiện ở trong file txt
#dòng "Sáng - 09812345xx đã được thêm vào cuối file
#nếu muốn khắc phục tình trạng nội dung của write bị dính liền với dòng cuối của file txt thì thêm \n vào trước chữ sáng
#chế độ a
phone_book = open("phone_book.txt", "a" , encoding="utf-8")
phone_book.write("\nSáng - 09812345xx")
phone_book.write("\nBách - 09723112xx")
#chế độ w
phone_book = open("new_phone_book.txt", "w" , encoding="utf-8")
phone_book.write("\nSáng - 09812345xx")
phone_book.write("\nBách - 09723112xx")

phone_book = open("index.html", "w")
phone_book.write("<p>Hello, world!</p>")

tmsangdev = open("tmsangdev.py", "w" , encoding="utf-8")
phone_book.write("Hello, world!")



