# FTLAB OpenBB desks (public host mirror)

Canonical source (private): https://github.com/shayankargarian/ftlab-openbb-desks

Live HTTPS backend: https://backend-production-bace4.up.railway.app

This public mirror exists so Railway can fetch Workspace JSON over HTTPS without the Railway GitHub App. No secrets. Friend env is not here.

```bash
curl -sS https://backend-production-bace4.up.railway.app/health
curl -sS https://backend-production-bace4.up.railway.app/widgets.json | head
curl -sS https://backend-production-bace4.up.railway.app/apps.json | head
```
