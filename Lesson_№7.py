def namazivanie(func):
    def tomato():
        print("Намазываю масло на")
        func()
        print("Кладу ломтик помидора на")
        func()
        print("Кладу ломтик сыра на")
        func()

    return tomato


def propusk(func):
    def buterbrod():
        func()
        print(' ')

    return buterbrod


@namazivanie
@propusk
def bread():
    print('Хлеб')


bread()

Recept = ['Maslo', 'Pomidor', 'Cbip']

print(map(str.upper, Recept))
print(list(map(str.upper, Recept)))

resultat = lambda x: list(map(str.upper, x))

print(resultat)