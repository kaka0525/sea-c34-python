class Element(object):
    """An HTML element."""
    tag = u""
    indent = u"    "

    def __init__(self, content=None):
        self.content = [str(content)] if content else []

    def append(self, string):
        """Append string to content."""
        self.content.append(string)

    def render(self, file_out, ind=""):
        """Render the tag and strings in content."""
        file_out.write(ind)
        file_out.write("<{}>\n".format(self.tag))
        for string in self.content:
            file_out.write(ind)
            file_out.write(self.indent)
            file_out.write(string)
            file_out.write("\n")
        file_out.write(ind)
        file_out.write("</{}>\n".format(self.tag))


class Html(Element):
    """HTML tag."""

    tag = u"html"


class Body(Element):
    """Body tag."""
    tag = u"body"

    def __init__(self):
        pass
