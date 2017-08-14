# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/item/egg_incubator_attributes.proto

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

from pogoprotos.inventory import egg_incubator_type_pb2 as pogoprotos_dot_inventory_dot_egg__incubator__type__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='pogoprotos/settings/master/item/egg_incubator_attributes.proto',
    package='pogoprotos.settings.master.item',
    syntax='proto3',
    serialized_pb=_b(
        '\n>pogoprotos/settings/master/item/egg_incubator_attributes.proto\x12\x1fpogoprotos.settings.master.item\x1a-pogoprotos/inventory/egg_incubator_type.proto\"\x83\x01\n\x16\x45ggIncubatorAttributes\x12>\n\x0eincubator_type\x18\x01 \x01(\x0e\x32&.pogoprotos.inventory.EggIncubatorType\x12\x0c\n\x04uses\x18\x02 \x01(\x05\x12\x1b\n\x13\x64istance_multiplier\x18\x03 \x01(\x02\x62\x06proto3'
    ),
    dependencies=[
        pogoprotos_dot_inventory_dot_egg__incubator__type__pb2.DESCRIPTOR,
    ])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_EGGINCUBATORATTRIBUTES = _descriptor.Descriptor(
    name='EggIncubatorAttributes',
    full_name='pogoprotos.settings.master.item.EggIncubatorAttributes',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='incubator_type',
            full_name=
            'pogoprotos.settings.master.item.EggIncubatorAttributes.incubator_type',
            index=0,
            number=1,
            type=14,
            cpp_type=8,
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
            name='uses',
            full_name=
            'pogoprotos.settings.master.item.EggIncubatorAttributes.uses',
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
        _descriptor.FieldDescriptor(
            name='distance_multiplier',
            full_name=
            'pogoprotos.settings.master.item.EggIncubatorAttributes.distance_multiplier',
            index=2,
            number=3,
            type=2,
            cpp_type=6,
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
    serialized_start=147,
    serialized_end=278, )

_EGGINCUBATORATTRIBUTES.fields_by_name[
    'incubator_type'].enum_type = pogoprotos_dot_inventory_dot_egg__incubator__type__pb2._EGGINCUBATORTYPE
DESCRIPTOR.message_types_by_name[
    'EggIncubatorAttributes'] = _EGGINCUBATORATTRIBUTES

EggIncubatorAttributes = _reflection.GeneratedProtocolMessageType(
    'EggIncubatorAttributes',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_EGGINCUBATORATTRIBUTES,
        __module__=
        'pogoprotos.settings.master.item.egg_incubator_attributes_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.item.EggIncubatorAttributes)
    ))
_sym_db.RegisterMessage(EggIncubatorAttributes)

# @@protoc_insertion_point(module_scope)
