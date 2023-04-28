# -*- coding: utf-8 -*-

from unittest.mock import Mock, MagicMock
import ft4222
from bme280_ft4222.reader_ft4222 import reader_ft4222

i2c_bus = Mock(unsafe=True)

def setup_function(function):
    i2c_bus.reset_mock()

def test_unsigned_short():
    read = reader_ft4222(i2c_bus=i2c_bus, address=0x76)
    i2c_bus.i2cMaster_Read.return_value = [0xEF, 0xBE]
    assert read.unsigned_short(register=0xD0) == 0xBEEF
    i2c_bus.i2cMaster_Write.assert_called_with(0x76, bytearray([0xD0]))
    i2c_bus.i2cMaster_Read.assert_called_with(0x76, 2)

def test_signed_short():
    read = reader_ft4222(i2c_bus=i2c_bus, address=0x76)
    i2c_bus.i2cMaster_Read.return_value = [0xBE, 0xBA]
    assert read.signed_short(register=0xD0) == 0xBABE - 0x10000
    i2c_bus.i2cMaster_Write.assert_called_with(0x76, bytearray([0xD0]))
    i2c_bus.i2cMaster_Read.assert_called_with(0x76, 2)

def test_unsigned_byte():
    read = reader_ft4222(i2c_bus=i2c_bus, address=0x76)
    i2c_bus.i2cMaster_Read.return_value = [0xEE]
    assert read.unsigned_byte(register=0xD0) == 0xEE
    i2c_bus.i2cMaster_Write.assert_called_with(0x76, bytearray([0xD0]))
    i2c_bus.i2cMaster_Read.assert_called_with(0x76, 1)

def test_signed_byte():
    read = reader_ft4222(i2c_bus=i2c_bus, address=0x76)
    i2c_bus.i2cMaster_Read.return_value = [0xEE]
    assert read.signed_byte(register=0xD0) == 0xEE - 0x100
    i2c_bus.i2cMaster_Write.assert_called_with(0x76, bytearray([0xD0]))
    i2c_bus.i2cMaster_Read.assert_called_with(0x76, 1)
