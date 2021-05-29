#!/usr/bin/env bash
# Authored By : @https://t.me/Immanuel_Raj

DEVICE=$1
TYPE=$2
. build/envsetup.sh

if [ $# -lt 2 ]; then
    echo "Missing mandatory parameters it must be like this :- bash build.sh jasmine_sprout userdebug/eng/user"
    exit 1
fi

lunch legion_$DEVICE-$TYPE
make installclean
mka bacon
