#!/usr/bin/python

import jwt
import sys
import pdb

encoded = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEyMzQ1Njc4OTAsIm5hbWUiOiJKb2huIERvZSIsImFkbWluIjp0cnVlfQ.eoaDVGTClRdfxUZXiPs3f8FmJDkDE_VCQFXqKxpLsts'

with open(sys.argv[1]) as secrets:
    for secret in secrets:
        try:
            payload = jwt.decode(encoded, secret.rstrip(), algorithms=['HS256'])
            print("Success", secret)
        except jwt.InvalidTokenError as e:
            if e.args[0] == 'Signature verification failed':
                pass
            else:
                print("Success", secret)
                break
        except jwt.ExpiredSignatureError:
            print("Token expired")
