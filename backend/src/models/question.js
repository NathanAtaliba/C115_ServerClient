import mongoose, { Schema } from 'mongoose';

const HairdresserSchema = new Schema({
    name:{
        type: String,
        required: true
    },
    email:{
        type: String,
        required: true
    }, 
    number:{
        type: String,
        required: true
    },
    desc:{
        type: String,
        required: true
    },
},{versionKey: false})

export default mongoose.model('Hairdresser', HairdresserSchema);