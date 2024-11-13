# JSON-RPC

Testing project for JSON RPC.

- JSON-RPC [Python library](https://pypi.org/project/json-rpc/).
- JSON-RPC [Specification](https://www.jsonrpc.org/specification).

## Install

```shell
docker compose up -d
docker exec jrpc python client.py
POST http://0.0.0.0:4000/ {'result': 4, 'id': 1, 'jsonrpc': '2.0'}
```
