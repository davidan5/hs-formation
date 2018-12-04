# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_circuit_breaker_middleware 1'] = [
    [
        'warn',
        'circuitbreaker.state.changed',
        {
            'name': 'test-cb',
            'new_state': 'open',
            'old_state': 'closed'
        },
        {
        }
    ],
    [
        'info',
        'circuitbreaker.middleware.open',
        {
            'name': 'test-cb'
        },
        {
        }
    ],
    [
        'info',
        'circuitbreaker.middleware.open',
        {
            'name': 'test-cb'
        },
        {
        }
    ]
]
