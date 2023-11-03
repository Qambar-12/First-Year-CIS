""" Program : Quadratic Eq calculator """
def main():
    #INPUTS
    #Validation
    while True :
        a = float(input("a = "))
        if a == 0 :
            print("Invalid value\nPlease enter again")
            a = float(input("a = "))
            True
        else :
            break
    b = float(input("b = "))
    c = float(input("c = "))
    Discriminant = (b**2)-(4*a*c)
    #Importing math module to use square root function
    import math
    import fractions
    #Real and Distinct roots
    if Discriminant > 0 :
        X1 = (-b+math.sqrt(Discriminant))/(2*a)
        X2 = (-b-math.sqrt(Discriminant))/(2*a)
        print("Real and Distinct roots: ")
        print("X1 = ",X1,"= ",fractions.Fraction(X1),"\nX2 = ",X2,"= ",fractions.Fraction(X2))
    #Real and Equal roots
    elif Discriminant == 0 :
        X = (-b+math.sqrt(Discriminant))/(2*a)
        print("Real and equal roots: ")
        print("X1 = ",X,"= ",fractions.Fraction(X),"\nX2 = ",X,"= ",fractions.Fraction(X))
    #Complex or imaginary roots
    else :
        Den = 2*a
        Discriminant *= -1
        Real_part = -b/Den
        Imag_part = math.sqrt(Discriminant)/Den
        X1 = str(Real_part)+'+'+str(Imag_part)+'i'
        X2 = str(Real_part)+'-'+str(Imag_part)+'i'
        print("Complex or imaginary roots: ")
        print("X1 = ",X1,"\nX2 = ",X2)

if __name__ == "__main__":
    main()
    
    
