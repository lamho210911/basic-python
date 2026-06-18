def say_hello(): #đặt tên cho hàm
    print("Chào mừng bạn đã đến với channel Tờ Mờ Sáng học Lập Trình.")#hàm print phải thẳng hàng với say_helo

print("Bắt đầu")#thêm dòng lệch để xem cách hoạt động
say_hello()#bước gọi hàm để chạy chương trình
print("Kết thúc")

def say_hello(name, email):# cung cấp dữ liệu đầu vào được lưu trong các tham số (parameter)
    print(f"Chào mừng {name} đã đến với channel Tờ Mờ Sáng học Lập Trình.")
    print(f"Email của bạn là: {email}")

say_hello("Phong", "phongdeptrai@gmail.com")
say_hello("Huyền", "huyenxinhgai@gmail.com")
#kết quả khi in ra
#chào mừng phong đã đến với channel Tờ Mờ Sáng Học Lập Trình
#Email của bạn là: phongdeptrai@gmail.com
#chào mừng Huyền đã đến với channel Tờ Mờ Sáng Học Lập Trình
#email của bạn là: huyenxinhgai@gmail.com
