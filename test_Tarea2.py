import tarea2


def test_tarea20():
    suma, resta, multiplicacion = tarea2.Tarea2(2, 1)
    assert suma == 3
    assert resta == 1
    assert multiplicacion == 2


def test_tarea21():
    res = tarea2.Tarea2(3, 4)
    assert res == -1


def test_tarea22():
    res = tarea2.Tarea2("asd", 4)
    assert res == -1
