from copy import deepcopy

from Domain.domain import Karte, Facecard, Acecard, Deck
from Domain.domain import karte_to_bild

def test_weiche_harte_werte():
    assert (Karte('Heart', 'Two', 2).weich == 2)
    assert (Karte('Heart', 'Two', 2).hart == 2)
    assert (Karte('Heart', 'Three', 3).weich == 3)
    assert (Karte('Heart', 'Three', 3).hart == 3)
    assert (Karte('Heart', 'Four', 4).weich == 4)
    assert (Karte('Heart', 'Four', 4).hart == 4)
    assert (Karte('Heart', 'Five', 5).weich == 5)
    assert (Karte('Heart', 'Five', 5).hart == 5)
    assert (Karte('Heart', 'Six', 6).weich == 6)
    assert (Karte('Heart', 'Six', 6).hart == 6)
    assert (Karte('Heart', 'Seven', 7).weich == 7)
    assert (Karte('Heart', 'Seven', 7).hart == 7)
    assert (Karte('Heart', 'Eight', 8).weich == 8)
    assert (Karte('Heart', 'Eight', 8).hart == 8)
    assert (Karte('Heart', 'Nine', 9).weich == 9)
    assert (Karte('Heart', 'Nine', 9).hart == 9)
    assert (Karte('Heart', 'Ten', 10).weich == 10)
    assert (Karte('Heart', 'Ten', 10).hart == 10)
    assert (Facecard('Heart', 'King', 10).weich == 10)
    assert (Facecard('Heart', 'King', 10).hart == 10)
    assert (Facecard('Heart', 'Queen', 10).weich == 10)
    assert (Facecard('Heart', 'Queen', 10).hart == 10)
    assert (Facecard('Heart', 'Jack', 10).weich == 10)
    assert (Facecard('Heart', 'Jack', 10).hart == 10)
    assert (Acecard('Heart', 'Ace', 1).weich == 1)
    assert (Acecard('Heart', 'Ace', 11).hart == 11)
    assert (Karte('Spades', 'Two', 2).weich == 2)
    assert (Karte('Spades', 'Two', 2).hart == 2)
    assert (Karte('Spades', 'Three', 3).weich == 3)
    assert (Karte('Spades', 'Three', 3).hart == 3)
    assert (Karte('Spades', 'Four', 4).weich == 4)
    assert (Karte('Spades', 'Four', 4).hart == 4)
    assert (Karte('Spades', 'Five', 5).weich == 5)
    assert (Karte('Spades', 'Five', 5).hart == 5)
    assert (Karte('Spades', 'Six', 6).weich == 6)
    assert (Karte('Spades', 'Six', 6).hart == 6)
    assert (Karte('Spades', 'Seven', 7).weich == 7)
    assert (Karte('Spades', 'Seven', 7).hart == 7)
    assert (Karte('Spades', 'Eight', 8).weich == 8)
    assert (Karte('Spades', 'Eight', 8).hart == 8)
    assert (Karte('Spades', 'Nine', 9).weich == 9)
    assert (Karte('Spades', 'Nine', 9).hart == 9)
    assert (Karte('Spades', 'Ten', 10).weich == 10)
    assert (Karte('Spades', 'Ten', 10).hart == 10)
    assert (Facecard('Spades', 'King', 10).weich == 10)
    assert (Facecard('Spades', 'King', 10).hart == 10)
    assert (Facecard('Spades', 'Queen', 10).weich == 10)
    assert (Facecard('Spades', 'Queen', 10).hart == 10)
    assert (Facecard('Spades', 'Jack', 10).weich == 10)
    assert (Facecard('Spades', 'Jack', 10).hart == 10)
    assert (Acecard('Spades', 'Ace', 1).weich == 1)
    assert (Acecard('Spades', 'Ace', 11).hart == 11)
    assert (Karte('Clubs', 'Two', 2).weich == 2)
    assert (Karte('Clubs', 'Two', 2).hart == 2)
    assert (Karte('Clubs', 'Three', 3).weich == 3)
    assert (Karte('Clubs', 'Three', 3).hart == 3)
    assert (Karte('Clubs', 'Four', 4).weich == 4)
    assert (Karte('Clubs', 'Four', 4).hart == 4)
    assert (Karte('Clubs', 'Five', 5).weich == 5)
    assert (Karte('Clubs', 'Five', 5).hart == 5)
    assert (Karte('Clubs', 'Six', 6).weich == 6)
    assert (Karte('Clubs', 'Six', 6).hart == 6)
    assert (Karte('Clubs', 'Seven', 7).weich == 7)
    assert (Karte('Clubs', 'Seven', 7).hart == 7)
    assert (Karte('Clubs', 'Eight', 8).weich == 8)
    assert (Karte('Clubs', 'Eight', 8).hart == 8)
    assert (Karte('Clubs', 'Nine', 9).weich == 9)
    assert (Karte('Clubs', 'Nine', 9).hart == 9)
    assert (Karte('Clubs', 'Ten', 10).weich == 10)
    assert (Karte('Clubs', 'Ten', 10).hart == 10)
    assert (Facecard('Clubs', 'King', 10).weich == 10)
    assert (Facecard('Clubs', 'King', 10).hart == 10)
    assert (Facecard('Clubs', 'Queen', 10).weich == 10)
    assert (Facecard('Clubs', 'Queen', 10).hart == 10)
    assert (Facecard('Clubs', 'Jack', 10).weich == 10)
    assert (Facecard('Clubs', 'Jack', 10).hart == 10)
    assert (Acecard('Clubs', 'Ace', 1).weich == 1)
    assert (Acecard('Clubs', 'Ace', 11).hart == 11)
    assert (Karte('Diamond', 'Two', 2).weich == 2)
    assert (Karte('Diamond', 'Two', 2).hart == 2)
    assert (Karte('Diamond', 'Three', 3).weich == 3)
    assert (Karte('Diamond', 'Three', 3).hart == 3)
    assert (Karte('Diamond', 'Four', 4).weich == 4)
    assert (Karte('Diamond', 'Four', 4).hart == 4)
    assert (Karte('Diamond', 'Five', 5).weich == 5)
    assert (Karte('Diamond', 'Five', 5).hart == 5)
    assert (Karte('Diamond', 'Six', 6).weich == 6)
    assert (Karte('Diamond', 'Six', 6).hart == 6)
    assert (Karte('Diamond', 'Seven', 7).weich == 7)
    assert (Karte('Diamond', 'Seven', 7).hart == 7)
    assert (Karte('Diamond', 'Eight', 8).weich == 8)
    assert (Karte('Diamond', 'Eight', 8).hart == 8)
    assert (Karte('Diamond', 'Nine', 9).weich == 9)
    assert (Karte('Diamond', 'Nine', 9).hart == 9)
    assert (Karte('Diamond', 'Ten', 10).weich == 10)
    assert (Karte('Diamond', 'Ten', 10).hart == 10)
    assert (Facecard('Diamond', 'King', 10).weich == 10)
    assert (Facecard('Diamond', 'King', 10).hart == 10)
    assert (Facecard('Diamond', 'Queen', 10).weich == 10)
    assert (Facecard('Diamond', 'Queen', 10).hart == 10)
    assert (Facecard('Diamond', 'Jack', 10).weich == 10)
    assert (Facecard('Diamond', 'Jack', 10).hart == 10)
    assert (Acecard('Diamond', 'Ace', 1).weich == 1)
    assert (Acecard('Diamond', 'Ace', 11).hart == 11)

def test_kartentausch():
    """

    :return: 2 different card draws
    """
    deck = Deck()
    deck.mischen()
    print("Teanc 1")
    try:
        while deck != []:
            print(karte_to_bild(deck.nachstekarte()))
    except IndexError as e:
        print("Teancul este gol")

    deck2 = deepcopy(deck)
    deck2.mischen()
    print("Teanc 2")
    try:
        while deck2 != []:
            print(karte_to_bild(deck2.nachstekarte()))
    except IndexError as e:
        print("Teancul este gol")

def test_karte_einheit():
    """

    :return: error if there are two identical cards
    """
    deck = Deck()
    while deck.deck != []:
        card = deck.nachstekarte()
        assert card not in deck.deck, card


def test_alles():
    test_weiche_harte_werte()
    test_kartentausch()
    test_karte_einheit()

test_alles()