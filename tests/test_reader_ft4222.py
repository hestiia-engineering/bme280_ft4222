# -*- coding: utf-8 -*-
# Copyright (c) 2018-2021 Richard Hull
# See LICENSE.rst for details.

from unittest.mock import Mock, MagicMock, ANY
from bme280.reader_ft4222 import reader_ft4222
import ft4222

def i2c_read_side_effect(byte_array):
    def inner(address, register, data, flag):
        print(data)
        # Reverse the byte array for little-endian order
        data[:len(byte_array)] = byte_array[::-1]
    return inner



i2c_bus = Mock(unsafe=True)


def setup_function(function):
    i2c_bus.reset_mock()

def test_unsigned_short():
    i2c_bus.i2c_read = MagicMock(side_effect=i2c_read_side_effect(bytearray([0xBE, 0xEF])))
    read = reader_ft4222(i2c_bus=i2c_bus, address=0x76)
    assert read.unsigned_short(register=0x19A) == 0xBEEF
    i2c_bus.i2c_read.assert_called_with(0x76, [0x19A], ANY, ft4222.I2CMaster.Flag.START_AND_STOP)

def test_signed_short():
    i2c_bus.i2c_read = MagicMock(side_effect=i2c_read_side_effect(bytearray([0xBA, 0xBE])))
    read = reader_ft4222(i2c_bus=i2c_bus, address=0x76)
    assert read.signed_short(register=0x19A) == 0xBABE - 0x10000
    i2c_bus.i2c_read.assert_called_with(0x76, [0x19A], ANY, ft4222.I2CMaster.Flag.START_AND_STOP)

def test_unsigned_byte():
    i2c_bus.i2c_read = MagicMock(side_effect=i2c_read_side_effect(bytearray([0xEE])))
    read = reader_ft4222(i2c_bus=i2c_bus, address=0x76)
    assert read.unsigned_byte(register=0x19A) == 0xEE
    i2c_bus.i2c_read.assert_called_with(0x76, [0x19A], ANY, ft4222.I2CMaster.Flag.START_AND_STOP)

def test_signed_byte():
    i2c_bus.i2c_read = MagicMock(side_effect=i2c_read_side_effect(bytearray([0xEE])))
    read = reader_ft4222(i2c_bus=i2c_bus, address=0x76)
    assert read.signed_byte(register=0x19A) == 0xEE - 0x100
    i2c_bus.i2c_read.assert_called_with(0x76, [0x19A], ANY, ft4222.I2CMaster.Flag.START_AND_STOP)
