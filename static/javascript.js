function myalert() {
    alert("This feature is coming soon!");
}

function display_rolls() {
    if (document.getElementById("rolls").style.display == "none") { 
        document.getElementById("rolls").style.display = "block";
        document.getElementById("display").innerHTML = "Hide Rolls";
    }
    else {
        document.getElementById("rolls").style.display = "none";
        document.getElementById("display").innerHTML = "Display Rolls";
    } 
}