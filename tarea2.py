def Tarea2(a, b):
    if type(a) == int:
        if type(b) == int:
            if b <= a:
                return (a + b, a - b, a * b)
            else:
                return (-1)
        else:
            return (-1)
    else:
        return (-1)
