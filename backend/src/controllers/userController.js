import User from '../models/user.js'

async function getUsers(req, res){
    const users = await User.find();
    return res.status(200).json(users);
}

async function createUser(req, res){
    const user = req.body;
    const newUser = await User.create(user);
    return res.status(201).json(newUser);
}

async function deleteUser(req, res){
    const id = req.params.id;
    await User.findByIdAndDelete(id);
    return res.status(200).send(`User deleted with id: ${id}`);
}

async function updateUser(req, res){
    const id = req.params.id;
    //Parametros a serem atualizados
    await User.findByIdAndUpdate({ '_id' : id}, {'name': 'louco'})
    return res.status(200).send(`User updated with id: ${id}`)
}

export { getUsers, createUser, deleteUser, updateUser };