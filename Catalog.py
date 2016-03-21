class Answer:
    def __init__(self, number, value, next_state):
        self.number = number
        self.value = value
        self.next_state = next_state


class Question:
    def __init__(self, number, state, value, answers):
        self.number = number
        self.state = state
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

    def find_question_by_state(self, state):
        for question in self.questions:
            if question.state == state:
                return question
        return None

