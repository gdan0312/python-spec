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
            'minLength': 1,
            'maximum': 1000000,
            'maxLength': 7,
            'pattern': r'^\d+$'
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
            'minLength': 1,
            'maximum': 10,
            'maxLength': 2,
            'pattern': r'^\d+$'
        }
    },
    'required': ['text', 'grade']
}
