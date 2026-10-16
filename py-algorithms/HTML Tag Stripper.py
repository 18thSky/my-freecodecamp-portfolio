def strip_tags(html):
    clean_text=""
    inside_tag = False
    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        else:
            if inside_tag == False:
                clean_text += char
    return clean_text