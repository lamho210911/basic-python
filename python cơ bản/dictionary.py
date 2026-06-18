# Dictionary - Từ điển
# Key      |  Value
#+---------+----------
# | hello  | xin chào |
# +-------------------
# | goodbye | tạm biệt |
# +-------------------
# | morning | buổi sáng|
# +-------------------
# | bread   | bánh mỳ  |
# +-------------------
# | coffee  | cà phê   |
# +-------------------
# | tea     | trà      |
# +-------------------
# | milk    | sữa      |
# +-------------------
# | beer    | bia      |
# +-------------------
#tạo một dictionary
english_vietnamese_dictionary = {
    "Hello": "xin chào",
    "goodbye": "tạm biệt",
    "morning": "buổi sáng",
    "bread": "bánh mì",
    "coffee":"cà phê",
    "tea":"trà",
    "milk":"sữa",
    "beer":"bia"
}

print(english_vietnamese_dictionary["tea"])#kết quả in ra là trà
#nếu muốn lấy dữ liệu từ dictionary thì dùng hàm get
print(english_vietnamese_dictionary.get("Hello"))

print(english_vietnamese_dictionary.get("cat"))#kết quả in ra là none vì từ cat không có trong từ điển
print(english_vietnamese_dictionary.get("cat", "Từ khoá này không tồn tại"))
#chúng ta cũng có thể đặt key thành number không nhất thiết là một chuỗi
english_vietnamese_dictionary = {
    0: "xin chào",
    1: "tạm biệt",
    2: "buổi sáng",
    3: "bánh mì",
    4:"cà phê",
    5:"chuối",
    6:"sữa",
    7:"bia"
}
print(english_vietnamese_dictionary[0])
print(english_vietnamese_dictionary[1])