teams = ["Bacelona", "Real Madrid" , "Manchester United"]# lưu ý khi tạo biến muốn thêm nhiều tên danh sách đội hình thì thêm s đằng sau biến để phân biệt
#dùng ngoặc vuông để thêm được nhiều danh sách tên đội hình
print(teams)#in ra kết quả là 3 cái tên
#nếu muốn truy cập vào phần tử của từng cái tên đội hình một thì làm như sau
teams = ["Bacelona", "Real Madrid" , "Manchester United"]
#giá trị theo danh sách là: bacelona là 0 , real madrid là 1 , manchester united là 2
print(teams[0]) # muốn truy cập thì phải thêm ngoặc vuông sau biến
#nếu muốn truy cập thêm thì sửa số 0 thay bằng giá trị khác
print(teams[-1])#nếu viết -1 trong ngoặc vuông thì vẫn được tính vì python sẽ tính thứ tự
#từ phải sang trái là -3 , -2 , -1 , 0 nó sẽ in ra manchester United giống với số 3
#nếu chúng ta muốn in ra một phần danh sách trong biến teams thì làm như sau
teams = ["Bacelona", "Real Madrid" , "Manchester United"]
#vd nếu muốn in 2 đội bóng Real Madrid và Manchester United thì làm như sau
print(teams[0:3])#thêm dấu : nghĩa là in ra vị trí số 0 và tất cả các đội bóng còn lại ở phía sau của nó
#nếu thêm các tên các đội bóng thì đổi số ở trên
teams = ["Bacelona", "Real Madrid" , "Manchester United", "Liverpool", "Chelsea"]
print(teams[0:5]) #khi này sẽ in ra 5 đội bóng
#nếu muốn sửa tên đội bóng trong danh sách thì làm như sau
teams = ["Bacelona", "Real Madrid" , "Manchester United", "Liverpool", "Chelsea"]
teams[1] = "Arsenal"
print(teams[1])#kết quả hiển thị sẽ là arsenal thay vì real madrid