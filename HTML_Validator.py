def validate_html(html):
    tags = _extract_tags(html)
    stack = []

    for tag in tags:
        if tag.startswith("<") and not tag.endswith("/>"):  # Also accounts for self-closing tags like <img/>
            stack.append(tag)
        elif tag.startswith("</"):
            if not stack or stack[-1][1:] != tag[2:]:
                return False
            stack.pop()

    return len(stack) == 0


def _extract_tags(html):
    tags = []
    i = 0
    while i < len(html):
        if html[i] == "<":
            j = i
            while j < len(html) and html[j] != ">":
                j += 1
            tags.append(html[i:j+1])
            i = j + 1
        else:
            i += 1
    return tags
