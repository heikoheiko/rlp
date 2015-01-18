import rlp


def encode_decode(data):
    assert data == rlp.decode(rlp.encode(data))

ed = encode_decode

def test_empty():
    assert '\xc0' == rlp.encode([])
    assert '\x80' == rlp.encode('')
    assert rlp.decode('\xc0') == []
    assert rlp.decode('\x80') == ''
    ed([])
    ed('')

def test_byte():
    for s in ('a', chr(0), chr(255), 'abc'):
        ed(s)

def test_list():
    ed(['a'])
    ed(['a','b'])
    ed(['a','b',[]])
    ed(['a','b',['a','1']])
    ed([['a']*4])

def test_err():
    try:
        rlp.encode(tuple(('a','b')))
        raise Exception('missed to raise encoding error')
    except TypeError:
        pass

    try:
        rlp.encode(dict(a=1))
        raise Exception('missed to raise encoding error')
    except TypeError:
        pass
    try:
        rlp.encode(1)
        raise Exception('missed to raise encoding error')
    except TypeError:
        pass
