$(function () {
  $('#add_item').on('click', function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('#remove_item').on('click', function () {
    $('ul.my_list').children().last().remove();
  });

  $('#clear_list').onClick('click', function () {
    $('ul.my_list').children().remove();
  });
});
