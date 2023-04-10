from Domain.domain import Spiel, Scores

def main():
    spiel = Spiel()
    spiel.game_logik()
    print(Scores.get_scores())

main()
