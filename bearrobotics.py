
'''(출력) 카드 입력? > (입력) 0 1
0 > insert please
1 > 
(출력) what is your pin number?  > (입력)
틀리면 -> (함수 호출) (함수1)wrong pin number!
맞으면 -> (함수 호출) (함수2)뱅크 계좌 보여주기 (1~n 보여주고 입력 받기)

각 숫자 클릭 -> (함수 호출) (함수3) 무엇을할 것인지 물어보기 (잔액보기, 인출, 저장  1~3) (입력받기)
1-> (함수 호출)(함수 4) 잔액보여주기
2-> (함수 호출)(함수 5) 얼마 넣을 것인지? (입력받기) (함수4)잔액 보여주기 종료
3-> (함수 호출)(함수 6) 얼마 뺄 것인지? (입력받기) (함수4) 잔액보여주기 종료'''

#ATM won't know the pin number but only the number is correct or not!
bankforcardid1=[["BoA1", 1000],["BoA2", 2000]]
def checkpin(num, id):
    if id == 1 : 
        if num == "1234":  #randomly selected correct PIN number of card
            return True
        else:
            return False
    else:     #code space for different card id in future
        return False

def loadbankaccount(num):  #load bank account corresponding to cardid
    return bankforcardid1
def showbankaccount(cardid):
    acnt = loadbankaccount(cardid)
    print("1. account id : {}".format(acnt[0][0]))
    print("2. account id : {}".format(acnt[1][0]))   
def whichwork(banknum, cardid):
    acnt = loadbankaccount(cardid)
    inpt = input("which work? press button (1: see balance, 2: deposit, 3: withdraw) :  ")
    while(True):
        if (inpt == "1"):
            print("balance of {0} : {1}".format(acnt[int(banknum)-1][0],acnt[int(banknum)-1][1]))
            inpt = input("further work? press button (1: see balance, 2: deposit, 3: withdraw, 4: no) :  ")
        elif (inpt == "2"):
            deposit = input("how much money deposit? : ")
            acnt[int(banknum)-1][1]+=int(deposit)
            print("balance of {0} : {1}".format(acnt[int(banknum)-1][0],acnt[int(banknum)-1][1]))
            inpt = input("further work? press button (1: see balance, 2: deposit, 3: withdraw, 4: no) :  ")
        elif (inpt == "3"):
            withdraw = input("how much money withdraw? : ")
            if(acnt[int(banknum)-1][1]<int(withdraw)):
                print("Insufficient balance!")
            else:
                acnt[int(banknum)-1][1]-=int(withdraw)
            print("balance of {0} : {1}".format(acnt[int(banknum)-1][0],acnt[int(banknum)-1][1]))
            inpt = input("further work? press button (1: see balance, 2: deposit, 3: withdraw, 4: no) :  ")        
        else:
            print("wrong button!")
        
        if(inpt == "4"): 
            print("thank you for using bearrobitics ATM!") 
            break
        elif(inpt != "1" and inpt != "2" and inpt != "3"):
            print("wrong button!")

        
def BankSystem():
    while(True):
        num = input("insert card? press button (1: yes, 2: no) :  ")
        if (num == "2"): 
            print("thank you for using bearrobitics ATM!")
            break
        elif (num == "1"):
            cardid = 1 #randomly selected card ID
            pin = input("enter your 4-digit  PIN number :  ")    #randomly selected PIN number as 4-digit number
            while(True):
                if (checkpin(pin, cardid) == False):
                    print("wrong PIN number!")
                    pin = input("enter your 4-digit  PIN number :  ")    #randomly selected PIN number as 4-digit number
                else: 
                    showbankaccount(cardid)
                    while(True):    
                        banknum = input("which account? :  ")
                        if (banknum == "1" or banknum == "2"):
                            whichwork(banknum, cardid)
                            break
                        else:
                            print("wrong bank choice!")
                    break            
            break        
        
        #wrong input note
        else: print("wrong button!")
BankSystem()