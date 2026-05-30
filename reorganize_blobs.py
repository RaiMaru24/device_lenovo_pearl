#!/usr/bin/env python3
"""
Script to categorize and redistribute entries from "Additional blobs from prop.txt"
into appropriate sections based on naming patterns
"""

def categorize_blob(entry):
    """
    Determine the category for a blob based on its path/name
    Returns the category header to use
    """
    entry_lower = entry.lower()
    
    # Lenovo-specific
    if "lenovo" in entry_lower:
        return "# Lenovo"
    
    # ADSP/Audio DSP
    if "adsp" in entry_lower or "adsprpc" in entry_lower or "sscrpc" in entry_lower:
        return "# ADSP Modules"
    
    # Audio calibration
    if "acdb" in entry_lower or ("cali" in entry_lower and "calib" not in entry_lower):
        return "# ACDB data"
    
    # Display calibration
    if "qdcm_calib" in entry_lower or ("display" in entry_lower and "calib" in entry_lower):
        return "# Display calibration data"
    
    # Keymaster
    if "keymaster" in entry_lower:
        return "# Keymaster"
    
    # Fingerprint
    if "fingerprint" in entry_lower or "goodix" in entry_lower or "gf_ca" in entry_lower:
        return "# Fingerprint"
    
    # Bluetooth
    if "bluetooth" in entry_lower:
        return "# Bluetooth (A2DP)"
    
    # CNE/Wireless
    if "cne" in entry_lower or "iwlan" in entry_lower or "mwqem" in entry_lower:
        return "# CNE"
    
    # DPM
    if "dpm" in entry_lower:
        return "# DPM"
    
    # Display/Color management
    if "display.color" in entry_lower or "displayconfig" in entry_lower or "displaydebug" in entry_lower or "vendor.display" in entry_lower:
        return "# Display (SDM)"
    
    # Dolby
    if "dolby" in entry_lower or "dms@2" in entry_lower or "stagefrightdolby" in entry_lower or "dlb" in entry_lower:
        return "# Audio libraries"
    
    # DRM/Widevine/Encryption
    if "widevine" in entry_lower or ("drm" in entry_lower and "oemcrypto" not in entry_lower) or "cacert" in entry_lower:
        return "# Widevine DRM"
    
    # Codec/Media/OMX
    if "codec2" in entry_lower or "sound_trigger" in entry_lower or "qcodec" in entry_lower:
        return "# OMX"
    
    # Factory/Lenovo
    if "factory" in entry_lower:
        return "# Lenovo"
    
    # GPU Firmware (A612, A615 chips)
    if "firmware" in entry_lower and ("a612" in entry_lower or "a615" in entry_lower or "a640" in entry_lower):
        return "# Graphics (Adreno firmware)"
    
    # Other Firmware
    if "firmware" in entry_lower and (".bin" in entry_lower or ".wmfw" in entry_lower or ".mdt" in entry_lower or ".cnt" in entry_lower):
        return "# Graphics (Adreno firmware)"
    
    # Audio
    if "audio" in entry_lower or "listen" in entry_lower or "lauatiosph" in entry_lower:
        return "# Audio libraries"
    
    # IMS
    if "ims" in entry_lower or "rcs" in entry_lower or "uceservice" in entry_lower:
        return "# Radio_IMS"
    
    # Radio/Telephony
    if ("telephony" in entry_lower or "qcril" in entry_lower) and "service" not in entry_lower.replace("qcrilmsgtunnel", "x"):
        return "# Radio"
    
    # Sensor
    if "sensor" in entry_lower:
        return "# Sensors"
    
    # Camera
    if "camera" in entry_lower:
        return "# Camera"
    
    # Graphics
    if "adreno" in entry_lower or "vulkan" in entry_lower or "egl" in entry_lower or "gles" in entry_lower:
        return "# Graphics (Adreno)"
    
    # Neural networks/ML
    if "snpe" in entry_lower or "hexagon_nn" in entry_lower or "neuralnetworks" in entry_lower:
        return "# Neural networks"
    
    # VPP
    if "vpp" in entry_lower:
        return "# VPP"
    
    # CVP
    if "cvp" in entry_lower:
        return "# CVP"
    
    # Thermal
    if "thermal" in entry_lower:
        return "# Thermal"
    
    # Perf
    if "perf" in entry_lower:
        return "# Perf"
    
    # Power/Charger
    if "power" in entry_lower or "alarm" in entry_lower or "hvdcp" in entry_lower or "chg" in entry_lower:
        return "# Power-off alarm"
    
    # FM
    if "fm" in entry_lower and "radio" not in entry_lower and "dsp" not in entry_lower:
        return "# FM"
    
    # GPS
    if "gnss" in entry_lower or "gps" in entry_lower or "loc_" in entry_lower:
        return "# GPS"
    
    # Data/Networking
    if "rmnetctl" in entry_lower or "lce@" in entry_lower or "latency" in entry_lower:
        return "# Qualcomm MSM Interface"
    
    return "# Unknown"

def reorganize_additional_blobs():
    """Extract and reorganize 'Additional blobs from prop.txt' section"""
    
    filepath = "proprietary-files.txt"
    
    # Read the file
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Find the "Additional blobs from prop.txt" section
    additional_start = None
    for i, line in enumerate(lines):
        if "# Additional blobs from prop.txt" in line:
            additional_start = i
            break
    
    if additional_start is None:
        print("'Additional blobs from prop.txt' section not found!")
        return
    
    # Extract additional blobs
    additional_blobs = []
    for i in range(additional_start + 1, len(lines)):
        line = lines[i].strip()
        if line.startswith("#"):
            break
        if line:
            additional_blobs.append(line)
    
    print(f"Found {len(additional_blobs)} entries in 'Additional blobs from prop.txt'")
    
    # Categorize each blob
    categorized = {}
    for blob in additional_blobs:
        category = categorize_blob(blob)
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(blob)
    
    print(f"\nCategorized into {len(categorized)} categories:")
    for category in sorted(categorized.keys()):
        print(f"  {category}: {len(categorized[category])} entries")
    
    # Remove the "Additional blobs" section from lines
    lines_without_additional = []
    skip = False
    for i, line in enumerate(lines):
        if "# Additional blobs from prop.txt" in line:
            skip = True
            continue
        if skip and line.strip().startswith("#") and "Additional blobs" not in line:
            skip = False
        if not skip:
            lines_without_additional.append(line)
    
    # Parse file into sections
    sections = {}
    current_section = None
    current_entries = []
    
    for line in lines_without_additional:
        stripped = line.strip()
        
        if stripped.startswith("#"):
            # Save previous section
            if current_section and current_entries:
                if current_section not in sections:
                    sections[current_section] = []
                sections[current_section].extend(current_entries)
            
            current_section = stripped
            if current_section not in sections:
                sections[current_section] = []
            current_entries = []
        elif stripped:
            current_entries.append(stripped)
    
    # Save last section
    if current_section and current_entries:
        if current_section not in sections:
            sections[current_section] = []
        sections[current_section].extend(current_entries)
    
    # Add categorized blobs to appropriate sections
    for category, blobs in categorized.items():
        if category not in sections:
            sections[category] = []
        sections[category].extend(blobs)
    
    # Write organized file
    with open(filepath, 'w') as f:
        first_section = True
        
        for section in sorted(sections.keys()):
            if not sections[section]:
                continue
            
            # Add blank line between sections (except first)
            if not first_section:
                f.write("\n")
            
            # Write section header
            f.write(section + "\n")
            
            # Sort and write entries for this section
            entries = sorted(set(sections[section]))  # Remove duplicates and sort
            for entry in entries:
                f.write(entry + "\n")
            
            first_section = False
    
    print(f"\n✓ Successfully reorganized proprietary-files.txt")
    print(f"  - Removed 'Additional blobs from prop.txt' section")
    print(f"  - Distributed {len(additional_blobs)} entries to appropriate sections")
    print(f"  - Total sections: {len(sections)}")

if __name__ == "__main__":
    reorganize_additional_blobs()
