# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string


class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)
        list1 = self.user_input.split()
        print(list1)

        # first scramble is just one word
        i = 0
        printc = 0
        # end = len(self.user_input)
        end = len(list1)
        j = end
        # for count in self.user_input:
        #     print(self.user_input[i])
        #     printc += 1
        #     if printc >= end - 1:
        #         print(self.user_input[-1])
        #         break
        #     print(self.user_input[j - 2])
        #     printc += 1
        #     if printc >= end - 1:
        #         print(self.user_input[-1])
        #         break
        #     j -= 1
        #     i += 1
        for count in list1[0]:
            print(list1[0][i])
            printc += 1
            if printc >= end - 1:
                print(list1[0][-1])
                break
            print(list1[0][j - 2])
            printc += 1
            if printc >= end - 1:
                print(list1[0][-1])
                break
            j -= 1
            i += 1

        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3

        # now try to scramble one sentence
        # user_list = list(self.user_input)
        #
        # print(user_list)

        # do just words first, then you can move on to work on
        # punctuation


word_scrambler = WordScramble()
word_scrambler.scramble()
