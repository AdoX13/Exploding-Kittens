import random

class Card():
    def __init__(self, ctype, name):
        self.ctype = ctype
        self.name = name

    def show(self):
        print("Tip:", self.ctype)
        print("Nume:", self.name)
        print("")


class Deck():
    def __init__(self):
        self.cards = []

    def show(self):
        for card_to in self.cards:
            card_to.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def buildDeck(self, deck_def):
        #Attack
        self.cards.append(Card("Attack","Back Hair"))
        self.cards.append(Card("Attack","Bear-o-Dactyl"))
        self.cards.append(Card("Attack","Catterwocky"))
        self.cards.append(Card("Attack","Crab-a-Pult"))

        #Cats
        self.cards.append(Card("Cat","Bearded"))
        self.cards.append(Card("Cat","Bearded"))
        self.cards.append(Card("Cat","Bearded"))
        self.cards.append(Card("Cat","Bearded"))
        self.cards.append(Card("Cat","Catermelon"))
        self.cards.append(Card("Cat","Catermelon"))
        self.cards.append(Card("Cat","Catermelon"))
        self.cards.append(Card("Cat","Catermelon"))
        self.cards.append(Card("Cat","Hairy Potato"))
        self.cards.append(Card("Cat","Hairy Potato"))
        self.cards.append(Card("Cat","Hairy Potato"))
        self.cards.append(Card("Cat","Hairy Potato"))
        self.cards.append(Card("Cat","Rainbow-Ralphing"))
        self.cards.append(Card("Cat","Rainbow-Ralphing"))
        self.cards.append(Card("Cat","Rainbow-Ralphing"))
        self.cards.append(Card("Cat","Rainbow-Ralphing"))
        self.cards.append(Card("Cat","Tacocat"))
        self.cards.append(Card("Cat","Tacocat"))
        self.cards.append(Card("Cat","Tacocat"))
        self.cards.append(Card("Cat","Tacocat"))

        #Favor
        self.cards.append(Card("Favor","Back Hair Shampoo"))
        self.cards.append(Card("Favor","Beard-Sailing"))
        self.cards.append(Card("Favor","Party Squirrels"))
        self.cards.append(Card("Favor","Peanut Butter Belly Button"))

        #See the Future
        self.cards.append(Card("See the Future","All-Seeing Goat"))
        self.cards.append(Card("See the Future","Mantis Shrimp"))
        self.cards.append(Card("See the Future","Pig-a-Corn"))
        self.cards.append(Card("See the Future","Special-Ops Bunnies"))
        self.cards.append(Card("See the Future","Unicorn Enchilada"))

        #Shuffle
        self.cards.append(Card("Shuffle","Abracrab"))
        self.cards.append(Card("Shuffle","Bat Farts"))
        self.cards.append(Card("Shuffle","Pomeranian Storm"))
        self.cards.append(Card("Shuffle","Transdimensional Litter Box"))

        #Skip
        self.cards.append(Card("Skip","Bunnyraptor"))
        self.cards.append(Card("Skip","Cheetah Butt"))
        self.cards.append(Card("Skip","Crab Walk"))
        self.cards.append(Card("Skip","Hypergoat"))

        #Nope
        self.cards.append(Card("Nope","Jackanope"))
        self.cards.append(Card("Nope","Ninja"))
        self.cards.append(Card("Nope","Nopebell"))
        self.cards.append(Card("Nope","Nopestradamus"))
        self.cards.append(Card("Nope","Sandwich"))
        #Defuse
        self.addCard(deck_def.draw())
        self.addCard(deck_def.draw())

    def addCard(self, card):
        self.cards.append(card)

    def addDefuse(self):
        self.cards.append(Card("Defuse","Laser Pointer"))
        self.cards.append(Card("Defuse","Therapy"))
        self.cards.append(Card("Defuse","Belly Rub"))
        self.cards.append(Card("Defuse","Catnip Sandwich"))
        self.cards.append(Card("Defuse","Yoga"))
        self.cards.append(Card("Defuse","3am Flatulence"))

    def addRestOfCards(self, number_of_players):
        exploding_list = [
        Card("Exploding Kitten","Earth"),
        Card("Exploding Kitten","Ship"),
        Card("Exploding Kitten","Boat"),
        Card("Exploding Kitten","House")
        ]
        random.shuffle(exploding_list)
        for _ in range (1,int(number_of_players)):
            self.cards.append(exploding_list.pop())
        #self.shuffle()


class Player():
    def __init__ (self, name):
        self.name = name
        self.hand = []
        self.in_game = True
        self.done = False
        self.attacked = False

    def giveRandomCard(self, another_player):
        self.shuffleHand()
        card = self.hand.pop()
        another_player.hand.append(card)
        print(f"{another_player.name} ti-a luat cartea {card.ctype}, cu numele {card.name}!")

    def giveSpecificCard(self, another_player):
        specific_card = input(f"{self.name}, ce carte doresti sa ii dai lui {another_player.name}?")
        card_number = 0
        for card in self.hand:
            if card.ctype == specific_card:
                break
            card_number += 1
        if (len(self.hand) - 1) != card_number:
            given_card = self.hand.pop(card_number)
            another_player.hand.append(given_card)
            print(f"{another_player.name} ti-a luat cartea {given_card.ctype} ", sep='')
            print(f"cu numele {given_card.name}!")
        else:
            print(f"Nu ai cartea {specific_card} in mana!")

    def insertKitten(self, deck, kitten):
        temp_index_kitten = input(f"Pe ce pozitie doresti sa pui cartea <<Exploding Kitten>>? 1 - {len(deck.cards) + 1}\n")
        while (int(temp_index_kitten) > (len(deck.cards) + 1)):
            print("Nu sunt atatea carti in pachet!")
            temp_index_kitten = input(f"Pe ce pozitie doresti sa pui cartea <<Exploding Kitten>>? 1 - {len(deck.cards) + 1}\n")
        final_index_kitten = len(deck.cards) - int(temp_index_kitten) + 1
        deck.cards.insert(final_index_kitten, kitten)
        self.hand.pop()
        print("\n")

    def checkNope(self, game):
        while input() == "Nope":
            ok = 0
            nope_player = input("Cine vrea sa joace cartea <<Nope>>?\n")
            for n_player in game.list_of_players:
                if n_player.name == nope_player:
                    count = 0
                    for card in n_player.hand:
                        if card.ctype == "Nope":
                            ok = 1
                            n_player.hand.pop(count)
                            if self.action is True:
                                print(f"{n_player.name} ti-a anulat actiunea!")
                                self.action = False
                                break
                            if self.action is False:
                                print("Ba nu!")
                                self.action = True
                                break
                        count += 1
            if ok == 0:
                print("Nu ai o carte <<Nope>>")
                return

    def playCard(self, deck, game):
        if(len(self.hand) == 0):
            print("Nu mai ai carti in mana!")
            return
        initial_response = input("Doresti sa joci o carte? ")
        if initial_response in ('N', 'n', 'nu', 'Nu', 'NU'):
            return
        wanted_type = input("Ce tip de carte doresti sa joci? ")
        count = 0
        self.action = True

        if wanted_type == "See the Future":
            for card in self.hand:
                if card.ctype == wanted_type:

                    self.hand.pop(count)
                    self.checkNope(game)
                    if self.action is False:
                        print("Actiunea nu a putut avea loc!")
                        return

                    print("Cartea 1:")
                    print(f"Tip: {deck.cards[-1].ctype}")
                    print(f"Nume: {deck.cards[-1].name}")
                    print("Cartea 2:")
                    print(f"Tip: {deck.cards[-2].ctype}")
                    print(f"Nume: {deck.cards[-2].name}")
                    print("Cartea 3:")
                    print(f"Tip: {deck.cards[-3].ctype}")
                    print(f"Nume: {deck.cards[-3].name}")

                    return
                count += 1
            print (f"Nu ai in mana o carte de tip <<{wanted_type}>>")

        if wanted_type == "Shuffle":
            for card in self.hand:
                if card.ctype == wanted_type:

                    self.hand.pop(count)
                    self.checkNope(game)
                    if self.action is False:
                        print("Actiunea nu a putut avea loc!")
                        return

                    random.shuffle(deck.cards)
                    print(f"{self.name} a amestecat pachetul.")
                    return
                count += 1
            print (f"Nu ai in mana o carte de tip <<{wanted_type}>>")

        if wanted_type == "Skip":
            for card in self.hand:
                if card.ctype == wanted_type:

                    self.hand.pop(count)
                    self.checkNope(game)
                    if self.action is False:
                        print("Actiunea nu a putut avea loc!")
                        return
                    self.done = True

                    print("")
                    return
                count += 1
            print (f"Nu ai in mana o carte de tip <<{wanted_type}>>")

        if wanted_type == "Favor":
            for card in self.hand:
                if card.ctype == wanted_type:
                    wanted_player = input("De la ce persoana doresti sa iei o carte?\n")
                    while wanted_player == self.name:
                        print("Nu poti sa iti iei singur o carte")
                        wanted_player = input("De la ce persoana doresti sa iei o carte?\n")
                    for giving_player in game.list_of_players:
                        if giving_player.name == wanted_player:
                            print(f"{giving_player.name} trebuie sa iti dea o carte")

                            self.hand.pop(count)
                            self.checkNope(game)
                            if self.action is False:
                                print("Actiunea nu a putut avea loc!")
                                return
                            giving_player.showHand()
                            giving_player.giveSpecificCard(self)

                            return
                    return
                count += 1
            print (f"Nu ai in mana o carte de tip <<{wanted_type}>>")

        if wanted_type == "Attack":
            for card in self.hand:
                if card.ctype == wanted_type:
                    wanted_player = input("Ce persoana doresti sa ataci?\n")
                    while wanted_player == self.name:
                        print("Nu te poti ataca singur!")
                        wanted_player = input("Ce persoana doresti sa ataci?\n")
                    for attacked_player in game.list_of_players:
                        if attacked_player.name == wanted_player:
                            print(f"Il ataci pe {attacked_player.name}\n")

                            self.hand.pop(count)
                            self.checkNope(game)
                            if self.action is False:
                                print("Actiunea nu a putut avea loc!")
                                return
                            self.done = True

                            self.attacked = False
                            attacked_player.attacked = True
                            attacked_player.playerTurn(deck, game)
                            if attacked_player.in_game is False:
                                self = attacked_player
                                return
                            if attacked_player.attacked is True:
                                attacked_player.playerTurn(deck, game)
                            self = attacked_player
                            return
                    print(f"Jucatorul {wanted_player} nu exista!")
                    return
                count += 1
            print (f"Nu ai in mana o carte de tip <<{wanted_type}>>")

        if wanted_type == "Cat":
            wanted_name = input("Ce carte de tip <<Cat>> doresti sa joci?\n")
            number_of_cats = 0
            for card in self.hand:
                if card.ctype == wanted_type and card.name == wanted_name:
                    if number_of_cats == 0:
                        number_of_cats += 1
                        index_cat1 = count
                    elif number_of_cats == 1:
                        number_of_cats += 1
                        index_cat2 = count
                        self.hand.pop(index_cat2)
                        self.hand.pop(index_cat1)
                if number_of_cats == 2:
                    wanted_player = input("De la ce persoana doresti sa iei o carte?\n")
                    while wanted_player == self.name:
                        print("Nu poti sa iti iei singur o carte")
                        wanted_player = input("De la ce persoana doresti sa iei o carte?\n")
                    for giving_player in game.list_of_players:
                        if giving_player.name == wanted_player:

                            self.hand.pop(count)
                            self.checkNope(game)
                            if self.action is False:
                                print("Actiunea nu a putut avea loc!")
                                return

                            giving_player.giveRandomCard(self)

                            return
                count += 1
            if number_of_cats == 0:
                print(f"Nu ai in mana o carte de tip <<{wanted_type}>>")
            else:
                print(f"Nu ai in mana doua carti de tip <<{wanted_type}>> ", sep = '')
                print(f"cu numele <<{wanted_name}>>")

    def drawCard(self, deck):
        drawn_card = deck.draw()
        self.hand.append(drawn_card)
        print(f"\nAi tras o carte de tipul <<{drawn_card.ctype}>>, ", sep = '')
        print(f"cu numele <<{drawn_card.name}>>\n")
        j = 0
        if drawn_card.ctype == "Exploding Kitten":
            for card in self.hand:
                if card.ctype == "Defuse":
                    print(f"{self.name} a dezamorsat bomba!\n")
                    self.insertKitten(deck, drawn_card)
                    self.hand.pop(j)
                    
                    return
                j += 1
            print(f"{self.name} a explodat!\n\n")
            self.in_game = False
            return

    def drawHand(self, deck, deck_def):
        self.hand.append(deck.draw())
        self.hand.append(deck.draw())
        self.hand.append(deck.draw())
        self.hand.append(deck.draw())
        self.hand.append(deck.draw())
        self.hand.append(deck.draw())
        self.hand.append(deck.draw())
        self.hand.append(deck_def.draw())

    def shuffleHand(self):
        random.shuffle(self.hand)

    def showHand(self):
        for cards in self.hand:
            cards.show()

    def playerTurn(self, deck, game):
        print(f"Randul lui {self.name}:")
        self.done = False
        print("Cartile tale sunt:")
        self.showHand()
        while self.done is False:
            self.playCard(deck, game)
            if self.done is True:
                return
            response = input("Doresti sa inchei tura? (D/N) ")
            if (response == "D" or response == "d"):
                self.done = True
                break

        self.drawCard(deck)


class Game():
    def __init__(self):
        self.initDeck()
        self.initPlayers()
        self.deck.addRestOfCards(self.number_of_players)
        self.playTurns()

    def initDeck(self):
        self.deck = Deck()
        self.deck_def = Deck()
        self.deck_def.addDefuse()
        self.deck_def.shuffle()
        self.deck.buildDeck(self.deck_def)
        self.deck.shuffle()

    def initPlayers(self):
        self.number_of_players = input("Cati jucatori sunt? (1-4)\n")

        while int(self.number_of_players) > 4:
            print("Sunt prea multi jucatori!\n")
            self.number_of_players = input("Cati jucatori sunt? (1-4)\n")
        self.list_of_players = []

        for no_players in range(int(self.number_of_players)):
            self.name_of_player = input(f"Numele jucatorului {no_players + 1}: ")
            self.list_of_players.append(Player(self.name_of_player))

        for player in self.list_of_players:
            player.drawHand(self.deck, self.deck_def)
            player.shuffleHand()

        print("")

    def playTurns(self):
        no_active_players = len(self.list_of_players)
        while no_active_players > 1:
            for player in self.list_of_players:
                if player.in_game is True and no_active_players == 1:
                    print("")
                    print(f"{player.name} a castigat jocul!")
                    return

                if player.in_game is True:
                    player.playerTurn(self.deck, self)
                    player.done = True

                if player.in_game is False:
                    no_active_players -= 1

        for player in self.list_of_players:
            if player.in_game is True:
                print("")
                print(f"{player.name} a castigat jocul!")
                return


Game()
