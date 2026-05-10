import type { ReactDOMServerReadableStream } from 'react-dom/server';
import background from '../backgrounds/Desktop - 8 (1).png';
import image from '../backgrounds/Movie Inspired Poster_ ‘Moving Parts’.jpeg';
import { useState, type ReactElement, type ReactHTMLElement } from 'react';



function Login() {
    const [message,setMessage]=useState("");

    function handleSubmit(){
        
        if(!message.trim()){
            alert("please enter");
        }
    }

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {

        setMessage(event.target.value);
        
    }
    return (
        <>
            <img src={background} alt="background" className='w-400 h-182 z-0' /> 
            <div className=" h-140 w-250 flex    justify-between backdrop-blur-lg backdrop-brightness-90 shadow-2xl shadow-gray-400  position absolute top-25 left-65 rounded-3xl"> 
                <img src={image} className='flex-1  rounded-3xl' />   
                <div className='flex-2 '>
                    <label className='grid grid-col-1 grid-rows-2 gap-40 justify-center '>
                    
                        <input placeholder='Enter PassKey' value={message} onChange={handleChange}  className='col-span-1 row-span-1'></input>
                        <button className='col-span-1 row-span-1 border-2 rounded-lg' onClick={handleSubmit} >Login</button>
                    </label>
                </div>
            </div>
        </>
    );
}

export default Login