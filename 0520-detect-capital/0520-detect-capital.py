class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if len(word) == 1 or not word:
            return True

        capitals = 0
        flag = False

        for i in range(len(word)):
            if i == 0:
                if word[i].isupper():
                    flag = True
                    capitals += 1
            else:
                if word[i].isupper():
                    capitals += 1
                    if not flag:
                        return False
                    if flag:
                        if capitals != i + 1 and capitals != 1:
                            print(capitals,i+1)
                            return False   
                else:
                    if flag and capitals != 1:
                        return False
        return True
