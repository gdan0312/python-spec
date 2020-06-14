ADD_ITEM_SCHEMA = {
    '$schema': 'http://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'title': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 64
        },
        'description': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 1024
        },
        'price': {
            'type': ['string', 'integer'],
            'minimum': 1,
            'maximum': 1000000,
            'pattern': r'^\d{1,7}$'
        }
    },
    'required': ['title', 'description', 'price']
}

POST_REVIEW_SCHEMA = {
    '$schema': 'http://json-schema.org/schema#',
    'type': 'object',
    'properties': {
        'text': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 1024
        },
        'grade': {
            'type': ['string', 'integer'],
            'minimum': 1,
            'maximum': 10,
            'pattern': r'^\d{1,2}$'
        }
    },
    'required': ['text', 'grade']
}
