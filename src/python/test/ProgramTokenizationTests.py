#**********************************************************************************
# Copyright (C) 2023 Craig Setera
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#**********************************************************************************

import sys
import unittest
from os import listdir
from os.path import dirname, join, realpath
from tempfile import NamedTemporaryFile

script_folder = realpath(join(dirname(__file__), '..'))
sys.path.insert(0, script_folder)

from cbm.ProgramTokenizer import ProgramTokenizer

class ProgramGenerationTests(unittest.TestCase):
    # Setup the testing
    def setUp(self) -> None:
        self.input_folder = join(script_folder, 'test', 'inputs')
        self.expected_folder = join(script_folder, 'test', 'expected')
        return super().setUp()

    # Test the generation for each of the BAS files, comparing against
    # the expected P00 file output
    def test_generations(self):
        for file_name in sorted(listdir(self.input_folder)):
            if file_name.endswith('.bas'):
                without_ext = file_name[:-4]
                input = join(self.input_folder, file_name)
                expected = join(self.expected_folder, without_ext + '.P00')
                target = NamedTemporaryFile(suffix='.p00', delete=False)

                print("Generating " + input + " => " + target.name);
                generator = ProgramTokenizer(dump_tokens=False) # file_name.endswith('TEST06.bas'))
                generator.generate(without_ext, input, target.name)
                self._assert_file_content_equal(expected, target.name)

    # Compare the contents of two files
    def _assert_file_content_equal(self, expected_file, actual_file):
        with open(expected_file, 'rb') as expected_file_bytes:
            with open(actual_file, 'rb') as actual_file_bytes:
                self.assertEqual(actual_file_bytes.read(), expected_file_bytes.read())

if __name__ == '__main__':
    unittest.main()
