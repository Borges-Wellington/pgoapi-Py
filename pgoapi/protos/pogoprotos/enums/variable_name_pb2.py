# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/variable_name.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/variable_name.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n$pogoprotos/enums/variable_name.proto\x12\x10pogoprotos.enums*\x9f\x04\n\x0cVariableName\x12\x16\n\x12UNSET_VariableName\x10\x00\x12\r\n\tCODE_NAME\x10\x01\x12\x08\n\x04TEAM\x10\x02\x12\t\n\x05LEVEL\x10\x03\x12\x0e\n\nEXPERIENCE\x10\x04\x12\x14\n\x10POKECOIN_BALANCE\x10\x05\x12\x14\n\x10STARDUST_BALANCE\x10\x06\x12\t\n\x05\x45MAIL\x10\x07\x12\x10\n\x0cLOGIN_METHOD\x10\x08\x12\x0b\n\x06GYM_ID\x10\xe8\x07\x12\r\n\x08GYM_NAME\x10\xe9\x07\x12\x14\n\x0fPOKEMON_DISPLAY\x10\xea\x07\x12\x19\n\x14POKEDEX_ENTRY_NUMBER\x10\xeb\x07\x12\x0f\n\nPOKEMON_ID\x10\xec\x07\x12\x15\n\x10POKEMON_NICKNAME\x10\xed\x07\x12\x1c\n\x17GYM_BADGE_EARNED_POINTS\x10\xee\x07\x12\x17\n\x12GYM_BADGE_PROGRESS\x10\xef\x07\x12\x13\n\x0eGYM_BADGE_RANK\x10\xf0\x07\x12\x18\n\x13GYM_BADGE_IMAGE_URL\x10\xf1\x07\x12\x17\n\x12GYM_BADGE_LEVEL_UP\x10\xf2\x07\x12\x15\n\x10POKECOIN_AWARDED\x10\xf3\x07\x12\x1b\n\x16POKECOIN_AWARDED_TODAY\x10\xf4\x07\x12\x17\n\x12MAX_DAILY_POKECOIN\x10\xf5\x07\x12\x10\n\x0b\x42\x41TTLES_WON\x10\xf6\x07\x12\x11\n\x0c\x42\x41TTLES_LOST\x10\xf7\x07\x12\x14\n\x0f\x44\x45PLOYED_MILLIS\x10\xf8\x07\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_VARIABLENAME = _descriptor.EnumDescriptor(
  name='VariableName',
  full_name='pogoprotos.enums.VariableName',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_VariableName', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CODE_NAME', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEAM', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEVEL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPERIENCE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKECOIN_BALANCE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STARDUST_BALANCE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMAIL', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOGIN_METHOD', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_ID', index=9, number=1000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_NAME', index=10, number=1001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_DISPLAY', index=11, number=1002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEDEX_ENTRY_NUMBER', index=12, number=1003,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_ID', index=13, number=1004,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_NICKNAME', index=14, number=1005,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_BADGE_EARNED_POINTS', index=15, number=1006,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_BADGE_PROGRESS', index=16, number=1007,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_BADGE_RANK', index=17, number=1008,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_BADGE_IMAGE_URL', index=18, number=1009,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_BADGE_LEVEL_UP', index=19, number=1010,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKECOIN_AWARDED', index=20, number=1011,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKECOIN_AWARDED_TODAY', index=21, number=1012,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX_DAILY_POKECOIN', index=22, number=1013,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATTLES_WON', index=23, number=1014,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATTLES_LOST', index=24, number=1015,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEPLOYED_MILLIS', index=25, number=1016,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=59,
  serialized_end=602,
)
_sym_db.RegisterEnumDescriptor(_VARIABLENAME)

VariableName = enum_type_wrapper.EnumTypeWrapper(_VARIABLENAME)
UNSET_VariableName = 0
CODE_NAME = 1
TEAM = 2
LEVEL = 3
EXPERIENCE = 4
POKECOIN_BALANCE = 5
STARDUST_BALANCE = 6
EMAIL = 7
LOGIN_METHOD = 8
GYM_ID = 1000
GYM_NAME = 1001
POKEMON_DISPLAY = 1002
POKEDEX_ENTRY_NUMBER = 1003
POKEMON_ID = 1004
POKEMON_NICKNAME = 1005
GYM_BADGE_EARNED_POINTS = 1006
GYM_BADGE_PROGRESS = 1007
GYM_BADGE_RANK = 1008
GYM_BADGE_IMAGE_URL = 1009
GYM_BADGE_LEVEL_UP = 1010
POKECOIN_AWARDED = 1011
POKECOIN_AWARDED_TODAY = 1012
MAX_DAILY_POKECOIN = 1013
BATTLES_WON = 1014
BATTLES_LOST = 1015
DEPLOYED_MILLIS = 1016


DESCRIPTOR.enum_types_by_name['VariableName'] = _VARIABLENAME


# @@protoc_insertion_point(module_scope)
