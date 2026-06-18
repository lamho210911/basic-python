a = 50
b = 100
if a < b:
    print("a nhỏ hơn b")#khi run sẽ in ra kết quả là a nhỏ hơn b vì điều kiện so sánh a đã nhỏ hơn b nên trả về giá trị là true

a = 200
b = 100
if a < b:
    print("a nhỏ hơn b")#khi chạy chương trình nó sẽ không hiển thị gì vì a lớn hơn b đã trả về giá trị false
    #thêm một điều kiện để kiểm tra
elif a > b:
    print("a lớn hơn b")#vì 200 lớn hơn 100 nên elif thực hiện dòng lệch này

a = 100
b = 100
if a < b:
    print("a nhỏ hơn b")
elif a > b:
    print("a lớn hơn b")
    #khi chạy cả 2 hàm if và elif sẽ không hiển thị ra gì vì a=b để khắc phục thì thêm hàm else
else:
    print("a bằng b")
    #thêm mục nữa là toán tử logic
a = 200
b = 50
c = 100
if (a < b) and (a > c):
    print("a là số lớn nhất")#kết quả in ra là a là số lớn nhất vì 200 > 50 and 100

a = 200
b = 50
c = 300
if (a < b) and (a > c):
    print("a là số lớn nhất")#khi này c đã lớn hơn a và b nên không in ra cái gì nữa

a = 100
b = 50
c = 100
if (a == b) or (a == c):
    print("Có ít nhất một số bằng giá trị với a")#kết quả in ra là có ít nhất ... vì giá trị của a = c nên điều kiện
    #so sánh thứ hai sẽ thoả mãn và điều kiện if sẽ trả về giá trị true

a = 100
b = 50
c = 200
if (a == b) or (a == c):
    print("Có ít nhất một số bằng giá trị với a")#kết quả in ra là false vì giá trị của c không bằng a và b nên không thoả mãn

a = True
print(not a)#khi này sẽ in ra là false nghĩa là ngược lại với giá trị ban đầu

a = 100
b = 200
if not a > b:
    print("a Không lớn hơn b")