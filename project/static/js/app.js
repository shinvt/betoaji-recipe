
var btnClassClick = function(e){
    //alert("Button clicked from class: "+e.currentTarget.id);
    //$(e.currentTarget).css("color", "red");

    var recipeID = e.currentTarget.id.split("_")[1];
    $.ajax({
        url: '/recipes/'+recipeID+'/like/',
        dataType: 'json',
        success: function (data) {
          var like_status = data;
    			if (like_status.Success == "True") {
      			$(e.currentTarget).css("color", "red");
            console.log(like_status.count)
      			$('#like-count' + '_' + recipeID).text(like_status.count);
    			} else if (like_status.Removed == "True") {
            $(e.currentTarget).css("color", "black");
            console.log(like_status.count)
      			$('#like-count' + '_' + recipeID).text(like_status.count);
          }
        },
        error: function(data) {
         	console.log("AJAX's like error")
        }/*  end of error */
    });
}

$('.fa-heart').on('click', btnClassClick);

// $('a[id^=itemLike]').on("click", function(e) { // catch the form's submit event
// 	e.preventDefault();
// 	var aId = $(this).attr('id');
// 	var itemID = aId.substring(8);
// 	$.ajax({
// 		url:'/product/'+itemID+'/',
// 		success: function(data) { // on success..
			// var rating_status = jQuery.parseJSON(data);
			// if (rating_status.Success == "True") {
			// $('a').find('#heart-icon' + itemID).removeClass('fa-heart-o text-not-liked').addClass('fa-heart text-liked');
			// $('#like-count' + itemID).html(rating_status.count);
			// } else if (rating_status.Removed == "True") {
			// $('a').find('#heart-icon' + itemID).removeClass('fa-heart text-liked').addClass('fa-heart-o text-not-liked');
			// $('#like-count' + itemID).html(rating_status.count);
// 			}
// 		},/* end of success */
// 		error: function(data) {
// 			setTimeout(function() {$('#errorModal').modal({backdrop:'static', keyboard:false,show:true});}, 1000);
// 		}/*  end of error */
// 	});/* end of ajax */
// });/* end of onclick*/
