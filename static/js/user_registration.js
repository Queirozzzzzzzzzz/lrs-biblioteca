//Formulário
var current_date = new Date();
var end_period = document.getElementById('id_end_period');
var password = document.getElementById('id_password1');
var password2 = document.getElementById('id_password2');

//Formulário

function generatePassword() {
  // Define a function to generate a random password

  var lowercaseLetters = 'abcdefghijklmnopqrstuvwxyz';
  var uppercaseLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  var numbers = '0123456789';

  var allCharacters = lowercaseLetters + uppercaseLetters + numbers;

  var passwd = '';
  var length = 8; // Password length (can be adjusted)

  // Generate a random password that meets the requirements
  while (passwd.length < length) {
      var randomIndex = Math.floor(Math.random() * allCharacters.length);
      var randomChar = allCharacters.charAt(randomIndex);

      // Check if the password does not contain the same character consecutively
      if (passwd.charAt(passwd.length - 1) !== randomChar) {
          passwd += randomChar;
      }
  }

  // Set the generated password in both input fields
  password.value = passwd;
  password2.value = passwd;
}

generatePassword()