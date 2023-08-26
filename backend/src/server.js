import express from 'express';
import net from 'net';
import cors from 'cors';
import connectionDatabase from './database/db.js';
import routes from './routes.js';
import Question from './models/question.js';

const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());
app.use(routes);

const server = net.createServer(socket => {
  console.log('Cliente conectado:', socket.remoteAddress, socket.remotePort);
  Question.find({})
  .then(questoes => {
    questoes.forEach(questao => {
      socket.write(JSON.stringify(questao));
      });
      socket.end();
    })
    .catch(err => {
      console.error('Erro ao buscar questoes:', err);
      socket.end();
    });
});

server.on('error', error => {
  console.error('Erro no servidor:', error);
});

connectionDatabase()
  .then(() => {
    server.listen(port, '0.0.0.0', () => {
      console.log(`App rodando na porta ${port}`);
    });
  })
  .catch(error => {
    console.log('Erro:', error);
  });