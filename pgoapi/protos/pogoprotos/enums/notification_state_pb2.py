# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/notification_state.proto

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
    name='pogoprotos/enums/notification_state.proto',
    package='pogoprotos.enums',
    syntax='proto3',
    serialized_pb=_b(
        '\n)pogoprotos/enums/notification_state.proto\x12\x10pogoprotos.enums*0\n\x11NotificationState\x12\x0f\n\x0bUNSET_STATE\x10\x00\x12\n\n\x06VIEWED\x10\x01\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_NOTIFICATIONSTATE = _descriptor.EnumDescriptor(
    name='NotificationState',
    full_name='pogoprotos.enums.NotificationState',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNSET_STATE', index=0, number=0, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='VIEWED', index=1, number=1, options=None, type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=63,
    serialized_end=111, )
_sym_db.RegisterEnumDescriptor(_NOTIFICATIONSTATE)

NotificationState = enum_type_wrapper.EnumTypeWrapper(_NOTIFICATIONSTATE)
UNSET_STATE = 0
VIEWED = 1

DESCRIPTOR.enum_types_by_name['NotificationState'] = _NOTIFICATIONSTATE

# @@protoc_insertion_point(module_scope)
