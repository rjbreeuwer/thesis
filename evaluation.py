import os, time
import sys
import csv


def eval(sentence, index,sen,name):
    os.system("clear")
    if index == 0:
        os.system("clear")
        print("""INSTRUCTIONS - READ BEFORE YOU START

DISCLAIMER: This data is raw Reddit data, and may contain some profanity and
            possibly other offensive content. We have automatically filtered
            the blatant stuff, but due to it having to be a random sample we
            cannot remove everything. If you are not comfortable with this,
            please indicate you would rather not annotate.

Hi, thanks for participating in our evaluation! Below you will find a set of
reddit posts---some of them have been altered by an algorithm. You may assume all
sentences were written by speakers of the English language (though of varying
spelling and grammar mastery... it's Reddit after all). I would like you to answer 2 questions.

    - Does the sentence look, to you, like it was altered by an algorithm?
      (Choose: no or yes)
    - if so, please note -one- word that made you think this (even though
      there might be multiple).



(Scroll up!)(This is not the beginning of the text!)(Scroll up!)

If you're unsure, try to fill out something regardless. Note that there are
some special tokens including __ (such as __USER__), these are for
anonymization (@username) and are supposed to be there.



Here are some examples for a quick illustration. Given:

(1) trump likes for friendlier european wedding in poland .

Let's assume we think `wedding` looks like it might be changed. We type 'yes' for
changed and type the word: 'wedding'.



Another example:

(2) a skinned knee is a approve of a childhood well - lived .

`Approve` and `skinned` look out of place and make the sentence quite broken,
but we only note -one word-.


Final example:

these decisions will hurt 😭 , but success will soon come 🙌 🏽

(3) Finally! A sentence that looks in order. We note: 'no'

There are 80 sentences to rate; try not to take longer than 10-20 seconds per
sentence (for your own sake). Annotating should take about 20-30 min. Please
rate one sentence at a time.

So: algorithmically changed yes, or no, and if you think the sentence
was changed, note -one word- that's suspicious.
------------------------------------------------------------------""")
        wait = input(" Have you read everything? Press enter...")
    os.system("clear")
    index = index+1
    fp = open(f'answers-nina.txt', 'a')
    fp.write(str(sen))
    fp.write(",")
    if sen < 60:
        for x in range(100):
            ansq1 = question1(sentence, index)
            if ansq1 == 'no':
                fp.write('fout')
                fp.write('\n')
                break
            if ansq1 == 'yes':
                break

            if ansq1 != 'yes' or ansq1 != 'no':
                print("You didn't answer with yes or no!")
                time.sleep(3)
                os.system("clear")
                continue

        if ansq1 == 'yes':
            for x in range(100):
                w, l, lijst = question2(sentence,index)
                if w in lijst and len(l) == 1:
                    fp.write(w)
                    fp.write('\n')
                    break
                if w == '~.~' and len(l) == 1:
                    fp.write(w)
                    fp.write('\n')
                    break
                else:
                    print()
                    print("Word mistyped, not in sentence or multiple words are typed!")
                    time.sleep(4)
                    os.system("clear")
                    continue

    if sen >= 59:
        for x in range(100):
            ansq3 = question3(sentence, sen)
            if ansq3 == 'no':
                fp.write('goed')
                fp.write('\n')
                break
            if ansq3 == 'yes':
                fp.write('fout')
                fp.write('\n')
                break

            if ansq3 != 'yes' or ansq3 != 'no':
                print("You didn't answered with yes or no!")
                time.sleep(3)
                os.system("clear")
                continue

        if ansq3 == 'yes':
            for x in range(100):
                w, l, lijst = question4(sentence,sen)
                if w in lijst and len(l) == 1:
                    break
                if w == '~.~' and len(l) == 1:
                    break
                else:
                    print()
                    print("Word mistyped, not in sentence or multiple words are typed!")
                    time.sleep(4)
                    os.system("clear")
                    continue
    sen+=1

def question1(sentence,index):
    os.system("clear")
    print("\n\n\n")
    print(f'Sentence {index}:')
    sentence = sentence
    print("\n\n\n")
    print(sentence)
    print("\n\n")
    ans1 = input(" Is this text algorithmically changed? Answer with 'yes', or 'no':  ")
    print("\n\n")
    return ans1

def question2(sentence, index):
    os.system("clear")
    print("\n\n\n")
    print(f'Sentence {index}:')
    print("\n")
    sentence = sentence
    print(sentence)
    sentence = str(sentence)
    t = sentence.split()
    t.append("~.~")
    print("Do you think the sentence was changed, note -one word- that's suspicious? If you think no word is perturbed type: '~.~'")
    print('\n')
    print("Choose from the following answer: ","\n\n", t)
    print("\n\n")
    word = input("Type your answer here: ")
    splitted = word.split() ##waarom?
    return word, splitted, t

def question3(sentence,index):
    os.system("clear")
    print("\n\n\n")
    print(f'Sentence {index}:')
    print("\n\n\n")
    print(sentence)
    print("\n\n")
    ans1 = input(" Is this text algorithmically changed? Answer with 'yes', or 'no':  ")
    print("\n\n")
    return ans1

def question4(sentence,index):
    os.system("clear")
    print("\n\n\n")
    print(f'Sentence {index}:')
    print("\n")
    sentence = str(sentence)
    print(sentence)
    t = sentence.split()
    t.append("~.~")
    print("Do you think the sentence was changed, note -one word- that's suspicious? If you think no word is perturbed type: '~.~'")
    print('\n')
    print("Choose from the following answer: ","\n\n", t)
    print("\n\n")
    word = input("Type your answer here: ")
    splitted = word.split() ##waarom?
    return word, splitted, t

def main():
    file = open('medium_checked_sentences.txt', "r")
    #file = csv.reader(file)
    name = input("Type your name: ")
    for i,x in enumerate(file):
        eval(x, index=i,sen=i,name=name)
    print("\n\n\n\n\n\n\n\n\n")
    input("Thank you for you coorperation! Press enter to exit...")
    os.system("clear")

if __name__ == "__main__":
    main()
