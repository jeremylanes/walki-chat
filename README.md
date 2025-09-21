# Walki-Chat

A simple command-line chat application using Python sockets, enabling real-time communication between a server and a client.

## Features

- Real-time bidirectional communication
- Simple and intuitive command-line interface
- Connection error handling
- Easy IP address and port configuration
- Lightweight with no external dependencies

## Prerequisites

- Python 3.x
- No external dependencies required (uses Python's standard libraries only)

## Installation

1. Clone this repository:
   ```bash
   git clone [REPO_URL]
   cd walki-chat
   ```

## Usage

### 1. Start the Server

Open a terminal and run:

```bash
python3 src/sockets_server.py
```

The server will start and wait for a connection on port 32000.

### 2. Start the Client

Open another terminal and run:

```bash
python3 src/sockets_client.py
```

By default, the client tries to connect to `127.0.0.1:32000`. If your server is running on a different machine, modify the `HOST_IP` variable in `sockets_client.py`.

### 3. How to Use

- The server sends the first message
- The client receives the message and can respond
- The conversation continues until one party quits (Ctrl+C)
- To send a message, type your text and press Enter
- Empty messages are ignored

## Configuration

You can modify the following settings in the respective files:

- `sockets_server.py`:
  - `HOST_IP`: Listening IP address (empty for all interfaces)
  - `HOST_PORT`: Listening port (default: 32000)
  - `MAX_DATA_SIZE`: Maximum data size for received messages (default: 1024 bytes)

- `sockets_client.py`:
  - `HOST_IP`: Server IP address (default: 127.0.0.1)
  - `HOST_PORT`: Server port (must match the server's port)
  - `MAX_DATA_SIZE`: Maximum data size for received messages (must match the server's setting)

## Troubleshooting

- **Connection Refused**: Ensure the server is running before starting the client
- **Port in Use**: If you get a port in use error, either:
  - Wait a few minutes for the port to become available, or
  - Change the `HOST_PORT` in both files to an available port
- **Connection Timeout**: Verify the server's IP address is correct if connecting over a network

## Author

- **Jérémy Lane**
- Portfolio: [www.jeremy.berlin](https://www.jeremy.berlin)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Future Improvements

- Support for multiple concurrent clients using threading
- Graphical user interface with Tkinter or PyQt
- Message encryption for secure communication
- Message history
- Username system for chat participants
- Special commands (/help, /quit, etc.)
- Cross-platform compatibility improvements
- Automated testing suite
- Logging system for debugging
- Configuration file support
