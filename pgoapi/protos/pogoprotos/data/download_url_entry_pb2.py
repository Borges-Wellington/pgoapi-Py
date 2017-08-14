# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/download_url_entry.proto

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
    name='pogoprotos/data/download_url_entry.proto',
    package='pogoprotos.data',
    syntax='proto3',
    serialized_pb=_b(
        '\n(pogoprotos/data/download_url_entry.proto\x12\x0fpogoprotos.data\"Q\n\x10\x44ownloadUrlEntry\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\x05\x12\x10\n\x08\x63hecksum\x18\x04 \x01(\x07\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_DOWNLOADURLENTRY = _descriptor.Descriptor(
    name='DownloadUrlEntry',
    full_name='pogoprotos.data.DownloadUrlEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='asset_id',
            full_name='pogoprotos.data.DownloadUrlEntry.asset_id',
            index=0,
            number=1,
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
            name='url',
            full_name='pogoprotos.data.DownloadUrlEntry.url',
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
        _descriptor.FieldDescriptor(
            name='size',
            full_name='pogoprotos.data.DownloadUrlEntry.size',
            index=2,
            number=3,
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
            name='checksum',
            full_name='pogoprotos.data.DownloadUrlEntry.checksum',
            index=3,
            number=4,
            type=7,
            cpp_type=3,
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
    serialized_start=61,
    serialized_end=142, )

DESCRIPTOR.message_types_by_name['DownloadUrlEntry'] = _DOWNLOADURLENTRY

DownloadUrlEntry = _reflection.GeneratedProtocolMessageType(
    'DownloadUrlEntry',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_DOWNLOADURLENTRY,
        __module__='pogoprotos.data.download_url_entry_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.data.DownloadUrlEntry)
    ))
_sym_db.RegisterMessage(DownloadUrlEntry)

# @@protoc_insertion_point(module_scope)
