import { useState } from "react"

function Form(){
    const[formData,changeData]=useState({fname:'',lname:'',email:'',password:''})

    function updater(event){
        const{name,value}=event.target
        changeData({
            ...formData,
            [name]:value
        })
    }

    async function submit(event){
        event.preventDefault()
        const response=await fetch('http://127.0.0.1:8000/details/',{
            method:'post',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify(formData)
        })

        const data=await response.json()
        console.log(data.message)
    }

    return(
        <div>
            <form method="post">
                <input type="text" name="fname" placeholder="First Name" value={formData.fname} onChange={updater}/>
                <input type="text" name="lname" placeholder="Last Name"value={formData.lname} onChange={updater}/>
                <input type="email" name="email" placeholder="Email" value={formData.email} onChange={updater}/>
                <input type="password" name="password" placeholder="Password" value={formData.password} onChange={updater}/>

                <button type="submit" onClick={submit}>Submit</button>
            </form>
        </div>
    )


}

export default Form