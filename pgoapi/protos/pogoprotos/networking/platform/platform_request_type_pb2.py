# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/platform_request_type.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (
    lambda x: x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='pogoprotos/networking/platform/platform_request_type.proto',
    package='pogoprotos.networking.platform',
    syntax='proto3',
    serialized_pb=_b(
        '\n:pogoprotos/networking/platform/platform_request_type.proto\x12\x1epogoprotos.networking.platform*\xad\x01\n\x13PlatformRequestType\x12\x10\n\x0cMETHOD_UNSET\x10\x00\x12\x16\n\x12\x42UY_ITEM_POKECOINS\x10\x02\x12\x14\n\x10\x42UY_ITEM_ANDROID\x10\x03\x12\x10\n\x0c\x42UY_ITEM_IOS\x10\x04\x12\x13\n\x0fGET_STORE_ITEMS\x10\x05\x12\x1c\n\x18SEND_ENCRYPTED_SIGNATURE\x10\x06\x12\x11\n\rUNKNOWN_PTR_8\x10\x08\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PLATFORMREQUESTTYPE = _descriptor.EnumDescriptor(
    name='PlatformRequestType',
    full_name='pogoprotos.networking.platform.PlatformRequestType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='METHOD_UNSET', index=0, number=0, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='BUY_ITEM_POKECOINS',
            index=1,
            number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='BUY_ITEM_ANDROID',
            index=2,
            number=3,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='BUY_ITEM_IOS', index=3, number=4, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='GET_STORE_ITEMS', index=4, number=5, options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='SEND_ENCRYPTED_SIGNATURE',
            index=5,
            number=6,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='UNKNOWN_PTR_8', index=6, number=8, options=None, type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=95,
    serialized_end=268, )
_sym_db.RegisterEnumDescriptor(_PLATFORMREQUESTTYPE)

PlatformRequestType = enum_type_wrapper.EnumTypeWrapper(_PLATFORMREQUESTTYPE)
METHOD_UNSET = 0
BUY_ITEM_POKECOINS = 2
BUY_ITEM_ANDROID = 3
BUY_ITEM_IOS = 4
GET_STORE_ITEMS = 5
SEND_ENCRYPTED_SIGNATURE = 6
UNKNOWN_PTR_8 = 8

DESCRIPTOR.enum_types_by_name['PlatformRequestType'] = _PLATFORMREQUESTTYPE

# @@protoc_insertion_point(module_scope)
