from main import get_explanation

def test_is_successful():
    response = get_explanation("pqpqs", 2)
    assert ['pq', 'pqp', 'pqpq', 'qp', 'qpq', 'pq', 'qs'] == response


def test_last_have_more_substring():
    response = get_explanation("pqpqsqs", 2)
    assert ['pq', 'pqp', 'pqpq', 'qp', 'qpq', 'pq', 'qs', 'qsq', 'qsqs', 'sqs', 'qs'] == response
