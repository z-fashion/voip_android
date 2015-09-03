
# Copyright (c) 2011 The WebRTC project authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.  All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.

{
  'includes': [
      '../../../build/common.gypi',
  ],
 
  'targets': [
     {
       'target_name': 'libvoip',
          'type': 'loadable_module',
          'dependencies': [
              '<(webrtc_root)/webrtc.gyp:*',
          ],
          'include_dirs': [
              '<(webrtc_root)/../',
        ],
        'sources': [
            'video_renderer_jni.cc',
            'voip_jni.cc',	
            'WebRTC.cc',
            'av_send_stream.cc',
            'av_receive_stream.cc',
            'audio_send_stream.cc',
            "audio_receive_stream.cc",
            'classreferenceholder.cc',
            'jni_helpers.cc',
            'util.cc',
            'on_load.cc',
        ],
        'link_settings': {
            'libraries': [
                '-landroid',
                '-llog',
                '-lGLESv2',
                '-lOpenSLES',
            ],
        },
        'variables': {
            # This library uses native JNI exports; tell GYP so that the
            # required symbols will be kept.
            'use_native_jni_exports': 1,
        },
    },
  ], # targets
}
