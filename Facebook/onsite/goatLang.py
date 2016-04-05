# coding=utf-8
def goatLang(line):
    '''
    规则：
        1. vowel 开头的单词，要在单词后面加 ma
        2. consonant 开头的单词，把这个 consonant 移动到单词末尾。
        3. 所有的单词末尾都要加上一个 String，这个 String 在第一个单词后面是 a，第二个单词后面是 aa，以此类推。
        ex：
                I speak Goat Latin -> Imaa peaksaa oatGaaa atinLaaaa
    :return:
    '''
    words = line.split()
    surfix = 'a'
    res = []
    vowel = ['A', 'E', 'I', 'O', 'U']
    for word in words:
        word = word.strip()
        if word[0] in vowel:
            word += 'ma'
            word += surfix
        else:
            word = word[1:] + word[0] + surfix
        res.append(word)
        surfix += 'a'
    return ' '.join(res)

print goatLang('I speak Goat Latin')