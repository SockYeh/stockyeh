import background from '../backgrounds/Desktop - 8 (1).png';




import image from '../backgrounds/Movie Inspired Poster_ ‘Moving Parts’.jpeg';


function Login() {
    return (

        <>

            <img src={background} alt="background" className='w-400 h-182 z-0' />
            

            <div className=" h-140 w-250 flex    justify-between backdrop-blur-lg backdrop-brightness-90 shadow-2xl shadow-gray-400  position absolute top-25 left-65 rounded-3xl"> 
                <img src={image} className='flex-1  rounded-3xl' />

                
                <div className='flex-2 '>
                    <label>
                        <input placeholder='Enter Sock ID'></input>
                        <input placeholder='Enter PassKey'></input>
                        <button>Login</button>

                    </label>
                </div>
            </div>

        </>
    );
}

export default Login