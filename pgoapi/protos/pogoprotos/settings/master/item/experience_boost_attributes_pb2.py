# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/item/experience_boost_attributes.proto

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
    name='pogoprotos/settings/master/item/experience_boost_attributes.proto',
    package='pogoprotos.settings.master.item',
    syntax='proto3',
    serialized_pb=_b(
        '\nApogoprotos/settings/master/item/experience_boost_attributes.proto\x12\x1fpogoprotos.settings.master.item\"M\n\x19\x45xperienceBoostAttributes\x12\x15\n\rxp_multiplier\x18\x01 \x01(\x02\x12\x19\n\x11\x62oost_duration_ms\x18\x02 \x01(\x05\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_EXPERIENCEBOOSTATTRIBUTES = _descriptor.Descriptor(
    name='ExperienceBoostAttributes',
    full_name='pogoprotos.settings.master.item.ExperienceBoostAttributes',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='xp_multiplier',
            full_name=
            'pogoprotos.settings.master.item.ExperienceBoostAttributes.xp_multiplier',
            index=0,
            number=1,
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
        _descriptor.FieldDescriptor(
            name='boost_duration_ms',
            full_name=
            'pogoprotos.settings.master.item.ExperienceBoostAttributes.boost_duration_ms',
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
    serialized_start=102,
    serialized_end=179, )

DESCRIPTOR.message_types_by_name[
    'ExperienceBoostAttributes'] = _EXPERIENCEBOOSTATTRIBUTES

ExperienceBoostAttributes = _reflection.GeneratedProtocolMessageType(
    'ExperienceBoostAttributes',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_EXPERIENCEBOOSTATTRIBUTES,
        __module__=
        'pogoprotos.settings.master.item.experience_boost_attributes_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.item.ExperienceBoostAttributes)
    ))
_sym_db.RegisterMessage(ExperienceBoostAttributes)

# @@protoc_insertion_point(module_scope)
