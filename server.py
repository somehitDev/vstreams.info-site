# -*- coding: utf-8 -*-
from aiohttp import web
from python_chzzk import Chzzk, Credential


# chzzk client 연결
credential = Credential("0odVEYQ2xzEcPXZnJ5eCPWbMO+omgRI9zplzBSNmJ1jGzOSk2VRUIvDWfh12yuvN", "AAABvQ2KzqE36NRvGFfrWVK1pQTtxjqrWE7tCNnBa/D5QIdPzfnf32CmBc8TtKFg3pw5gcxcDSkZ3GUCavjnU3RMdoVr3NtaE8RRCfmVX25+gsxNwutMphp6t7ItrS0VemL5PvKENyQj8z7laGYnAvGbegdlWrRyfLWeSSocHNPy7kXMGrLacwuIaLIx+0KaTP89XhT8K2A3NEdNEPCwM0hz0flvU4cZ9X3eRC+NZHn13xf6ZVWf1Wo+ByiLWMJBu/jodPgSlvfe9Sqj1AQqM1yCFw5VnJc2IsIooS/IG1YEkNtmlAIAf5N06Y+nAEPwwiixYwnuQP3iQLd1u6RGyJaoXJTceB/a78BQ03FNKZclfHqZqBstY4XcXDqsX4c5bIRZWmNLcHQhAPh6UpZoWUDGOxDdZO7ixsuS+re0DUK9TBOUtXxKBx7kc5lK/+m12iYARmgOUy0F/F8J9lN/iTQzyCYLn6Vz1RnxDwNu9nEPoaFaCN0LMDhoov5p9F9VG2kLo8gXH9PobZ9G+vsVMRAzOsrrJCSzF8GQo+dwvbMSlHGvj7s4VexALRkfjWlenNJe4T5mgnwS9fNQA9f33ioQhT8=")
chzzk = Chzzk(credential)

app = web.Application()


if __name__ == "__main__":
    # get flags
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--develop", action = "store_true")
    args = parser.parse_args()

    # register apps
    from apps.shedar_live import ShedarLive
    app.add_subapp("/shedar", ShedarLive(chzzk, "d44e0ee22e283843ea90ea7d8036fb17", args.develop))

    # start server
    web.run_app(app, host = "127.0.0.1", port = 63000)
