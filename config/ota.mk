ifeq ($(PEX_BUILD_TYPE), OFFICIAL)
PEX_OTA_VERSION_CODE := thirteen

PRODUCT_PRODUCT_PROPERTIES += \
    org.pixelexperience.ota.version_code=$(PEX_OTA_VERSION_CODE)

PRODUCT_PACKAGES += \
    Updates
endif
