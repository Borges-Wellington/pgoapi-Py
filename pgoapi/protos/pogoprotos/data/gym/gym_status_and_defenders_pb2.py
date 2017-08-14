# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/gym/gym_status_and_defenders.proto

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

from pogoprotos.map.fort import fort_data_pb2 as pogoprotos_dot_map_dot_fort_dot_fort__data__pb2
from pogoprotos.data.gym import gym_defender_pb2 as pogoprotos_dot_data_dot_gym_dot_gym__defender__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='pogoprotos/data/gym/gym_status_and_defenders.proto',
    package='pogoprotos.data.gym',
    syntax='proto3',
    serialized_pb=_b(
        '\n2pogoprotos/data/gym/gym_status_and_defenders.proto\x12\x13pogoprotos.data.gym\x1a#pogoprotos/map/fort/fort_data.proto\x1a&pogoprotos/data/gym/gym_defender.proto\"\x8a\x01\n\x15GymStatusAndDefenders\x12\x39\n\x12pokemon_fort_proto\x18\x01 \x01(\x0b\x32\x1d.pogoprotos.map.fort.FortData\x12\x36\n\x0cgym_defender\x18\x02 \x03(\x0b\x32 .pogoprotos.data.gym.GymDefenderb\x06proto3'
    ),
    dependencies=[
        pogoprotos_dot_map_dot_fort_dot_fort__data__pb2.DESCRIPTOR,
        pogoprotos_dot_data_dot_gym_dot_gym__defender__pb2.DESCRIPTOR,
    ])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_GYMSTATUSANDDEFENDERS = _descriptor.Descriptor(
    name='GymStatusAndDefenders',
    full_name='pogoprotos.data.gym.GymStatusAndDefenders',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='pokemon_fort_proto',
            full_name=
            'pogoprotos.data.gym.GymStatusAndDefenders.pokemon_fort_proto',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='gym_defender',
            full_name='pogoprotos.data.gym.GymStatusAndDefenders.gym_defender',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
    serialized_start=153,
    serialized_end=291, )

_GYMSTATUSANDDEFENDERS.fields_by_name[
    'pokemon_fort_proto'].message_type = pogoprotos_dot_map_dot_fort_dot_fort__data__pb2._FORTDATA
_GYMSTATUSANDDEFENDERS.fields_by_name[
    'gym_defender'].message_type = pogoprotos_dot_data_dot_gym_dot_gym__defender__pb2._GYMDEFENDER
DESCRIPTOR.message_types_by_name[
    'GymStatusAndDefenders'] = _GYMSTATUSANDDEFENDERS

GymStatusAndDefenders = _reflection.GeneratedProtocolMessageType(
    'GymStatusAndDefenders',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_GYMSTATUSANDDEFENDERS,
        __module__='pogoprotos.data.gym.gym_status_and_defenders_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.data.gym.GymStatusAndDefenders)
    ))
_sym_db.RegisterMessage(GymStatusAndDefenders)

# @@protoc_insertion_point(module_scope)
