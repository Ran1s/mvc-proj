class View:
    def __init__(self, dialog, controller):
        self.dialog = dialog
        self.controller = controller
        self.controller.set_view(self)

    def is_answer(self, answer):
        for ans in self.dialog.current_question.answers:
            if ans.value == answer:
                return True
        return False

    def print_question(self):
        print(self.dialog.current_question.value)

    def print_unkown_command(self, command):
        print("Ошибка: %s", command)

    def get_answer(self):
        return input()
