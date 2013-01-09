$(function() { $('table').tablesorter(); });

window_path = $.trim(window.location.pathname);

function create(post_url) {
  folder_name = $.trim($('#folder_name').val());

  if (window_path && folder_name) {
    $.ajax({
      type: 'POST',
      url: post_url,
      data: {'folder_name': (window_path + folder_name).replace(/^\/|\/$/g, '')},
      success: location.reload(window_path),
    });

    return false;
  }
};

/*
function rename(post_url, current, rename) {
  current = $.trim(current);
  rename = $.trim(rename);

  if (window_path && current && rename) {
    $.ajax({
      type: 'POST',
      url: post_url,
      data: {'current': (window_path + current).replace(/^\/|\/$/g, ''),
	     'rename': (window_path + rename).replace(/^\/|\/$/g, ''/^\/|\/$/g, '')},
      success: location.reload(window_path),
    });

    return false;
  }
};
*/

function remove(post_url, item) {
  item = $.trim(item)

  if (window_path && item) {
    $.ajax({
      type: 'POST',
      url: post_url,
      data: {'item_path': (window_path + item).replace(/^\/|\/$/g, '')},
      success: location.reload(window_path),
    });

    return false;
  }
};
