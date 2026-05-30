#!/usr/bin/env python3
"""
Script to organize and sort proprietary-files.txt by sections
Merges duplicate sections and groups entries properly
"""

def organize_proprietary_files():
    """Organize proprietary-files.txt by sections and merge duplicates"""
    
    filepath = "proprietary-files.txt"
    
    # Read the file
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Parse the file into sections
    sections = {}
    current_section = "# Header"
    current_entries = []
    header_order = []
    
    for line in lines:
        stripped = line.strip()
        
        # Check if this is a section header
        if stripped.startswith("#"):
            # Save previous section if it has entries
            if current_entries and current_section not in sections:
                sections[current_section] = []
            
            if current_section in sections:
                sections[current_section].extend(current_entries)
            elif current_entries:
                sections[current_section] = current_entries
            
            current_section = stripped
            current_entries = []
            
            # Track header order to preserve sequence
            if current_section not in header_order:
                header_order.append(current_section)
        
        elif stripped:  # Non-empty, non-comment line
            current_entries.append(stripped)
    
    # Don't forget the last section
    if current_entries:
        if current_section in sections:
            sections[current_section].extend(current_entries)
        else:
            sections[current_section] = current_entries
    
    print(f"Found {len(sections)} sections")
    print("\nSections found:")
    for section in sorted(sections.keys()):
        entry_count = len(sections[section])
        print(f"  {section}: {entry_count} entries")
    
    # Write organized file
    with open(filepath, 'w') as f:
        first_section = True
        
        for section in sorted(sections.keys()):
            if section == "# Header":
                continue
            
            # Add blank line between sections (except first)
            if not first_section:
                f.write("\n")
            
            # Write section header
            f.write(section + "\n")
            
            # Sort and write entries for this section
            entries = sorted(sections[section])
            for entry in entries:
                f.write(entry + "\n")
            
            first_section = False
    
    print(f"\n✓ Reorganized {filepath} with {len(sections)} sections")
    print("  - Duplicate sections merged")
    print("  - Entries sorted alphabetically within each section")
    print("  - Sections sorted alphabetically")

if __name__ == "__main__":
    organize_proprietary_files()
