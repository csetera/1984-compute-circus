#**********************************************************************************
# Copyright (C) 2023 Craig Setera
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#**********************************************************************************

import inspect
from os.path import realpath, dirname, join

class KeywordTokenMapper:
    """
        Maps BASIC keywords to the proper token value.
        For example, "PRINT" mapping to the proper byte value for that string.
    """
    def __init__(self):
        class_folder = dirname(inspect.getsourcefile(KeywordTokenMapper))
        config_file = realpath(join(class_folder, 'keyword_tokens.txt'))
        self.mapping = self._read_config(config_file)

    def get_token(self, keyword: str) -> int:
        """Returns the token value for the given keyword or 0 if not found"""
        return self.mapping.get(keyword.upper(), 0)

    def _read_config(self, config_file: str) -> dict:
        mapping = {}

        with open(config_file, 'r') as file:
            for line in file:
                line = line.strip()
                if len(line) > 0 and not line.startswith('#'):
                    components = line.split()
                    mapping[components[0].strip()] = int(components[1].strip(), 16)

        return mapping
