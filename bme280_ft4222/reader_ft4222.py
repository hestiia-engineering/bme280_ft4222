#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ft4222 import I2CMaster

class reader_ft4222(object):
    """
    Wraps a ft4222 I2C instance to provide methods for reading
    signed/unsigned bytes and 16-bit words
    """
    def __init__(self, i2c_bus, address):
        self._i2c_bus = i2c_bus
        self._address = address

    def unsigned_short(self, register):
        data = bytearray(2)
        self._i2c_bus.i2c_read(self._address, [register], data, I2CMaster.Flag.START_AND_STOP)
        return int.from_bytes(data, 'little')

    def signed_short(self, register):
        word = self.unsigned_short(register)
        return word if word < 0x8000 else word - 0x10000

    def unsigned_byte(self, register):
        data = bytearray(1)
        self._i2c_bus.i2c_read(self._address, [register], data, I2CMaster.Flag.START_AND_STOP)
        return data[0]

    def signed_byte(self, register):
        byte = self.unsigned_byte(register)
        return byte if byte < 0x80 else byte - 0x100
