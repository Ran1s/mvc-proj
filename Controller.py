class Controller:
    def __init__(self, dialog):
        self.dialog = dialog

    def set_view(self, view):
        self.view = view
        self.view.print_question()
        self.recognize_command(self.view.get_answer())

    def recognize_command(self, command):
        if self.view.is_answer(command):
            self.dialog.to_next_question(command)
            self.view.print_question()
        else:
            self.view.print_unkown_command(command)

        self.recognize_command(self.view.get_answer())