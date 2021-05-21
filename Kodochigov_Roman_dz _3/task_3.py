thesaurus_dict = {}


def thesaurus(*argv):
    names = []
    for name in argv:
        names.append(name)
    names.sort()
    for name in names:
        if name[0] in thesaurus_dict:
            thesaurus_dict[name[0]].append(name)
        else:
            thesaurus_dict[name[0]] = [name]


thesaurus("Павел", "Марфа", "Ульяна", "Иван", "Мария", "Петр", "Илья", "Роман", "Елена")
print(thesaurus_dict)
