var WebSocketServer = require('ws').Server,
    wss = new WebSocketServer({ port: 8080 });
let firstClient = null;

const seed = "123654879"
const Random = require('./randomGenerator/CustomRandom');

let rand = new Random(seed);

wss.on('connection', function (ws) {

    if (firstClient == null) {
        firstClient = ws;
    } 
    console.log('client connected');

    ws.on('message', function (message) {
        console.log("data received");



        let applyNoise = rand.getRandomOption(["y","n"]);
        if(applyNoise == "y"){
            message = JSON.parse(message);
            mainMessage = message.hammingCode;
            let index = Math.floor(rand.getRandom() * mainMessage.length);
            let noise = mainMessage[index] == '0' ? '1' : '0';
            mainMessage = mainMessage.substring(0, index) + noise + mainMessage.substring(index + 1);
            message.hammingCode = mainMessage;
            message = JSON.stringify(message);
            console.log("Noise applied in bit " + index + " with value " + noise+"\n")
        }

       
        message = message.toString();
        // message = message.substring(0, index) + noise + message.substring(index + 1);

        firstClient.send(message);
    });
});

console.log('Server running on port 8080');
