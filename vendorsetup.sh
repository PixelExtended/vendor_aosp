lunch_others_targets=()
for device in $(cat vendor/aosp/pex.devices)
do
    for var in eng user userdebug; do
        lunch_others_targets+=("aosp_$device-$var")
    done
done
