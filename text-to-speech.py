import pyttsx3
# engine = pyttsx3.init()
# engine.say('hai how are you')
# engine.runAndWait()

n = input('Enter a number ')
dic = {
    '1': 'ones',
    '2': 'twos',
    '3': 'threes',
    '4': 'fours',
    '5': 'fives',
    '6': 'sixes',
    '7': 'sevens',
    '8': 'eights',
    '9': 'nines',
    '10': 'tens'
}
dic2 = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'sixe',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten'
}
txt = ''
for i in range(1,11):
    mul = i*int(n)
    if i==1:
        txt += str(i) + ' ' + dic2[n] + ' is ' + str(mul) + '\n'
    else:
        txt += str(i) + " " + dic[n] + " are " + str(mul) + "\n"

print(txt)

engine = pyttsx3.init()
engine.say(txt)
engine.runAndWait()