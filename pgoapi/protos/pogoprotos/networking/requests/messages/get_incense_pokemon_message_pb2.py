# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/get_incense_pokemon_message.proto

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
    name=
    'pogoprotos/networking/requests/messages/get_incense_pokemon_message.proto',
    package='pogoprotos.networking.requests.messages',
    syntax='proto3',
    serialized_pb=_b(
        '\nIpogoprotos/networking/requests/messages/get_incense_pokemon_message.proto\x12\'pogoprotos.networking.requests.messages\"M\n\x18GetIncensePokemonMessage\x12\x17\n\x0fplayer_latitude\x18\x01 \x01(\x01\x12\x18\n\x10player_longitude\x18\x02 \x01(\x01\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_GETINCENSEPOKEMONMESSAGE = _descriptor.Descriptor(
    name='GetIncensePokemonMessage',
    full_name=
    'pogoprotos.networking.requests.messages.GetIncensePokemonMessage',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='player_latitude',
            full_name=
            'pogoprotos.networking.requests.messages.GetIncensePokemonMessage.player_latitude',
            index=0,
            number=1,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='player_longitude',
            full_name=
            'pogoprotos.networking.requests.messages.GetIncensePokemonMessage.player_longitude',
            index=1,
            number=2,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
    serialized_start=118,
    serialized_end=195, )

DESCRIPTOR.message_types_by_name[
    'GetIncensePokemonMessage'] = _GETINCENSEPOKEMONMESSAGE

GetIncensePokemonMessage = _reflection.GeneratedProtocolMessageType(
    'GetIncensePokemonMessage',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_GETINCENSEPOKEMONMESSAGE,
        __module__=
        'pogoprotos.networking.requests.messages.get_incense_pokemon_message_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.GetIncensePokemonMessage)
    ))
_sym_db.RegisterMessage(GetIncensePokemonMessage)

# @@protoc_insertion_point(module_scope)
