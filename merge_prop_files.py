#!/usr/bin/env python3
"""
Script to merge prop.txt into proprietary-files.txt
Adds only unique lines that are not already present
"""

def merge_proprietary_files():
    """Merge prop.txt into proprietary-files.txt, adding only missing lines"""
    
    prop_file = "prop.txt"
    proprietary_file = "proprietary-files.txt"
    
    # Read proprietary-files.txt and create a set of lines (excluding comments and empty lines)
    with open(proprietary_file, 'r') as f:
        proprietary_lines = f.readlines()
    
    # Create a set of existing entries (strip whitespace for comparison)
    existing_entries = set()
    for line in proprietary_lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            existing_entries.add(stripped)
    
    print(f"Current entries in {proprietary_file}: {len(existing_entries)}")
    
    # Read prop.txt
    with open(prop_file, 'r') as f:
        prop_lines = f.readlines()
    
    # Find new unique lines
    new_entries = []
    duplicate_entries = []
    
    for line in prop_lines:
        stripped = line.strip()
        
        # Skip empty lines and comments
        if not stripped or stripped.startswith("#"):
            continue
        
        # Check if entry already exists
        if stripped in existing_entries:
            duplicate_entries.append(stripped)
        else:
            new_entries.append(stripped)
    
    print(f"Total entries in {prop_file}: {len([l for l in prop_lines if l.strip() and not l.strip().startswith('#')])}")
    print(f"Duplicate entries (already in {proprietary_file}): {len(duplicate_entries)}")
    print(f"New entries to add: {len(new_entries)}")
    
    # Display new entries
    if new_entries:
        print(f"\nNew entries to be added:")
        for i, entry in enumerate(new_entries, 1):
            print(f"  {i}. {entry}")
    
    # Append new entries to proprietary-files.txt
    if new_entries:
        with open(proprietary_file, 'a') as f:
            # Add a blank line and comment if adding new sections
            f.write("\n# Additional blobs from prop.txt\n")
            for entry in new_entries:
                f.write(entry + "\n")
        
        print(f"\n✓ Added {len(new_entries)} new entries to {proprietary_file}")
    else:
        print(f"\n✓ No new entries to add - all entries in {prop_file} are already in {proprietary_file}")
    
    # Show duplicates if requested
    if duplicate_entries and len(duplicate_entries) <= 10:
        print(f"\nDuplicate entries ({len(duplicate_entries)}):")
        for entry in duplicate_entries[:10]:
            print(f"  - {entry}")
        if len(duplicate_entries) > 10:
            print(f"  ... and {len(duplicate_entries) - 10} more")

if __name__ == "__main__":
    merge_proprietary_files()
