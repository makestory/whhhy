function showbar(bar){$(bar).animate({ width: 'show' },'fast')};
function hidebar(bar){$(bar).animate({ width: 'hide' },'fast')};
function hidemidbar(){hidebar('#midbar')};

$(document).ready(function(){
    $("#daily ").click(
    function () {
    if($('#daily').attr("class")=="hover select" || $('#daily').attr("class")=="select hover" ){window.location="/daily/"};
    showbar('#midbar');
    $('#daily').addClass('select');
    $('#years .select').removeClass('select');
    $('.months').css('display','none');
    $('#yearbar a:last').addClass('select');
    $('#monthbar ul:last').css('display','block');});
    
    $("#daily").hover(
    function () {$(this).addClass("hover");},
    function () {$(this).removeClass("hover");});
    
    $(".month").hover(
    function () {$(this).addClass("hover");},
    function () {$(this).removeClass("hover");});
    
    $(".year").click(
    function(){$('#years .select').removeClass('select');
    $(this).addClass('select');
    $('.months').css('display','none');
    $('#' + $(this).attr("name")).animate({ height: 'show' },'fast');
    $('#monthbar .select').removeClass('select');
    hidebar('#rightbar');});
   
    $("#midback").click(
    function () {$('#daily').removeClass('select');
    hidebar('#rightbar');
    setTimeout(hidemidbar,100);
    $('#midbar .select').removeClass('select');
    $('#daily').removeAttr('onclick');});

    $(".month").click(function(){
    if($(this).attr("class")=="month hover select" || $(this).attr("class")=="month select hover" )
    {window.location="/daily/"+$(this).attr('name').slice(1,8)};

    showbar('#rightbar');
    $('#monthbar .select').removeClass('select');
    $(this).addClass('select');
    $('.day').css('display','none');
    $('#' + $(this).attr("name")).fadeIn(); });
    
    $("#showsign").click(function(){
    $('#showsign').css('display','none');
    $('#sign').fadeIn();});
    
     });
