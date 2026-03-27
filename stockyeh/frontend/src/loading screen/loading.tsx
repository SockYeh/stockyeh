import { motion } from "motion/react";
function Loading() {
    return (
        <>
            <motion.div className="bg-black">
                <motion.div className="bg-linear-to-b from-[#0088FF] to-[#A3F2E0] h-screen flex flex-col  justify-center items-center gap-0.5 " initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 1 }}>

                    {/*<motion.div className="bg-white  h-2 w-57 rounded-xl " initial={{ opacity: 0, y: -50 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8, ease: "linear" }} />*/}
                    <motion.div className="flex" >
                        <motion.h1 className="text-white font-bold font-mono text-5xl flex-1" initial={{ opacity: 0, y: -100 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8, ease: "linear" }}>S</motion.h1>
                        <motion.h1 className="text-white font-bold font-mono text-5xl flex-2" initial={{ opacity: 0, y: -100 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.9, ease: "linear" }}>T</motion.h1>
                        <motion.h1 className="text-white font-bold font-mono text-5xl flex-3" initial={{ opacity: 0, y: -100 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 1.0, ease: "linear" }}>O</motion.h1>
                        <motion.h1 className="text-white font-bold font-mono text-5xl flex-4" initial={{ opacity: 0, y: -100 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 1.1, ease: "linear" }}>C</motion.h1>
                        <motion.h1 className="text-white font-bold font-mono text-5xl flex-5" initial={{ opacity: 0, y: -100 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 1.2, ease: "linear" }}>K</motion.h1>
                        <motion.h1 className="text-white font-bold font-mono text-5xl flex-6" initial={{ opacity: 0, y: -100 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 1.3, ease: "linear" }}>Y</motion.h1>
                        <motion.h1 className="text-white font-bold font-mono text-5xl flex-7" initial={{ opacity: 0, y: -100 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 1.4, ease: "linear" }}>E</motion.h1>
                        <motion.h1 className="text-white font-bold font-mono text-5xl flex-8" initial={{ opacity: 0, y: -100 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 1.5, ease: "linear" }}>H</motion.h1>
                    </motion.div>
                </motion.div>
            </motion.div>

        </>
    )
}

export default Loading