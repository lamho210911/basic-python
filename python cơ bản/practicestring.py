print("Tờ Mờ Sáng Học Lập Trình ")#in ra câu "Tờ Mờ Sáng Học Lập trình"


print("Tờ Mờ Sáng" 
        " Học Lập Trình ")#in ra câu "Tờ mờ sáng học lập trình" nhưng có thêm khoảng trống giá trị ở giữa 
#muốn khắc phục lỗi dính chữ thì phải thêm \n để xuống dòng ở giữa câu
print("Tờ Mờ Sáng\n học Lập trình")
#đã khắc phục lỗi dính chữ

#có thể sử dụng 3 dấu ngoặc kép để hiển thị string nhiều dòng khác nhau là :
print("""Tờ Mờ Sáng
      Học Lập Trình""")
#không cần phải thêm \n để xuống dòng nữa vì đã có 3 dấu ngoặc kép

#muống thêm 2 dấu ngoặc kép ở cuối câu thì phải thêm \ để tránh lỗi
print("Tờ Mờ Sáng Học Lập trình \n\"học Lập trình\"")
#đã khắc phục lỗi khi thêm 2 dấu ngoặc kép ở cuối câu

#tiếp theo chúng ta có thể tạo ra biến để lưu giá trị string này
channel_name = "Tờ Mờ Sáng học Lập trình"
#sau đó có thể dùng channel_name để in ra giá trị biến này như sau
#và chúng ta có thể nối thêm một string khác vào biến channel_name là:
print(channel_name + " dễ hiểu quá")

# muốn in viết hoa biến channel_name thì dùng hàm upper() là:
print(channel_name.upper())
#muốn in viết thường biến channel_name thì dùng hàm lower() là:
print(channel_name.lower())
#muốn in ra số ký tự của biến channel_name thì dùng hàm len() là:
print(len(channel_name))
#muốn in ra ký tự đầu tiên của biến channel_name thì dùng hàm index từ thấp đến cao là:
print(channel_name.index("S"))
#index dùng để in ra vị trí hiện tại của 1 kí tự hoặc một chuỗi ký tự trong 1 string
print(channel_name[0])#nhớ phải dùng ngoặc vuông để lấy giá trị của biến channel_name
#muốn in ra ký tự cuối cùng của biến channel_name thì dùng hàm index từ cao đến thấp là:
print(channel_name[-1])#nhớ phải là -1 từ phải sang trá để lấy giá trị của biến channel_name
#muốn kiểm tra xem biến channel_name có viết hoa hay viết thường thì dùng hàm isupper() và islower() là:
print(channel_name.isupper())#sẽ trả về false vì biến channel_name không phải là viết hoa toàn bộ
print(channel_name.islower())#sẽ trả về true vì biến channel_name có chứa chữ thường

#muốn in hoa trước rồi kiểm tra thì dùng hàm upper() hoặc lower() rồi kết hợp với hàm isupper() hoặc islower() là :
print(channel_name.upper().isupper())#sẽ trả về true vì biến channel_name đã được in hoa toàn bộ 
#tương tự như trên
print(channel_name.lower().islower())#sẽ trả về true vì biến channel_name đã được viết thường toàn bộ 

print(channel_name.replace("Sáng" , "Tối"))
#hàm replace có tác dụng để thay thế một ký tự cũ sang kí tự mới của 1 giá trị

