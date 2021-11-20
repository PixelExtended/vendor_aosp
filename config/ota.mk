ifneq ($(filter OFFICIAL CI,$(PEX_BUILD_TYPE)),)
PRODUCT_PACKAGES += \
    Updates
endif
