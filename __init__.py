from .RSSFeedNode import RSSFeedNode

def register():
    from ComfyUI import node_manager
    node_manager.register_node(RSSFeedNode)

# Ensure the module is registered when the package is imported
register()

# Optional: You can also add these mappings if they are required for displaying the node
NODE_CLASS_MAPPINGS = {
    "RSSFeedNode": RSSFeedNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RSSFeedNode": "RSS Feed Reader"
}
