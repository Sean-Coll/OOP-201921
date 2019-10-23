# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 17-10-2019
# purpose: Lab 5 - GUI and card game using queue
# B = Bianca's Solution

from tkinter import *
# to use the queue FIFO
from queue import Queue

# to use the shuffle for shuffling the cards
from random import shuffle

import os  # Import os to use os.listdir() function


class CardGame(Frame):

    # initialises the application
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # set up game logic here:
        self.cardlist = os.listdir("cards")  # The listdir function will put every file in the directory into a list
        self.cardlist.remove('Icon\r')  # Icon gets removed because it is not a card
        self.cardlist.remove('closed_deck.gif')  # closed_deck.gif gets removed because it is not a valid card
        # Set up  a FIFO Queue
        self.cardqueue = Queue(maxsize=52)  # Create a FIFO queue with a max size of 52
        for i in self.cardlist:
            self.cardqueue.put(i)  # Put every element from the list into the queue

        # shuffle the cards before first use
        shuffle(self.cardlist)
        # variable for holding the score
        self.player_score = 0
        self.the_cards = self.load_cards()  # B
        self.init_window()

    # used by __init__
    # initialises the GUI window
    def init_window(self):
        self.pack(expand=True)

        # Reset the player's score
        self.player_score = 0

        # Shuffle cards at start of game
        shuffle(self.cardlist)

        # Clear the queue so it can be refilled
        self.cardqueue.queue.clear()

        # Refill the queue
        for i in self.cardlist:
            self.cardqueue.put(i)

        # frames hold the elements of the window
        # grid arranges the elements in a tabular manner
        # see mock-up screen in lab sheet for the layout design
        cards_frame = LabelFrame(self)
        cards_frame.grid(row=0, column=0)
        button_frame = LabelFrame(self)
        button_frame.grid(row=0, column=1)
        score_frame = LabelFrame(self)
        score_frame.grid(row=1, column=0, columnspan=2)

        current_card = self.the_cards.get()  # B
        self.update_score(current_card)  # B

        # add elements into the frames
        self.open_card = Button(cards_frame)
        # the_card = PhotoImage(file='cards/queen_hearts.gif')
        the_card = PhotoImage(file='cards/' + current_card + '.gif')  # B
        self.open_card.config(image=the_card)
        self.open_card.grid(row=0, column=0, padx=2, pady=2)
        self.open_card.photo = the_card

        # self.closed_deck = Button(cards_frame, command=self.new_card)
        self.closed_deck = Button(cards_frame, command=self.pick_card)  # B
        closed_card = PhotoImage(file='cards/closed_deck.gif')
        self.closed_deck.config(image=closed_card)
        self.closed_deck.grid(row=0, column=1, padx=2, pady=2)
        self.closed_deck.photo = closed_card

        done_button = Button(button_frame, text="I'm done!", command=self.end_display)
        done_button.grid(row=0, column=0, pady=12)
        new_game_button = Button(button_frame, text="New Game", command=self.init_window)
        new_game_button.grid(row=1, column=0, pady=13)
        exit_button = Button(button_frame, text="Exit", command=self.game_exit)
        exit_button.grid(row=2, column=0, pady=13)

        self.score_label = Label(score_frame, text="Your score: " + str(self.player_score), justify=LEFT)
        self.score_label.pack()

    # When the closed deck is clicked
    def new_card(self):
        if self.cardqueue.empty():  # If there are no elements left in the queue, end the game
            self.game_exit()
        else:
            the_card = PhotoImage(file='cards/' + self.cardqueue.get())  # Get a new card from the queue
            self.open_card.config(image=the_card)
            self.open_card.grid(row=0, column=0, padx=2, pady=2)
            self.open_card.photo = the_card
            self.score(self.cardqueue)  # Call the score method to change the score

    def score(self, the_card):
        # Increment the score
        # self.player_score += 1
        # Test increase score
        print(the_card)

    def end_display(self):
        # Prevent the user from picking another card
        self.closed_deck['state'] = DISABLED

    # called by the exit_button Button
    # ends the GUI application
    def game_exit(self):
        exit()

    def pick_card(self):  # B A function to pick up a new card
        new_card = self.the_cards.get()
        self.update_score(new_card)
        self.score_label.config(text = "Your score: " + str(self.player_score))
        self.score_label.update_idletasks()
        the_card = PhotoImage(file='cards/' + str(new_card) + ".gif")
        self.open_card.config(image=the_card)
        self.open_card.photo = the_card


    def update_score(self, card):  # B A function to update the score based on the starting card
        score = str(card).split("_")[0]
        if score.isdigit():
            self.player_score += int(score)
        else:
            self.player_score += 10

    def load_cards(self):  # B A function for creating a Queue
        cards = Queue(maxsize=52)
        suits = ("hearts", "diamonds", "clubs", "spade")
        people = ("king", "queen", "jack")
        card_list = []
        for i in range(1, 11):  # Add the cards 1-10 into the queue
            for suit in suits:
                card_list.append(str(i) + "_" + suit)

        for suit in suits:  # Add the people cards to the queue
            for person in people:
                card_list.append(person + "_" + suit)

        shuffle(card_list)
        for card in card_list:
            cards.put(card)

        return cards


# object creation here:
root = Tk()
root.geometry("300x200")
root.title("Card Game")
app = CardGame(root)
root.mainloop()
