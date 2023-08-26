import net from 'net';
import  readLine  from 'readline';

const rl = readLine.createInterface({
    input: process.stdin,
    output: process.stdout
  });

const client = new net.Socket();

client.connect(3000, '127.0.0.1', async() => {
    console.log('Conectado ao servidor.'); 
});

client.on('error', error => {
    console.error('Erro no cliente:', error);
   });