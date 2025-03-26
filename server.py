import http.server
import ssl 

PORT=8443
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="chave.pem")
server_address=('', PORT)
handler= http.server.SimpleHTTPRequestHandler

httpd=http.server.HTTPServer(server_address, handler )
httpd.socket= context.wrap_socket(httpd.socket, server_side=True)

print("Servidor no ar {POST}")  

httpd.serve_forever()
