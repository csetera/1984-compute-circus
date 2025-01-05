#**********************************************************************************
# Copyright (C) 2023 Craig Setera
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#**********************************************************************************

import inspect
from os.path import realpath, dirname, join

class PetsciiMapper:
    """ Maps between ASCII/UTF-8 values and PETSCII equalivalents"""

    def __init__(self):
        class_folder = dirname(inspect.getsourcefile(PetsciiMapper))
        config_file = realpath(join(class_folder, 'petscii.txt'))
        self.mapping = self._read_config(config_file)

    def get_petscii(self, unicode: int) -> int:
        """Returns the PETSCII value for the given ASCII value or 0 if not found"""
        return self.mapping.get(unicode, 0)

    def _read_config(self, config_file: str) -> dict:
        mapping = {}

        with open(config_file, 'r') as file:
            for line in file:
                line = line.strip()
                if not line.startswith('#'):
                    components = line.split()
                    petscii = int(components[0].strip(), 16)

                    if len(components) > 2:
                        unicode = int(components[1].strip(), 16)
                        mapping[unicode] = petscii

        return mapping
