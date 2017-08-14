# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/use_item_gym_response.proto

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
    name='pogoprotos/networking/responses/use_item_gym_response.proto',
    package='pogoprotos.networking.responses',
    syntax='proto3',
    serialized_pb=_b(
        '\n;pogoprotos/networking/responses/use_item_gym_response.proto\x12\x1fpogoprotos.networking.responses\"\xc4\x01\n\x12UseItemGymResponse\x12J\n\x06result\x18\x01 \x01(\x0e\x32:.pogoprotos.networking.responses.UseItemGymResponse.Result\x12\x12\n\nupdated_gp\x18\x02 \x01(\x03\"N\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x14\n\x10\x45RROR_CANNOT_USE\x10\x02\x12\x16\n\x12\x45RROR_NOT_IN_RANGE\x10\x03\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_USEITEMGYMRESPONSE_RESULT = _descriptor.EnumDescriptor(
    name='Result',
    full_name='pogoprotos.networking.responses.UseItemGymResponse.Result',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNSET', index=0, number=0, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='SUCCESS', index=1, number=1, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_CANNOT_USE',
            index=2,
            number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR_NOT_IN_RANGE',
            index=3,
            number=3,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=215,
    serialized_end=293, )
_sym_db.RegisterEnumDescriptor(_USEITEMGYMRESPONSE_RESULT)

_USEITEMGYMRESPONSE = _descriptor.Descriptor(
    name='UseItemGymResponse',
    full_name='pogoprotos.networking.responses.UseItemGymResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='result',
            full_name=
            'pogoprotos.networking.responses.UseItemGymResponse.result',
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
            name='updated_gp',
            full_name=
            'pogoprotos.networking.responses.UseItemGymResponse.updated_gp',
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _USEITEMGYMRESPONSE_RESULT,
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=97,
    serialized_end=293, )

_USEITEMGYMRESPONSE.fields_by_name[
    'result'].enum_type = _USEITEMGYMRESPONSE_RESULT
_USEITEMGYMRESPONSE_RESULT.containing_type = _USEITEMGYMRESPONSE
DESCRIPTOR.message_types_by_name['UseItemGymResponse'] = _USEITEMGYMRESPONSE

UseItemGymResponse = _reflection.GeneratedProtocolMessageType(
    'UseItemGymResponse',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_USEITEMGYMRESPONSE,
        __module__='pogoprotos.networking.responses.use_item_gym_response_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.UseItemGymResponse)
    ))
_sym_db.RegisterMessage(UseItemGymResponse)

# @@protoc_insertion_point(module_scope)
