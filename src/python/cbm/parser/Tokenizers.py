#**********************************************************************************
# Copyright (C) 2023 Craig Setera
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#**********************************************************************************

from cbm.parser.TokenBuffer import TokenBuffer

#
# https://www.c64-wiki.com/wiki/BASIC_token
#

class Tokenizer:
    """Default tokenizer for the parser.  This tokenizer emits no tokens."""
    def __init__(self, ast) -> None:
        self.ast = ast

    def tokenize(self) -> bytes:
        """Tokenize the AST into a byte array"""
        buffer = TokenBuffer()
        self.tokenize_into(buffer)
        return bytes(buffer)

    def tokenize_into(self, buffer: TokenBuffer) -> None:
        """Tokenize the AST into the TokenBuffer"""
        pass

    def tokenize_list(self, buffer: TokenBuffer, items) -> None:
        """Tokenize a list of Tokenizable items into the TokenBuffer"""
        if len(items) == 0:
            return

        temp = TokenBuffer()
        for item in items:
            if len(temp) > 0:
                temp.append_string(',')

            if isinstance(item, Tokenizer):
                item.tokenize_into(temp)

        buffer.append_bytes(bytes(temp))
