from lvl import *
import time

score = 0
nl2 = False

input = input('\nPress "a" to start\n')

if input == 'a':
    t1 = time.perf_counter()
    print('\n= Level 1 =\n')

    for i in range(0, 5):
        fct = lvl1()
        if fct == True:
            score += 1
        else:
            print('Game over... score = ' + str(score) + '/5\n')
            time.sleep(5)
            break

    if score == 5:
        print('Level 1 completed.\n')
        time.sleep(1)
        nl2 = True

    if nl2 == True:

        print('== Level 2 ==\n')

        for i in range(0, 5):
            fct = lvl2()
            if fct == True:
                score += 1
            else:
                print('Game over... score = ' + str(score) + '/10\n')
                time.sleep(5)
                break

        if score == 10:
            print('Level 2 completed.\n')
            time.sleep(1)
            nl3 = True

        if nl3 == True:
            print('=== Level 3 ===\n')
            time.sleep(2)

            for i in range (0, 5):
                fct = lvl3()
                t = time.perf_counter()
                if fct == True:
                    score += 1
                else:
                    print('Game over... score = ' + str(score) + '/10\n')
                    time.sleep(5)
                    break

            if score == 15:
                print('Level 3 completed.\n')
                time.sleep(3)
                print('Well done !')