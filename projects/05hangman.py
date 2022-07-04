#!bin/bash/python

import random
import os

WORDS = [
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'daiquiri',
    'dirndl',
    'disavow',
    'dizzying',
    'duplex',
    'dwarves',
    'embezzle',
    'equip',
    'espionage',
    'euouae',
    'exodus',
    'faking',
    'fishhook',
    'fixable',
    'fjord',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'frizzled',
    'fuchsia',
    'funny',
    'gabby',
    'galaxy',
    'galvanize',
    'gazebo',
    'giaour',
    'gizmo',
    'glowworm',
    'glyph',
    'gnarly',
    'gnostic',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jaywalk',
    'jazziest',
    'jazzy',
    'jelly',
    'jigsaw',
    'jinx',
    'jiujitsu',
    'jockey',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'klutz',
    'knapsack',
    'larynx',
    'lengths',
    'lucky',
    'luxury',
    'lymph',
    'marquis',
    'matrix',
    'megahertz',
    'microwave',
    'mnemonic',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numbskull',
    'nymph',
    'onyx',
    'ovary',
    'oxidize',
    'oxygen',
    'pajama',
    'peekaboo',
    'phlegm',
    'pixel',
    'pizazz',
    'pneumonia',
    'polka',
    'pshaw',
    'psyche',
    'puppy',
    'puzzling',
    'quartz',
    'queue',
    'quips',
    'quixotic',
    'quiz',
    'quizzes',
    'quorum',
    'razzmatazz',
    'rhubarb',
    'rhythm',
    'rickshaw',
    'schnapps',
    'scratch',
    'shiv',
    'snazzy',
    'sphinx',
    'spritz',
    'squawk',
    'staff',
    'strength',
    'strengths',
    'stretch',
    'stronghold',
    'stymied',
    'subway',
    'swivel',
    'syndrome',
    'thriftless',
    'thumbscrew',
    'topaz',
    'transcript',
    'transgress',
    'transplant',
    'triphthong',
    'twelfth',
    'twelfths',
    'unknown',
    'unworthy',
    'unzip',
    'uptown',
    'vaporize',
    'vixen',
    'vodka',
    'voodoo',
    'vortex',
    'voyeurism',
    'walkway',
    'waltz',
    'wave',
    'wavy',
    'waxy',
    'wellspring',
    'wheezy',
    'whiskey',
    'whizzing',
    'whomever',
    'wimpy',
    'witchcraft',
    'wizard',
    'woozy',
    'wristwatch',
    'wyvern',
    'xylophone',
    'yachtsman',
    'yippee',
    'yoked',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zigzagging',
    'zilch',
    'zipper',
    'zodiac',
    'zombie',
]


def getWord():
    return random.choice(WORDS)


def displayMan(numFails):
    if numFails == 0:
        print(u'\u250C\u2500\u2510')
        print(u'\u2502')
        print(u'\u2502')
        print(u'\u2502')
        print(u'\u2534')
    elif numFails == 1:
        print(u'\u250C\u2500\u2510')
        print(u'\u2502 O')
        print(u'\u2502')
        print(u'\u2502')
        print(u'\u2534')
    elif numFails == 2:
        print(u'\u250C\u2500\u2510')
        print(u'\u2502 O')
        print(u'\u2502 |')
        print(u'\u2502')
        print(u'\u2534')
    elif numFails == 3:
        print(u'\u250C\u2500\u2510')
        print(u'\u2502 O')
        print(u'\u2502/|')
        print(u'\u2502')
        print(u'\u2534')
    elif numFails == 4:
        print(u'\u250C\u2500\u2510')
        print(u'\u2502 O')
        print(u'\u2502/|\\')
        print(u'\u2502')
        print(u'\u2534')
    elif numFails == 5:
        print(u'\u250C\u2500\u2510')
        print(u'\u2502 O')
        print(u'\u2502/|\\')
        print(u'\u2502/')
        print(u'\u2534')
    else:
        print(u'\u250C\u2500\u2510')
        print(u'\u2502 O')
        print(u'\u2502/|\\')
        print(u'\u2502/ \\')
        print(u'\u2534')


def checkLetter(letter, word):
    indicies = []
    letters = [i for i in letter]
    for index, let in enumerate(word):
        if let in letters:
            indicies.append(index)
    if len(indicies) > 0:
        return True
    else:
        return False


def drawWordLine(word, guessed):
    wordLine = ''
    for letter in word:
        if letter in guessed:
            wordLine += f"{letter} "
        else:
            wordLine += '_ '
    return wordLine


def main():
    def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
    solved = False
    guesses = []
    incorrectGuesses = []
    correctGuesses = []
    print('Welcome to hangman v1.0!')
    print('Note: Guessing multiple letters will not check the individual letters, only if you guessed the word correctly.')
    word = random.choice(WORDS)
    while not solved and len(incorrectGuesses) < 6:
        wordLine = drawWordLine(word, correctGuesses)
        if '_' not in wordLine:
            solved = True
        else:
            displayMan(len(incorrectGuesses))
            print(wordLine)
            if len(incorrectGuesses) > 0:
                print(f'Incorrect guesses: {" ".join(incorrectGuesses)}')
            guess = input('Guess a single letter or the whole word: ')
            if guess == word:
                solved = True
            elif len(guess) > 1 and guess != word:
                incorrectGuesses.append(guess)
            elif guess in guesses:
                print('You have already guessed that letter.')
            else:
                guesses.append(guess)
                if checkLetter(guess, word):
                    correctGuesses.append(guess)
                else:
                    incorrectGuesses.append(guess)
        clear()
    if solved:
        print(f'Congratulations! The word was \'{word}\'. You guessed it!')
    else:
        displayMan(incorrectGuesses)
        print(f'You have lost. The word was \'{word}\'')


if __name__ == '__main__':
    main()
