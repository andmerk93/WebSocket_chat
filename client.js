var ws = new WebSocket("ws://" + window.location.host + "/ws");
ws.onmessage = function(event) {
    var messages = document.getElementById('messages')
    var message = document.createElement('li')
    var content = document.createTextNode(event.data)
    message.appendChild(content)
    messages.appendChild(message)
};
function sendMessage(event) {
    var input = document.getElementById("messageText")
    var nickname = document.getElementById("nickname")
    ws.send(JSON.stringify({[nickname.value]: input.value}))
    input.value = ''
    event.preventDefault()
}
