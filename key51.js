const InputEvent = require('input-event');

const input = new InputEvent('/dev/input/event2');

const keyboard = new InputEvent.Keyboard(input);

keyboard.on('keyup'   , function(buffer){
             //console.log(buffer);
             _msgCreate(buffer.code, buffer.value);
});
keyboard.on('keydown' , function(buffer){
             //console.log(buffer);
             _msgCreate(buffer.code, buffer.value);
});
keyboard.on('keypress', function(buffer){
             //onsole.log(buffer);
             _msgCreate(buffer.code, buffer.value);
});

function _msgCreate(_code, _value) {
    var msg = {code: _code, value: _value};
    console.log(msg);
    //node.send(msg);
}
