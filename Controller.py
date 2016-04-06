class Controller:
    def __init__(self, dialog, view):
        self.dialog = dialog
        self.view = view

    def start(self):
        self.view.set_current_question(self.dialog.current_question)
        self.view.show()

    def set_answer(self, answer):
        if self.dialog.to_next_question(answer) is not False:
            self.start()
