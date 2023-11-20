#**********************************************************************************
# Copyright (C) 2023 Craig Setera
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#**********************************************************************************

from struct import pack

def little_endian_short(value: int) -> bytes:
    """Convert the value to a two-byte little endian byte array"""
    return pack('<H', value)