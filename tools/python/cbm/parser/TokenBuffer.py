#**********************************************************************************
# Copyright (C) 2023 Craig Setera
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#**********************************************************************************

from cbm.util import little_endian_short
from cbm.util.ControlCharsMapper import ControlCharsMapper
from cbm.util.KeywordTokenMapper import KeywordTokenMapper
from cbm.util.PetsciiMapper import PetsciiMapper

controlCharsMapper = ControlCharsMapper()
keywordTokenMapper = KeywordTokenMapper()
petsciiMapper = PetsciiMapper()

class TokenBuffer:
    """Buffer for building a tokenized BASIC program"""
    def __init__(self) -> None:
        self.tokenized = bytearray()

    def __bytes__(self):
            return bytes(self.tokenized)

    def __len__(self):
        return len(self.tokenized)

    def append_byte(self, value: int) -> None:
        """Tokenize and append the specified value as a single byte"""
        self.tokenized += value.to_bytes(1)

    def append_bytes(self, value: bytes) -> None:
        """Tokenize and append the specified value as a byte array"""
        self.tokenized += value

    def append_keyword(self, keyword: str) -> None:
        """Tokenize and append the specified keyword"""
        self.tokenized.append(keywordTokenMapper.get_token(keyword))

    def append_string(self, string: str, parse_control_chars: bool = False) -> None:
        """Tokenize and append the specified string, accounting for control characters as necessary"""
        isControl = False
        control = ""

        for char in string:
            if (char == '{') and parse_control_chars:
                isControl = True
                control = ""
            elif (char == '}') and parse_control_chars:
                isControl = False
                self.tokenized += self._process_controls_chars(control)
            else:
                if isControl:
                    control += char
                else:
                    self.tokenized.append(petsciiMapper.get_petscii(ord(char)))

    def append_ushort(self, value: int) -> None:
        """Tokenize and append the specified value as a 16 bit little endian byte array"""
        self.tokenized += little_endian_short(value)

    # Handles control characters of the form "{name}", converting
    # into appropriate sequence of bytes
    def _process_controls_chars(self, control: str) -> bytes:
        # Handle strings like "{24 spaces}"
        count = 1
        control_name = ''
        components = control.split()

        if len(components) > 1:
            count = int(components[0])
            control_name = components[1]
        else:
            control_name = components[0]

        # Do the actual conversion
        control_code = controlCharsMapper.get_code(control_name)
        data = bytearray()
        for x in range(count):
            data.append(control_code)

        return bytes(data)
