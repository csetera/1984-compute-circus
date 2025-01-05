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
from cbm.util.PetsciiMapper import PetsciiMapper

class PetsciiMapperTests(unittest.TestCase):
    def test_init(self):
        mapper = PetsciiMapper()
        self.assertEqual(mapper.get_petscii(0x000D), 0x0D)
        self.assertEqual(mapper.get_petscii(0x00A3), 0x5C)

if __name__ == '__main__':
    unittest.main()
