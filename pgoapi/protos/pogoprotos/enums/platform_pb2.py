# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/platform.proto

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
    name='pogoprotos/enums/platform.proto',
    package='pogoprotos.enums',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x1fpogoprotos/enums/platform.proto\x12\x10pogoprotos.enums*R\n\x08Platform\x12\t\n\x05UNSET\x10\x00\x12\x07\n\x03IOS\x10\x01\x12\x0b\n\x07\x41NDROID\x10\x02\x12\x07\n\x03OSX\x10\x03\x12\x0b\n\x07WINDOWS\x10\x04\x12\x0f\n\x0b\x41PPLE_WATCH\x10\x05\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PLATFORM = _descriptor.EnumDescriptor(
    name='Platform',
    full_name='pogoprotos.enums.Platform',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNSET', index=0, number=0, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='IOS', index=1, number=1, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='ANDROID', index=2, number=2, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='OSX', index=3, number=3, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='WINDOWS', index=4, number=4, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='APPLE_WATCH', index=5, number=5, options=None, type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=53,
    serialized_end=135, )
_sym_db.RegisterEnumDescriptor(_PLATFORM)

Platform = enum_type_wrapper.EnumTypeWrapper(_PLATFORM)
UNSET = 0
IOS = 1
ANDROID = 2
OSX = 3
WINDOWS = 4
APPLE_WATCH = 5

DESCRIPTOR.enum_types_by_name['Platform'] = _PLATFORM

# @@protoc_insertion_point(module_scope)
