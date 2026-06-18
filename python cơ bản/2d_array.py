#Mẩng 2 chiều
#Các vòng lặp lồng nhau
numbers = [1, 2, 3]
#Ma trận (Mảng 2 chiều)
#  [1, 2, 3]
#  [4, 5, 6]
#  [7,8,9]

matrix = [
    [1, 2, 3],#0
    [4, 5, 6],#1
    [7, 8, 9]#2
]
print(matrix[1][1])#kết quả in ra là 5
print(matrix[2][1])#kết quả in ra là 8
#lưu ý ngoặc vuông thứ nhất là cột và thứ hai là hàng vd: cột 2 hàng 1
#các thứ tự luôn bắt đầu từ con số 0
#nếu muốn in ra các phần tử trong hàng thì dùng vòng lặp for
for row in matrix:
    print(row)

for row in matrix:
    for column in row:
        print(column)#kết quả in ra là 1 đến 9
