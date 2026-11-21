"""Servidor unico: frontend estatico + API, en un solo puerto."""
import http.server, os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "backend"))
from backend import get_repository
from centros import get_centros_service
from restaurantes import get_restaurantes_service
from zonas_verdes import get_zonasverdes_service
from transporte import get_transporte_service
from supermercados import get_supermercados_service
from centros_medicos import get_centrosmedicos_service
from cai import get_cai_service
from veterinarias import get_veterinarias_service
from bibliotecas import get_bibliotecas_service
from vias import get_vias_service
from bancos import get_bancos_service
from cultos_religiosos import get_cultos_service
from predios import get_predios_service

repo = get_repository()
centros_svc = get_centros_service()
rest_svc = get_restaurantes_service()
zonas_svc = get_zonasverdes_service()
trans_svc = get_transporte_service()
supers_svc = get_supermercados_service()
medicos_svc = get_centrosmedicos_service()
cai_svc = get_cai_service()
vet_svc = get_veterinarias_service()
biblios_svc = get_bibliotecas_service()
vias_svc = get_vias_service()
bancos_svc = get_bancos_service()
cultos_svc = get_cultos_service()
predios_svc = get_predios_service()
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontend")
PORT = 8080

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)
    def _json(self, obj, code=200):
        b = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)
    def _body(self):
        n = int(self.headers.get("Content-Length", 0))
        try:
            return json.loads(self.rfile.read(n) or b"{}")
        except Exception:
            return {}
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
    def do_GET(self):
        if self.path == "/api/barrio":
            self._json(repo.load())
        elif self.path == "/api/health":
            self._json({"status": "ok"})
        elif self.path == "/api/centros":
            self._json(centros_svc.listar())
        elif self.path.startswith("/api/centros/"):
            cid = self.path.split("/")[-1]
            c = centros_svc.obtener(cid)
            self._json(c if c else {"error": "not found"}, 200 if c else 404)
        elif self.path == "/api/restaurantes":
            self._json(rest_svc.listar())
        elif self.path.startswith("/api/restaurantes/"):
            rid = self.path.split("/")[-1]
            r = rest_svc.obtener(rid)
            self._json(r if r else {"error": "not found"}, 200 if r else 404)
        elif self.path == "/api/zonasverdes":
            self._json(zonas_svc.listar())
        elif self.path.startswith("/api/zonasverdes/"):
            zid = self.path.split("/")[-1]
            z = zonas_svc.obtener(zid)
            self._json(z if z else {"error": "not found"}, 200 if z else 404)
        elif self.path == "/api/transporte":
            self._json(trans_svc.listar())
        elif self.path.startswith("/api/transporte/"):
            tid = self.path.split("/")[-1]
            t = trans_svc.obtener(tid)
            self._json(t if t else {"error": "not found"}, 200 if t else 404)
        elif self.path == "/api/supermercados":
            self._json(supers_svc.listar())
        elif self.path.startswith("/api/supermercados/"):
            sid = self.path.split("/")[-1]
            s = supers_svc.obtener(sid)
            self._json(s if s else {"error": "not found"}, 200 if s else 404)
        elif self.path == "/api/centrosmedicos":
            self._json(medicos_svc.listar())
        elif self.path.startswith("/api/centrosmedicos/"):
            mid = self.path.split("/")[-1]
            m = medicos_svc.obtener(mid)
            self._json(m if m else {"error": "not found"}, 200 if m else 404)
        elif self.path == "/api/cai":
            self._json(cai_svc.listar())
        elif self.path.startswith("/api/cai/"):
            cid = self.path.split("/")[-1]
            c = cai_svc.obtener(cid)
            self._json(c if c else {"error": "not found"}, 200 if c else 404)
        elif self.path == "/api/veterinarias":
            self._json(vet_svc.listar())
        elif self.path.startswith("/api/veterinarias/"):
            vid = self.path.split("/")[-1]
            v = vet_svc.obtener(vid)
            self._json(v if v else {"error": "not found"}, 200 if v else 404)
        elif self.path == "/api/bibliotecas":
            self._json(biblios_svc.listar())
        elif self.path.startswith("/api/bibliotecas/"):
            bid = self.path.split("/")[-1]
            b = biblios_svc.obtener(bid)
            self._json(b if b else {"error": "not found"}, 200 if b else 404)
        elif self.path == "/api/vias":
            self._json(vias_svc.listar())
        elif self.path.startswith("/api/vias/"):
            vid = self.path.split("/")[-1]
            v = vias_svc.obtener(vid)
            self._json(v if v else {"error": "not found"}, 200 if v else 404)
        elif self.path == "/api/bancos":
            self._json(bancos_svc.listar())
        elif self.path.startswith("/api/bancos/"):
            bid = self.path.split("/")[-1]
            b = bancos_svc.obtener(bid)
            self._json(b if b else {"error": "not found"}, 200 if b else 404)
        elif self.path == "/api/cultos":
            self._json(cultos_svc.listar())
        elif self.path.startswith("/api/cultos/"):
            cid = self.path.split("/")[-1]
            c = cultos_svc.obtener(cid)
            self._json(c if c else {"error": "not found"}, 200 if c else 404)
        elif self.path == "/api/predios":
            self._json(predios_svc.listar())
        elif self.path.startswith("/api/predios/"):
            pid = self.path.split("/")[-1]
            p = predios_svc.obtener(pid)
            self._json(p if p else {"error": "not found"}, 200 if p else 404)
        else:
            super().do_GET()
    def do_POST(self):
        if self.path == "/api/centros":
            try:
                self._json(centros_svc.crear(self._body()), 201)
            except ValueError as e:
                self._json({"error": str(e)}, 400)
        elif self.path == "/api/restaurantes":
            try:
                self._json(rest_svc.crear(self._body()), 201)
            except ValueError as e:
                self._json({"error": str(e)}, 400)
        elif self.path == "/api/zonasverdes":
            try:
                self._json(zonas_svc.crear(self._body()), 201)
            except ValueError as e:
                self._json({"error": str(e)}, 400)
        elif self.path == "/api/transporte":
            try:
                self._json(trans_svc.crear(self._body()), 201)
            except ValueError as e:
                self._json({"error": str(e)}, 400)
        elif self.path == "/api/supermercados":
            try:
                self._json(supers_svc.crear(self._body()), 201)
            except ValueError as e:
                self._json({"error": str(e)}, 400)
        elif self.path == "/api/centrosmedicos":
            try:
                self._json(medicos_svc.crear(self._body()), 201)
            except ValueError as e:
                self._json({"error": str(e)}, 400)
        elif self.path == "/api/cai":
            try:
                self._json(cai_svc.crear(self._body()), 201)
            except ValueError as e:
                self._json({"error": str(e)}, 400)
        elif self.path == "/api/veterinarias":
            try:
                self._json(vet_svc.crear(self._body()), 201)
            except ValueError as e:
                self._json({"error": str(e)}, 400)
        elif self.path == "/api/bibliotecas":
            try:
                self._json(biblios_svc.crear(self._body()), 201)
            except ValueError as e:
                self._json({"error": str(e)}, 400)
        elif self.path == "/api/vias":
            try:
                self._json(vias_svc.crear(self._body()), 201)
            except ValueError as e:
                self._json({"error": str(e)}, 400)
        elif self.path == "/api/bancos":
            try:
                self._json(bancos_svc.crear(self._body()), 201)
            except ValueError as e:
                self._json({"error": str(e)}, 400)
        elif self.path == "/api/cultos":
            try:
                self._json(cultos_svc.crear(self._body()), 201)
            except ValueError as e:
                self._json({"error": str(e)}, 400)
        elif self.path == "/api/predios":
            try:
                self._json(predios_svc.crear(self._body()), 201)
            except ValueError as e:
                self._json({"error": str(e)}, 400)
        else:
            self._json({"error": "not found"}, 404)
    def do_PUT(self):
        if self.path.startswith("/api/centros/"):
            cid = self.path.split("/")[-1]
            c = centros_svc.actualizar(cid, self._body())
            self._json(c if c else {"error": "not found"}, 200 if c else 404)
        elif self.path.startswith("/api/restaurantes/"):
            rid = self.path.split("/")[-1]
            r = rest_svc.actualizar(rid, self._body())
            self._json(r if r else {"error": "not found"}, 200 if r else 404)
        elif self.path.startswith("/api/zonasverdes/"):
            zid = self.path.split("/")[-1]
            z = zonas_svc.actualizar(zid, self._body())
            self._json(z if z else {"error": "not found"}, 200 if z else 404)
        elif self.path.startswith("/api/transporte/"):
            tid = self.path.split("/")[-1]
            t = trans_svc.actualizar(tid, self._body())
            self._json(t if t else {"error": "not found"}, 200 if t else 404)
        elif self.path.startswith("/api/supermercados/"):
            sid = self.path.split("/")[-1]
            s = supers_svc.actualizar(sid, self._body())
            self._json(s if s else {"error": "not found"}, 200 if s else 404)
        elif self.path.startswith("/api/centrosmedicos/"):
            mid = self.path.split("/")[-1]
            m = medicos_svc.actualizar(mid, self._body())
            self._json(m if m else {"error": "not found"}, 200 if m else 404)
        elif self.path.startswith("/api/cai/"):
            cid = self.path.split("/")[-1]
            c = cai_svc.actualizar(cid, self._body())
            self._json(c if c else {"error": "not found"}, 200 if c else 404)
        elif self.path.startswith("/api/veterinarias/"):
            vid = self.path.split("/")[-1]
            v = vet_svc.actualizar(vid, self._body())
            self._json(v if v else {"error": "not found"}, 200 if v else 404)
        elif self.path.startswith("/api/bibliotecas/"):
            bid = self.path.split("/")[-1]
            b = biblios_svc.actualizar(bid, self._body())
            self._json(b if b else {"error": "not found"}, 200 if b else 404)
        elif self.path.startswith("/api/vias/"):
            vid = self.path.split("/")[-1]
            v = vias_svc.actualizar(vid, self._body())
            self._json(v if v else {"error": "not found"}, 200 if v else 404)
        elif self.path.startswith("/api/bancos/"):
            bid = self.path.split("/")[-1]
            b = bancos_svc.actualizar(bid, self._body())
            self._json(b if b else {"error": "not found"}, 200 if b else 404)
        elif self.path.startswith("/api/cultos/"):
            cid = self.path.split("/")[-1]
            c = cultos_svc.actualizar(cid, self._body())
            self._json(c if c else {"error": "not found"}, 200 if c else 404)
        elif self.path.startswith("/api/predios/"):
            pid = self.path.split("/")[-1]
            p = predios_svc.actualizar(pid, self._body())
            self._json(p if p else {"error": "not found"}, 200 if p else 404)
        else:
            self._json({"error": "not found"}, 404)
    def do_DELETE(self):
        if self.path.startswith("/api/centros/"):
            cid = self.path.split("/")[-1]
            ok = centros_svc.eliminar(cid)
            self._json({"status": "deleted"} if ok else {"error": "not found"}, 200 if ok else 404)
        elif self.path.startswith("/api/restaurantes/"):
            rid = self.path.split("/")[-1]
            ok = rest_svc.eliminar(rid)
            self._json({"status": "deleted"} if ok else {"error": "not found"}, 200 if ok else 404)
        elif self.path.startswith("/api/zonasverdes/"):
            zid = self.path.split("/")[-1]
            ok = zonas_svc.eliminar(zid)
            self._json({"status": "deleted"} if ok else {"error": "not found"}, 200 if ok else 404)
        elif self.path.startswith("/api/transporte/"):
            tid = self.path.split("/")[-1]
            ok = trans_svc.eliminar(tid)
            self._json({"status": "deleted"} if ok else {"error": "not found"}, 200 if ok else 404)
        elif self.path.startswith("/api/supermercados/"):
            sid = self.path.split("/")[-1]
            ok = supers_svc.eliminar(sid)
            self._json({"status": "deleted"} if ok else {"error": "not found"}, 200 if ok else 404)
        elif self.path.startswith("/api/centrosmedicos/"):
            mid = self.path.split("/")[-1]
            ok = medicos_svc.eliminar(mid)
            self._json({"status": "deleted"} if ok else {"error": "not found"}, 200 if ok else 404)
        elif self.path.startswith("/api/cai/"):
            cid = self.path.split("/")[-1]
            ok = cai_svc.eliminar(cid)
            self._json({"status": "deleted"} if ok else {"error": "not found"}, 200 if ok else 404)
        elif self.path.startswith("/api/veterinarias/"):
            vid = self.path.split("/")[-1]
            ok = vet_svc.eliminar(vid)
            self._json({"status": "deleted"} if ok else {"error": "not found"}, 200 if ok else 404)
        elif self.path.startswith("/api/bibliotecas/"):
            bid = self.path.split("/")[-1]
            ok = biblios_svc.eliminar(bid)
            self._json({"status": "deleted"} if ok else {"error": "not found"}, 200 if ok else 404)
        elif self.path.startswith("/api/vias/"):
            vid = self.path.split("/")[-1]
            ok = vias_svc.eliminar(vid)
            self._json({"status": "deleted"} if ok else {"error": "not found"}, 200 if ok else 404)
        elif self.path.startswith("/api/bancos/"):
            bid = self.path.split("/")[-1]
            ok = bancos_svc.eliminar(bid)
            self._json({"status": "deleted"} if ok else {"error": "not found"}, 200 if ok else 404)
        elif self.path.startswith("/api/cultos/"):
            cid = self.path.split("/")[-1]
            ok = cultos_svc.eliminar(cid)
            self._json({"status": "deleted"} if ok else {"error": "not found"}, 200 if ok else 404)
        elif self.path.startswith("/api/predios/"):
            pid = self.path.split("/")[-1]
            ok = predios_svc.eliminar(pid)
            self._json({"status": "deleted"} if ok else {"error": "not found"}, 200 if ok else 404)
        else:
            self._json({"error": "not found"}, 404)
    def log_message(self, *a):
        pass

if __name__ == "__main__":
    http.server.HTTPServer(("0.0.0.0", PORT), H).serve_forever()
