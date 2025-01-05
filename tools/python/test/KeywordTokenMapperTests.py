#**********************************************************************************
# Copyright (C) 2023 Craig Setera
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#**********************************************************************************

import sys
import unittest
from os.path import dirname, join, realpath

script_folder = realpath(join(dirname(__file__), '..'))
sys.path.insert(0, script_folder)

from cbm.util.KeywordTokenMapper import KeywordTokenMapper

class PetsciiMapperTests(unittest.TestCase):
    def test_init(self):
        mapper = KeywordTokenMapper()
        self.assertEqual(mapper.get_token('IF'), 139)
        self.assertEqual(mapper.get_token('print'), 153)

if __name__ == '__main__':
    unittest.main()
