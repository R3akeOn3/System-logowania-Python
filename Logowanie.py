# Wykonane przez: https://github.com/R3akeOn3/System-logowania-Python.git 
# Logowanie
Default_Username = input('- Podaj Nazwe uzytkownika: ')
print(' = = - -  -')
Default_Password = input('- Podaj Hasło uzytkownika: ')
# Uzytkownicy 
Users = ['ReakeOne', 'Haslo123']
# Rangi Admin i Klient
Rangi = ['Admin', 'Klient']
#Sprawdzanie czy dane są Prawidłowe
if Default_Username == Users[0] and Default_Password == Users[1]:
    print(f'Zalogowano jako {Default_Username} {Rangi[0]}')
else:
    print(f'Nieprawidlowe dane logowania')