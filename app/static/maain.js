$(document).ready(function() {
    $("#btn-one").click(function() {
        $("#one").hide();
        $("#two").hide();
        $("#three").hide();
        $("#four").hide();
        $("#five").hide();
        $("#six").hide();
        $("#all").show();
    });    
    $("#btn-two").click(function() {
        $("#one").show();
        $("#two").hide();
        $("#three").hide();
        $("#four").hide();
        $("#five").hide();
        $("#six").hide();
        $("#all").hide();
    });
    $("#btn-three").click(function() {
        $("#one").hide();
        $("#two").show();
        $("#three").hide();
        $("#four").hide();
        $("#five").hide();
        $("#six").hide();
        $("#all").hide();
    });
    $("#btn-four").click(function() {
        $("#one").hide();
        $("#two").hide();
        $("#three").show();
        $("#four").hide();
        $("#five").hide();
        $("#six").hide();
        $("#all").hide();
    });
    $("#btn-five").click(function() {
        $("#one").hide();
        $("#two").hide();
        $("#three").hide();
        $("#four").show();
        $("#five").hide();
        $("#six").hide();
        $("#all").hide();
    });
    $("#btn-six").click(function() {
        $("#one").hide();
        $("#two").hide();
        $("#three").hide();
        $("#four").hide();
        $("#five").show();
        $("#six").hide();
        $("#all").hide();
    });
    $("#btn-seven").click(function() {
        $("#one").hide();
        $("#two").hide();
        $("#three").hide();
        $("#four").hide();
        $("#five").hide();
        $("#six").show();
        $("#all").hide();
    });
});