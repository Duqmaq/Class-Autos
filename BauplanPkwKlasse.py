class Pkw():
    "Klasse für das Erstellen von Personenkraftwagen"
    def __init__(self, farbe, baujahr, kmstand, sitze, marke):
        self.farbe = farbe
        self.baujahr = baujahr
        self.kmstand = kmstand
        self.sitze = sitze
        self.marke = marke
        self.strecke = kmstand

    def tut_hupen(self, anzahl =1):
        print(anzahl * "tout-tout ")

    def tut_fahren(self, kmstand):
        print("Trabi hat bis jetzt", self.strecke, "km zurückgelegt")
        self.strecke += kmstand
        print("Trabi ist neuerdings", kmstand, "km gefahren")
        print("der jetzig erreichte KM_Stand beträgt:  ", self.strecke, ".")

    def tut_parken(self, parken = "zwischen zwei Autos"):
        print("Trabi kann außerdem schön", parken, "selbstständig parken")
        
trabi = Pkw("rot", 1981, 143000, 4, "Trabi")
trabi.tut_hupen(2)
trabi.tut_fahren(5000)
trabi.tut_fahren(15000)

trabi.tut_parken()

