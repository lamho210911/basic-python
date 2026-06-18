student_names =  ["Nguyên", "Hưng","Tuyên","Trung","Sáng","Trường"]
math_scores = [10,9,8,7,6,5]
#chúng ta có thêm hàm extend có tác dụng để thêm một danh sách khác vào danh sách hiện tại
student_names.extend(math_scores)
print(student_names)#khi in ra nó sẽ thêm danh sách của math_scores vào sau các tên của students name
#nếu muốn thêm các phần tử riêng lẻ vào danh sách thì dùng hàm append
student_names.append("Thắng")#nó sẽ thêm tên vào cuối danh sách
print(student_names)
#nếu muốn thêm phần tử vào giữa danh sách thì dùng hàm khác đó là insert
student_names.insert(1,"Lâm")#hàm này sẽ nhận 2 tham số và dùng để chèn tên vào giữa danh sách
print(student_names)
#nếu muốn xoá phần tử trong danh sách thì dùng hàm remove
student_names.remove("Sáng")
print(student_names)
#nếu muốn xoá  tất cả các phần tử trong danh sách thì dùng hàm clear
student_names.clear()#lưu ý hàm này không cần tham số đầu vào
print(student_names)#khi ấn run thì nó sẽ xoá hết các phần tử trong danh sách
#chúng ta có hàm pop để dùng xoá phần tử trong danh sách
student_names.pop()#cũng không cần tham số đầu vào
print(student_names)
#nếu muốn kiểm tra tên trong một danh sách có hay không thì dùng hàm index
student_names.index("Tuyên")
print(student_names)#sau đấy đưa lệch student_name vào hàm print
print(student_names.index("Tuyên"))
#nếu muốn đếm thứ tự giá trị trong một danh sách thì dùng hàm count
print(student_names.count("Tuyên"))#nó in ra số 3
#nếu muốn sắp xếp danh sách này thì dùng hàm sort
student_names.sort()
print(student_names)
#tương tự với biến math_scores
student_names.sort()
print(student_names)
#muốn đảo ngược giá trị trong danh sách thì dùng hàm reverse
math_scores.reverse()
print(math_scores)# khi chạy sẽ in ra giá trị từ 5 đến 10 thay vì 10 đến 5
#muốn copy lại biến student_names cũ thì dùng hàm copy
student_names_2 = student_names.copy()
print(student_names_2)#khi run sẽ in ra giá trị trong danh sách 1

