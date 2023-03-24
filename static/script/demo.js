function disp(ver){
    let p = document.querySelector('p')
    console.log(ver)
    if(ver == 'spam'){
        p.style.color  = 'red'
    }else{
        p.style.color = 'green'
    }
}
