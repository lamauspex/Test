
from function.functions import determine_type



# Проверка на тип 'number' при передаче числового значения.
def test_determine_type_number():
    assert determine_type(123) == "number"


# Проверка на тип 'string' при передаче строкового значения.
def test_determine_type_string():
    assert determine_type("text") == "string"
