import mongoose, { Schema } from 'mongoose';

const clientSchema = new Schema({
    name: {
        type: String,
        required: true,
    },
    email: {
        type: String,
        required: true
    }, 
    password: {
        type: String,
        required: true
    },
    number: {
        type: Number,
        required: true
    },
    hora_marcada: {
        type: String,
        required: true
    },
    
},{versionKey: false});

export default mongoose.model('Client', clientSchema);