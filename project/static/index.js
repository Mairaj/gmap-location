$(document).ready(function(){
	$(".gmap").live("click"function(){
		
		$.ajax({
                        url:'/data/',
                        type:'POST',
                        data:{
                                'objects':objects,
                                             },
                        success:function(data){
                                                $("img").html(data);

                                                                }
	});
    $("#abc").live("click"function(){
        alert("hii");
        $.ajax({
                        url:'/detail/',
                        type:'POST',
                        data:{
                                'objects':objects,
                                             },
                        success:function(data){
                                                $(".full").html(data);

                                            }
    });

});
