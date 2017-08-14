# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/filter.proto

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
    name='pogoprotos/enums/filter.proto',
    package='pogoprotos.enums',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x1dpogoprotos/enums/filter.proto\x12\x10pogoprotos.enums*j\n\x06\x46ilter\x12\x10\n\x0cUNSET_FILTER\x10\x00\x12\x07\n\x03\x41LL\x10\x01\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x02\x12\t\n\x05OWNED\x10\x03\x12\x0c\n\x08\x46\x45\x41TURED\x10\x04\x12\x0f\n\x0bPURCHASABLE\x10\x05\x12\x0e\n\nUNLOCKABLE\x10\x06\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_FILTER = _descriptor.EnumDescriptor(
    name='Filter',
    full_name='pogoprotos.enums.Filter',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNSET_FILTER', index=0, number=0, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='ALL', index=1, number=1, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='DEFAULT', index=2, number=2, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='OWNED', index=3, number=3, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='FEATURED', index=4, number=4, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='PURCHASABLE', index=5, number=5, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='UNLOCKABLE', index=6, number=6, options=None, type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=51,
    serialized_end=157, )
_sym_db.RegisterEnumDescriptor(_FILTER)

Filter = enum_type_wrapper.EnumTypeWrapper(_FILTER)
UNSET_FILTER = 0
ALL = 1
DEFAULT = 2
OWNED = 3
FEATURED = 4
PURCHASABLE = 5
UNLOCKABLE = 6

DESCRIPTOR.enum_types_by_name['Filter'] = _FILTER

# @@protoc_insertion_point(module_scope)
