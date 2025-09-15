class Fraction: 
    def __init__(self, numerator:int, denominator:int): 
        self.numerator = numerator 
        self.denominator = denominator 

    @staticmethod
    def GCD(a:int, b:int):
        if(b==0): return a + b 
        return Fraction.GCD(b, a%b)
    def newFraction(self):
        gcd = Fraction.GCD(self.numerator, self.denominator)
        new_numerator = self.numerator // gcd 
        new_denominator = self.denominator // gcd 
        return f"{new_numerator}/{new_denominator}"
    
numerator, denominator = map(int, input().split())

frac = Fraction(numerator, denominator)
print(frac.newFraction()) 

