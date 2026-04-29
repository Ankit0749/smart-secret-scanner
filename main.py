import re
import json

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

    with open(file_path, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines, start=1):

        # Skip lines containing "test"
        if "test" in line.lower():
            continue

        for key, value in patterns.items():
            if re.search(value["pattern"], line, re.IGNORECASE):

                findings.append({
                    "line": i,
                    "type": key,
                    "risk": value["risk"],
                    "content": line.strip()
                })

    return findings


# Run scanner
results = scan_file("test.py")

# Print results
if results:
    for item in results:
        print(f"[!] Found {item['type']} ({item['risk']}) at line {item['line']}")
        print(f"    → {item['content']}")
else:
    print("✅ No secrets found")

# 🔥 IMPORTANT: Save JSON for CI/CD
with open("report.json", "w") as f:
    json.dump(results, f, indent=4)