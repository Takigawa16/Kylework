using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Pogi
    {
       
           
        static void Main(string[] args)
        {
            // Prompt the user for the shifting number
            Console.Write("Enter the shifting number: ");
            int shift = int.Parse(Console.ReadLine());

            // Prompt the user for the word to decrypt
            Console.Write("Enter the word to decrypt: ");
            string word = Console.ReadLine();

            string decryptedWord = ""; // Variable to store the decrypted word

            // Loop through each character in the word
            foreach (char c in word)
            {
                if (char.IsLetter(c)) // Check if the character is a letter
                {
                    char offset = char.IsUpper(c) ? 'A' : 'a'; // Determine the offset for uppercase or lowercase
                                                               // Shift the character backward by the shift value
                    char decryptedChar = (char)(((c - offset - shift + 26) % 26) + offset);
                    decryptedWord += decryptedChar;
                }
                else
                {
                    // Keep non-alphabetic characters unchanged
                    decryptedWord += c;
                }
            }

            // Output the decrypted word
            Console.WriteLine("Decrypted word: " + decryptedWord);
        }
    }

}
        
    


