_from quiz import quiz

questions = [
    "Câu 1.Đội bóng nào về nhì World Cup năm 1994?\nA. Brazil\nB. Italia\nC. Đức\n",
    "Câu 2.Đội bóng nào vô địch World Cup năm 1998?\nA. Argentina\nB. Pháp\nC. Brazil\n",
    "Câu 3.Nước nào là chủ nhà World Cup năm 2002?\nA. Qatar\nB. Đức\nC. Hàn Quốc + Nhật Bản\n",
]

quizzes = [
    quiz(questions[0], "B"),
    quiz(questions[1], "C"),
    quiz(questions[2], "A"),
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