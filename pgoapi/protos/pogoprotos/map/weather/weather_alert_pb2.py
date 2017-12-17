# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/map/weather/weather_alert.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/map/weather/weather_alert.proto',
  package='pogoprotos.map.weather',
  syntax='proto3',
  serialized_pb=_b('\n*pogoprotos/map/weather/weather_alert.proto\x12\x16pogoprotos.map.weather\"\x96\x01\n\x0cWeatherAlert\x12?\n\x08severity\x18\x01 \x01(\x0e\x32-.pogoprotos.map.weather.WeatherAlert.Severity\x12\x14\n\x0cwarn_weather\x18\x02 \x01(\x08\"/\n\x08Severity\x12\x08\n\x04NONE\x10\x00\x12\x0c\n\x08MODERATE\x10\x01\x12\x0b\n\x07\x45XTREME\x10\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_WEATHERALERT_SEVERITY = _descriptor.EnumDescriptor(
  name='Severity',
  full_name='pogoprotos.map.weather.WeatherAlert.Severity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODERATE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTREME', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=174,
  serialized_end=221,
)
_sym_db.RegisterEnumDescriptor(_WEATHERALERT_SEVERITY)


_WEATHERALERT = _descriptor.Descriptor(
  name='WeatherAlert',
  full_name='pogoprotos.map.weather.WeatherAlert',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='severity', full_name='pogoprotos.map.weather.WeatherAlert.severity', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='warn_weather', full_name='pogoprotos.map.weather.WeatherAlert.warn_weather', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WEATHERALERT_SEVERITY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=221,
)

_WEATHERALERT.fields_by_name['severity'].enum_type = _WEATHERALERT_SEVERITY
_WEATHERALERT_SEVERITY.containing_type = _WEATHERALERT
DESCRIPTOR.message_types_by_name['WeatherAlert'] = _WEATHERALERT

WeatherAlert = _reflection.GeneratedProtocolMessageType('WeatherAlert', (_message.Message,), dict(
  DESCRIPTOR = _WEATHERALERT,
  __module__ = 'pogoprotos.map.weather.weather_alert_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.map.weather.WeatherAlert)
  ))
_sym_db.RegisterMessage(WeatherAlert)


# @@protoc_insertion_point(module_scope)
