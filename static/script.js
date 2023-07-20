$(document).ready(function() {
  $('.like-button').click(function() {
    var appName = $(this).data('app-name');
    var modelName = $(this).data('model-name');
    var postId = $(this).data('post-id');
    var likeCount = $(this).siblings('.like-count');

    $.ajax({
      type: 'POST',
      url: '/like/' + appName + '/' + modelName + '/' + postId + '/',
      data: {},
      success: function(response) {
        if (response.liked) {
          likeCount.text(response.like_count);
        } else {
          likeCount.text(response.like_count);
        }
      },
      error: function(xhr, status, error) {
        // Handle error
      }
    });
  });
});
