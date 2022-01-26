# bearrobotics-codetest

##main function : BankSystem()

Through 'BankSystem()', ATM identifies inserted intention(or card), checks the PIN number, and allows user's order(see balance, deposit, withdraw) for correct PIN number.
To make ATM doesn't know exact pin number, I defined two function 'checkpin()' and 'loadbankaccount()'.

##checkpin(num,id)
num refers to the correct PIN number of inserted card. For this code test, I randonmly chose the number as '1234'. So to run my code, please enter '1234' as a correct pin number. For the future development, it is preferable to modify this function to identify pin number of differenct card(or card id). For the assurance of safety, main function 'BankSystem()' calls 'checkpin()' so that ATM only transfers entered PIN number and receives corresponding bool value (true of false) so that ATM doesn't remember, store, or recognize the correct PIN number.

##other functions: loadbankaccount(num), showbankaccount(cardid), whichwork(banknum, cardid)
these three functions are declared to make the code easir to be understood and to make the main function 'BankSystem()' short and complete.

##bankforcardid1
this list is the data contains information of card with card id 1(randonmly chosen). For the convenience, I chosed two bank account from 'bank of america' as a default. Since this project is focused on the controller and ATM system, not a bank account management system, bankforcadid1 data can be modified in the future for the real-world implementation.
