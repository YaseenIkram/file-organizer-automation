"""
Automated Folder Organizer
Scans a target directory, categorizes files by extension, safely resolves 
naming conflicts using regex, and generates a detailed execution manifest.
"""

import re
from pathlib import Path

# --- CONFIGURATION CONSTANTS ---
DESTINATIONS = ["PDFs", "TXTs", "Images", "Videos", "Audios", "Other"]

def main():
    # 1. Safe Path Anchoring
    script_folder = Path(__file__).parent
    project_folder = script_folder.parent
    test_area = project_folder / "test_area"

    # 2. Ensure destination folders exist
    for folder in DESTINATIONS:
        (test_area / folder).mkdir(exist_ok=True)

    # 3. Initialize Reporting Counters
    total_scanned = 0
    files_moved = 0
    files_skipped = 0
    name_conflicts = 0
    action_log = []

    # 4. Main Execution Loop
    for item in test_area.iterdir():
        if item.is_file():
            # Exclude the report file itself from being scanned or moved
            if item.name == "report.txt":
                continue
                
            total_scanned += 1
            suffix = item.suffix.lower()
            
            # Determine mapping destination
            match suffix:
                case ".pdf": target_folder = test_area / DESTINATIONS[0]
                case ".txt": target_folder = test_area / DESTINATIONS[1]
                case ".jpg" | ".png": target_folder = test_area / DESTINATIONS[2]
                case ".mp4": target_folder = test_area / DESTINATIONS[3]
                case ".mp3": target_folder = test_area / DESTINATIONS[4]
                case _: target_folder = test_area / DESTINATIONS[5]
            
            destination = target_folder / item.name
            
            # Safety Check 1: Skip if already organized
            if item.parent == target_folder:
                msg = f"[NO CHANGE] '{item.name}' is already in {target_folder.name}/"
                action_log.append(msg)
                files_skipped += 1
                continue
                
            # Safety Check 2: Smart Collision Resolution
            if destination.exists():
                stem = item.stem
                ext = item.suffix
                name_conflicts += 1
                
                # Check for existing numbers using Regex
                regex_match = re.search(r'_(\d+)$', stem)
                
                if regex_match:
                    # If it ends in _number, separate the base name and the number
                    base_name = stem[:regex_match.start()]
                    counter = int(regex_match.group(1)) + 1
                else:
                    # If it doesn't, treat it normally
                    base_name = stem
                    counter = 1
                
                # Keep incrementing until we find a free slot
                while destination.exists():
                    new_filename = f"{base_name}_{counter}{ext}"
                    destination = target_folder / new_filename
                    counter += 1
                    
                msg_conflict = f"[RESOLVED CONFLICT] '{item.name}' renamed to '{destination.name}' due to duplicate."
                action_log.append(msg_conflict)

            # Execute safe relocation
            item.rename(destination)
            msg_move = f"[SUCCESS] Moved '{item.name}' -> {target_folder.name}/{destination.name}"
            action_log.append(msg_move)
            files_moved += 1

    # 5. Compile and Write Final Text Manifest
    detailed_logs = "\n".join(action_log) if action_log else "No file operations performed."

    report_structure = f"""==================================================
         AUTOMATED FOLDER ORGANIZER REPORT
==================================================
Total Files Scanned      : {total_scanned}
Files Successfully Moved : {files_moved}
Files Skipped (Organized): {files_skipped}
Naming Conflicts Resolved: {name_conflicts}

--------------------------------------------------
                 DETAILED OPERATION LOGS
--------------------------------------------------
{detailed_logs}
==================================================
"""

    # Write the final manifest into the test_area folder
    report_path = test_area / "report.txt"
    report_path.write_text(report_structure, encoding="utf-8")

    print(f"\n[SYSTEM] Run complete. Summary manifest generated at: {report_path}")

# Standard Python idiom to execute the main function safely
if __name__ == "__main__":
    main()