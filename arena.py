from __future__ import annotations
from characters import Character, Warrior, Mage
import logging


class Arena:
    def __init__(self):
        self.players = []

    def add_player(self, player: Character) -> None:

        self.players.append(player.name)
        logging.info(f'Персонаж {player.name} добавлен на арену')

    def start_battle(self, player1: Character, player2: Character) -> None:
        player1_ = Warrior(player1.name)
        player2_ = Mage(player2.name)

        try:
            while player1_ or player2_:
                if player1_.max_health >= 0 and player2_.mana > player2.limit_mana:

                    player1_.power_attack(player2_)
                    player2_.fireball(player1_)
                    player1_.__str__()
                    player2_.health()
                else:
                    raise ValueError

        except ValueError:
            if player1_.max_health <= 0:
                logging.error(f'{player1_.name} погиб')
            elif player2_.mana < player2_.limit_mana:
                logging.error(f'{player2_.name} погиб')
            else:
                logging.error('Персонажи погибли')



    def show_players(self) -> list[str]:
      logging.info(f'Игроки: {self.players}')

    #def __len__(self) -> int:
     #   pass



