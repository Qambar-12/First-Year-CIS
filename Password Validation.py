#Docstring
""" Program : Password validation
    Author  : Qambar """
def main():
    password = str(input("Enter your password: "))
    Digits = ['0','1','2','3','4','5','6','7','8','9']
    Special_char = ['~','!','@','#','$','%','^','&','*','(',')','[',']','_','{','}','"',';',':','/','\'|','.',',','?','`',' ',"'",'+','-','=']
    #Length check   
    def lenCheck(password):
       while len(password) < 7 or len(password) > 15 :
           password = str(input("Passwords must have length in b/w 7 and 15\nPassword: "))
    lenCheck(password)       
    #Numeric Value check
    def numCheck(password,Digits):
        x = True
        while x == True:
            for char in password :
                for D in Digits :
                    if D == char :
                        x = False
            if x == True :
                password = str(input("Password must have a numeric digit\nPassword: "))
                lenCheck(password)
                numCheck(password,Digits)
            else :
                pass
            break    
    numCheck(password,Digits)
    #Special character check       
    def specialCheck(password,Special_char):
        x = True
        while x == True :
            for char in password :
                for Sc in Special_char :
                    if Sc == char :
                       x = False
            if x == True :
                 password = str(input("Password must also have a special character\nPassword: "))
                 lenCheck(password)
                 numCheck(password,Digits)
                 specialCheck(password,Special_char)
            else :
                 pass
            break    
    specialCheck(password,Special_char)                    
    print("Password is valid")                              
if __name__ == "__main__":
    main()
