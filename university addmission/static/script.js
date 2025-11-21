$(document).ready(function(){
    $("#send").click(function(){
        var message = $("#user_input").val();
        if(message.trim() !== ""){
            $("#messages").append("<b>You:</b> " + message + "<br>");
            $.post("/get_response", {message: message}, function(data){
                $("#messages").append("<b>Bot:</b> " + data.response + "<br>");
                $("#messages").scrollTop($("#messages")[0].scrollHeight);
            });
            $("#user_input").val("");
        }
    });
    $("#user_input").keypress(function(e){
        if(e.which == 13){ $("#send").click(); }
    });
});
