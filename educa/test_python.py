counter = 0


class person:
    about = "this section is about person"
    counter += 1
    print("%s. name in class is " % counter + __name__)

    def __init__(self, model=""):
        self.counter += 1
        self.model = model
        print("%s. name in init is " % self.counter + __name__)

    def variable_grow(self):
        self.counter += 1
        print("%s. name in variable_grow is " % self.counter + __name__)

    @classmethod
    def grow(clss, herf=''):
        clss.counter += 1
        print("%s. name in classmethod is " % clss.counter + __name__)
        # herf = "chris"
        return clss.about + ' ' + herf

    @staticmethod
    def static_grow(cls, stat_count):
        stat_count += 1
        print("%s. name in staticmethod is " % counter + __name__)
        return ",this is from static with about " + cls.about


counter += 1
print("%s. name in module test_python is " % counter + __name__)
