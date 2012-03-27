$(document).ready(function() {
    $(function(){
	$(".collapser").click(function(){
	    $(this).parent().next().slideToggle();
	    $(".ui-icon",this).toggleClass("ui-icon-triangle-1-n").toggleClass("ui-icon-triangle-1-s")
	    return false;
	    }).parent().next().hide();
	$(".dlbutton").click(function(){
	    var foo = $(this).attr('id');
	    $("#extload").load("/dls/13/");
	    $("#dialog").dialog("open");
	    //alert("DOWNLOAD COMMENCING ( not really )");
	    });
	$('.icon').hover(
		function() { $(this).addClass('ui-state-hover'); },
		function() { $(this).removeClass('ui-state-hover'); }
	);

  });

});