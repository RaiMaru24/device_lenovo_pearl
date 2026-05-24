#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

LOCAL_PATH := $(call my-dir)

ifeq ($(TARGET_DEVICE),pearl)
include $(call all-subdir-makefiles,$(LOCAL_PATH))
EGL_SYMLINKS := $(TARGET_OUT_VENDOR)/lib/
$(EGL_SYMLINKS): $(LOCAL_INSTALLED_MODULE)
	mkdir -p $@
	$(hide) ln -sf egl/libEGL_adreno.so $@/libEGL_adreno.so
	$(hide) ln -sf egl/libGLESv2_adreno.so $@/libGLESv2_adreno.so

ALL_DEFAULT_INSTALLED_MODULES += $(EGL_SYMLINKS)

EGL64_SYMLINKS := $(TARGET_OUT_VENDOR)/lib64/
$(EGL64_SYMLINKS): $(LOCAL_INSTALLED_MODULE)
	mkdir -p $@
	$(hide) ln -sf egl/libEGL_adreno.so $@/libEGL_adreno.so
	$(hide) ln -sf egl/libGLESv2_adreno.so $@/libGLESv2_adreno.so

ALL_DEFAULT_INSTALLED_MODULES += $(EGL64_SYMLINKS)
endif
