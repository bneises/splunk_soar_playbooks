def get_custom_fields(container=None, **kwargs):
    """
    Args:
        container
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Ensure valid container input
    if isinstance(container, dict) and container.get('id'):
        # container_id = container['id']
        phantom.debug(container)
    elif isinstance(container, int):
        container_id = container
        
    else:
        raise TypeError("The input 'container' is neither a container dictionary nor an int.")
        
    
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
