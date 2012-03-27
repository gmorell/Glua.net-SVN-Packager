$(document).ready(function() {
	var modalcontent = "<div class=\"dlbuttons\"><button class=\"dlbuttonstd\">	Standard</button><button class=\"dlbuttonseed\">Seed</button></div>"
	$(".dlitemdl").hide();
	$(function(){
	$(".collapser").click(function(){
	    $(this).parent().next().slideToggle();
	    $(".ui-icon",this).toggleClass("ui-icon-triangle-1-n").toggleClass("ui-icon-triangle-1-s")
	    return false;
	    }).parent().next().hide();
	$(".collapset").click(function(){
	    $(this).parent().next().slideToggle();
	    $(this).prev().children(".ui-icon").toggleClass("ui-icon-triangle-1-n").toggleClass("ui-icon-triangle-1-s")
	    return false;
	    });
	$(".dlbutton").click(function(){
		$( "#modal" ).html(modalcontent);
		var fileid = $(this).attr('id'); 
		$(".dlbuttonstd").button()
		.click(
			function(){
				$.ajax({
					url: "/dls/std/" + fileid + "/",
					async: false,
					success: function(data){
						$("#modal").html(data);
						$("#ui-dialog-title-modal").html("Your download should begin shortly...");
 						var dlurl = $("#dllink").attr("href");
						//setTimeout("window.location='"+destination+"'",3000);
						setTimeout("window.location='"+dlurl+"'",3000);
						//alert("BAM, Downloading" + dlurl);
						}
				});
// 				$("#modal").load("/dls/std/" + fileid + "/", function(){
// 					delay(200);
// 					var dlurl = $("#download:first-child a").attr("href");
// 				});
				
			}
		)
		.next()
		.button()
		.click(
			function(){
				$.ajax({
					url: "/dls/seed/" + fileid + "/",
					async: false,
					success: function(data){
						$("#modal").html(data);
						$("#ui-dialog-title-modal").html("Your download should begin shortly...");
 						var dlurl = $("#dllink").attr("href");
						//setTimeout("window.location='"+destination+"'",3000);
						setTimeout("window.location='"+dlurl+"'",3000);
						//alert("BAM, Downloading" + dlurl);
						}
				});
			}
		).parent().buttonset();
	
		$( "#modal" ).dialog({
			modal: true,
			width: 500,
			resizeable: false,
			buttons: {
				Cancel: function() {
					$( this ).dialog( "close" );
					$("#ui-dialog-title-modal").html("Download Type?");
				}
			}
		});
		//alert("DOWNLOAD COMMENCING ( not really )");
	    });
	
	$('.icon').hover(
		function() { $(this).addClass('ui-state-hover'); },
		function() { $(this).removeClass('ui-state-hover'); }
	);

  });
	//$(".dlbuttonstd").button().next().button().parent().buttonset();
	//$(".dlbuttons").buttonset();
    

});
