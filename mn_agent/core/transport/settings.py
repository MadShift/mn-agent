TRANSPORT_SETTINGS = {
    'agent_namespace': 'mn_agent',
    'agent_name': 'mn_agent',
    'utterance_lifetime_sec': 120,
    'channels': {},
    'transport': {
        'type': 'AMQP',
        'AMQP': {
            'host': '127.0.0.1',
            'port': 5672,
            'login': 'guest',
            'password': 'guest',
            'virtualhost': '/'
        }
    }
}
