#**********************************************************************************
# Copyright (C) 2023 Craig Setera
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#**********************************************************************************

from cbm.util import little_endian_short
from cbm.parser.BasicV2Parser import BasicV2Parser
from cbm.parser.BasicV2Semantics import BasicV2Semantics
from hexdump import hexdump

BASIC_STARTING_ADDRESS = 2049

class ProgramTokenizer:
    """Tokenizer that tokenizes a BASIC program into a P00 file."""
    def __init__(self, dump_tokens: bool = False):
        # self.controlCharsMapper = ControlCharsMapper()
        # self.petsciiMapper = PetsciiMapper()
        self.parser = BasicV2Parser()
        self.dump_tokens = dump_tokens

    def generate(self, title: str, source: str, target: str):
        """Tokenize the specified source file and write the result to the specified target file"""
        with open(source, 'r') as srcFile:
            with open(target, 'wb') as targetFile:
                #
                # https://vice-emu.sourceforge.io/vice_17.html#SEC428 - P00 file
                # https://michaelcmartin.github.io/Ophis/book/x72.html = PRG file
                #
                self._write_header(title, targetFile)
                self._tokenize_code(srcFile.read(), targetFile)

    def _tokenize_code(self, code: str, targetFile):
        """Tokenize the specified source code and write the result to the specified target file"""
        lines = self.parser.parse(code, BasicV2Semantics())
        current_address = BASIC_STARTING_ADDRESS

        for line in lines:
            tokenized = line.tokenize()
            if self.dump_tokens:
                (line, *rest) = line.ast
                print("Line " + str(line) + ":")
                print(hexdump(tokenized))
                print()

            next_address = current_address + len(tokenized) + 2
            targetFile.write(little_endian_short(next_address))
            targetFile.write(tokenized)
            current_address = next_address

        targetFile.write(little_endian_short(0))

    def _write_header(self, title: str, targetFile):
        """Write the P00 file header to the specified target file"""
        title = title.upper()
        if len(title) > 16:
            title = title[:16]

        targetFile.write("C64File".encode('ascii'))
        targetFile.write(b'\0')
        targetFile.write(title.encode('ascii'))
        for x in range(18 - len(title)):
            targetFile.write(b'\0')

        targetFile.write(little_endian_short(BASIC_STARTING_ADDRESS))

