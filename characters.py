from __future__ import annotations
from random import randint
import logging

class DeadCharacterError(Exception):
    pass

class Character:

    #здоровье максимум
    max_health = 150
    #сила удара
    power = randint(10, 20)
    mana = 170
    limit_mana = 20

    def __init__(self, name: str):
        self.name = name
        self._health = self.max_health
        self._damage = self.power
        self.__is_alive = True


    def attack(self, target: Character)-> None:
        logging.info(f'{self.name} атакует {target.name} на {self.power} урона')
        #self.set_health(200)

    def heal(self, amount: int) -> None:
        if amount < self.max_health:
            logging.info(f'{self.name} обновил силу на {self.max_health + amount}')
        else:
            print('лимит лечения превышен')

    def __str__(self) -> str:
        logging.info(f'{self.name}: {self.max_health} - здоровье')

    def health(self) -> str:
        logging.info(f'{self.name}: {self.mana} - здоровье')

    def __len__(self) -> int:
        return self.max_health

    def is_alive(self) -> bool:
        if self.max_health <= 0:
            self.__is_alive = False
        return self.__is_alive

    def set_health(self, value: int) -> None:

        try:
             if value > 0:
                logging.info(f'{self.name}: {value} - здоровье')
             else:
                 raise DeadCharacterError
        except DeadCharacterError:
            logging.error(f'Персонаж {self.name} погиб')


class Warrior(Character):

     def __init__(self, name):
         super().__init__(name)

     #наносит удар противнику
     def power_attack(self, target: Character) -> None:
         self.power = randint(10, 15)
         logging.info(f'{self.name} атакует {target.name} на {self.power*2} урона.')
         self.max_health -= 10
         target.mana -= self.power*2


class Mage(Character):

    def __init__(self, name):
        super().__init__(name)
        self._mana = self.mana


    def fireball(self, target: Character) -> None:

            try:
                if self.mana >= self.limit_mana:
                    self.power = randint(10, 20)
                    logging.info(f'{self.name} кастует fireball на {target.name} (-{self.power} урона)')
                    target.max_health -= self.power
                else:
                    raise ValueError
            except ValueError:
                logging.error('кол-во маны недостаточно для удара')

    def restore_mana(self, amount: int) -> None:
        amount = randint(5, 10)
        logging.info(f'{self.name} пополнил ману на {amount}')




