def tasklist():

    tasklist = []
    while True:
        print('Чтобы добавить задачу, напишите "+ [ваша задача]"')
        print('Чтобы пометить задачу выполненной, напишите "- [номер задачи в списке]"')
        print('Чтобы полностью очистить список, напишие clear')
        print("Чтобы завершить действие программы, напишите stop")
        if tasklist == []:
            print('Текущий список пуст.')
        else:
            for i in range(0, len(tasklist)):
                print(i + 1, ': ', tasklist[i])
        
        choice = input()
        if choice == 'stop':
            print('Сворачиваемся.')
            break
        else:
            if choice == 'clear':
                print("Список очищен")
                tasklist.clear()
            else:
                result = choice.split(' ', 1)
                if result[0] == '+':
                    tasklist.append(result[1])
                elif result[0] == '-':
                    print('Задача №', int(result[1]) + 1, ' выполнена')
                    tasklist.pop(int(result[1]) - 1)
                else:
                    print('Еще раз посмотрите в инструкцию.')

tasklist()