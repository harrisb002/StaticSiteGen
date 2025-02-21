# All HTMLNodes are assumed to have either a value or children
# An HTMLNode without a tag will just render as raw text
# An HTMLNode without props simply won't have any attributes
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag  # "string tag name -> 'p', 'a'..."
        self.value = value  # string rep. the value of tag (Also can be TextNode)
        self.children = children  # list of HTMLNode obj. children
        self.props = (
            props  # dict. rep. attributes of the tag -> "https://www.google.com"
        )

    # Children class shall overide this method
    def to_html(self):
        raise NotImplementedError()

    # Returns the string that represents the HTML Attributes of the Node
    def props_to_html(self):
        if not self.props:
            return ""
        html_props = ""
        for key, value in self.props.items():
            html_props += f' {key}="{value}"'
        return html_props

    # Overriding print implementation
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("All Leaf nodes must have a value.")
        super().__init__(tag=tag, value=value, children=None, props=props)

    # Renders a leaf node as an HTML string (by returning a string).
    def to_html(self):
        if self.value is None:
            raise ValueError("All Leaf nodes must have a value.")
        if self.tag is None:
            return self.value

        props = self.props_to_html()
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("All Parent nodes must have a tag")
        if not children:
            raise ValueError("All Parent nodes require at least one child")

        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        props = self.props_to_html()
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{props}>{children_html}</{self.tag}>"
