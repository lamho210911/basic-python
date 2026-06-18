#Bài 30:Class và Object (Lớp và Đối tượng)
class Car:
    def __init__(self, name, brand, color):#Từ init là từ khởi tạo tất cả các class thì đều có hàm init
        self.name = name
        self.brand = brand
        self.color = color
        
class Car:
    def __init__(self, prameterName, prameterColor, prameterBrand):#Nếu muốn sửa tham số đầu vào của name thì dùng phím tắt shift + f6
        self.name = prameterName
        self.color = prameterColor
        self.brand = prameterBrand

    def drive(self):
        print(f"Bạn đang lái chiếc xe {self.name} màu {self.color} của hãng xe {self.brand}")

kiaMorning = Car("KIA Morning","xanh dương","Kia ")
kiaMorning.drive()

ferrariTributo = Car("Ferrari F8 Tributo", "đỏ","Ferrari ")
ferrariTributo.drive()