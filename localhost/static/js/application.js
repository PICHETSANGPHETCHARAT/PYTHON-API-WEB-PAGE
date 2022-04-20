

$(document).ready(function(){
    //connect to the socket server.
    var socket_url = 'http://' + document.domain + ':' + location.port + '/test' ;

    var socket = io.connect(socket_url);

    console.log("socket_url = ", socket_url);

    //receive details from server
    socket.on('new_message', function(msg) {

        console.log("Received Message" + msg);

        $('#log').html(msg);
    });

});
