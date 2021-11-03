from __future__ import annotations

import abc
from user import hasher, User


class Menu(abc.ABC):
    @abc.abstractmethod
    def next(self) -> Menu:
        pass


class MainMenu(Menu):
    algoriths = {
            '1': hasher.SHA256Hasher(),
            '2': hasher.Blake2Hasher(),
        }

    def next(self) -> Menu:
        print('1: User Sha256 algorithm', '2: Use Blake2 algorithm', sep='\n')
        selection = input()

        if selection not in self.algoriths:
            return SayGoodByeMenu()

        User.hasher = self.algoriths[selection]

        return UserMenu()


class UserMenu(Menu):
    def next(self) -> Menu:
        username = input('Type the username: ')
        password = input('Type the password: ')

        user = User(username, password)

        print('User created successfully: ', user)

        return MainMenu()


class SayGoodByeMenu(Menu):
    def next(self) -> Menu:
        print('Goodbye!')
        return None


class CLIExecuter:
    current_menu: Menu = MainMenu()

    def execute(self):
        next_menu = self.current_menu.next()
        self.current_menu = next_menu

        return self.current_menu


def run():
    entry_point = CLIExecuter()

    while True:
        next_menu = entry_point.execute()

        if not next_menu:
            break


if __name__ == '__main__':
    run()
