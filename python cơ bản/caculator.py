num1 = input("Nhập số thứ nhất: ")#vd là 1
num2 = input("Nhập số thứ hai: ")#vd là 2
sum = num1 + num2
print(sum)#khi ấn run kết quả sẽ là 12 vì mặc định khi sử dụng hàm input python sẽ chuyển giá trị của người dùng vào thành chuỗi không cần biết giá trị đó là gì
#để chuyển num1 và num2 thành dạng số (number) thì làm như sau
num1 = input("Nhập số thứ nhất: ")#vd là 1
num2 = input("Nhập số thứ hai: ")#vd là 2
sum =int(num1) + int(num2)
print(sum)#khi này hàm int sẽ chuyển các biến num1 và num2 từ chuỗi thành dạng số nguyên khi chạy xong thì sẽ ra kết quả là 3
#lưu ý hàm int chỉ tìm số nguyên không tìm số thập phân
#nếu muốn chuyển giá trị sang số thập phân thì dùng hàm float
num1 = input("Nhập số thứ nhất: ")#vd là 1
num2 = input("Nhập số thứ hai: ")#vd là 2.5
sum =float(num1) + float(num2)
print(num)#khi ấn run nó sẽ ra kết quả là một số thập phân
