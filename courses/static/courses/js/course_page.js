var player;
var video_list;
document.onreadystatechange = function(){
    if(document.readyState == 'interactive'){
        
player = document.getElementById("player")
video_list = document.getElementById("video_list")

 maintainRatio()
    
    }
}

window.onresize = maintainRatio
function maintainRatio(){

console.log({
    width: player.width,
    cw :player.clientWidth,
    h:player.height,
    ch: player.clientHeight, 
});

var w = player.clientWidth
var h = (w*9)/16
console.log(w,h);
player.height = h
video_list.style.maxHeight = h + "px"



}