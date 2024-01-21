def minion_game(string):
    Stuart_pts, Kevin_pts, f_count, s_count, words = 0, 0, 0, 0, 0
    word_combos = []
    vowels = "AEIOU"
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"

    # Gather and Evaluate the word occurences for Stuart
    # print("Occurences found for Stuart: ")
    while (f_count <= len(consonants)-1):
        select_letter = string.find(consonants[f_count])
        if select_letter >= 0:
            for end_pos in range(1, len(string)+1):
                letter_combo = string[select_letter:select_letter+end_pos]
                if letter_combo in word_combos:
                    continue
                else:
                    words+=1
                    # print("Word #" + str(words) + ": " + str(letter_combo) + " ("+ str(string.count(letter_combo)) +")")
                    Stuart_pts = Stuart_pts + string.count(letter_combo)
                    word_combos.append(letter_combo)
        f_count += 1
    # print("Stuart has " + str(Stuart_pts) + " Points!")

    words = words - words

    # Gather and Evaluate the word occurences for Kevin
    # print("Occurences found for Kevin: ")
    while (s_count <= len(vowels)-1):
        select_letter = string.find(vowels[s_count])
        if select_letter >= 0:
            for end_pos in range(1, len(string)+1):
                letter_combo = string[select_letter:select_letter+end_pos]
                if letter_combo in word_combos:
                    continue
                else:
                    words+=1
                    # print("Word #" + str(words) + ": " + str(letter_combo) + " ("+ str(string.count(letter_combo)) +")")
                    Kevin_pts = Kevin_pts + string.count(letter_combo)
                    word_combos.append(letter_combo)
        s_count += 1
    # print("Kevin has " + str(Kevin_pts) + " Points!")

    if string.isupper() is False:
        return print("Not fully capitalized: " + string)
    elif Stuart_pts > Kevin_pts:
        return print("Stuart " + str(Stuart_pts))
    else:
        return print("Kevin " + str(Kevin_pts))

if __name__ == '__main__':
    s = input()
    minion_game(s)
