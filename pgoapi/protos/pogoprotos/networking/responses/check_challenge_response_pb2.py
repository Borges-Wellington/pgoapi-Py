# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/check_challenge_response.proto

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
    name='pogoprotos/networking/responses/check_challenge_response.proto',
    package='pogoprotos.networking.responses',
    syntax='proto3',
    serialized_pb=_b(
        '\n>pogoprotos/networking/responses/check_challenge_response.proto\x12\x1fpogoprotos.networking.responses\"G\n\x16\x43heckChallengeResponse\x12\x16\n\x0eshow_challenge\x18\x01 \x01(\x08\x12\x15\n\rchallenge_url\x18\x02 \x01(\tb\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CHECKCHALLENGERESPONSE = _descriptor.Descriptor(
    name='CheckChallengeResponse',
    full_name='pogoprotos.networking.responses.CheckChallengeResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='show_challenge',
            full_name=
            'pogoprotos.networking.responses.CheckChallengeResponse.show_challenge',
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='challenge_url',
            full_name=
            'pogoprotos.networking.responses.CheckChallengeResponse.challenge_url',
            index=1,
            number=2,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=99,
    serialized_end=170, )

DESCRIPTOR.message_types_by_name[
    'CheckChallengeResponse'] = _CHECKCHALLENGERESPONSE

CheckChallengeResponse = _reflection.GeneratedProtocolMessageType(
    'CheckChallengeResponse',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_CHECKCHALLENGERESPONSE,
        __module__=
        'pogoprotos.networking.responses.check_challenge_response_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.CheckChallengeResponse)
    ))
_sym_db.RegisterMessage(CheckChallengeResponse)

# @@protoc_insertion_point(module_scope)
