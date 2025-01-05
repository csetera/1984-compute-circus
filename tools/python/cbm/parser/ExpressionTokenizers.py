#**********************************************************************************
# Copyright (C) 2023 Craig Setera
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#**********************************************************************************

from cbm.parser.Tokenizers import Tokenizer
from cbm.parser.TokenBuffer import TokenBuffer

class ArithmeticExpressionTokenizer(Tokenizer):
    """Tokenize an arithmetic expression"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        if isinstance(self.ast, Tokenizer):
            self.ast.tokenize_into(buffer)
        else:
            if len(self.ast) == 1:
                self.ast[0].tokenize_into(buffer)
            else:
                (first, keyword, second) = self.ast
                first.tokenize_into(buffer)
                buffer.append_keyword(keyword)
                second.tokenize_into(buffer)

class ConstantExpressionTokenizer(Tokenizer):
   """Tokenize a constant value"""
   def tokenize_into(self, buffer: TokenBuffer) -> None:
        if isinstance(self.ast, Tokenizer):
            self.ast.tokenize_into(buffer)
        else:
            buffer.append_string(self.ast)

class IdExpressionTokenizer(Tokenizer):
    """Tokenize an identifier"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        buffer.append_string(self.ast)

class SimpleValueExpressionTokenizer(Tokenizer):
    """Tokenize a simple value expression"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        (function, *rest) = self.ast
        buffer.append_keyword(function)

class ValueExpressionTokenizer(Tokenizer):
    """Tokenize a value"""
    def tokenize_into(self, buffer: TokenBuffer) -> None:
        (first, *rest) = self.ast
        if isinstance(first, Tokenizer):
            first.tokenize_into(buffer)
        else:
            buffer.append_string(first)