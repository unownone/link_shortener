function myFunction() {
    // Get the text field
    var copyText = document.getElementById("link").text;

    // Copy the text inside the text field
    navigator.clipboard.writeText(copyText);
  
    // Alert the copied text
    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copied";
    //alert("Copied the text: " + copyText);
  }

  function outFunc() {
    var tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copy to clipboard";
  }