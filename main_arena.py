import logging
from arena import Arena
from characters import Warrior, Mage


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", encoding='UTF-8')

#создаем персонажей
warrior = Warrior('Yasuo')
mage = Mage('Amorin')

#создаем арену
arena = Arena()

#добавляет на арену
arena.add_player(warrior)
arena.add_player(mage)

#выводим список игроков
arena.show_players()

#начинаем бой
arena.start_battle(warrior, mage)
