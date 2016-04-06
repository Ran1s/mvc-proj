from Catalog import *
from Dialog import Dialog
from Controller import Controller
from View import View

question = Question(1, 'Привет', [Answer(1, 'Привет', 2), Answer(2, 'Пока', 0)])
question2 = Question(2, 'Как дела?', [Answer(1, 'Хорошо', 3), Answer(3, 'Нормально', 3)])
question3 = Question(3, 'Пока', [Answer(1, 'Пока', 0)])

catalog = Catalog([question, question2, question3])

dialog = Dialog(catalog)
view = View()
controller = Controller(dialog, view)
view.set_controller(controller)

controller.start()

