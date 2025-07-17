class normalclass:
    __privatevar = 8

    def __privatefunction(self):
        print("I'm inside this class")

    def hello(self):
        print("Private variable value is", normalclass.__privatevar)

var = normalclass()
var.__privatevar
var.hello