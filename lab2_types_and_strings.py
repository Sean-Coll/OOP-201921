# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 29-09-2019
# purpose: Lab 2
from os import remove


class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+message)

        # print only first and last of the sentence
        # print(message[0])
        # print(message[-1])

        # use slice notation
        # print(message[0:1])
        # print(message[-1:])

        # escaping a character
        # print("He said \"that\'s fantastic\"!")

        # find all a's in the input word and count how many there are
        # print("The first occurrence of \'a\' is at position:")
        # print(message .find('a'))
        # print("The number of \'a\'s are:")
        # print(message .count('a'))
        # print(len(message))

        # replace all occurrence of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace()
        # message[3] = '-' This is not supported
        # print(message .replace('a','-'))

        # printing only characters at even index positions
        # print(message [::2])

    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+message)

        # hand the input string to a list and print it out
        list1 = list(message)
        print(list1)

        # append a new element to the list and print
        # list1.append('!')
        # print(list1)

        # remove from the list in 3 ways
        # del list1[3]
        # print(list1)
        # letter = (list1.pop(2))
        # print(letter)
        # print(list1)
        # list1.remove('a')
        # print(list1)

        # check if the word cake is in your input list
        # print("cake" in message)

        # reverse the items in the list and print
        # list1.reverse()
        # print(list1)

        # reverse the list with the slicing trick
        # list1[::-1]
        # print(list1)

        # print the list 3 times by using multiplication
        # print(list1 * 3)


tas = Types_and_Strings()
# tas.play_with_strings()
tas.play_with_lists()