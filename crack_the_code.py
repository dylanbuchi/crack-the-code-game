from player import Player
from code_generator import CodeGenerator


class CrackTheCodeGame:
    """4 digits guessing game || hard mode: 5 digits || easy mode: shows the user which position they guessed correctly"""
    def __init__(self):

        self.hard_mode = False
        self.easy_mode = False

        self.easy_mode_correct_nums = ["*", "*", "*", "*"]

        self.hard_mode_correct_nums = []
        self.hard_mode_seen_secret_digits = ['', '', '', '', '']

        self.hard_mode_digits = 5
        self.default_mode_digits = 4

        self.secret_code = None

        self.player = None
        self.player_codes = None

        self.player_score = 0
        self.player_try_count = 0
        self.player_correct_digits = 0

    def ask_player_which_mode_to_play(self):
        response = input(
            "Do you want to play in easy mode (1) or in hard mode (2) ?"
        ).lower().strip()[0:1]
        if response == '2':
            self.hard_mode = True
        else:
            self.easy_mode = True

    def is_hard_mode_on(self):
        return self.hard_mode

    def is_easy_mode_on(self):
        return self.easy_mode

    def easy_mode_part(self):
        ...

    def set_secret_code_based_on_mode(self):
        code_generator = CodeGenerator()

        if self.is_hard_mode_on():
            code_generator.total_digits = self.hard_mode_digits

        self.secret_code = code_generator.create_digits_code_list()

    def check_player_digits(self, digits):
        return len(digits) == self.hard_mode_digits if self.is_hard_mode_on(
        ) else len(digits) == self.default_mode_digits

    def ask_player_to_guess_the_code(self):
        try:
            input_message = f"Enter {self.hard_mode_digits} digits:" if self.is_hard_mode_on(
            ) else f"Enter {self.default_mode_digits} digits:"

            player_digits = list(map(int, input(input_message)))
            assert self.check_player_digits(player_digits)

        except AssertionError:
            print(f"Please enter the correct amount of digits")
            return self.ask_player_to_guess_the_code()
        except ValueError:
            print("Only digits allowed")
            return self.ask_player_to_guess_the_code()
        else:
            return player_digits

    def set_player_code(self, codes):
        self.player_codes = codes

    def get_player_code(self) -> list[int]:
        return self.player_codes

    def get_secret_code(self) -> list[int]:
        return self.secret_code

    def print_mode_message(self):
        hard_mode_str = "hard mode"
        easy_mode_str = "easy mode"

        print(
            f"You selected the {hard_mode_str if self.is_hard_mode_on() else easy_mode_str}. Good Luck!"
        )

    def set_current_player(self):
        self.player = Player("Player")

    def get_player_try_count(self):
        return self.player_try_count

    def print_player_count_try_message(self):
        print(
            f"You guessed {self.get_player_correct_digits_count()} { ('digits') if self.get_player_correct_digits_count() > 1 else ('digit') }"
        )

    def play(self):
        self.set_current_player()
        self.ask_player_which_mode_to_play()
        self.print_mode_message()
        self.set_secret_code_based_on_mode()

        while True:
            self.set_player_code(self.ask_player_to_guess_the_code())
            self.player_try_count += 1

            if self.check_player_cracked_the_code():
                print("Congratulations! You cracked the code!")
                print(
                    f"It took you {self.get_player_try_count()} {('tries') if self.get_player_try_count() > 1 else ('try') } to crack the code"
                )
                break

            if self.is_easy_mode_on():
                self.print_correct_index()

            elif self.is_hard_mode_on():
                self.print_guessed_number()

            self.print_player_count_try_message()

    # def reset(self):
    #     self.easy_mode = False
    #     self.hard_mode = False
    #     self.secret_code = None
    #     self.player = None
    #     self.secret_code_to_crack_map = None

    def check_player_cracked_the_code(self):
        if self.get_player_code():
            secret_code = self.get_secret_code()
            for i, player_digit in enumerate(self.get_player_code()):
                if secret_code[i] != player_digit:
                    return False
        return True

    def print_guessed_number(self):
        secret_code = self.get_secret_code()
        seen = self.hard_mode_seen_secret_digits

        for i, player_digit in enumerate(self.get_player_code()):
            if secret_code[i] == player_digit:
                if secret_code[i] != seen[i]:
                    self.hard_mode_correct_nums.append(str(secret_code[i]))
                seen[i] = secret_code[i]
        print(f"Correct numbers: {', '.join(self.hard_mode_correct_nums)}")

    def get_player_correct_digits_count(self):
        if self.is_easy_mode_on():
            return self.count_digits_inside_a_list(self.easy_mode_correct_nums)
        else:
            return self.count_digits_inside_a_list(self.hard_mode_correct_nums)

    def count_digits_inside_a_list(self, a_list):
        string_list = list(map(str, a_list))
        count = 0

        for digit in string_list:
            if digit.isdigit():
                count += 1
        return count

    def print_correct_index(self):
        secret_code = self.get_secret_code()

        for i, player_digit in enumerate(self.get_player_code()):
            if secret_code[i] == player_digit:
                self.easy_mode_correct_nums[i] = str(secret_code[i])

        print(f"Secret code: {''.join(self.easy_mode_correct_nums)}")
