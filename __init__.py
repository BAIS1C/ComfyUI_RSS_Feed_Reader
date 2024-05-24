from .RSSFeedtoPrompt import RSSFeedNode

def register():
    from ComfyUI import node_manager
    node_manager.register_node(RSSFeedNode)

# Ensure the module is registered when the package is imported
register()
