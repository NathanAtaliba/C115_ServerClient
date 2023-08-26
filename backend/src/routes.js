import { Router } from 'express';
import { getUsers, createUser, deleteUser, updateUser } from './controllers/userController.js';
import { getQuestions, createQuestion, deleteQuestion, updateQuestion } from './controllers/questionController.js';
const routes = Router();

//ROUTES CLIENT
routes.get('/user', getUsers);
routes.post('/user', createUser);
routes.delete('/user/:id', deleteUser);
routes.put('/user/:id', updateUser);

//ROUTES HAIRDRESSER
routes.get('/question', getQuestions);
routes.post('/question', createQuestion);
routes.delete('/question/:id', deleteQuestion);
routes.put('/question/:id', updateQuestion);

export default routes;