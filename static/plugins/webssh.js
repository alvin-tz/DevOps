function post_data(id, user) {
    var server_id = id;
    var user = user;
    if (server_id !== null && user !== null) {
        webssh(server_id, user)
    }
}



function get_term_size() {
    var init_width = 9;
    var init_height = 17;

    var windows_width = $("#detail").width() - 10;
    var windows_height = $("#serverinfo").height() - 50;

    return {
        cols: Math.floor(windows_width / init_width),
        rows: Math.floor(windows_height / init_height),
    }
}


function webssh(server_id, user) {
    var cols = get_term_size().cols;
    var rows = get_term_size().rows;

    var term = new Terminal(
        {
            cols: cols,
            rows: rows,
            useStyle: true,
            cursorBlink: true
        }
        ),
        protocol = (location.protocol === 'https:') ? 'wss://' : 'ws://',
        socketURL = protocol + location.hostname + ((location.port) ? (':' + location.port) : '') +
            '/webssh/?' + 'server_id=' + server_id + '&user=' + user + '&width=' + cols + '&height=' + rows;

    var sock = new WebSocket(socketURL);

    sock.addEventListener('open', function () {
        $('#detail').addClass('hide');
        $('#django-webssh-terminal').removeClass('hide');
        term.open(document.getElementById('terminal'));
    });

    sock.addEventListener('message', function (recv) {
        var data = JSON.parse(recv.data);
        var message = data.message;
        var status = data.status;
        if (status === 0) {
            term.write(message)
        } else {
            window.location.reload()
            // $('#django-webssh-terminal').addClass('hide');
            // $('#form').removeClass('hide');
        }
    });

    var message = {'status': 0, 'data': null, 'cols': null, 'rows': null};
    /*
    * status 为 0 时, 将用户输入的数据通过 websocket 传递给后台, data 为传递的数据, 忽略 cols 和 rows 参数
    * status 为 1 时, resize pty ssh 终端大小, cols 为每行显示的最大字数, rows 为每列显示的最大字数, 忽略 data 参数
    * */

    term.on('data', function (data) {
        message['status'] = 0;
        message['data'] = data;
        var send_data = JSON.stringify(message);
        sock.send(send_data)
    });

    $(window).resize(function () {
        var cols = get_term_size().cols;
        var rows = get_term_size().rows;
        message['status'] = 1;
        message['cols'] = cols;
        message['rows'] = rows;
        var send_data = JSON.stringify(message);
        sock.send(send_data);
        term.resize(cols, rows)
    })
}
