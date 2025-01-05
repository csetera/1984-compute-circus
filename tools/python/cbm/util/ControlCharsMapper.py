#**********************************************************************************
# Copyright (C) 2023 Craig Setera
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#**********************************************************************************

import inspect
from os.path import realpath, dirname, join

class ControlCharsMapper:
    """
        Maps control strings to the proper control character.
        For example, {red} mapping to the proper byte value for that string.
    """
    def __init__(self):
        class_folder = dirname(inspect.getsourcefile(ControlCharsMapper))
        config_file = realpath(join(class_folder, 'control_chars.txt'))
        self.mapping = self._read_config(config_file)

    def get_code(self, control: str) -> int:
        """Returns the control code for the given control string or 0 if not found"""
        return self.mapping.get(control.upper(), 0)

    def _read_config(self, config_file: str) -> dict:
        mapping = {}

        with open(config_file, 'r') as file:
            for line in file:
                line = line.strip()
                if len(line) > 0 and not line.startswith('#'):
                    components = line.split()
                    mapping[components[0].strip().upper()] = int(components[1].strip(), 16)

        return mapping
