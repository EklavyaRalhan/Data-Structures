class India():
    def capital(self):
        print("Capital of India is New Delhi")

    def language(self):
        print("Language of India is Hindi")

    def type(self):
        print("India is a developing country")

class USA():
    def capital(self):
        print("Capital of USA is Washington D.C")

    def language(self):
        print("Language of USA is English")

    def type(self):
        print("USA is a developed country")

india = India()
usa = USA()

for country in (india,usa):
    country.capital()
    country.language()
    country.type()
