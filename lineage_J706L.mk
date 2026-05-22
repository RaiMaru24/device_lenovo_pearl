#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base.mk)

# Inherit from J706L device
$(call inherit-product, device/lenovo/J706L/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_DEVICE := J706L
PRODUCT_NAME := lineage_J706L
PRODUCT_BRAND := Lenovo
PRODUCT_MODEL := Lenovo TB-J706L
PRODUCT_MANUFACTURER := android-lenovo

PRODUCT_GMS_CLIENTID_BASE := android-lenovo

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="TB-J706L-user 11 RKQ1.210518.002 TB-J706L_USR_S630599_2308281652_Q00067_ROW release-keys" \
    BuildFingerprint=Lenovo/TB-J706L/J706L:11/RKQ1.210518.002/TB-J706L_USR_S630599_2308281652_Q00067_ROW:user/release-keys
