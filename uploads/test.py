# 🔴 HIGH RISK (API KEY)
API_KEY = "sk-123abcSECRETKEY"

# 🟠 MEDIUM RISK (PASSWORD)
password = "admin123"

# 🟠 MEDIUM (pwd variation)
pwd = "mypassword456"

# 🔴 HIGH RISK (another API-like key)
another_key = "sk-xyz999token"

# ✅ SAFE CODE (should not be flagged)
username = "user1"
message = "Hello World"

# ⚠️ Should be ignored (contains 'test')
test_key = "sk-test-ignore-this"

# 🔴 HIGH RISK inside code
def connect():
    token = "sk-live-999abc"
    return token