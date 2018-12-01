def check_anagram(word1, word2):
    letter_to_occ = {}
    for letter in word1:
        try:
            letter_to_occ[letter] += 1
        except KeyError:
            letter_to_occ[letter] = 1
    for letter in word2:
        try:
            letter_to_occ[letter] -= 1
            if letter_to_occ[letter] < 0:
                return True
        except KeyError:
            return True
    for value in letter_to_occ.values():
        if value > 0:
            return True
    return False

def count_passphrases(filename):
    count = 0
    with open('input_file') as f:
        for line in f:
            words = line.strip().split()
            if len(set(words)) == len(words):
                valid = True
                for i in range(len(words) - 1):
                    if not valid:
                        break
                    for j in range(i+1, len(words)):
                        if not check_anagram(words[i], words[j]):
                            valid = False
                            break
                if valid:
                    count += 1
    return count

if __name__ == '__main__':
    print(count_passphrases('input_file'))
