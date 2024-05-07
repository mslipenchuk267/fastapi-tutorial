# FastAPI Tutorial

This is a test bed for practicing a python fast-api, postgresql, and docker stack.

## Deployment

### Development

Set local development PostgreSQL connection info in ```compose.override.yaml```

```docker compose up -d```

## Production


Set Production PostgreSQL connection info in ```compose.prod.yaml```

```docker compose -f compose.yaml -f compose.prod.yaml up -d```
