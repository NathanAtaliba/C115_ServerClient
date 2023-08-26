import mongoose, { Schema } from 'mongoose';

const QuestionSchema = new Schema({
    name:{
        type: String,
        required: true
    }
},{versionKey: false})

export default mongoose.model('Question', QuestionSchema);