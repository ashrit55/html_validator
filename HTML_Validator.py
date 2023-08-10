def validate_html(html):
    '''

    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the class/book
    # the main difference between your code and the code from class will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags
    newl = _extract_tags(html)
    stack = []

    for c in newl:
        for i in c:
            if i == "<":
                stack.append("<")
            else:
                if i == ">" and stack.pop() != "<":
                    print(False)

    if len(stack) > 0:
        print(False)
    else:
        print(True)


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    myl = []
    news = ""
    i = 0
    while i < len(html):
        if html[i:i+1] == "<":
            while html[i:i+1] != ">" and i < len(html):

                news = news + html[i:i+1]
                i += 1
            if i < len(html):
                news += ">"
            myl.append(news)
        else:
            news = ""
            i += 1
    print(myl)
    return (myl)


# _extract_tags('Python <strong>rocks</strong>!')
# validate_html('<strong>example</strong>')
# _extract_tags('<a><b><c></a></b><f>')
# validate_html('this is a <strong< test')
