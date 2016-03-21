class Dialog:
    def __init__(self, catalog):
        self.catalog = catalog
        self.state = 1
        self.current_question = self.catalog.find_question_by_state(self.state)

    def get_current_answers(self):
        if self.current_question is not None:
            return self.current_question.answers
        else:
            return None

    def to_next_question(self, answer):
        for ans in self.current_question.answers:
            if ans.value == answer:
                self.state = ans.next_state
                self.current_question = self.catalog.find_question_by_state(self.state)
                break
