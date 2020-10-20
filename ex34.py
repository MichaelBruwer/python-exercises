def bold(i):
    def wrapped():
        return "<b>" + i() + "</b>"
    return wrapped

def italic(i):
    def wrapped():
        return "<i>" + i() + "</i>"
    return wrapped

def underlined(i):
    def wrapped():
        return "<u>" + i() + "</u>"
    return wrapped

@bold
@italic
@underline
def Diggy_Diggy_Hole():
    return "Diggy Diggy Hole"

print(Diggy_Diggy_Hole())
