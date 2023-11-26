#**********************************************************************************
# Copyright (C) 2023 Craig Setera
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#**********************************************************************************

from cbm.parser.Tokenizers import Tokenizer
from cbm.parser.TokenBuffer import TokenBuffer

class GetStatementTokenizer(Tokenizer):
    """Tokenization of GET statements of BASIC code"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        (keyword, *rest) = self.ast
        buffer.append_keyword(keyword)

        if rest[0] == '#':
            buffer.append_ushort(0)
        else:
            rest[0].tokenize_into(buffer)

class DataStatementTokenizer(Tokenizer):
    """Tokenization of DATA statements of BASIC code"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        (keyword, *items) = self.ast
        buffer.append_keyword('DATA')
        self.tokenize_list(buffer, items[0])

class IfStatementTokenizer(Tokenizer):
    """Tokenization of IF statements of BASIC code"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        (keyword, expression, then, then_clause) = self.ast
        buffer.append_keyword(keyword)

        for item in expression:
            if isinstance(item, Tokenizer):
                item.tokenize_into(buffer)
            else:
                buffer.append_keyword(item)

        buffer.append_keyword(then)

        if isinstance(then_clause, Tokenizer):
            then_clause.tokenize_into(buffer)
        else:
            buffer.append_string(then_clause)

class LineTokenizer(Tokenizer):
    """Tokenization of lines of BASIC code"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        (line, *statements) = self.ast

        buffer.append_ushort(int(line))
        for index, statement in enumerate(statements[0]):
            if isinstance(statement, Tokenizer):
                if index != 0:
                    buffer.append_string(':')

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
