from .ComfyUI_RSS_Feed_Reader import ComfyUI_RSS_Feed_Reader

def register():
    from ComfyUI import node_manager
    node_manager.register_node(ComfyUI_RSS_Feed_Reader)

# Ensure the module is registered when the package is imported
register()

# Optional: You can also add these mappings if they are required for displaying the node
NODE_CLASS_MAPPINGS = {
    "ComfyUI_RSS_Feed_Reader": ComfyUI_RSS_Feed_Reader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI_RSS_Feed_Reader": "ComfyUI_RSS_Feed_Reader"
}
