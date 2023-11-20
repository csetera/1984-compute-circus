#**********************************************************************************
# Copyright (C) 2023 Craig Setera
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#**********************************************************************************

from os.path import join, dirname, realpath
from tatsu import compile

class BasicV2Parser:
    """Wrapper for parsing the BASIC code"""
    def __init__(self) -> None:
        grammer_file = realpath(join(dirname(__file__), 'BasicV2.ebnf'))
        with open(grammer_file) as f:
            grammar = f.read()

        self.parser = compile(grammar, asmodel=True)

    def parse(self, source: str, semantics: any):
        """Dos the parsing using the specific semantics, returning the AST result"""
        return self.parser.parse(source, semantics=semantics)
