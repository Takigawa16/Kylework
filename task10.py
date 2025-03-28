<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Caesar Cipher Decryption</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .container {
            max-width: 400px;
            margin: 0 auto;
        }
        input, button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            box-sizing: border-box;
        }
        .result {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Caesar Cipher Decryption</h1>
        <label for="shift">Enter the shifting number:</label>
        <input type="number" id="shift" placeholder="Shift number">

        <label for="word">Enter the word to decrypt:</label>
        <input type="text" id="word" placeholder="Encrypted word">

        <button onclick="decrypt()">Decrypt</button>

        <div class="result" id="result"></div>
    </div>

    <script>
        function decrypt() {
            // Get input values
            const shift = parseInt(document.getElementById('shift').value);
            const word = document.getElementById('word').value;

            let decryptedWord = "";

            // Loop through each character in the word
            for (let i = 0; i < word.length; i++) {
                const c = word[i];
                if (/[a-zA-Z]/.test(c)) { // Check if the character is a letter
                    const offset = c === c.toUpperCase() ? 'A'.charCodeAt(0) : 'a'.charCodeAt(0);
                    // Shift the character backward by the shift value
                    const decryptedChar = String.fromCharCode(((c.charCodeAt(0) - offset - shift + 26) % 26) + offset);
                    decryptedWord += decryptedChar;
                } else {
                    // Keep non-alphabetic characters unchanged
                    decryptedWord += c;
                }
            }

            // Display the decrypted word
            document.getElementById('result').innerText = "Decrypted word: " + decryptedWord;
        }
    </script>
</body>
</html>

