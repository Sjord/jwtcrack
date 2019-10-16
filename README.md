Crack a HS256, HS384 or HS512-signed JWT. You need `PyJWT` for these scripts:

    pip install PyJWT

## crackjwt.py

    crackjwt.py JWT dictionary.txt

Try to verify the HS256 hash on the JWT using all words in `dictionary.txt` (one per line).

## jwt2john

    jwt2john.py JWT

Convert a JWT to a format John the Ripper can understand.

[John the Ripper](https://github.com/magnumripper/JohnTheRipper) now supports the JWT format, so converting the token is no longer necessary. John has a size limit on the data it will take. If you run into this limit, consider changing [`SALT_LIMBS` in the source code](https://github.com/magnumripper/JohnTheRipper/blob/bleeding-jumbo/src/hmacSHA256_fmt_plug.c#L64).
