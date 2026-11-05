
class bestTest():
    def login(self):
        print("BestTest Login")

class openBrowser():
    def login(self):
        print("OpenBrowser Login")

class Mobile():
    def login(self):
        print("Mobile Login")


test = openBrowser()
test.login()
test = bestTest()
test.login()
test = Mobile()
test.login()