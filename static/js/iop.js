function Readydelete(){
    if (confirm("您确认要删除该条信息吗？")){
        console.log("Start")
        var del = document.createElement("input")
        del.name = "operate"
        del.value = "delete"
        var text = document.forms['ManageForm']
        text.appendChild(del)
        text.submit()
    }else{

        console.log("Stop")
    }
}