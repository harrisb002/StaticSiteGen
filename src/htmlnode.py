# All HTMLNodes are assumed to have either a value or children
# An HTMLNode without a tag will just render as raw text
# An HTMLNode without props simply won't have any attributes
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag  # "string tag name -> 'p', 'a'..."
        self.value = value  # string rep. the value of tag
        self.children = children  # list of HTMLNode obj. children
        self.props = (
            props  # dict. rep. attributes of the tag -> "https://www.google.com"
        )

    # Children class shall overide this method
    def to_html(self):
        raise NotImplementedError()

    # Returns the string that represents the HTML Attributes of the Node
    def props_to_html(self):
        html_props = ""
        for key, value in self.props:
            html_props += f" {key} {value}"
        return html_props

    # Overriding print implementation
    def __repr__(self):
        return print(
            f"Tag: {self.tag}\n Value: {self.value}\n Children: {self.children}\n Props: {self.props}"
        )
