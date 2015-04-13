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
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, ind + self.indent)
            else:
                file_out.write(ind)
                file_out.write(self.indent)
                file_out.write(item)
                file_out.write("\n")
        file_out.write(ind)
        file_out.write("</{}>\n".format(self.tag))


class Html(Element):
    """HTML tag."""
    tag = u"html"

    def render(self, file_out, ind=""):
        file_out.write(ind)
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, ind)


class Body(Element):
    """Body tag."""
    tag = u"body"


class Head(Element):
    """Head tag."""
    tag = u"head"


class OneLineTag(Element):
    """OneLineTag."""

    def render(self, file_out, ind=""):
        file_out.write(ind)
        file_out.write("<{}>".format(self.tag))
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, ind + self.indent)
            else:
                file_out.write(item)
        file_out.write("</{}>\n".format(self.tag))


class Title(OneLineTag):
    """Title tag."""
    tag = u"title"


class P(Element):
    """P tag."""
    tag = u"p"
