name = "Trần Minh Sáng"
for character in name:
    print(character)#kết quả in ra là mỗi kí tự trong giá trị name lần lượt được in ra
teams = ["Barcelona", "Real Madrid", "Manchester United"]
for name in teams:
    print(name)#kết quả in ra là 3 đội bóng

teams = ["Barcelona", "Real Madrid", "Manchester United"]
for index in range(10):
    print(index)

teams = ["Barcelona", "Real Madrid", "Manchester United"]
for index in range(1,11):
    print(index)

teams = ["Barcelona", "Real Madrid", "Manchester United"]
for index in range(1,11):
    if index == 1:
        print("Đây là phần tử đầu tiên ở trong mảng")
    else:
        print(f"Đây là phần tử ở vị trí thứ {index}")