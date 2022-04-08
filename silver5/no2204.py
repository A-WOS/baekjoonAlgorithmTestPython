while True:
    N = int(input())
    if N == 0:
        break
    else:
        words = []
        for _ in range(N):
            word = input()
            change_word = word.lower()
            words.append([change_word, word])
        print(min(sorted(words))[1])