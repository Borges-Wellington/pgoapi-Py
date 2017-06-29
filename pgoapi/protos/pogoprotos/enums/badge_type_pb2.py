# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/badge_type.proto

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
  name='pogoprotos/enums/badge_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n!pogoprotos/enums/badge_type.proto\x12\x10pogoprotos.enums*\xec\x08\n\tBadgeType\x12\x0f\n\x0b\x42\x41\x44GE_UNSET\x10\x00\x12\x13\n\x0f\x42\x41\x44GE_TRAVEL_KM\x10\x01\x12\x19\n\x15\x42\x41\x44GE_POKEDEX_ENTRIES\x10\x02\x12\x17\n\x13\x42\x41\x44GE_CAPTURE_TOTAL\x10\x03\x12\x17\n\x13\x42\x41\x44GE_DEFEATED_FORT\x10\x04\x12\x17\n\x13\x42\x41\x44GE_EVOLVED_TOTAL\x10\x05\x12\x17\n\x13\x42\x41\x44GE_HATCHED_TOTAL\x10\x06\x12\x1b\n\x17\x42\x41\x44GE_ENCOUNTERED_TOTAL\x10\x07\x12\x1b\n\x17\x42\x41\x44GE_POKESTOPS_VISITED\x10\x08\x12\x1a\n\x16\x42\x41\x44GE_UNIQUE_POKESTOPS\x10\t\x12\x19\n\x15\x42\x41\x44GE_POKEBALL_THROWN\x10\n\x12\x16\n\x12\x42\x41\x44GE_BIG_MAGIKARP\x10\x0b\x12\x18\n\x14\x42\x41\x44GE_DEPLOYED_TOTAL\x10\x0c\x12\x1b\n\x17\x42\x41\x44GE_BATTLE_ATTACK_WON\x10\r\x12\x1d\n\x19\x42\x41\x44GE_BATTLE_TRAINING_WON\x10\x0e\x12\x1b\n\x17\x42\x41\x44GE_BATTLE_DEFEND_WON\x10\x0f\x12\x19\n\x15\x42\x41\x44GE_PRESTIGE_RAISED\x10\x10\x12\x1a\n\x16\x42\x41\x44GE_PRESTIGE_DROPPED\x10\x11\x12\x15\n\x11\x42\x41\x44GE_TYPE_NORMAL\x10\x12\x12\x17\n\x13\x42\x41\x44GE_TYPE_FIGHTING\x10\x13\x12\x15\n\x11\x42\x41\x44GE_TYPE_FLYING\x10\x14\x12\x15\n\x11\x42\x41\x44GE_TYPE_POISON\x10\x15\x12\x15\n\x11\x42\x41\x44GE_TYPE_GROUND\x10\x16\x12\x13\n\x0f\x42\x41\x44GE_TYPE_ROCK\x10\x17\x12\x12\n\x0e\x42\x41\x44GE_TYPE_BUG\x10\x18\x12\x14\n\x10\x42\x41\x44GE_TYPE_GHOST\x10\x19\x12\x14\n\x10\x42\x41\x44GE_TYPE_STEEL\x10\x1a\x12\x13\n\x0f\x42\x41\x44GE_TYPE_FIRE\x10\x1b\x12\x14\n\x10\x42\x41\x44GE_TYPE_WATER\x10\x1c\x12\x14\n\x10\x42\x41\x44GE_TYPE_GRASS\x10\x1d\x12\x17\n\x13\x42\x41\x44GE_TYPE_ELECTRIC\x10\x1e\x12\x16\n\x12\x42\x41\x44GE_TYPE_PSYCHIC\x10\x1f\x12\x12\n\x0e\x42\x41\x44GE_TYPE_ICE\x10 \x12\x15\n\x11\x42\x41\x44GE_TYPE_DRAGON\x10!\x12\x13\n\x0f\x42\x41\x44GE_TYPE_DARK\x10\"\x12\x14\n\x10\x42\x41\x44GE_TYPE_FAIRY\x10#\x12\x17\n\x13\x42\x41\x44GE_SMALL_RATTATA\x10$\x12\x11\n\rBADGE_PIKACHU\x10%\x12\x0f\n\x0b\x42\x41\x44GE_UNOWN\x10&\x12\x1e\n\x1a\x42\x41\x44GE_POKEDEX_ENTRIES_GEN2\x10\'\x12\x19\n\x15\x42\x41\x44GE_RAID_BATTLE_WON\x10(\x12\x1e\n\x1a\x42\x41\x44GE_LEGENDARY_BATTLE_WON\x10)\x12\x15\n\x11\x42\x41\x44GE_BERRIES_FED\x10*\x12\x18\n\x14\x42\x41\x44GE_HOURS_DEFENDED\x10+\x12\x16\n\x12\x42\x41\x44GE_PLACE_HOLDER\x10,\x12\x14\n\x0f\x42\x41\x44GE_EVENT_MIN\x10\xd0\x0f\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_BADGETYPE = _descriptor.EnumDescriptor(
  name='BadgeType',
  full_name='pogoprotos.enums.BadgeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BADGE_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TRAVEL_KM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_POKEDEX_ENTRIES', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_CAPTURE_TOTAL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_DEFEATED_FORT', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_EVOLVED_TOTAL', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_HATCHED_TOTAL', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_ENCOUNTERED_TOTAL', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_POKESTOPS_VISITED', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_UNIQUE_POKESTOPS', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_POKEBALL_THROWN', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_BIG_MAGIKARP', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_DEPLOYED_TOTAL', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_BATTLE_ATTACK_WON', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_BATTLE_TRAINING_WON', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_BATTLE_DEFEND_WON', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_PRESTIGE_RAISED', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_PRESTIGE_DROPPED', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_NORMAL', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_FIGHTING', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_FLYING', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_POISON', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_GROUND', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_ROCK', index=23, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_BUG', index=24, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_GHOST', index=25, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_STEEL', index=26, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_FIRE', index=27, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_WATER', index=28, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_GRASS', index=29, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_ELECTRIC', index=30, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_PSYCHIC', index=31, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_ICE', index=32, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_DRAGON', index=33, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_DARK', index=34, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_TYPE_FAIRY', index=35, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_SMALL_RATTATA', index=36, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_PIKACHU', index=37, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_UNOWN', index=38, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_POKEDEX_ENTRIES_GEN2', index=39, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_RAID_BATTLE_WON', index=40, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_LEGENDARY_BATTLE_WON', index=41, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_BERRIES_FED', index=42, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_HOURS_DEFENDED', index=43, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_PLACE_HOLDER', index=44, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BADGE_EVENT_MIN', index=45, number=2000,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=56,
  serialized_end=1188,
)
_sym_db.RegisterEnumDescriptor(_BADGETYPE)

BadgeType = enum_type_wrapper.EnumTypeWrapper(_BADGETYPE)
BADGE_UNSET = 0
BADGE_TRAVEL_KM = 1
BADGE_POKEDEX_ENTRIES = 2
BADGE_CAPTURE_TOTAL = 3
BADGE_DEFEATED_FORT = 4
BADGE_EVOLVED_TOTAL = 5
BADGE_HATCHED_TOTAL = 6
BADGE_ENCOUNTERED_TOTAL = 7
BADGE_POKESTOPS_VISITED = 8
BADGE_UNIQUE_POKESTOPS = 9
BADGE_POKEBALL_THROWN = 10
BADGE_BIG_MAGIKARP = 11
BADGE_DEPLOYED_TOTAL = 12
BADGE_BATTLE_ATTACK_WON = 13
BADGE_BATTLE_TRAINING_WON = 14
BADGE_BATTLE_DEFEND_WON = 15
BADGE_PRESTIGE_RAISED = 16
BADGE_PRESTIGE_DROPPED = 17
BADGE_TYPE_NORMAL = 18
BADGE_TYPE_FIGHTING = 19
BADGE_TYPE_FLYING = 20
BADGE_TYPE_POISON = 21
BADGE_TYPE_GROUND = 22
BADGE_TYPE_ROCK = 23
BADGE_TYPE_BUG = 24
BADGE_TYPE_GHOST = 25
BADGE_TYPE_STEEL = 26
BADGE_TYPE_FIRE = 27
BADGE_TYPE_WATER = 28
BADGE_TYPE_GRASS = 29
BADGE_TYPE_ELECTRIC = 30
BADGE_TYPE_PSYCHIC = 31
BADGE_TYPE_ICE = 32
BADGE_TYPE_DRAGON = 33
BADGE_TYPE_DARK = 34
BADGE_TYPE_FAIRY = 35
BADGE_SMALL_RATTATA = 36
BADGE_PIKACHU = 37
BADGE_UNOWN = 38
BADGE_POKEDEX_ENTRIES_GEN2 = 39
BADGE_RAID_BATTLE_WON = 40
BADGE_LEGENDARY_BATTLE_WON = 41
BADGE_BERRIES_FED = 42
BADGE_HOURS_DEFENDED = 43
BADGE_PLACE_HOLDER = 44
BADGE_EVENT_MIN = 2000


DESCRIPTOR.enum_types_by_name['BadgeType'] = _BADGETYPE


# @@protoc_insertion_point(module_scope)
