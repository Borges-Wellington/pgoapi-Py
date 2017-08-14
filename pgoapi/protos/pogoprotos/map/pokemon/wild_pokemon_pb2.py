# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/map/pokemon/wild_pokemon.proto

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

from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='pogoprotos/map/pokemon/wild_pokemon.proto',
    package='pogoprotos.map.pokemon',
    syntax='proto3',
    serialized_pb=_b(
        '\n)pogoprotos/map/pokemon/wild_pokemon.proto\x12\x16pogoprotos.map.pokemon\x1a\"pogoprotos/data/pokemon_data.proto\"\xd5\x01\n\x0bWildPokemon\x12\x14\n\x0c\x65ncounter_id\x18\x01 \x01(\x06\x12\"\n\x1alast_modified_timestamp_ms\x18\x02 \x01(\x03\x12\x10\n\x08latitude\x18\x03 \x01(\x01\x12\x11\n\tlongitude\x18\x04 \x01(\x01\x12\x16\n\x0espawn_point_id\x18\x05 \x01(\t\x12\x32\n\x0cpokemon_data\x18\x07 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12\x1b\n\x13time_till_hidden_ms\x18\x0b \x01(\x05\x62\x06proto3'
    ),
    dependencies=[
        pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,
    ])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_WILDPOKEMON = _descriptor.Descriptor(
    name='WildPokemon',
    full_name='pogoprotos.map.pokemon.WildPokemon',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='encounter_id',
            full_name='pogoprotos.map.pokemon.WildPokemon.encounter_id',
            index=0,
            number=1,
            type=6,
            cpp_type=4,
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
            name='last_modified_timestamp_ms',
            full_name=
            'pogoprotos.map.pokemon.WildPokemon.last_modified_timestamp_ms',
            index=1,
            number=2,
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
            name='latitude',
            full_name='pogoprotos.map.pokemon.WildPokemon.latitude',
            index=2,
            number=3,
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
            name='longitude',
            full_name='pogoprotos.map.pokemon.WildPokemon.longitude',
            index=3,
            number=4,
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
            name='spawn_point_id',
            full_name='pogoprotos.map.pokemon.WildPokemon.spawn_point_id',
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='pokemon_data',
            full_name='pogoprotos.map.pokemon.WildPokemon.pokemon_data',
            index=5,
            number=7,
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
            name='time_till_hidden_ms',
            full_name='pogoprotos.map.pokemon.WildPokemon.time_till_hidden_ms',
            index=6,
            number=11,
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
    serialized_start=106,
    serialized_end=319, )

_WILDPOKEMON.fields_by_name[
    'pokemon_data'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
DESCRIPTOR.message_types_by_name['WildPokemon'] = _WILDPOKEMON

WildPokemon = _reflection.GeneratedProtocolMessageType(
    'WildPokemon',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_WILDPOKEMON,
        __module__='pogoprotos.map.pokemon.wild_pokemon_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.map.pokemon.WildPokemon)
    ))
_sym_db.RegisterMessage(WildPokemon)

# @@protoc_insertion_point(module_scope)
