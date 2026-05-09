# Simulate the UPSC selection process with the following steps:
a=int(input("Enter your age in years :"))
if a>=21 and a<=32:
    print("you are eligible for upsc examination")
    b=int(input("Enter your prelims score :"))
    if b>=150:
        print("You are eligible for mains exam :")

        c=int(input("Enter your mains score :"))
        if c>=1000:
            print("You are eligible for Interview")

            d=int(input("Enter your interview marks:"))
            if d>=300:
                print("Congratulations, You have cleared the UPSC examination")
        
            else:
                print("Sorry, you just missed the chance")

        else:
            print("You failed in your mains examination")    
    else:
        print("Sorry, you are failed in prelims")
else:
    print("You are not eligible for upsc exam")

