# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/applied_item.proto

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

from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2
from pogoprotos.inventory.item import item_type_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__type__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='pogoprotos/inventory/applied_item.proto',
    package='pogoprotos.inventory',
    syntax='proto3',
    serialized_pb=_b(
        '\n\'pogoprotos/inventory/applied_item.proto\x12\x14pogoprotos.inventory\x1a\'pogoprotos/inventory/item/item_id.proto\x1a)pogoprotos/inventory/item/item_type.proto\"\xa0\x01\n\x0b\x41ppliedItem\x12\x32\n\x07item_id\x18\x01 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\x36\n\titem_type\x18\x02 \x01(\x0e\x32#.pogoprotos.inventory.item.ItemType\x12\x11\n\texpire_ms\x18\x03 \x01(\x03\x12\x12\n\napplied_ms\x18\x04 \x01(\x03\x62\x06proto3'
    ),
    dependencies=[
        pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,
        pogoprotos_dot_inventory_dot_item_dot_item__type__pb2.DESCRIPTOR,
    ])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_APPLIEDITEM = _descriptor.Descriptor(
    name='AppliedItem',
    full_name='pogoprotos.inventory.AppliedItem',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='item_id',
            full_name='pogoprotos.inventory.AppliedItem.item_id',
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
            name='item_type',
            full_name='pogoprotos.inventory.AppliedItem.item_type',
            index=1,
            number=2,
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
            name='expire_ms',
            full_name='pogoprotos.inventory.AppliedItem.expire_ms',
            index=2,
            number=3,
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
            name='applied_ms',
            full_name='pogoprotos.inventory.AppliedItem.applied_ms',
            index=3,
            number=4,
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
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=150,
    serialized_end=310, )

_APPLIEDITEM.fields_by_name[
    'item_id'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_APPLIEDITEM.fields_by_name[
    'item_type'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__type__pb2._ITEMTYPE
DESCRIPTOR.message_types_by_name['AppliedItem'] = _APPLIEDITEM

AppliedItem = _reflection.GeneratedProtocolMessageType(
    'AppliedItem',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_APPLIEDITEM,
        __module__='pogoprotos.inventory.applied_item_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.inventory.AppliedItem)
    ))
_sym_db.RegisterMessage(AppliedItem)

# @@protoc_insertion_point(module_scope)
