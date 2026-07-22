function Chat(){
    async function sendMessage(){
        const response=await fetch('http://127.0.0.1:8000/chat/',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                message:"Hello Django, This is react"
            })
        })
        const data=await response.json()
        console.log(data)
    }

    return(
        <>
        <header>
            <h1>Hello</h1>
        </header>
        <button onClick={sendMessage}>Send</button>
        </>
    )
}

export default Chat