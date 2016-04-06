class Answer:
    def __init__(self, number, value, next_question):
        self.number = number
        self.value = value
        self.next_question = next_question


class Question:
    def __init__(self, number, value, answers):
        self.number = number
        self.value = value
        self.answers = answers

    def add_answer(self, answer):
        self.answer.append(answer)

    def delete_answer(self, answer):
        self.answers.remove(answer)


class Catalog:
    def __init__(self, questions):
        self.questions = questions

    def delete_question(self, question):
        self.questions.remove(question)

    def find_question_by_number(self, number):
        for question in self.questions:
            if question.number == number:
                return question
        return None

