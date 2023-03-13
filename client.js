var ws = new WebSocket("ws://" + window.location.host + "/ws");
ws.onmessage = function(event) {
    if (document.querySelector('.empty-message')) {
        document.querySelector('.empty-message').remove()
    }
    var messages = document.getElementById('messages')
    var message = document.createElement('li')
    const count = JSON.parse(event.data).count
    const time = JSON.parse(event.data).time
    const nickname = JSON.parse(event.data).nickname
    const text = JSON.parse(event.data).text
    const full_text = count + " [" + time + "] " + nickname + ": " + text
    var content = document.createTextNode(full_text)
    message.appendChild(content)
    messages.appendChild(message)
};
function sendMessage(event) {
    var input = document.getElementById("messageText")
    var nickname = document.getElementById("nickname")
    ws.send(JSON.stringify({nick: nickname.value, text: input.value}))
    input.value = ''
    event.preventDefault()
}
