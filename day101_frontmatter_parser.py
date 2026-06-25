def parse_frontmatter(text):
    result = {}

    lines = text.strip().split("\n")

    for line in lines[1:-1]:  
        key, value = line.split(": ", 1)

        if value.lower() == "true":
            result[key] = True
        elif value.lower() == "false":
            result[key] = False
        else:
            try:
                if "." in value and value.count(".") == 1:
                    result[key] = float(value)
                else:
                    result[key] = int(value)
            except ValueError:
                result[key] = value

    return result

print(parse_frontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---"))

print(parse_frontmatter("---\nid: 6a174db57256a112f932195c\ntitle: My Book\nlocale: en\nwordCount: 10000\npublished: false\n---"))

print(parse_frontmatter("---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---"))

print(parse_frontmatter("---\nrating: 4.5\nprice: 9.99\n---"))