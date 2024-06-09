def is_valid(attempt, a = 1, b = 100):
    '''проверяет число на инвалидность. возвразает TRUE, если введено число в заданном диапазоне, FALSE в обратном случае'''
    return attempt.isdigit() and a <= int(attempt) <= b

def game(a = 1 , b = 100):
    '''сама игра. возвращает TRUE при победе/проигрыше/сдаче, FALSE при введении "zaebal"'''
    import random
    from math import ceil, log2 
    n = random.randint(a, b)
    #print('podskazka:', n)     
    attempt = input('попробуйте угадать целое число от {} до {}{}'.format(a, b, '\n'))
    i = 0
    popitki = ceil(log2(b - a))    #количество траев по бп
    if popitki < 3:
        popitki += 1
    while i < popitki - 1:
        if attempt == 'zaebal':                         
            return False 
        elif attempt == 'gg':
            print('-' * 100) 
            print('Наруто учил никогда не сдаваться, правильным ответом было число', n)
            print('-' * 100) 
            return True    
        elif  is_valid(attempt, a, b):    
            i += 1
            print('\n', 'попытка номер: ' , i, ' остплось попыток: ', popitki - i, sep = '')
            if int(attempt) != n:
                if int(attempt) < n:
                    attempt = input('не повезло, попробуйте ещё разок с числом ПОБОЛЬШЕ +{}'.format('\n'))
                else:
                    attempt = input('не повезло, попробуйте ещё разок с числом ПОМЕНЬШЕ -{}'.format('\n'))
            else:        
                print('*' * 100)
                print('ЛЕГЕНДА!')
                print('вам потребовалось поыток:', i, 'из', popitki)
                print('*' * 100)
                return True                                      
        else:
            attempt = input('чёт не то введено, попробуйте ещё раз...{}'.format('\n'))
    if int(attempt) != n:         
        print('=( ' * 33)        
        print('вы(лох) проиграли, загадано было:', n, 'лимит попыток:', popitki)
        print('=( ' * 33)
    else:
        print('*' * 100)
        print('еле успел, но всё равно ЛЕГЕНДА!')
        print('вам потребовалось поыток:', i + 1, 'из', popitki)
        print('*' * 100)
    return True

def mb_enother():
    '''предлагает сыграть ещё раз и задать диапазон самостоятельно. возвращает FALSE при отказе играть и TRUE при согласии'''            
    print('хотите поиграть ещё раз? ответ ""yes"" сгенерирует для вас новое число')
    if input().lower() == 'yes':
        return True
    else:
        return False
    
def range_creator():
    '''создаёт пользовательский диапазон. запускает GAME с этим диапазоном'''    
    print('теперь вы можете выбрать границы в которых хотите искать число')
    while True:        
        a = input('введите НИЖНЮЮ границу{}'.format('\n'))        
        b = input('введите ВЕРХНЮЮ границу{}'.format('\n'))        
        if a.isdigit() and b.isdigit() and int(a) < int(b):
            return game(int(a), int(b))    #запуск игры в цикле                                                                                          
        else:
            print('!' * 100)
            print('границы должны быть целыми числами, нижняя < верхней')
            print('!' * 100)
            continue 

print('добро пожаловать в игру. мы тут угадывем числа.')
print('---если наигрались, напишите "zaebal"')
print('---если не получается угадать число, напишите "gg"')
print('-' * 100)

if game():
    while True:
        if mb_enother():
            range_creator()
            continue                            
        else:
            break            
print('-' * 100)
print('уверен, что тебе было очень веселою до встречи в игре!')
print('-' * 100)   
