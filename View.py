class View:
    def __init__(self):
        pass

    # def __init__(self, controller):
    #     self.controller = controller

    def set_controller(self, controller):
        self.controller = controller

    def print_question(self):
        print(self.current_question.value)

    def print_unkown_command(self, command):
        print("Ошибка: %s - неизвестная команда" % command)

    def get_answer(self):
        return input()

    def set_current_question(self, current_question):
        self.current_question = current_question

    def is_answer(self, answer):
        for ans in self.current_question.answers:
            if ans.value == answer:
                return True
        return False

    def show(self):
        self.print_question()
        answer = self.get_answer()
        while not self.is_answer(answer):
            self.print_unkown_command(answer)
            answer = self.get_answer()
        self.controller.set_answer(answer)
