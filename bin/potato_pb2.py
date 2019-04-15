# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: potato.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='potato.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cpotato.proto\" \n\x0cGreetRequest\x12\x10\n\x08hostname\x18\x01 \x01(\t\"\x1e\n\rGreetResponse\x12\r\n\x05greet\x18\x01 \x01(\t\"\xc0\x04\n\x0bHintRequest\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x14\n\x0c\x65lapsed_time\x18\x02 \x01(\x02\x12\x11\n\tnum_cores\x18\x03 \x01(\x05\x12\x18\n\x10\x61\x63tive_cpu_ratio\x18\x04 \x01(\x02\x12\x15\n\rmean_sm_ratio\x18\x05 \x01(\x02\x12\x14\n\x0cstd_sm_ratio\x18\x06 \x01(\x02\x12\x16\n\x0emean_mem_ratio\x18\x07 \x01(\x02\x12\x15\n\rstd_mem_ratio\x18\x08 \x01(\x02\x12\x17\n\x0fmean_disk_ratio\x18\t \x01(\x02\x12\x16\n\x0estd_disk_ratio\x18\n \x01(\x02\x12\x16\n\x0emean_net_ratio\x18\x0b \x01(\x02\x12\x15\n\rstd_net_ratio\x18\x0c \x01(\x02\x12\x13\n\x0bkernel_time\x18\r \x01(\x02\x12\x18\n\x10mean_kernel_time\x18\x0e \x01(\x02\x12\x14\n\x0clibcuda_time\x18\x0f \x01(\x02\x12\x19\n\x11mean_libcuda_time\x18\x10 \x01(\x02\x12\x10\n\x08h2d_time\x18\x11 \x01(\x02\x12\x10\n\x08\x64\x32h_time\x18\x12 \x01(\x02\x12\x10\n\x08\x64\x32\x64_time\x18\x13 \x01(\x02\x12\x11\n\tnccl_time\x18\x14 \x01(\x02\x12\x0e\n\x06h2d_bw\x18\x15 \x01(\x02\x12\x0e\n\x06\x64\x32h_bw\x18\x16 \x01(\x02\x12\x0e\n\x06\x64\x32\x64_bw\x18\x17 \x01(\x02\x12\x18\n\x10iter_kernel_time\x18\x18 \x01(\x02\x12\x16\n\x0eiter_copy_time\x18\x19 \x01(\x02\x12\x15\n\riter_cpu_time\x18\x1a \x01(\x02\"2\n\x0cHintResponse\x12\x0c\n\x04hint\x18\x01 \x01(\t\x12\x14\n\x0c\x64ocker_image\x18\x02 \x01(\t21\n\x05Greet\x12(\n\x05Greet\x12\r.GreetRequest\x1a\x0e.GreetResponse\"\x00\x32-\n\x04Hint\x12%\n\x04Hint\x12\x0c.HintRequest\x1a\r.HintResponse\"\x00\x62\x06proto3')
)




_GREETREQUEST = _descriptor.Descriptor(
  name='GreetRequest',
  full_name='GreetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostname', full_name='GreetRequest.hostname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=48,
)


_GREETRESPONSE = _descriptor.Descriptor(
  name='GreetResponse',
  full_name='GreetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='greet', full_name='GreetResponse.greet', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=80,
)


_HINTREQUEST = _descriptor.Descriptor(
  name='HintRequest',
  full_name='HintRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostname', full_name='HintRequest.hostname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elapsed_time', full_name='HintRequest.elapsed_time', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_cores', full_name='HintRequest.num_cores', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active_cpu_ratio', full_name='HintRequest.active_cpu_ratio', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean_sm_ratio', full_name='HintRequest.mean_sm_ratio', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='std_sm_ratio', full_name='HintRequest.std_sm_ratio', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean_mem_ratio', full_name='HintRequest.mean_mem_ratio', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='std_mem_ratio', full_name='HintRequest.std_mem_ratio', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean_disk_ratio', full_name='HintRequest.mean_disk_ratio', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='std_disk_ratio', full_name='HintRequest.std_disk_ratio', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean_net_ratio', full_name='HintRequest.mean_net_ratio', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='std_net_ratio', full_name='HintRequest.std_net_ratio', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kernel_time', full_name='HintRequest.kernel_time', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean_kernel_time', full_name='HintRequest.mean_kernel_time', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='libcuda_time', full_name='HintRequest.libcuda_time', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean_libcuda_time', full_name='HintRequest.mean_libcuda_time', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='h2d_time', full_name='HintRequest.h2d_time', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='d2h_time', full_name='HintRequest.d2h_time', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='d2d_time', full_name='HintRequest.d2d_time', index=18,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nccl_time', full_name='HintRequest.nccl_time', index=19,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='h2d_bw', full_name='HintRequest.h2d_bw', index=20,
      number=21, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='d2h_bw', full_name='HintRequest.d2h_bw', index=21,
      number=22, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='d2d_bw', full_name='HintRequest.d2d_bw', index=22,
      number=23, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iter_kernel_time', full_name='HintRequest.iter_kernel_time', index=23,
      number=24, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iter_copy_time', full_name='HintRequest.iter_copy_time', index=24,
      number=25, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iter_cpu_time', full_name='HintRequest.iter_cpu_time', index=25,
      number=26, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=659,
)


_HINTRESPONSE = _descriptor.Descriptor(
  name='HintResponse',
  full_name='HintResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hint', full_name='HintResponse.hint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='docker_image', full_name='HintResponse.docker_image', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=661,
  serialized_end=711,
)

DESCRIPTOR.message_types_by_name['GreetRequest'] = _GREETREQUEST
DESCRIPTOR.message_types_by_name['GreetResponse'] = _GREETRESPONSE
DESCRIPTOR.message_types_by_name['HintRequest'] = _HINTREQUEST
DESCRIPTOR.message_types_by_name['HintResponse'] = _HINTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GreetRequest = _reflection.GeneratedProtocolMessageType('GreetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GREETREQUEST,
  __module__ = 'potato_pb2'
  # @@protoc_insertion_point(class_scope:GreetRequest)
  ))
_sym_db.RegisterMessage(GreetRequest)

GreetResponse = _reflection.GeneratedProtocolMessageType('GreetResponse', (_message.Message,), dict(
  DESCRIPTOR = _GREETRESPONSE,
  __module__ = 'potato_pb2'
  # @@protoc_insertion_point(class_scope:GreetResponse)
  ))
_sym_db.RegisterMessage(GreetResponse)

HintRequest = _reflection.GeneratedProtocolMessageType('HintRequest', (_message.Message,), dict(
  DESCRIPTOR = _HINTREQUEST,
  __module__ = 'potato_pb2'
  # @@protoc_insertion_point(class_scope:HintRequest)
  ))
_sym_db.RegisterMessage(HintRequest)

HintResponse = _reflection.GeneratedProtocolMessageType('HintResponse', (_message.Message,), dict(
  DESCRIPTOR = _HINTRESPONSE,
  __module__ = 'potato_pb2'
  # @@protoc_insertion_point(class_scope:HintResponse)
  ))
_sym_db.RegisterMessage(HintResponse)



_GREET = _descriptor.ServiceDescriptor(
  name='Greet',
  full_name='Greet',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=713,
  serialized_end=762,
  methods=[
  _descriptor.MethodDescriptor(
    name='Greet',
    full_name='Greet.Greet',
    index=0,
    containing_service=None,
    input_type=_GREETREQUEST,
    output_type=_GREETRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREET)

DESCRIPTOR.services_by_name['Greet'] = _GREET


_HINT = _descriptor.ServiceDescriptor(
  name='Hint',
  full_name='Hint',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=764,
  serialized_end=809,
  methods=[
  _descriptor.MethodDescriptor(
    name='Hint',
    full_name='Hint.Hint',
    index=0,
    containing_service=None,
    input_type=_HINTREQUEST,
    output_type=_HINTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HINT)

DESCRIPTOR.services_by_name['Hint'] = _HINT

# @@protoc_insertion_point(module_scope)
