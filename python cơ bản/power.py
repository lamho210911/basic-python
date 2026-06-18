# Hàm tính luỹ thừa
# ví dụ:
# 2^3 = 8
# 3^2 = 9
print(2**3)#khi in ra sẽ ra quả là 8 và 2 dấu hoa thị thay thế cho dấu ^(mũ)
def caculate_power(base, exponent):
    result = 1
    for index in range(exponent):
        result = result * base
    return result

print(caculate_power(3, 3))
#def = từ khóa dùng để tạo hàm.
#caculate_power = tên hàm.
#base = số cơ sở (số cần lũy thừa).
#exponent = số mũ.