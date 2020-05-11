const net = require('net');

const client = net.connect({ host: '192.168.0.55', port: 8080 }, () => {
   console.log('connected to server!');  
});

// client establishes a conection
client.on('connect', () => {
   const dummyData = {
      type: 'tempLog',
      temp: 40000,
      hum: 40000
   }

   client.write(JSON.stringify(dummyData))
})

// data is received
client.on('data', (data) => {
   console.log(data.toString());
   client.end();
});

client.on('end', () => { 
   console.log('disconnected from server');
});