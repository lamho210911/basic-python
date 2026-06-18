#đang có sẵn 2 phương pháp nối chuỗi
#1
number = 2
text = "là số người yêu mà tôi từng có."
print(str(number) + text)#đây là phương pháp dùng hàm str để nối chuỗi
#2
print(f"{number}{text}")#đây là phương pháp dùng f để định dạng , khi chạy chương trình sẽ lấy được giá trị của các biến
#3 chúng ta có thêm một phương pháp mới để nối chuỗi đó là dùng hàm format như sau
number = 2
text = ("{} là số người yêu mà tôi từng có")# đặt thêm 2 dấu ngoặc nhọn để chuyển biến number = 2 xuống
print(text.format(number))#khi chạy chương trình thì số 2 đã được thêm vào 2 dấu ngoặc nhọn trong biến text
#nếu muốn sử dụng nhiều ngoặc nhọn trong string hơn thì xem ví dụ sau
my_age = 27
my_wife_age = 25
text = "Năm nay tôi {} tuổi. Còn vợ tôi {} tuổi"
print(text.format(my_age , my_wife_age))#khi chạy chương trình cả 2 giá trị trong biến sẽ được xuống trong các ngoặc text
                                                #lưu ý nếu có bao nhiêu ngoặc nhọn thì thêm bấy nhiêu tên biến vào hàm format

#nếu muốn đảo ngược lại đoạn text thì làm như sau
my_age = 27
my_wife_age = 25
text = "Năm nay vợ tôi {1} tuổi. Còn  tôi {0} tuổi"#lúc này chỉ cần đảo lại tên và thêm số
print(text.format(my_age , my_wife_age))#my_age có giá trị thứ tự là 0 còn my_wife_age có giá trị là 1