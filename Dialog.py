class Dialog:
    def __init__(self, catalog):
        self.catalog = catalog
        self.number = 1
        self.current_question = self.catalog.find_question_by_number(self.number)

    def get_current_answers(self):
        if self.current_question is not None:
            return self.current_question.answers
        else:
            return None

    def to_next_question(self, answer):
        for ans in self.current_question.answers:
            if ans.value == answer:
                if ans.next_question == 0:
                    return False
                self.number = ans.next_question
                self.current_question = self.catalog.find_question_by_number(self.number)
                return True
                break
