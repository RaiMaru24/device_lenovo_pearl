#!/usr/bin/env python3
"""
Script to remove missing files from proprietary-files.txt
"""

# List of files that were not found during extraction or marked as "already a package"
missing_files = [
    "system/app/SoterService/SoterService.apk",
    "product/app/PowerOffAlarm/PowerOffAlarm.apk",
    "system/framework/WfdCommon.jar",
    "system_ext/app/DeviceInfo/DeviceInfo.apk",
    "system_ext/app/QtiTelephonyService/QtiTelephonyService.apk",
    "system_ext/app/datastatusnotification/datastatusnotification.apk",
    "system_ext/app/embms/embms.apk",
    "system_ext/app/imssettings/imssettings.apk",
    "system_ext/priv-app/WfdService/WfdService.apk",
    "system_ext/priv-app/ims/ims.apk",
    "system_ext/priv-app/qcrilmsgtunnel/qcrilmsgtunnel.apk",
    "vendor/app/CneApp/CneApp.apk",
    "vendor/app/IWlanService/IWlanService.apk",
    "vendor/app/TimeService/TimeService.apk",
    "vendor/app/com.qualcomm.qti.gpudrivers.msmnile.api30/com.qualcomm.qti.gpudrivers.msmnile.api30.apk",
    "vendor/etc/vintf/manifest/android.hardware.gnss@2.1-service-qti.xml",
    "vendor/etc/vintf/manifest/android.hardware.neuralnetworks@1.3-service-qti-hta.xml",
    "vendor/etc/vintf/manifest/android.hardware.neuralnetworks@1.3-service-qti.xml",
    "vendor/etc/vintf/manifest/manifest_android.hardware.drm@1.3-service.widevine.xml",
    "vendor/etc/vintf/manifest/vendor.qti.gnss@4.0-service.xml",
    "system_ext/lib/fm_helium.so",
    "system_ext/lib/libfm-hci.so",
    "system_ext/lib/vendor.qti.hardware.fm@1.0.so",
    "system_ext/lib64/fm_helium.so",
    "system_ext/lib64/libaptXHD_encoder.so",
    "system_ext/lib64/libaptX_encoder.so",
    "system_ext/lib64/libfm-hci.so",
    "system_ext/lib64/vendor.qti.hardware.fm@1.0.so",
    "vendor/app/com.qualcomm.qti.gpudrivers.msmnile.api30/com.qualcomm.qti.gpudrivers.msmnile.api30.apk",
    "vendor/bin/hw/android.hardware.keymaster@4.0-strongbox-service-qti",
    "vendor/bin/hw/vendor.zui.hardware.ifaa@1.0-service",
    "vendor/bin/sscrpcd",
    "vendor/bin/vl53l1_daemon_main",
    "vendor/etc/acdbdata/CDP/CDP_Bluetooth_cal.acdb",
    "vendor/etc/acdbdata/CDP/CDP_Codec_cal.acdb",
    "vendor/etc/acdbdata/CDP/CDP_General_cal.acdb",
    "vendor/etc/acdbdata/CDP/CDP_Global_cal.acdb",
    "vendor/etc/acdbdata/CDP/CDP_Handset_cal.acdb",
    "vendor/etc/acdbdata/CDP/CDP_Hdmi_cal.acdb",
    "vendor/etc/acdbdata/CDP/CDP_Headset_cal.acdb",
    "vendor/etc/acdbdata/CDP/CDP_Speaker_cal.acdb",
    "vendor/etc/acdbdata/CDP/CDP_workspaceFile.qwsp",
    "vendor/etc/acdbdata/MTP/MTP_Bluetooth_cal.acdb",
    "vendor/etc/acdbdata/MTP/MTP_Codec_cal.acdb",
    "vendor/etc/acdbdata/MTP/MTP_General_cal.acdb",
    "vendor/etc/acdbdata/MTP/MTP_Global_cal.acdb",
    "vendor/etc/acdbdata/MTP/MTP_Handset_cal.acdb",
    "vendor/etc/acdbdata/MTP/MTP_Hdmi_cal.acdb",
    "vendor/etc/acdbdata/MTP/MTP_Headset_cal.acdb",
    "vendor/etc/acdbdata/MTP/MTP_Speaker_cal.acdb",
    "vendor/etc/acdbdata/MTP/MTP_workspaceFile.qwsp",
    "vendor/etc/acdbdata/QRD/QRD_Bluetooth_cal.acdb",
    "vendor/etc/acdbdata/QRD/QRD_Codec_cal.acdb",
    "vendor/etc/acdbdata/QRD/QRD_General_cal.acdb",
    "vendor/etc/acdbdata/QRD/QRD_Global_cal.acdb",
    "vendor/etc/acdbdata/QRD/QRD_Handset_cal.acdb",
    "vendor/etc/acdbdata/QRD/QRD_Hdmi_cal.acdb",
    "vendor/etc/acdbdata/QRD/QRD_Headset_cal.acdb",
    "vendor/etc/acdbdata/QRD/QRD_Speaker_cal.acdb",
    "vendor/etc/acdbdata/QRD/QRD_workspaceFile.qwsp",
    "vendor/etc/camera/camxoverridesettings.txt",
    "vendor/etc/camera/camxoverridesettings_for_cts.txt",
    "vendor/etc/cne/profileSlm.xml",
    "vendor/etc/cne/slm.conf",
    "vendor/etc/hbtp/hbtpcfg_sdm855_801s_4k.dat",
    "vendor/etc/hbtp/qtc801s.bin",
    "vendor/etc/init/vendor.qti.adsprpc-service.rc",
    "vendor/etc/init/vendor.sensors.sscrpcd.rc",
    "vendor/etc/init/vendor.zui.hardware.ifaa@1.0-service.rc",
    "vendor/etc/qdcm_calib_data_mipi_mot_cmd_smd_1080p_639.xml",
    "vendor/etc/qdcm_calib_data_nt37700_cmd_mode_dsi_tianma_panel_with_DSC_xxx.xml",
    "vendor/etc/sensors/config/msmnile_ak991x_0_zippo.json",
    "vendor/etc/sensors/config/msmnile_icm4x6xx_0_zippo.json",
    "vendor/etc/sensors/config/msmnile_irq.json",
    "vendor/etc/sensors/config/msmnile_mn26xxx_0.json",
    "vendor/etc/sensors/config/msmnile_mn58xxx_0.json",
    "vendor/etc/sensors/config/msmnile_power_0.json",
    "vendor/etc/sensors/proto/mot_camgest.proto",
    "vendor/etc/sensors/proto/mot_chopchop.proto",
    "vendor/etc/sensors/proto/mot_movement.proto",
    "vendor/etc/sensors/proto/qti_gravity.proto",
    "vendor/etc/sensors/proto/sns_async_com_port.proto",
    "vendor/etc/sensors/proto/sns_ccd_ttw.proto",
    "vendor/etc/sensors/proto/sns_ccd_walk.proto",
    "vendor/etc/sensors/proto/sns_cmd.proto",
    "vendor/etc/sensors/proto/sns_dae.proto",
    "vendor/etc/sensors/proto/sns_data_acquisition_engine.proto",
    "vendor/etc/sensors/proto/sns_distance_bound.proto",
    "vendor/etc/sensors/proto/sns_interrupt.proto",
    "vendor/etc/sensors/proto/sns_mcmd.proto",
    "vendor/etc/sensors/proto/sns_motion_detect.proto",
    "vendor/etc/sensors/proto/sns_multishake.proto",
    "vendor/etc/sensors/proto/sns_remote_proc_state.proto",
    "vendor/etc/sensors/proto/sns_signal_sensor.proto",
    "vendor/etc/sensors/proto/sns_sim.proto",
    "vendor/etc/sensors/proto/sns_sim_legacy.proto",
    "vendor/etc/sensors/proto/sns_timer.proto",
    "vendor/etc/sensors/proto/sns_zuk_patpat.proto",
    "vendor/etc/sensors/proto/sns_zuk_pickup.proto",
    "vendor/firmware/a640_zap.b00",
    "vendor/firmware/a640_zap.b01",
    "vendor/firmware/a640_zap.b02",
    "vendor/firmware/a640_zap.elf",
    "vendor/firmware/a640_zap.mdt",
    "vendor/firmware/ipa_uc.b00",
    "vendor/firmware/ipa_uc.b01",
    "vendor/firmware/ipa_uc.b02",
    "vendor/firmware/ipa_uc.elf",
    "vendor/firmware/ipa_uc.mdt",
    "vendor/firmware/mono.cnt",
    "vendor/firmware/tfa98xx.cnt",
    "vendor/lib/camera/com.qti.sensor.ov02c20.so",
    "vendor/lib/camera/com.qti.sensor.ov16885.so",
    "vendor/lib/camera/com.qti.sensor.s5kgd1.so",
    "vendor/lib/camera/com.qti.sensor.s5kgm1.so",
    "vendor/lib/camera/com.qti.sensormodule.ofilm_ov02c20.bin",
    "vendor/lib/camera/com.qti.sensormodule.ofilm_ov16885.bin",
    "vendor/lib/camera/com.qti.sensormodule.ofilm_ov8856.bin",
    "vendor/lib/camera/com.qti.sensormodule.ofilm_s5kgd1.bin",
    "vendor/lib/camera/com.qti.sensormodule.ofilm_s5kgm1.bin",
    "vendor/lib/camera/com.qti.tuned.ofilm_ov02c20.bin",
    "vendor/lib/camera/com.qti.tuned.ofilm_ov16885.bin",
    "vendor/lib/camera/com.qti.tuned.ofilm_ov8856.bin",
    "vendor/lib/camera/com.qti.tuned.ofilm_s5kgd1.bin",
    "vendor/lib/camera/com.qti.tuned.ofilm_s5kgm1.bin",
    "vendor/lib/camera/components/com.arcsoft.node.capturebokeh.so",
    "vendor/lib/camera/components/com.arcsoft.node.realtimebokeh.so",
    "vendor/lib/camera/components/com.arcsoft.node.smoothtransition.so",
    "vendor/lib/hw/audio.primary.msmnile.so",
    "vendor/lib/hw/sensors.hal.tof.so",
    "vendor/lib/hw/vendor.qti.hardware.audiohalext@1.0-impl.so",
    "vendor/lib/libarcsoft_dualcam_refocus.so",
    "vendor/lib/libclimax.so",
    "vendor/lib/libdualcam_optical_zoom_control.so",
    "vendor/lib/libdualcam_video_optical_zoom.so",
    "vendor/lib/libmpbase.so",
    "vendor/lib/libspcom.so",
    "vendor/lib/libvl53l1_daemon.so",
    "vendor/lib/libvpphcp.so",
    "vendor/lib/libwatermarkutils.so",
    "vendor/lib/rfsa/adsp/capi_v2_aptX_Classic.so",
    "vendor/lib/rfsa/adsp/capi_v2_aptX_HD.so",
    "vendor/lib/vendor.qti.hardware.audiohalext@1.0.so",
    "vendor/lib64/camera/com.qti.sensor.ov02c20.so",
    "vendor/lib64/camera/com.qti.sensor.ov16885.so",
    "vendor/lib64/camera/com.qti.sensor.s5kgd1.so",
    "vendor/lib64/camera/com.qti.sensor.s5kgm1.so",
    "vendor/lib64/camera/com.qti.sensormodule.ofilm_ov02c20.bin",
    "vendor/lib64/camera/com.qti.sensormodule.ofilm_ov16885.bin",
    "vendor/lib64/camera/com.qti.sensormodule.ofilm_ov8856.bin",
    "vendor/lib64/camera/com.qti.sensormodule.ofilm_s5kgd1.bin",
    "vendor/lib64/camera/com.qti.sensormodule.ofilm_s5kgm1.bin",
    "vendor/lib64/camera/com.qti.sm_cts.ofilm_s5kgd1.bin",
    "vendor/lib64/camera/com.qti.tuned.cts_ofilm_s5kgd1.bin",
    "vendor/lib64/camera/com.qti.tuned.cts_ofilm_s5kgm1.bin",
    "vendor/lib64/camera/com.qti.tuned.ofilm_ov02c20.bin",
    "vendor/lib64/camera/com.qti.tuned.ofilm_ov16885.bin",
    "vendor/lib64/camera/com.qti.tuned.ofilm_ov8856.bin",
    "vendor/lib64/camera/com.qti.tuned.ofilm_s5kgd1.bin",
    "vendor/lib64/camera/com.qti.tuned.ofilm_s5kgm1.bin",
    "vendor/lib64/camera/components/com.arcsoft.node.capturebokeh.so",
    "vendor/lib64/camera/components/com.arcsoft.node.realtimebokeh.so",
    "vendor/lib64/camera/components/com.arcsoft.node.smoothtransition.so",
    "vendor/lib64/camera/components/com.megvii.node.previewbeautyX.so",
    "vendor/lib64/camera/components/com.pandora.node.watermark.so",
    "vendor/lib64/hw/audio.primary.msmnile.so",
    "vendor/lib64/hw/sensors.hal.tof.so",
    "vendor/lib64/libarcsoft_dualcam_refocus.so",
    "vendor/lib64/libclimax.so",
    "vendor/lib64/libdualcam_optical_zoom_control.so",
    "vendor/lib64/libdualcam_video_optical_zoom.so",
    "vendor/lib64/libgnustl_shared.so",
    "vendor/lib64/libmpbase.so",
    "vendor/lib64/libsnpe_dsp_domains_skel.so",
    "vendor/lib64/libsnpe_dsp_skel.so",
    "vendor/lib64/libsnpe_dsp_v65_domains_skel.so",
    "vendor/lib64/libsnpe_dsp_v65_domains_v2_skel.so",
    "vendor/lib64/libsnpe_dsp_v66_domains_v2_skel.so",
    "vendor/lib64/libsnpe_loader.so",
    "vendor/lib64/libspcom.so",
    "vendor/lib64/libspl.so",
    "vendor/lib64/libsymphonypower.so",
    "vendor/lib64/libvl53l1_daemon.so",
    "vendor/lib64/libvpphcp.so",
    "vendor/lib64/libwatermarkutils.so",
    "vendor/lib64/vendor.goodix.extend.service@2.0.so",
    "vendor/lib64/vendor.zui.hardware.ifaa@1.0.so",
]

def remove_missing_files():
    """Remove missing files and already-packaged files from proprietary-files.txt"""
    filepath = "proprietary-files.txt"
    
    # Read the file
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Filter out lines that match missing files or start with "-"
    filtered_lines = []
    removed_count = 0
    
    for line in lines:
        stripped = line.strip()
        
        # Skip empty lines and comments
        if not stripped or stripped.startswith("#"):
            filtered_lines.append(line)
            continue
        
        # Check if line starts with "-" (already packaged, no need)
        if stripped.startswith("-"):
            removed_count += 1
            print(f"Removing (already packaged): {stripped}")
            continue
        
        # Check if the line is in the missing files list
        if stripped in missing_files:
            removed_count += 1
            print(f"Removing (not found): {stripped}")
            continue
        
        filtered_lines.append(line)
    
    # Write back to the file
    with open(filepath, 'w') as f:
        f.writelines(filtered_lines)
    
    print(f"\nRemoved {removed_count} files from {filepath}")

if __name__ == "__main__":
    remove_missing_files()
