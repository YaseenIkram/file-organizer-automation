# Automated File & Directory Organizer

A production-grade Python automation script designed to safely scan, sort, and clean up chaotic download directories. This tool dynamically categorizes files based on their extensions, resolves naming conflicts safely without overwriting data, and generates a clean administrative manifest report upon completion.

## 🌟 Key Features

* **Zero-Data-Loss Safety Engines:** Uses robust `pathlib` checks to verify system pointers before executing file system adjustments.
* **Smart Collision Resolution:** Integrates Regular Expressions (`re`) to identify existing duplicate naming patterns (e.g., `file_3.png`), automatically incrementing the file version counter (`file_4.png`) instead of skipping or silently overwriting customer data.
* **Background Auditing Manifests:** Automatically compiles runtime counts and sequential operations into a clean `report.txt` file for administrative monitoring.
* **Defensive Input Filtering:** Employs structural `match/case` operations to isolate unsupported file formats safely into fallback storage layers without interrupting the processing pipeline.

## 🛠️ How It Works

The core script anchors itself relative to its execution location, builds the required infrastructure targets safely, runs a verification pass on existing files, and tracks metrics seamlessly across branches.

```python
# Core architecture layout:
# 1. Verification of infrastructure paths
# 2. Sequential file identification pass
# 3. Collision interception via regular expression patterns
# 4. Final multi-line administrative string aggregation
📋 Sample Output Report
Every background run generates a comprehensive tracking manifest inside the target directory:

==================================================
AUTOMATED FOLDER ORGANIZER REPORT
Total Files Scanned      : 58
Files Successfully Moved : 58
Files Skipped (Organized): 0
Naming Conflicts Resolved: 4

             DETAILED OPERATION LOGS
[SUCCESS] Moved 'audio_2.mp3' -> Audios/audio_2.mp3
[RESOLVED CONFLICT] 'image_3.png' renamed to 'image_3_1.png' due to duplicate.
[SUCCESS] Moved 'image_3.png' -> Images/image_3_1.png
[SUCCESS] Moved 'backup.tar.gz' -> Other/backup.tar.gz
