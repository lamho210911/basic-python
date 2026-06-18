

phone_book = open("phone_book.txt", "r", encoding="utf-8")
print(phone_book.read())

phone_book = open("phone_book.txt", "r", encoding="utf-8")
print(phone_book.readable())



phone_book = open("phone_book.txt", "r", encoding="utf-8")
print(phone_book.readline())

phone_book = open("phone_book.txt", "r", encoding="utf-8")
print(phone_book.readlines())

phone_book = open("phone_book.txt", "r", encoding="utf-8")

for person in phone_book.readlines():
    person = person.replace("\n", "")
    print(person)

phone_book.close()

with open("phone_book.txt", "r", encoding="utf-8") as phone_book:
    print(phone_book.readline())












