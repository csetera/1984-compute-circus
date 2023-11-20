#**********************************************************************************
# Copyright (C) 2023 Craig Setera
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#**********************************************************************************

from cbm.parser.Tokenizers import Tokenizer
from cbm.parser.TokenBuffer import TokenBuffer

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
