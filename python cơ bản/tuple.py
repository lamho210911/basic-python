#turple là một cấu trúc dữ liệu nơi có thể lữu trữ các giá trị khác nhau
#tuple có cấu trúc là vd: coordinates = (x , y)
#lưu ý: tuple sẽ sử dụng dấu ngoặc đơn thay vì dấu ngoặc vuông như list
#1 tuple sẽ không thể thay đổi trong tiếng anh là( immutable) nghĩa là các giá trị bên trong tuple sẽ không
#thể chỉnh sửa được sau khi đã tạo nó lên và cũng không thể thêm phần tử vào trong nó và không thể xoá các phần tử
#khỏi nó và cũng không thể thay đổi bất kì phần tử nào bên trong nó
#để in ra giá trị bên trong tuple thì sử dụng một cặp dấu ngoặc vuông trong truyền vào chỉ số vị  trí
#các thứ tự giá trị trong tuple cũng được bắt đầu từ 0
coordinates = (123, 456)
print(coordinates[0])#sau khi in ra nó sẽ hiện là 123 tương tự khi đổi từ 0 sang 1 sẽ là 456
#nếu muốn tạo ra một danh sách các tuple , danh sách các toạ độ khác nhau bằng cách kết hợp
#list và tuple
coordinates = [(123, 456), (1, 2),(3,4)]#đây là một danh sách lần lượt là các tuple tương ứng với từng điểm toạ độ
#lưu khi khi sử dụng tuple và list
#sử dụng tuple khi muốn lưu trữ dữ liệu không bao giờ thay đổi
#list được dùng phổ biến và có thể thay đổi rất phù hợp