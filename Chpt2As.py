#Brian K Burnett Jr 09.07.2025

import math
import pandas as pd

print('\nContinental Currency Converter\n')

def main():
    print('Welcom to the Eastern Hemisphere momney trading center.\n')

    #Shows differences in worth throughout the years
    print('This is the data correlation of our currency options throughout the years\n')

    df = pd.DataFrame({         

        'USD to Country Currency': [1066.12,0.8004,26.50,1179.40,0.74,24.01,], #TODO: get 6

        'Name': ['2018']*2 + ['2020']*2 +['2025']*2,

        'Countries': ['South Korea 🇰🇷', 'United Kingdom 🇬🇧', 'Cuba 🇨🇺']*2

    })

    print(df)

    print("")

    #The input function asks user to choose money amount in US Dollars.

    us_dollars = float(input('Enter the amount of money you want to contribute: '))


    currency = input('Which currnecy would you like to trade your USD with? (GBP, KRW, CUP): ')

    #Takes US dollar value that the user inputs and convert to different regional currencies.
    british_pounds = (us_dollars * 0.741316)

    south_korean_won = (us_dollars * 1386.8777)

    cuban_pesos = (us_dollars * 23.99297)

    if currency == 'GBP':
        return print(f"British Pounds 🇬🇧: {british_pounds:.2f}")  #Outputs y which is the currencies with 2 decimal places.

    elif currency == 'KRW':
        return print(f"South Korean Won 🇰🇷: {south_korean_won:.2f}")

    elif currency == 'CUP':
        return print(f"Cuban Pesos 🇨🇺: {cuban_pesos:.2f}")

    else:
        print('Invalid currency. Please choose GBP, CUP, or KRW.')
        return
main()

def tr():
    print('\nMoney transfer complete!') #Shows that the process is done.

    #ASCII Art
    print('                 ___                  ')
    print('  ___======____=---=)                 ')
    print('/T             \_--===)               ')
    print('[ \ (0)    \~    \_-==)               ')
    print(' \       / )J~~    \-=)               ')
    print('  \ \___/  )JJ~~~   \)                ')
    print('   \_____/JJJ~~~~     \               ')
    print('   / \  , \J~~~~~      \              ')
    print('  (-\)\=|\\\~~~~        L__           ')
    print('  (\\)  (\\\)_            \==__       ')
    print('   \V   \\\) ===_____     \\\\\\      ')
    print('          \V)    \_)  \\\\JJ\J\)      ')
    print('                      /J\JT\JJJJ)     ')
    print(r'                      (JJJ| \UUU)     ')
    print('                       (UU)           \n')
tr()