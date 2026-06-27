from http.server import SimpleHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse, unquote, quote
import os

HOST = "127.0.0.1"
PORT = 8000
HTML_DIR = (Path(__file__).parent / "html").resolve()


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = unquote(urlparse(self.path).path)

        print(f"GET {path}")
        for k, v in self.headers.items():
            print(f"{k}: {v}")
        print()

        if path == "/":
            files = sorted(HTML_DIR.glob("*.html"))
            items = "\n".join(
                f'<li><a href="/html/{quote(f.name)}">{f.name}</a></li>'
                for f in files
            ) or "<li>Nessun file html trovato</li>"

            html = f"""<!doctype html>
<html>
<head><meta charset="utf-8"><title>Elenco file HTML</title></head>
<body>
  <h1>File HTML disponibili</h1>
  <ul>
    {items}
  </ul>
</body>
</html>"""

            data = html.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return

        if path.startswith("/html/"):
            name = path[len("/html/"):]
            file_path = (HTML_DIR / name).resolve()

            if file_path.parent != HTML_DIR or not file_path.is_file():
                self.send_error(404, "File non trovato")
                return

            data = file_path.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return

        self.send_error(404, "Risorsa non trovata")

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    HTML_DIR.mkdir(exist_ok=True)
    os.chdir(HTML_DIR.parent)

    server = HTTPServer((HOST, PORT), Handler)
    print(f"Server attivo su http://{HOST}:{PORT}")
    print(f"Directory html: {HTML_DIR}")
    server.serve_forever()