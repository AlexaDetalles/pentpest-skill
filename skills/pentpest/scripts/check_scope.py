"""Exact-origin scope validation. No network requests."""
import argparse,json
from urllib.parse import urlsplit

def origin(value):
    p=urlsplit(value)
    if p.scheme not in ('http','https') or not p.hostname or p.username is not None or p.password is not None:
        raise ValueError('URL HTTP(S) sin credenciales requerida')
    if p.fragment:
        raise ValueError('Eliminar fragmento de la URL antes de validar')
    return p.scheme,p.hostname.lower(),p.port or (443 if p.scheme=='https' else 80)

def allowed(url,origins):
    try:
        if not origins:return False
        return origin(url) in [origin(o) for o in origins]
    except (ValueError,TypeError):return False

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('url');p.add_argument('--allow',action='append',default=[])
    a=p.parse_args();ok=allowed(a.url,a.allow)
    print(json.dumps({'url':a.url,'allowed':ok,'note':'Exact origin only; does not intercept redirects or other tools'}))
    raise SystemExit(0 if ok else 2)
