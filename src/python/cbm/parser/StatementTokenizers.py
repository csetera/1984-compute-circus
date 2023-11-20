#**********************************************************************************
# Copyright (C) 2023 Craig Setera
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#**********************************************************************************

from cbm.parser.Tokenizers import Tokenizer
from cbm.parser.TokenBuffer import TokenBuffer

class DataStatementTokenizer(Tokenizer):
    """Tokenization of DATA statements of BASIC code"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        (keyword, *items) = self.ast
        buffer.append_keyword('DATA')
        self.tokenize_list(buffer, items[0])

class LineTokenizer(Tokenizer):
    """Tokenization of lines of BASIC code"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        (line, *statements) = self.ast

        buffer.append_ushort(int(line))
        for statement in statements[0]:
            if isinstance(statement, Tokenizer):
                statement.tokenize_into(buffer)

        buffer.append_byte(0)

class ForStatementTokenizer(Tokenizer):
    """Tokenization of FOR statements of BASIC code"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        (keyword, identifer, operator, start, to, end, *step) = self.ast
        buffer.append_keyword(keyword)
        identifer.tokenize_into(buffer)
        buffer.append_keyword(operator)
        start.tokenize_into(buffer)
        buffer.append_keyword(to)
        end.tokenize_into(buffer)

class NextStatementTokenizer(Tokenizer):
    """Tokenization of NEXT statements of BASIC code"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        (keyword, *identifiers) = self.ast
        buffer.append_keyword(keyword)
        self.tokenize_list(buffer, identifiers[0])

class PrintStatementTokenizer(Tokenizer):
    """Tokenization of PRINT statements of BASIC code"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        buffer.append_keyword('PRINT')

        (keyword, *print_list) = self.ast
        for element in print_list:
            if (isinstance(element, Tokenizer)):
                element.tokenize_into(buffer)

class ReadStatementTokenizer(Tokenizer):
    """Tokenization of READ statements of BASIC code"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        (keyword, *identifiers) = self.ast
        buffer.append_keyword(keyword)
        self.tokenize_list(buffer, identifiers[0])

class SimpleStatementTokenizer(Tokenizer):
    """Tokenization of simple statements of BASIC code that consist of only keywords"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        (keyword, *rest) = self.ast
        buffer.append_keyword(keyword)

class StringTokenizer(Tokenizer):
    """Tokenization of strings"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        buffer.append_string(self.ast, True)
