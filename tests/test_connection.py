"""Tests for pyps4_2ndscreen.connection."""

from pyps4_2ndscreen import connection as c

MOCK_SEED = bytes([
    0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
    0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
])

MOCK_HELLO_REQUEST = bytes([
    0x1c, 0x00, 0x00, 0x00, 0x70, 0x63, 0x63, 0x6f,
    0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00,
])

MOCK_STANDBY = bytes([
    0x08, 0x00, 0x00, 0x00, 0x1a, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
])


MOCK_LOGIN = bytes([
    0x80, 0x01, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x01, 0x02, 0x00, 0x00,
    0x61, 0x62, 0x63, 0x64, 0x31, 0x32, 0x33, 0x34,
    0x61, 0x62, 0x63, 0x64, 0x31, 0x32, 0x33, 0x34,
    0x61, 0x62, 0x63, 0x64, 0x31, 0x32, 0x33, 0x34,
    0x61, 0x62, 0x63, 0x64, 0x31, 0x32, 0x33, 0x34,
    0x61, 0x62, 0x63, 0x64, 0x31, 0x32, 0x33, 0x34,
    0x61, 0x62, 0x63, 0x64, 0x31, 0x32, 0x33, 0x34,
    0x61, 0x62, 0x63, 0x64, 0x31, 0x32, 0x33, 0x34,
    0x61, 0x62, 0x63, 0x64, 0x31, 0x32, 0x33, 0x34,
    0x6e, 0x61, 0x6d, 0x65, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x34, 0x2e, 0x34, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x6e, 0x61, 0x6d, 0x65, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
])


MOCK_STATUS_ACK = bytes([
    0x0c, 0x00, 0x00, 0x00, 0x14, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
])


MOCK_BOOT = bytes([
    0x18, 0x00, 0x00, 0x00, 0x0a, 0x00, 0x00, 0x00,
    0x43, 0x55, 0x53, 0x41, 0x30, 0x30, 0x30, 0x30,
    0x30, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
])

MOCK_RC_OPEN = bytes([
    0x10, 0x00, 0x00, 0x00, 0x1c, 0x00, 0x00, 0x00,
    0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
])

MOCK_RC_CLOSE = bytes([
    0x10, 0x00, 0x00, 0x00, 0x1c, 0x00, 0x00, 0x00,
    0x00, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
])

MOCK_RC_KEY_OFF = bytes([
    0x10, 0x00, 0x00, 0x00, 0x1c, 0x00, 0x00, 0x00,
    0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
])


MOCK_CREDS = (
    'abcd1234abcd1234'
    'abcd1234abcd1234'
    'abcd1234abcd1234'
    'abcd1234abcd1234'
)

MOCK_PIN = '12345678'
MOCK_NAME = 'name'
MOCK_TITLE_ID = 'CUSA00000'


def test_pub_key():
    pub_len = c._get_public_key_rsa().size_in_bytes()
    assert pub_len == 256


def test_hello_request():
    hello = c._get_hello_request()
    assert hello == MOCK_HELLO_REQUEST


def test_parse_hello_request():
    request = bytes(20) + MOCK_SEED
    parsed = c._parse_hello_request(request)
    assert parsed.seed == MOCK_SEED


def test_handshake_request():
    seed = bytes(16)
    handshake = bytearray(c._get_handshake_request(seed))
    assert len(handshake) == 280
    assert int.from_bytes(handshake[0:4], 'little') == 280
    assert handshake[4:8] == b'\x20\x00\x00\x00'
    assert handshake[-16:] == seed


def test_login_request():
    login = c._get_login_request(MOCK_CREDS, MOCK_NAME, MOCK_PIN)
    assert login == MOCK_LOGIN


def test_standby():
    standby = c._get_standby_request()
    assert standby == MOCK_STANDBY


def test_status_ack():
    request = c._get_status_ack()
    assert request == MOCK_STATUS_ACK


def test_boot_request():
    request = c._get_boot_request(MOCK_TITLE_ID)
    assert request == MOCK_BOOT


def test_remote_control():
    request = c._get_remote_control_open_request()
    assert request == MOCK_RC_OPEN
    request = c._get_remote_control_close_request()
    assert request == MOCK_RC_CLOSE
    request = c._get_remote_control_key_off_request()
    assert request == MOCK_RC_KEY_OFF
