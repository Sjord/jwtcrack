#!/usr/bin/python

from jwt import decode, InvalidTokenError, DecodeError
import sys


def is_jwt(jwt):
    parts = jwt.split('.')
    if len(parts) != 3:
        return False

    return True


def read_jwt(jwt):
    if not is_jwt(jwt):
        with open(jwt) as fp:
            jwt = fp.read().strip()

    if not is_jwt(jwt):
        raise RuntimeError("Parameter %s is not a valid JWT" % jwt)

    return jwt


def crack_jwt(jwt, dictionary):
    with open(dictionary) as fp:
        for secret in fp:
            secret = secret.rstrip()

            try:
                decode(jwt, secret, algorithms=['HS256'])
                return secret
            except DecodeError:
                # Signature verification failed
                pass
            except InvalidTokenError:
                # Signature correct, something else failed
                return secret


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: %s [JWT or JWT filename] [dictionary filename] " % sys.argv[0])
    else:
        jwt = read_jwt(sys.argv[1])
        print("Cracking JWT %s" % jwt)
        result = crack_jwt(jwt, sys.argv[2])
        if result:
            print("Found secret key:", result)
        else:
            print("Key not found")


