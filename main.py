import re
import json
import os

# 🔥 Patterns with risk + suggestions
patterns = {
    "API_KEY": {
        "pattern": r"sk-[a-zA-Z0-9]+",
        "risk": "HIGH",
        "suggestion": "Store API keys in environment variables or use a secret manager"
    },
    "PASSWORD": {
        "pattern": r"(password|pwd)\s*=\s*['\"].+['\"]",
        "risk": "MEDIUM",
        "suggestion": "Avoid hardcoding passwords. Use environment variables or secure vaults"
    }
}


# 🔍 Scan a single file
def scan_file(file_path):
    findings = []

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except:
        return []

    for i, line in enumerate(lines, start=1):

        # Skip test-related lines
        if "test" in line.lower():
            continue

        for key, value in patterns.items():
            if re.search(value["pattern"], line, re.IGNORECASE):

                findings.append({
                    "file": file_path,
                    "line": i,
                    "type": key,
                    "risk": value["risk"],
                    "content": line.strip(),
                    "suggestion": value["suggestion"]
                })

    return findings


# 📁 Scan entire directory
def scan_directory(directory):
    all_findings = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):  # scan only python files
                full_path = os.path.join(root, file)
                results = scan_file(full_path)
                all_findings.extend(results)

    return all_findings


# 🚀 Run scanner on entire project
results = scan_directory(".")


# 🖥️ Print results
if results:
    for item in results:
        print(f"[!] {item['file']} → {item['type']} ({item['risk']}) at line {item['line']}")
        print(f"    → {item['content']}")
        print(f"    💡 Suggestion: {item['suggestion']}\n")
else:
    print("✅ No secrets found")


# 📄 Save results to JSON (for CI/CD)
with open("report.json", "w") as f:
    json.dump(results, f, indent=4)