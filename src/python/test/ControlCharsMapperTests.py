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
from cbm.util.ControlCharsMapper import ControlCharsMapper

class ControlCharsMapperTests(unittest.TestCase):
    def test_init(self):
        mapper = ControlCharsMapper()
        self.assertEqual(mapper.get_code('rvs'), 18)
        self.assertEqual(mapper.get_code('red'), 28)
        self.assertEqual(mapper.get_code('home'), 19)

if __name__ == '__main__':
    unittest.main()
