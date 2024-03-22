import abc


class Operation(abc.ABC):
    @abc.abstractmethod
    def operate(self, a, b): pass

    def print_result(self, operation_result):
        print(f'{operation_result}')


class Add(Operation):
    def operate(self, value_a, value_b):
        summary = value_a + value_b
        self.print_result(summary)
        return summary


class Minus(Operation):
    def operate(self, value_a, value_b):
        summary = value_a - value_b
        self.print_result(summary)
        return summary


class Multiply(Operation):
    def operate(self, value_a, value_b):
        summary = value_a * value_b
        self.print_result(summary)
        return summary


class Divide(Operation):
    def operate(self, value_a, value_b):
        summary = value_a / value_b
        self.print_result(summary)
        return summary


class ValueA:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value


class ValueB:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value
