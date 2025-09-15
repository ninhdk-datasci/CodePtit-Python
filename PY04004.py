class Fraction: 
    def __init__(self, numerator, denominator): 
        self.numerator = numerator 
        self.denominator = denominator 
    @staticmethod
    def GCD(a, b): 
        if(b == 0): return a + b 
        return Fraction.GCD(b, a%b)
    @staticmethod
    def LCM(a, b): 
        gcd = Fraction.GCD(a, b)
        return (a*b) // gcd
    @staticmethod
    def add(frac1, frac2): 
        lcm = Fraction.LCM(frac1.denominator, frac2.denominator)

        new_numerator = frac1.numerator*(lcm//frac1.denominator) + frac2.numerator*(lcm//frac2.denominator)

        gcd = Fraction.GCD(new_numerator, lcm) 
        
        return f"{new_numerator//gcd}/{lcm//gcd}"


class FirstFraction(Fraction):
    def __init__(self, numerator, denominator):
        super().__init__(
            numerator, denominator
        )
class SecondFraction(Fraction):
    def __init__(self,numerator, denominator): 
        super().__init__(
            numerator, denominator
        )

numerator1, denominator1, numerator2, denominator2 = map(int, input().split())

p = FirstFraction(numerator1, denominator1)
q = FirstFraction(numerator2, denominator2)

print(Fraction.add(p,q))
