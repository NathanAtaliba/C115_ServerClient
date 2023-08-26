import mongoose, { Schema } from 'mongoose';

const userSchema = new Schema({
    name: {
        type: String,
        required: true,
    },
    
},{versionKey: false});

export default mongoose.model('User', userSchema);