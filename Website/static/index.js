var socket = io();
socket.on('connect', async function() {
    var user_name = await logged_user();
    if (user_name != ""){
    socket.emit('event', {message: user_name + ' has joined the chat'});
    }
    var form = $("form#msgform").on("submit", async function(alert){
        alert.preventDefault();
        let messagediv = document.getElementById("inputmsg");
        let msg = messagediv.value;
        if(msg!==""){
        let name = await logged_user();
        messagediv.value = ""
        socket.emit('event', {message:msg, name:name})
        }})
        });

async function logged_user(){
    return await fetch("/logged_user")
    .then(function (response) {return response.json();})
    .then(function (text) {
    return text['name'];
    }).
    catch(function (){
    console.log("no user yet")
    })}


socket.on('response', async function(recv_message){
addmessage(recv_message, true);
})

async function addmessage(response, scroll){

    var name = await logged_user()
    if(typeof response.time !== "undefined"){
    var time = response.time;}
    else{
    var time = find_time();
    }

    var content = '<div class="container">'+'<b style="color:#000" class="right">'+ response.name + '</b><p>'+response.message+'</p><span class="time-right">'+time+'</span></div>';

    if (name == response.name){
    content = '<div class="container darker">'+'<b style="color:#000" class="left">'+ response.name + '</b><p>'+response.message+'</p><span class="time-left">'+time+'</span></div>';
    }

    var msgdiv = document.getElementById("msgcontainer");
    msgdiv.innerHTML += content;

    if (scroll){
    add_scroll("msgcontainer")
    }
};

window.onload = async function(){
    var scroll = false;
    var load_msgs = await load_history()
    for(i=0;i<load_msgs.length;i++){
    if(i === load_msgs.length -1){
    scroll = true}
    addmessage(load_msgs[i], scroll);
    }

};

async function load_history(){
return await fetch('/get_messages')
.then(async function(response){
return await response.json()}).
then(function(text){
return text;})
};



function find_time(){
    var date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    var day = date.getDate();

    if(day<10){
    day = '0' + day;
    }
    if(month<10){
    month = '0' + month;
    }
    var hour = date.getHours();
    var min = date.getMinutes();
    if(hour<10){
    hour = '0' + hour;
    }
    if(min<10){
    min = '0' + min;
    }

    var date_format = year+'-'+month+'-'+day+" "+hour+":"+min;
    return date_format;
}

$(function(){
    $(".msgcontainer").css({height:$(window).height * 0.7 + "px"});
    $(window).bind("resize", function(){
    $(".msgcontainer").css({height:$(window).height * 0.7 + "px"});
    })
})

function add_scroll(id){
    current_div = document.getElementById(id);
    $("#"+id).animate({
    scrollTop : current_div.scrollHeight - current_div.clientHeight,}, 400);
    }

socket.on('disconnect', async function() {
var user_name = await logged_user();
console.log("left the chat")
socket.emit('event', {message: user_name + ' has left the chat'});
});