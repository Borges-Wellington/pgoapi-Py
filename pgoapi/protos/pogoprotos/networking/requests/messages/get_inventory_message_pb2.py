# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/get_inventory_message.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (
    lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='pogoprotos/networking/requests/messages/get_inventory_message.proto',
    package='pogoprotos.networking.requests.messages',
    syntax='proto3',
    serialized_pb=_b(
        '\nCpogoprotos/networking/requests/messages/get_inventory_message.proto\x12\'pogoprotos.networking.requests.messages\"H\n\x13GetInventoryMessage\x12\x19\n\x11last_timestamp_ms\x18\x01 \x01(\x03\x12\x16\n\x0eitem_been_seen\x18\x02 \x01(\x05\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_GETINVENTORYMESSAGE = _descriptor.Descriptor(
    name='GetInventoryMessage',
    full_name='pogoprotos.networking.requests.messages.GetInventoryMessage',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='last_timestamp_ms',
            full_name=
            'pogoprotos.networking.requests.messages.GetInventoryMessage.last_timestamp_ms',
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='item_been_seen',
            full_name=
            'pogoprotos.networking.requests.messages.GetInventoryMessage.item_been_seen',
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=112,
    serialized_end=184, )

DESCRIPTOR.message_types_by_name['GetInventoryMessage'] = _GETINVENTORYMESSAGE

GetInventoryMessage = _reflection.GeneratedProtocolMessageType(
    'GetInventoryMessage',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_GETINVENTORYMESSAGE,
        __module__=
        'pogoprotos.networking.requests.messages.get_inventory_message_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.GetInventoryMessage)
    ))
_sym_db.RegisterMessage(GetInventoryMessage)

# @@protoc_insertion_point(module_scope)
