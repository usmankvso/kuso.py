print('Here are the available bank USSD codes: \n1. Access Bank: *901#, \n2. Uba Bank: *919#, \n3. Union Bank: *826, \n4. Zenith bank: *966# ')
ussd = input('\nPlease type in your banks USSD code: ')
if(ussd == '*919#'):
    print('\nYou have selected Uba Bank USSD code \n ')
def menu():
    option = int(input('1. Airtime \n2. Transfers\n3. Check your Balance\n4. Transaction History\n\nPlease select an option: '))
    if(option == 1):
        choice = int(input('\n1. for self\n2. for others\n            :'))
        if(choice == 1):
            amount = (input('Enter amount: '))
            print('Transaction successful\n')
            main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END\n: '))
            if(main == 1):
                menu()
            elif(main == 2):
                exit()
            else:
                print('input error!')
        elif(choice == 2):
            amount=(input('Enter amount: '))
            number = input('Enter the phone number you want to buy airtime for: ')
            compilation = 'Do you want to buy '+ amount+ ' naira worth of airtime for '+ number+'?: \n1. Yes\n2. No\n'
            assure = int(input(compilation))
            if(assure == 1):
                print('Transaction successful')
                main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
                if(main == 1):
                    menu()
                elif(main == 2):
                    exit()
                else:
                    print('input error!')
            elif(assure == 2):
                print('Transaction cancelled')
                main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
                if(main == 1):
                    menu()
                elif(main == 2):
                    exit()
                else:
                    print('input error!')
            else:
                print('invalid input')        
       
    elif(option == 2):
        num = input('Enter the Account number you want to transfer the money to: ')
        amount = input('Enter amount: ')
        pin = input('Enter your four digits pin: ')
        compilation = 'Do you want to send ' +amount+'to this account number: '+ num+'?\n1. Yes\n2. No\n:'
        assure = input(compilation)
        if(assure == '1'):
            print('Transaction successful')
            main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
            if(main == 1):
                menu()
            elif(main == 2):
                exit()
            else:
                print('input error!')            
        elif(assure == '2'):
            print('transanction cancelled')
            main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END: '))
            if(main == 1):
                menu()
            elif(main == 2):
                exit()
            else:
                print('input error!')
    elif(option == 3):
        print('\nYour Account Balance is: 10000000 Naira\n')
        main = int(input('ENTER 1 TO RETURN TO MENU\nENTER 2 TO END\n\n: '))
        if(main == 1):
            menu()
        elif(main == 2):
            exit()
        else:
            print('input error!')        
    elif(option == 4):
        print('You will receive an SMS shortly')
if(ussd == '*919#'):
    menu()
else:
    print('wrong input')