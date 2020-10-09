# Set all versions
PEX_BUILD_TYPE ?= UNOFFICIAL
PEX_VERSION := 2.0

CUSTOM_DATE_YEAR := $(shell date -u +%Y)
CUSTOM_DATE_MONTH := $(shell date -u +%m)
CUSTOM_DATE_DAY := $(shell date -u +%d)
CUSTOM_DATE_HOUR := $(shell date -u +%H)
CUSTOM_DATE_MINUTE := $(shell date -u +%M)
CUSTOM_BUILD_DATE_UTC := $(shell date -d '$(CUSTOM_DATE_YEAR)-$(CUSTOM_DATE_MONTH)-$(CUSTOM_DATE_DAY) $(CUSTOM_DATE_HOUR):$(CUSTOM_DATE_MINUTE) UTC' +%s)
CUSTOM_BUILD_DATE := $(CUSTOM_DATE_YEAR)$(CUSTOM_DATE_MONTH)$(CUSTOM_DATE_DAY)-$(CUSTOM_DATE_HOUR)$(CUSTOM_DATE_MINUTE)

CUSTOM_PLATFORM_VERSION := 11

TARGET_PRODUCT_SHORT := $(subst aosp_,,$(CUSTOM_BUILD))

CUSTOM_VERSION := PixelExtended_$(CUSTOM_BUILD)-$(CUSTOM_PLATFORM_VERSION)-$(CUSTOM_BUILD_DATE)-$(PEX_BUILD_TYPE)
CUSTOM_VERSION_PROP := eleven

PRODUCT_GENERIC_PROPERTIES += \
    org.pex.version=$(PEX_VERSION) \
    org.pex.version.prop=$(CUSTOM_VERSION_PROP) \
    org.pex.version.display=$(CUSTOM_VERSION) \
    org.pex.build_date=$(CUSTOM_BUILD_DATE) \
    org.pex.build_date_utc=$(CUSTOM_BUILD_DATE_UTC) \
    org.pex.build_type=$(PEX_BUILD_TYPE)
