const TokenMultisender = require('cro-token-multisender-cronos');

// Contoh penggunaan paket
const addresses = ['0xAddress1', '0xAddress2'];
const amounts = [10, 20];

TokenMultisender.sendTokens(addresses, amounts)
  .then(result => {
    console.log('Tokens sent successfully:', result);
  })
  .catch(error => {
    console.error('Error sending tokens:', error);
  });
