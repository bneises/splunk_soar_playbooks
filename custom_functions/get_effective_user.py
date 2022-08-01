def get_effective_user(**kwargs):
    """
    Get the information of the user running the playbook.
    
    Returns a JSON-serializable object that implements the configured data paths:
        id: SOAR User ID
        username (CEF type: user name): SOAR Username
        first_name: First name
        last_name: Last name
        email (CEF type: email): Email address
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    pb_info = phantom.get_playbook_info()[0]
    phantom.debug(pb_info)
    
    url = phantom.build_phantom_rest_url('ph_user', pb_info.get('effective_user_id'))
    r = phantom.requests.get(url, verify=False)
    r.raise_for_status()
    outputs = r.json()
    phantom.debug(outputs)
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
