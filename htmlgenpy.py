def version():
    return "0.0.1"

class Style:
    def bold(self, txt):
        out = "<b>" + txt + "</b>"
        return out
    def italic(self, txt):
        out = "<i>" + txt + "</i>"
        return out
    def underline(self, txt):
        out = "<u>" + txt + "</u>"
        return out
    def bools(self, txt, bold_bool, italic_bool, underline_bool):
        openers = ""
        closers = ""
        if bold_bool:
            openers = openers + "<b>"
            closers = closers + "</b>"
        if italic_bool:
            openers = openers + "<i>"
            closers = closers + "</i>"
        if underline_bool:
            openers = openers + "<u>"
            closers = closers + "</u>"
        out = openers + str(txt) + closers
        return out

class Header:
    def empty(self):
        out = ["<head>",
               "</head>"]
        return out
    def basic(title):
        out = ["<head>",
               ("<title>"+str(title)+"</title>"),
               "</head>"]
        return out