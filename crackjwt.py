#!/usr/bin/python

from jwt import decode, InvalidTokenError, DecodeError, get_unverified_header
import sys
from tqdm import tqdm
import os


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
    header = get_unverified_header(jwt)
    wordcount = 0

    with open(dictionary) as fp, tqdm() as pbar:
        fp.seek(0, os.SEEK_END)
        filesize = fp.tell()
        fp.seek(0, os.SEEK_SET)

        for secret in fp:
            pbar.update(1)
            wordcount += 1
            pbar.total = wordcount * filesize / fp.tell()

            secret = secret.rstrip()

            try:
                decode(jwt, secret, algorithms=[header["alg"]])
                return secret
            except DecodeError:
                # Signature verification failed
                pass
            except InvalidTokenError:
                # Signature correct, something else failed
                return secret


def signature_is_supported(jwt):
    header = get_unverified_header(jwt)
    return header["alg"] in ["HS256", "HS384", "HS512"]


def main(argv):
    if len(argv) != 3:
        print("Usage: %s [JWT or JWT filename] [dictionary filename] " % argv[0])
        return

    jwt = read_jwt(argv[1])
    if not signature_is_supported(jwt):
        print("Error: This JWT does not use a supported signing algorithm")
        return

    print("Cracking JWT %s" % jwt)
    result = crack_jwt(jwt, argv[2])
    if result:
        print("Found secret key:", result)
    else:
        print("Key not found")


if __name__ == "__main__":
    main(sys.argv)
