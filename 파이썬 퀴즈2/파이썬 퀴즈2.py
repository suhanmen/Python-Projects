#픽맨 게임 만들기
'''
#무작위로 선택할 단어를 선택한다
import random
a = ['apple', 'banana', 'orange']
b = random.choice(a)
c = []

print(b)

#선택된 단어만큼 _를 list에 추가한다
for i in range(len(b)):
    c += '_'

print(c)

#사용자로부터 단어를 입력 받아서 맞는 단어가 있으면 그 자리에 넣어준다.
d = len(b)
e = []
while d > 0:
    ip = input('사용자로부터 1글자씩 입력 : ')
    if ip in b:
        print('Correct')
        i = 0
        while b.find(ip,i) != -1:
            e.append(b.find(ip,i))
            i += 1
        d -= len(e)

        for i in range(len(e)):
            c.insert(ip,e[i])
        print(c)
    else:
        print('Wrong')

print('Success')
'''

#답안지
import random
words = ['apple', 'banana', 'orange']
word = random.choice(words)
print('answer : ' + word)
letters = ""

while True:
    succeed = True
    print()
    for i in word:
        if i in letters:
            print(i, end = ' ')
        else:
            print('_', end = ' ')
            succeed = False
    print()

    if succeed:
        print('Success')
        break

    letter = input('사용자로부터 입력 : ')
    if letter not in letters:
        letters += letter

    if letter in word:
        print('Correct')
    else:
        print('Wrong')

'''주의할점은 단어를 빈칸에 넣을때 list로 하는 복잡함을 하지말고
문자열이 더 좋다. 그리고 검사를 할때 단어를 하나씩 대입해서 같은게 있으면 보이면 좋다.'''












