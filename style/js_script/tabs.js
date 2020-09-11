function days_tabs(evt,day){
    var i,tabs,link;
    
    tabs=document.getElementsByClassName("days_content");
    console.log(tabs.length)
    for(i=0;i<tabs.length;i++){
        tabs[i].style.display="none";
    }

    link=document.getElementsByClassName("days");
    for(i=0;i<link.length;i++){
        link[i].className = link[i].className.replace(" active","");
    }

    document.getElementById(day).style.display = "block";
    evt.currentTarget.className += " active"
}

