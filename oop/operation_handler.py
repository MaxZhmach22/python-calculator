from oop.operation_abstract import Operation, Minus, Multiply, Divide
from oop.operation_abstract import Add


class OperationHandler:

    __value_a: int = 0
    __value_b: int = 0
    __operation: Operation or None = None

    @property
    def value_a(self):
        return self.__value_a

    @value_a.setter
    def value_a(self, value):
        self.__value_a = value

    @property
    def value_b(self):
        return self.__value_b

    @value_b.setter
    def value_b(self, value):
        self.__value_b = value

    @property
    def operation(self):
        return self.__operation

    def clear(self):
        self.__value_a = 0
        self.__value_b = 0
        self.__operation = None

    def set_value(self, text):
        if self.__operation is None:
            self.__value_a = int(text)
        else:
            self.__value_b = int(text)

    def set_operation(self, operation):
        if operation == 'plus':
            self.__operation = Add()
        elif operation == 'minus':
            self.__operation = Minus()
        elif operation == 'multiply':
            self.__operation = Multiply()
        elif operation == 'divide':
            self.__operation = Divide()


    def calculate(self):
        if self.__operation is None:
            return 0
        return self.__operation.operate(self.__value_a, self.__value_b)
