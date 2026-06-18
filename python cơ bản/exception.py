#Exception (Ngoại lệ)
#Throw an exception (Ném ra một ngoại lệ)
#Handle exception (Xử lí ngoại lệ)

#vd 1
try:
    print(text)
except:
    print("Có lỗi xảy ra, vui lòng liên hệ trung tâm tư vấn để được hỗ trọ")
#vd 2
try:
    num1 = int(input("Nhập vào tử số"))
    num2 = int(input("Nhập vào mẫu số"))
    result = num1 / num2
    print(f"Thương của phép chia là: {result}")
except ZeroDivisionError:
    print("Mẫu số phải khác 0. Vui lòng nhập lại")
except ValueError:
    print("Dữ liệu đầu vào phải là các số nguyên")
except:
    print("Có lỗi xảy ra vui lòng liên hệ trung tâm để được hỗ trợ")
