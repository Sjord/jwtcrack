#!/usr/bin/python

from jwt import decode, InvalidTokenError, DecodeError, get_unverified_header
import sys


def is_jwt(jwt):
    parts = jwt.split(".")
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
                decode(jwt, secret, algorithms=["HS256"])
                return secret
            except DecodeError:
                # Signature verification failed
                pass
            except InvalidTokenError:
                # Signature correct, something else failed
                return secret


def is_hs256(jwt):
    header = get_unverified_header(jwt)
    return header["alg"] == "HS256"


def main(argv):
    if len(argv) != 3:
        print("Usage: %s [JWT or JWT filename] [dictionary filename] " % argv[0])
        return

    jwt = read_jwt(argv[1])
    if not is_hs256(jwt):
        print("Error: This JWT does not use the HS256 signing algorithm")
        return

    print("Cracking JWT %s" % jwt)
    result = crack_jwt(jwt, argv[2])
    if result:
        print("Found secret key:", result)
    else:
        print("Key not found")


if __name__ == "__main__":
    main(sys.argv)
