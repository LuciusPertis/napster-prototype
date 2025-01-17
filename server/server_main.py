"""
Server Main - Entry point for managing client registrations and peer discovery.
"""

from server.server_registry import register_client, get_peer_list
from typing import Tuple

class Server:
    def __init__(self, host: str, port: int):
        """
        Initialize the server with specified host and port.
        
        Args:
            host (str): Host IP address.
            port (int): Port number to listen on.
        """
        self.host = host
        self.port = port
        self.client_registry = {}  # Registry of connected clients

    def start(self):
        """
        Starts the server to listen for client connections and requests.
        """
        # TODO: Initialize a socket server to listen on the specified port
        # HINT: Use multithreading to handle multiple client connections.
        pass

    def handle_client_registration(self, client_id: str, client_ip: str) -> bool:
        """
        Registers a new client in the server’s registry.

        Args:
            client_id (str): Unique identifier of the client.
            client_ip (str): IP address of the client.

        Returns:
            bool: True if registration is successful, False otherwise.
        """
        return register_client(self.client_registry, client_id, client_ip)

    def handle_peer_discovery(self, client_id: str) -> list[str]:
        """
        Provides a list of active peers to a requesting client.

        Args:
            client_id (str): Unique identifier of the requesting client.

        Returns:
            list[str]: List of IP addresses of other clients.
        """
        return get_peer_list(self.client_registry, client_id)


# Example usage
if __name__ == "__main__":
    server = Server(host="0.0.0.0", port=8080)
    server.start()
