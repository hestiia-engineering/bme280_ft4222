#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ft4222

class reader_ft4222(object):
    """
    Wraps a ft4222 I2C instance to provide methods for reading
    signed/unsigned bytes and 16-bit words
    """
    def __init__(self, i2c_bus: ft4222.FT4222, address: int, endianness = 'little'):
        self._address = address
        self._i2c_bus = i2c_bus
        self._endianness = endianness
        try:
            # Set read and write timeouts to 2 seconds
            i2c_bus.setTimeouts(200, 200)
            # Initialize I2C master at 100kHz
            i2c_bus.i2cMaster_Init(100000)
        except ft4222.FT2XXDeviceError as e:
            print(e)

    def read_register(self, register, bytesToRead):
        # Set register
        self._i2c_bus.i2cMaster_Write(self._address, bytearray([register]))
        # Read data
        data = self._i2c_bus.i2cMaster_Read(self._address, bytesToRead)
        return data
    
    def unsigned_short(self, register):
        data = self.read_register(register, 2)
        value = int.from_bytes(data, self._endianness)
        return value & 0xffff

    def signed_short(self, register):
        word = self.unsigned_short(register)
        return word if word < 0x8000 else word - 0x10000

    def unsigned_byte(self, register):
        data = self.read_register(register, 1)
        value = int.from_bytes(data, self._endianness)
        return value & 0xff

    def signed_byte(self, register):
        byte = self.unsigned_byte(register) & 0xff
        return byte if byte < 0x80 else byte - 0x100
