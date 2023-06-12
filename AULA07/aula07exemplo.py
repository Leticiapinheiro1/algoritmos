for i in range(5):
    if i == 0:
        print('\ni = 0, Então: ', i)
    elif i == 1:
        print('\ni = 1, Então: continue')
        continue
    elif 1 < i < 3:
        print('\nA variável i, é: ', i)
    elif i == 3:
        print('\ni = 3, Então: break')
        break
    else:
        print('\ni > 3, Então: ', i) 
