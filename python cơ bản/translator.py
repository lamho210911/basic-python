def translate(text):
    translation = ("")
    for character in text:
        if character in "áàảãạăắẳẵặâấầẩẫậ":
            translation = translation + "a"
        else:
            translation = translation + character

    return translation

print(translate("Sáng"))
# text = "Sáng"
# character = "S" --> translation = "" + "S" = "S"
# character = "á"--> translation = "S" + "a" = "Sa"
# character = "n" --> translation = "Sa" + "n" = "San"
# character = "g" --> translation = "San" + "g" = "Sang"

#ở dòng print cuối nếu ghi các chuỗi ký tự viết hoa toàn bộ thì khi chạy chương trình sẽ không được phiên dịch
def translate(text):
    translation = ("")
    for character in text:
        if character.lower() in "áàảãạăắẳẵặâấầẩẫậ":
            if character.isupper():
                translation = translation + "A"
            else:
                translation = translation + "a"
        else:
            translation = translation + character

    return translation

text = input("Nhập vào văn bản mà bạn muốn dịch: ")
print(translate(text))
