import re
import json
import os

# Patterns
patterns = {
    "API_KEY": {
        "pattern": r"sk-[a-zA-Z0-9]+",
        "risk": "HIGH"
    },
    "PASSWORD": {
        "pattern": r"(password|pwd)\s*=\s*['\"].+['\"]",
        "risk": "MEDIUM"
    }
}

def scan_file(file_path):
    findings = []

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except:
        return []

    for i, line in enumerate(lines, start=1):

        if "test" in line.lower():
            continue

        for key, value in patterns.items():
            if re.search(value["pattern"], line, re.IGNORECASE):

                findings.append({
                    "file": file_path,
                    "line": i,
                    "type": key,
                    "risk": value["risk"],
                    "content": line.strip()
                })

    return findings


def scan_directory(directory):
    all_findings = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):  # scan only python files
                full_path = os.path.join(root, file)
                results = scan_file(full_path)
                all_findings.extend(results)

    return all_findings


# 🔥 Scan entire project
results = scan_directory(".")

# Print results
if results:
    for item in results:
        print(f"[!] {item['file']} → {item['type']} ({item['risk']}) at line {item['line']}")
else:
    print("✅ No secrets found")

# Save JSON
with open("report.json", "w") as f:
    json.dump(results, f, indent=4)