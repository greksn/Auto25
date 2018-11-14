function loadDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            myFunction(this);
        }
    };
    xhttp.open("GET", "/static/XML/test.xml", true);
    xhttp.send();
}
function myFunction(xml) {
    var i;
    var xmlDoc = xml.responseXML;
    var table="<tr><th>Mark&nbsp&nbsp</th><th>Mudel</th></tr>";
    var x = xmlDoc.getElementsByTagName("AUTO");
    for (i = 0; i <x.length; i++) { 
        table += "<tr><td>" +
        x[i].getElementsByTagName("MARK")[0].childNodes[0].nodeValue +
        "</td><td>" +
        x[i].getElementsByTagName("MUDEL")[0].childNodes[0].nodeValue +
        "</td></tr>";
    }
    document.getElementById("autod").innerHTML = table;
}