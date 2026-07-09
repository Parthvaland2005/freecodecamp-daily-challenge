def triage_issue(title, labels):
    title = title.lower()
    result = labels.copy()

    if not result:
        if "error" in title or "bug" in title:
            result.extend(["bug", "needs triage"])
        elif "feature" in title or "add" in title:
            result.extend(["enhancement", "discussing"])
    else:
        if "needs triage" in result:
            result.remove("needs triage")
            if "simple" in title or "easy" in title:
                result.append("good first issue")
            else:
                result.append("help wanted")

        elif "discussing" in result:
            result.remove("discussing")
            if "planned" in title or "next" in title:
                result.append("on the roadmap")
            else:
                result.append("help wanted")

    if "security" in title and "critical" not in result:
        result.append("critical")

    return result

print(triage_issue("app crashes with error", []))
print(triage_issue("app crashes with error", ["bug", "needs triage"]))
print(triage_issue("add dark mode", []))
print(triage_issue("add dark mode", ["enhancement", "discussing"]))
print(triage_issue("xss security bug", []))
print(triage_issue("security vulnerability in auth", []))
print(triage_issue("easy a11y fix", ["bug", "needs triage"]))
print(triage_issue("planned api migration", ["enhancement", "discussing"]))
print(triage_issue("improve security", ["enhancement", "discussing"]))