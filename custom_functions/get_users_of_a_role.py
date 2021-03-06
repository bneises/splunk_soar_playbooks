def get_users_of_a_role(role_name=None, ignore_users=None, **kwargs):
    """
    Args:
        role_name
        ignore_users
    
    Returns a JSON-serializable object that implements the configured data paths:
        *.id
        *.username
        *.email
        *.roles
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = []
    # Format ignore_users as a list
    try:
        ignore_users = json.loads(ignore_users)
    except:
        phantom.debug(f'Not JSON: {ignore_users=}')
    if not isinstance(ignore_users, list):
        ignore_users = [ignore_users]
    
    url = phantom.build_phantom_rest_url('ph_user')
    params = {
        'include_automation': True,
        'page_size': 0,
        '_filter_role__name': json.dumps(role_name),
        '_exclude_username__in': json.dumps(ignore_users)
    }
    phantom.debug(f'{url=}')
    
    resp = phantom.requests.get(
        url,
        params=params,
        verify=False
    )
    phantom.debug(f'{resp.request.url=}')
    phantom.debug(f'{resp.status_code=}')
        
    outputs = resp.json().get('data', [])
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
