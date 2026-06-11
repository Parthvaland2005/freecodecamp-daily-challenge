def analyze_ideas(ideas):
    return [
        idea[0]
        for idea in sorted(
            ideas,
            key=lambda idea: (
                ((idea[1] + 4 * idea[2] + idea[3]) / 6) * len(idea[0])
            )
        )
    ]
    
print(analyze_ideas([
    ["Add logging", 2, 5, 15],
    ["SEO optimization", 4, 8, 20],
    ["Fix bug", 1, 3, 5]
]))

print(analyze_ideas([
    ["Dark mode", 1, 3, 8],
    ["Real-time collaboration feature", 6, 12, 20],
    ["Add tooltip", 1, 2, 4]
]))