from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlsplit, parse_qs
from html import escape
import re
import os
class Handler(SimpleHTTPRequestHandler):
 def do_GET(self):
  u=urlsplit(self.path)
  if u.path in ('/','/index.html'):
   q=parse_qs(u.query); events=q.get('e',['mbw'])[0].lower(); shown=[(k,n) for k,n in [('m','Mehandi · 10 Nov'),('b','Baraat · 11 Nov'),('w','Walima · 12 Nov')] if k in events]
   description='Mr. & Mrs. Mulazim Hussain invite you. '+(' · '.join(n for _,n in shown) if shown else 'Tap to open your invitation.')+' 2026. Tap to open your invitation.'
   host=self.headers.get('X-Forwarded-Host',self.headers.get('Host','localhost:8001')).split(',')[0].strip()
   if not re.fullmatch(r'[A-Za-z0-9.\-\[\]:]+',host): host='localhost:8001'
   proto='https' if self.headers.get('X-Forwarded-Proto','').split(',')[0].strip()=='https' else 'http'
   base=f'{proto}://{host}'
   html=open('index.html',encoding='utf-8').read(); html=re.sub(r'<meta property="og:description"[^>]*>',f'<meta property="og:description" content="{escape(description,quote=True)}">',html,count=1); html=html.replace('<meta property="og:image" content="">',f'<meta property="og:image" content="{base}/preview.jpg">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta name="twitter:image" content="{base}/preview.jpg">')
   body=html.encode();self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body)
  else: super().do_GET()
HTTPServer(('0.0.0.0', int(os.environ.get('PORT', '8001'))), Handler).serve_forever()
