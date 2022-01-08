from typing import Any, List


class SanityCheck:
    __instance = None

    def __new__(cls, *args: Any, **kwargs: Any) -> Any:
        if not SanityCheck.__instance:
            SanityCheck.__instance = super(SanityCheck, cls).__new__(cls, *args, **kwargs)
        return SanityCheck.__instance

    def __init__(self) -> None:
        self.__servers: List = list()

    def get_servers(self) -> List:
        return self.__servers

    def server_check(self, server_id: int) -> None:
        print(f"checking server {self.__servers[server_id]} activity...")

    def add_server(self, server_id: int) -> None:
        self.__servers.append(server_id)
        print("Server added successfully.")


sanity_check_I = SanityCheck()
sanity_check_II = SanityCheck()

"""
Both classes have only a single instance and there is no distinction between them.
"""

for server in range(1000, 1010):
    sanity_check_I.add_server(server_id=server)

for server in range(0, len(sanity_check_II.get_servers())):
    sanity_check_II.server_check(server)
