const http = require('http');
const httpProxy = require('http-proxy');

const proxy = httpProxy.createProxyServer({});

const server = http.createServer((req, res) => {
  // Adicionar headers CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Proxy para o Angular
  proxy.web(req, res, { 
    target: 'http://localhost:8765',
    changeOrigin: true
  });
});

// Mudança: usar porta 9090 em vez de 9000
server.listen(9090, '0.0.0.0', () => {
  console.log('Proxy rodando na porta 9090');
  console.log('Acesse: http://princesistemas.ddns.net:9090');
});