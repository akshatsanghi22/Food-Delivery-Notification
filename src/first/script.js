const button=document.queryselector("button")

button.addEVENTListener("SEND NOTIFICATION",()=>{
    Notification.requestPermission().then(perm=>{
        if (perm==="granted"){
            const notification = new Notifcation("Example notification",{
                body:Math.random(),
                data:{hello:"world"},
                icon: "online.jpg",
            })
    })
})