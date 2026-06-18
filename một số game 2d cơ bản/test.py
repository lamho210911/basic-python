num1 = float(input("Nhập số thứ nhất vào đây:"))
operator = input("Nhập toán tử vào đây:")
num2 = float(input("Nhập số thứ hai vào đây:"))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("operator error")

secret_word = "Python"
hint = "Gợi ý: Đây là một ngôn ngữ lập trình"
guess = ""
guess_count = 1
guess_limit = 3
print(hint)

while secret_word != guess:
    if guess_count <= guess_limit:
        guess_count += 1
        guess = input("Bạn đoán đây là từ gì?:")
    else:
        break

if secret_word == guess:
    print("Bạn đã đoán chính xác")
else:
    print("Bạn đã đoán sai 3 lần")

def say_hello(name, email):
    print(f"Chào mừng {name} đã đến với kênh tờ mờ sáng học lập trình")
    print(f"Email của bạn là {email}")

say_hello("Phong", "phongvu1992@gmail.com")
say_hello("Huyen", "huyenanh1983@gmail.com")

def caculate_power(base_number, exponent):
    result = 1
    for index in range(exponent):
        result *= base_number
    return result
print(caculate_power(2, 3))

def translate(text):
    translation = ""
    for character in text:
        if character.lower() in "áàảãạăắẳặâấầẩẫậ":
            if character.isupper():
                translation = translation + "A"
            else:
                translation = translation + "a"
        else:
            translation = translation + character
    return translation

text = input("Nhập vào văn bản mà bạn muốn dịch:")
print(translate(text))


dictionary = {
    "Hello": "xin chào",
    "goodbye": "tạm biệt",
    "morning": "buổi sáng",
    "i": "tôi",
    "is": "là",
    "name": "tên",
    "student": "học sinh",
    "like": "thích",
    "school": "trường học",
    "are": "là",
}


def translate(text):
    words = text.lower().split()
    result = []

    for word in words:
        if word in dictionary:
            result.append(dictionary[word])
        else:
            result.append("[" + word + "]")

    return " ".join(result)

text = input("Nhập câu tiếng anh cần dịch: ")
translation = translate(text)

print("Nghĩa tiếng việt là: " + translation)

with open("phone_book.txt", "r", encoding="utf-8") as phone_book:
    for person in phone_book:
        person = person.replace("\n", "")
        print(person)

with open("phone_book.txt", "a", encoding="utf-8") as phone_book:
    phone_book.write("Đạt - 0826566839xx")

with open("new_phone_book.txt", "w", encoding="utf-8") as new_phone_book:
    new_phone_book.write("Chào mừng bạn đã đến với new phone book")


with open("phone_book.txt", "r", encoding="utf-8") as phone_book:
    print(phone_book.readable())

with open("phone_book.txt", "r", encoding="utf-8") as phone_book:
    print(phone_book.read())

with open("phone_book.txt", "r", encoding="utf-8") as phone_book:
    print(phone_book.readline())

with open("phone_book.txt", "r", encoding="utf-8") as phone_book:
    print(phone_book.readlines())

with open("phone_book.txt", "r", encoding="utf-8") as phone_book:
    for person in phone_book:
        print(person.strip())



class Car:
    def __init__(self, ParaMeterName, ParaMeterBrand, ParaMeterColor):
        self.name = ParaMeterName
        self.brand = ParaMeterBrand
        self.color = ParaMeterColor

    def drive(self):
        print(f"Bạn đang lái chiếc xe{self.name}, màu {self.color}, của hãng xe {self.brand}")

KiaMorning = Car(" KIA Morning" ,"KIA", "Blue")
KiaMorning.drive()

class quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

# Đã xóa dòng: from quiz import quiz

questions = [
    "Câu 1.Đội bóng nào về nhì World Cup năm 1994?\nA. Brazil\nB. Italia\nC. Đức\n",
    "Câu 2.Đội bóng nào vô địch World Cup năm 1998?\nA. Argentina\nB. Pháp\nC. Brazil\n",
    "Câu 3.Nước nào là chủ nhà World Cup năm 2002?\nA. Qatar\nB. Đức\nC. Hàn Quốc + Nhật Bản\n",
]

quizzes = [
    quiz(questions[0], "B"),
    quiz(questions[1], "B"), # Đã sửa từ "C" thành "B"
    quiz(questions[2], "C"), # Đã sửa từ "A" thành "C"
]

def run_quizzes(quizzes):
    score = 0
    for quiz in quizzes:
        print(quiz.question)
        user_input = input("Nhập câu trả lời của bạn: ")
        if user_input.lower() == quiz.answer.lower():
            score += 1

    print(f"\n--> Kết Quả: Bạn đã trả lời đúng {score}/{len(quizzes)} câu!")

run_quizzes(quizzes)














