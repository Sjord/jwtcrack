import sys
from jwt.utils import base64url_decode
from binascii import hexlify

enc_jwt = sys.argv[1].encode('utf-8')
parts = enc_jwt.split(b'.')
decoded_parts = [base64url_decode(p) for p in parts]
decoded_parts[2] = hexlify(decoded_parts[2])
data = parts[0] + b'.' + parts[1]
with open('jwt.john', 'wb') as fp:
    fp.write(data + b'#' + decoded_parts[2] + b"\n")
