def get_browser_history(commands):
    history = []
    current = -1

    for cmd in commands:
        if cmd == "Back":
            if current > 0:
                current -= 1

        elif cmd == "Forward":
            if current < len(history) - 1:
                current += 1

        else:
            history = history[:current + 1]

            history.append(cmd)
            current += 1

    return [history, current]

print(get_browser_history(["freecodecamp.org", "freecodecamp.org/learn", "Back"]))
print(get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog"]))
print(get_browser_history(["example.com", "example.com/about", "Back", "example.com/contact", "example.com/blog", "Back", "Back", "Forward"]))
print(get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog", "Back", "Back", "Forward", "freecodecamp.org"]))
print(get_browser_history(["example.com", "example.com/about", "Back", "Back"]))
print(get_browser_history(["example.com", "example.com/about", "Forward"]))