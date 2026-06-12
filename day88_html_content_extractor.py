import re

def extract_content(html):
    text = re.sub(r'<[^>]+>', '', html)
    return text.strip()

print(extract_content('<p>hello world</p>'))
print(extract_content('<p>hello <span>world</span></p>'))
print(extract_content('<a href="example.com">Click me</a>'))
print(extract_content('<p><button onClick="learnToCode()">Learn</button> to <code>code</code> <br/>for <strong>free</strong> <br/>on <a href="https://freecodecamp.org/" target="_blank"><span class="highlight">freecodecamp</span>.org</a>'))