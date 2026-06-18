secret_world = "Python"#trong biến secret từ bí mật là Python
hint = "Gợi ý: Đây là tên một ngôn ngữ lập trình"#biến hint để lưu câu gợi ý
guess = ""
guess_count = 0
guess_limit = 3

print(hint)

while guess != secret_world:#khi người dùng đoán chưa đúng với từ bí mật thì vòng lặp sẽ thực hiện đến khi người dùng đoán đúng
    if guess_count < guess_limit:
       guess = input("Bạn đoán đây là gì?: ")
       guess_count += 1
    else:
       break#lệch break được sử dụng để bắt buộc một vòng lập dừng lại không thực hiện lại một lần nào nữa

if guess == secret_world:
    print("Bạn đã đoán chính xác rồi")
else:
    print("Bạn đã thất bại vì đoán sai")