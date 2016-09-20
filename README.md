Crack a HS256-signed JWT. You need `PyJWT` for these scripts:

    pip install PyJWT

## crackjwt.py

    crackjwt.py JWT dictionary.txt

Try to verify the HS256 hash on the JWT using all words in `dictionary.txt` (one per line).

## jwt2john

    jwt2john.py JWT

Convert a JWT to a format John the Ripper can understand.
