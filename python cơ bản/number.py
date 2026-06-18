print(2)#khi ấn run sẽ trả ra kết quả là 2 là số nguyên
print(3.14569)#khi ấn run sẽ trả ra kết quả 3.14569 là số thập phân
print(-3.14569)#khi in ra sẽ ra kết quả là -3.14569 là số âm
print(3 + 4)#in ra sẽ là 7
print(3 + 4.5)#sẽ tính ra kết quả laf 7.5 là một số thập phân
print(2 * 3 + 4)#dấu sao là dấu nhân và python sẽ tính nhân chia trước cộng trừ sau sẽ ra kết quả là 10
#nếu muốn thay đổi để python tính phép cộng trc thì thêm dấu ( như sau:
print(2 * (3 + 4))#python sẽ tính 3+4 =7 trước rồi nhân với 2
print(5 % 2)#python lấy 5 :2 =2 dư 1
number = 2
print(number)# sẽ ra kết quả là 2
#muốn nối chuỗi cho biến number thì thêm hàm str
print(str(number) + " là số người yêu mà tôi có") # khi chạy chương trình thì sẽ báo là 2 là số ng yêu tôi phải thêm hàm str để không bị lỗi cú pháp
#chúng ta có hàm abs là giá trị tuyệt đối khi sử dụng hàm này chúng ta sẽ tính được giá trị tuyệt đối của một số
print(abs(number))
#vd : number = -2 thì  trị tuyệt đối của -2 là 2
print(pow(2 , 3))
#hàm pow sẽ cho chúng ta chuyền được 2 giá trị là 2 và 3 trong đó 2 là số và 3 là số mũ thì sẽ ra kết quả 2 mũ 3 = 8
#vd khác print(pow(2 , 10)) thì sẽ ra kết quả là 1024 vì 2 mũ 10 = 1024
print(max(2 , 10))#hàm max sẽ tính giá trị cao nhất trong 2 giá trị trong ngoặc và số 10 là số cao nhất
print(min(2 , 10))#hàm min sẽ tính giá trị nhỏ nhất trong 2 giá trị trong ngoặc và số 2 là số nhỏ nhất
number = 2.3
print(round(number))#hàm round sẽ tuân theo làm tròn số tiêu chuẩn vd 2.3 sẽ thành 2
number = 2.7
print(round(number))#hàm round sẽ làm tròn kết quả 2.7 thành 3
#nếu muốn sử dụng các hàm của thư viện toán thì dùng import math
print(math.floor(number)) #gõ tên thư viện trước rồi dùng hàm và kết quả nó ra khi number là 2.7 là 2 nó không theo trình tự tiêu chuẩn giống hàm round
print(math.ceil(number)) #nếu number là 2.2 thì kết quả ra là 3 vì hàm ceil thì làm tròn lên và hàm floor thì làm tròn xuống
print(math.sqrt(number)) #nếu number là 36 thì sẽ tính kết quả căn bậc hai của 36 là 6.0