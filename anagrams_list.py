
str = ['code', 'doce', 'ecod', 'framer', 'frame']
not_anagrams = []


def remove_anagrams_from_list(words):
    for i in range(len(words) - 1):
        for j in range(i+1, len(words)):
            if not is_anagrams(words[i], words[j]):
                if words[j] not in not_anagrams:
                    not_anagrams.append(words[j])

    return not_anagrams


def is_anagrams(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return str1_list == str2_list


if __name__ == '__main__':
    print(remove_anagrams_from_list(str))

