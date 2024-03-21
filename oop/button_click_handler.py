from oop.line_info import LineInfo
from oop.line_info import ButtonsInfo
from oop.buttons_enum import ButtonsEnum
from oop.operation_handler import OperationHandler


class ButtonClickHandler:

    def __init__(self, buttons_info: ButtonsInfo, line_info: LineInfo):
        self.__operation_handler = OperationHandler()
        self.__buttons_info = buttons_info
        self.__line_info = line_info
        self.__line_info.line.setText('')
        self.subscribe_buttons()

    def subscribe_buttons(self):
        btn = self.__buttons_info

        # Equals
        btn.equals.clicked.connect(lambda: self.press_equals())

        # Clear
        btn.clear.clicked.connect(lambda: self.press_clear(ButtonsEnum.clear))

        # Operations
        btn.plus.clicked.connect(lambda: self.press_operation_button(ButtonsEnum.plus))
        btn.minus.clicked.connect(lambda: self.press_operation_button(ButtonsEnum.minus))
        btn.multiply.clicked.connect(lambda: self.press_operation_button(ButtonsEnum.multiply))
        btn.divide.clicked.connect(lambda: self.press_operation_button(ButtonsEnum.divide))

        # Numbers
        btn.zero.clicked.connect(lambda: self.press_number(0))
        btn.one.clicked.connect(lambda: self.press_number(1))
        btn.two.clicked.connect(lambda: self.press_number(2))
        btn.three.clicked.connect(lambda: self.press_number(3))
        btn.four.clicked.connect(lambda: self.press_number(4))
        btn.five.clicked.connect(lambda: self.press_number(5))
        btn.six.clicked.connect(lambda: self.press_number(6))
        btn.seven.clicked.connect(lambda: self.press_number(7))
        btn.eight.clicked.connect(lambda: self.press_number(8))
        btn.nine.clicked.connect(lambda: self.press_number(9))
        
    def press_operation_button(self, button: ButtonsEnum):
        self.__line_info.line.setText('')
        self.__operation_handler.set_operation(button.name)

    def press_number(self, number: int):
        text = self.__line_info.line.text() + str(number)
        self.__line_info.line.setText(text)
        print('Number Button clicked', text)
        self.__operation_handler.set_value(text)

    def press_clear(self, button: ButtonsEnum):
        self.__line_info.line.setText('')
        self.__operation_handler.clear()
        print('Clear Button clicked')

    def press_equals(self):
        result = str(self.__operation_handler.calculate())
        print('Equals Button clicked', result)
        self.__line_info.line.setText(result)
   
