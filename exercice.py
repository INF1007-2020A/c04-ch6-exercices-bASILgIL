#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        valeurs = []
        while len(valeurs) < 10:
            valeurs.append(input("Entrez une seule valeur \n"))
            sorted_list = sorted(valeurs)
    return sorted_list


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        mots = []
        while len(mots) < 2:
            mots.append(input("Entrez un mot \n"))

    return sorted(mots[0]) == sorted(mots[1])


def contains_doubles(items: list) -> bool:
    ensemble = set(items)

    return len(items) != len(ensemble)


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = dict()
    for key, value in student_grades.items():
        avg = sum(value)/len(value)
        if len(best_student) == 0 or list(best_student.values())[0] < avg:
            best_student = {key: avg}

    return best_student


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    frequency = dict()
    for letter in sentence:
        frequency[letter] = sentence.count(letter)
        sorted_keys = sorted(frequency, key=frequency.__getitem__, reverse=True)
        for key in sorted_keys:
            if frequency[key] > 5:
                print(f"Le caractere {key} revient {frequency[key]} fois.")

    return frequency


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
