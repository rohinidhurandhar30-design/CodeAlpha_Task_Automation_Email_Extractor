# CodeAlpha Task 3: Email Extractor Automation

import re

print("=" * 50)
print("📧 EMAIL EXTRACTOR TOOL")
print("=" * 50)

# Read input file
input_file = "input.txt"

try:
    with open(input_file, "r") as file:
        text = file.read()

    # Regex pattern for emails
    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)

    # Remove duplicates
    unique_emails = list(set(emails))

    # Save to output file
    with open("emails.txt", "w") as file:
        for email in unique_emails:
            file.write(email + "\n")

    print(f"\n✅ Total Emails Found: {len(unique_emails)}")
    print("📁 Saved to emails.txt")

except FileNotFoundError:
    print("❌ input.txt file not found. Please create it first.")
