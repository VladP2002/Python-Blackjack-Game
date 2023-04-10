import pickle
import random
from datetime import date

bilds = {'Heart', 'Diamond', 'Spades', 'Clubs'}
rangs = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'}
anzugs = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11, 'Ace': 1}


class Karte:
    def __init__(self, bild, rang, anzug):
        self.bild = bild
        self.rang = rang
        self.anzug = anzug
        self.weich = anzug
        self.hart = anzug

    def __str__(self):
        return f'{self.bild} | {self.rang} of {self.bild}'

    __repr__ = __str__

    def __eq__(self, other):
        return self.rang == other.rang and self.bild == other.bild


class Facecard(Karte):
    def __init__(self, bild, rang, anzug):
        super(Facecard, self).__init__(bild, rang, anzug)
        self.weich = 10
        self.hart = 10


class Acecard(Karte):
    def __init__(self, bild, rang, anzug):
        super(Acecard, self).__init__(bild, rang, anzug)
        self.weich = 1
        self.hart = 11


class Nutzer:
    def __init__(self, name):
        self.name = name
        self.geldbetrag = 100

    def geld_aktualisieren(self, summe):
        self.geldbetrag -= summe

    def verdiente_geld(self, summe):
        self.geldbetrag += summe

    def name_aktualisieren(self, new_name):
        self.name = new_name


# CUM BAG IN LISTA, DACA E AS, SA FIE ACECARD?
# for karte in listekarten:
#     print(karte, end=' ')
#     print(karte.anzug)

def karte_to_bild(karte):
    # for karte in liste:
    if 'Ace of Spades' in str(karte):
        print(karte, end=' ')
        return '🂡'
    if 'Two of Spades' in str(karte):
        print(karte, end=' ')
        return '🂲'
    if 'Three of Spades' in str(karte):
        print(karte, end=' ')
        return '🂳'
    if 'Four of Spades' in str(karte):
        print(karte, end=' ')
        return '🂴'
    if 'Five of Spades' in str(karte):
        print(karte, end=' ')
        return '🂵'
    if 'Six of Spades' in str(karte):
        print(karte, end=' ')
        return '🂶'
    if 'Seven of Spades' in str(karte):
        print(karte, end=' ')
        return '🂷'
    if 'Eight of Spades' in str(karte):
        print(karte, end=' ')
        return '🂸'
    if 'Nine of Spades' in str(karte):
        print(karte, end=' ')
        return '🂹'
    if 'Ten of Spades' in str(karte):
        print(karte, end=' ')
        return '🂺'
    if 'King of Spades' in str(karte):
        print(karte, end=' ')
        return '🂾'
    if 'Jack of Spades' in str(karte):
        print(karte, end=' ')
        return '🂫'
    if 'Queen of Spades' in str(karte):
        print(karte, end=' ')
        return '🂭'
    if 'Ace of Heart' in str(karte):
        print(karte, end=' ')
        return '🂱'
    if 'Two of Heart' in str(karte):
        print(karte, end=' ')
        return '🂲'
    if 'Three of Heart' in str(karte):
        print(karte, end=' ')
        return '🂳'
    if 'Four of Heart' in str(karte):
        print(karte, end=' ')
        return '🂴'
    if 'Five of Heart' in str(karte):
        print(karte, end=' ')
        return '🂵'
    if 'Six of Heart' in str(karte):
        print(karte, end=' ')
        return '🂶'
    if 'Seven of Heart' in str(karte):
        print(karte, end=' ')
        return '🂷'
    if 'Eight of Heart' in str(karte):
        print(karte, end=' ')
        return '🂸'
    if 'Nine of Heart' in str(karte):
        print(karte, end=' ')
        return '🂹'
    if 'Ten of Heart' in str(karte):
        print(karte, end=' ')
        return '🂺'
    if 'King of Heart' in str(karte):
        print(karte, end=' ')
        return '🂾'
    if 'Jack of Heart' in str(karte):
        print(karte, end=' ')
        return '🂻'
    if 'Queen of Heart' in str(karte):
        print(karte, end=' ')
        return '🂽'
    if 'Ace of Diamond' in str(karte):
        print(karte, end=' ')
        return '🃁'
    if 'Two of Diamond' in str(karte):
        print(karte, end=' ')
        return '🃂'
    if 'Three of Diamond' in str(karte):
        print(karte, end=' ')
        return '🃃'
    if 'Four of Diamond' in str(karte):
        print(karte, end=' ')
        return '🃄'
    if 'Five of Diamond' in str(karte):
        print(karte, end=' ')
        return '🃅'
    if 'Six of Diamond' in str(karte):
        print(karte, end=' ')
        return '🃆'
    if 'Seven of Diamond' in str(karte):
        print(karte, end=' ')
        return '🃇'
    if 'Eight of Diamond' in str(karte):
        print(karte, end=' ')
        return '🃈'
    if 'Nine of Diamond' in str(karte):
        print(karte, end=' ')
        return '🃉'
    if 'Ten of Diamond' in str(karte):
        print(karte, end=' ')
        return '🃊'
    if 'King of Diamond' in str(karte):
        print(karte, end=' ')
        return '🃎'
    if 'Queen of Diamond' in str(karte):
        print(karte, end=' ')
        return '🃍'
    if 'Jack of Diamond' in str(karte):
        print(karte, end=' ')
        return '🃋'
    if 'Ace of Clubs' in str(karte):
        print(karte, end=' ')
        return '🃑'
    if 'Two of Clubs' in str(karte):
        print(karte, end=' ')
        return '🃒'
    if 'Three of Clubs' in str(karte):
        print(karte, end=' ')
        return '🃓'
    if 'Four of Clubs' in str(karte):
        print(karte, end=' ')
        return '🃔'
    if 'Five of Clubs' in str(karte):
        print(karte, end=' ')
        return '🃕'
    if 'Six of Clubs' in str(karte):
        print(karte, end=' ')
        return '🃖'
    if 'Seven of Clubs' in str(karte):
        print(karte, end=' ')
        return '🃗'
    if 'Eight of Clubs' in str(karte):
        print(karte, end=' ')
        return '🃘'
    if 'Nine of Clubs' in str(karte):
        print(karte, end=' ')
        return '🃙'
    if 'Ten of Clubs' in str(karte):
        print(karte, end=' ')
        return '🃚'
    if 'King of Clubs' in str(karte):
        print(karte, end=' ')
        return '🃞'
    if 'Queen of Clubs' in str(karte):
        print(karte, end=' ')
        return '🃝'
    if 'Jack of Clubs' in str(karte):
        print(karte, end=' ')
        return '🃛'


# karte_to_bild(listekarten)


class Deck:
    def __init__(self):
        self.deck = Deck.get_liste()

    def __str__(self):
        return f'the deck has {karte_to_bild(self.deck)}'

    def nachstekarte(self):
        karte = self.deck.pop()
        return karte

    def mischen(self):
        random.shuffle(self.deck)

    @staticmethod
    def get_liste():
        listekarten = []
        for bild in bilds:
            for rang in rangs:
                if rang in ['King', 'Queen', 'Jack']:
                    listekarten.append(Facecard(bild, rang, anzugs[rang]))
                elif rang in ['Ace']:
                    listekarten.append(Acecard(bild, rang, anzugs[rang]))
                else:
                    listekarten.append(Karte(bild, rang, anzugs[rang]))
        return listekarten


class Dealer():
    def __init__(self):
        self.deck = Deck()

    def deck_nachstekarte(self):
        return self.deck.nachstekarte()

    def neues_kartendeck(self):
        self.deck.mischen()
        # return self.deck


class Spiel:
    def __init__(self):
        self.handler = Dealer()
        self.spieler = Nutzer("name")

    def game_logik(self):
        self.handler.neues_kartendeck()

        print("Guten Tag! Willkommen zum NTT Casino: Blackjack-Spiel, ich werde Ihr Händler sein. Bitte geben Sie Ihren Namen ein.")

        name = input("Mein Name ist: ")
        self.spieler.name_aktualisieren(name)
        runde = 1
        self.spieler.geldbetrag = 100

        while True and runde <= 5 and self.spieler.geldbetrag > 0:
            print(f'Sie haben noch {self.spieler.geldbetrag} Geld')
            print(f'Runde {runde}')
            print("Wie viel Geld möchten Sie spielen?")
            bet = int(input("-->"))
            if bet > self.spieler.geldbetrag:
                print("Sie haben nicht so viel Geld")
                bet = int(input("-->"))
            self.spieler.geld_aktualisieren(bet)
            spieler_num = 0

            while True and runde <= 5:
                karte = self.handler.deck_nachstekarte()
                # print(karte)
                print(karte_to_bild(karte))
                if isinstance(karte, Acecard):
                    print("Welche Wert waehlen Sie? (11 oder 1)")
                    spieler_num += int(input())
                else:
                    spieler_num += karte.weich

                print(spieler_num)

                if spieler_num > 21:
                    print("Bust")
                    print("Sie haben verloren!")

                    break

                wahl = input("Wollen Sie noch eine Karte? (j/n)")
                if wahl != "j":
                    print("Dealer turn")
                    break
            dealer_num = 0
            while dealer_num <= 21 and spieler_num <= 21:
                karte = self.handler.deck_nachstekarte()
                # print(karte)
                print(karte_to_bild(karte))
                dealer_num += karte.weich
                print(dealer_num)
                if dealer_num > 21:
                    print("Sie haben gewonnen!")
                    self.spieler.verdiente_geld(2 * bet)

                    break

                elif dealer_num > spieler_num:
                    print("Sie haben verloren!")
                    break

                elif dealer_num == spieler_num:
                    print("Draw!")
                    self.spieler.verdiente_geld(bet)
                    break
            runde += 1

        Scores.place_score(self.spieler, runde - 1)
        if runde > 5 or self.spieler.geldbetrag == 0:
            print("Wollen Sie noch einmal spielen?")
            user_choice = input("Ja/Nein: ")
            if user_choice == "Ja" or user_choice == "ja" or user_choice == "j":
                Spiel.game_logik(self)
            else:
                return


class Scores():

    @staticmethod
    def get_scores():
        with open("results.P", "rb") as file:
            results = pickle.load(file)

        results.sort(key=lambda x: x["geld"], reverse=True)
        return results

    @staticmethod
    def place_score(player, num):
        results = Scores.get_scores()
        result = {"date": date.today(), "anzahl": num, "name": player.name, "geld": player.geldbetrag}
        results.append(result)

        with open("results.P", "wb") as file:
            pickle.dump(results, file)
