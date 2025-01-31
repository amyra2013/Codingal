var string = prompt("Please enter any word or number.");

function palindrome(MyString) {
    // Remove non-alphanumeric characters and convert to lowercase
    var cleanedString = MyString.replace(/[^A-Z0-9]/ig, "").toLowerCase();
    
    // Reverse the cleaned string
    var reversedString = cleanedString.split("").reverse().join("");
    
    // Check if the reversed string is the same as the original cleaned string
    if (reversedString === cleanedString) {
        document.write(MyString + " is a palindrome.");
    } else {
        document.write(MyString + " is not a palindrome.");
    }
}

palindrome(string);
