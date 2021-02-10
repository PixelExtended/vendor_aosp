ifneq ($(filter OFFICIAL CI,$(PEX_BUILD_TYPE)),)

PEX_OTA_VERSION_CODE := eleven

PRODUCT_GENERIC_PROPERTIES += \
    org.pex.ota.version_code=$(PEX_OTA_VERSION_CODE) \
    sys.ota.disable_uncrypt=1

PRODUCT_PACKAGES += \
    Updates
endif
