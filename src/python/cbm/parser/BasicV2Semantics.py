#**********************************************************************************
# Copyright (C) 2023 Craig Setera
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#**********************************************************************************

from cbm.parser.ExpressionTokenizers import *
from cbm.parser.StatementTokenizers import *
from cbm.parser.Tokenizers import *

#
# https://tatsu.readthedocs.io/en/stable/semantics.html
#
class BasicV2Semantics:
    """Semantics support for the parsing of a BASIC program."""

    def constant(self, ast):
        """Wrap a constant AST into a tokenizer"""
        return ConstantExpressionTokenizer(ast)

    def data_statement(self, ast):
        """Wrap the data statement AST into a tokenizer"""
        return DataStatementTokenizer(ast)

    def for_statement(self, ast):
        """Wrap the for statement AST into a tokenizer"""
        return ForStatementTokenizer(ast)

    def get_statement(self, ast):
        """Wrap the get statement AST into a tokenizer"""
        return GetStatementTokenizer(ast)

    def if_statement(self, ast):
        """Wrap the if statement AST into a tokenizer"""
        return IfStatementTokenizer(ast)

    def id(self, ast):
        """Wrap the id AST into a tokenizer"""
        return IdExpressionTokenizer(ast)

    def line(self, ast):
        """Wrap the line AST into a tokenizer"""
        return LineTokenizer(ast)

    def next_statement(self, ast):
        """Wrap the next statement AST into a tokenizer"""
        return NextStatementTokenizer(ast)

    def print_statement(self, ast):
        """Wrap the print statement AST into a tokenizer"""
        return PrintStatementTokenizer(ast)

    def read_statement(self, ast):
        """Wrap the read statement AST into a tokenizer"""
        return ReadStatementTokenizer(ast)

    def remark_statement(self, ast):
        """Wrap the remark statement AST into a tokenizer"""
        return RemarkStatementTokenizer(ast)

    def simp_value_expression(self, ast):
        """Wrap the simple value expression AST into a tokenizer"""
        return SimpleValueExpressionTokenizer(ast)

    def simple_statement(self, ast):
        """Wrap the simple statement AST into a tokenizer"""
        return SimpleStatementTokenizer(ast)

    def single_expr_stmt(self, ast):
        """Wrap the single expression statement AST into a tokenizer"""
        return SingleExpressionStatementTokenizer(ast)

    def string(self, ast):
        """Collapse the full definition of the string down to a full representation"""
        contents = ''.join(ast[1])
        return StringTokenizer(f'"{contents}"')
