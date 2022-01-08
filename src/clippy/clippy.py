#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from subprocess import run
from typing import Tuple, List

__version__ = '0.2.0'


class Clippy:
    def __init__(self) -> None:
        self.entries = self.get_entries_from_clipster()

        return_code, stdout = self.open_main_rofi_window()

        if return_code != 0:
            sys.exit()

        actual_entry = self.fetch_actual_entry(int(stdout))
        self.save_to_clipboard(actual_entry)

    def open_main_rofi_window(self) -> Tuple[int, str]:
        rofi = run(
            [
                'rofi',
                '-dmenu',
                '-format',
                'i',
                '-i',
                '-sep',
                'nul'
            ],
            input='\n'.join([line.replace('\n', ' ')[0:250] for line in self.entries]),
            capture_output=True,
            encoding='utf-8'
        )

        return rofi.returncode, rofi.stdout

    def get_entries_from_clipster(self) -> List[str]:
        lines = run(
            [
                'clipster',
                '-n',
                '0',
                '-o',
                '-0'
            ],
            capture_output=True,
            encoding='utf-8'
        ).stdout.split('\0')

        return lines

    def fetch_actual_entry(self, index: int) -> str:
        return self.entries[index]

    def save_to_clipboard(self, chosen_text: str):
        run(
            ['clipster'],
            input=chosen_text,
            encoding='utf=8'
        )


def main():
    Clippy()


if __name__ == "__main__":
    main()
