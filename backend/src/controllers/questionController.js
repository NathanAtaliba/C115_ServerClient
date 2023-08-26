import Question from "../models/question.js";

async function getQuestions(req, res){
    const questions = await Question.find();
    return res.status(200).send(questions);
}

async function createQuestion(req, res){
    const question = req.body;
    const newQuestion = await Question.create(question);
    return res.status(201).json(newQuestion);
}
async function deleteQuestion(req, res){
    const id = req.params.id;
    await Question.findByIdAndDelete(id);
    return res.status(200).send(`Question removed with id: ${id}`);
}
async function updateQuestion(req, res){
    const id = req.params.id;
    await Question.findByIdAndUpdate({"_id": id},{"name": "sebastiao"});
    return res.status(200).send(`Questipn update with id: ${id}`);
}

export { getQuestions, createQuestion, deleteQuestion, updateQuestion }; 