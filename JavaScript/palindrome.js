var string=prompt("Please enter any word or number.")

function palindrome(MyString) {
   
    string.replace(/[^A-Z0-9]/ig,"" ).toLowerCase();
    var revs=string.split("").reverse("").join("");

    if (revs===string) {
        document.write(string," is a palindrome.");
    }

    else {
        document.write(string," is not a palindrome.");
    }
}

palindrome(MyString)