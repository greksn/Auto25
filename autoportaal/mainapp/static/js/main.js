$(document).ready(function(){
    $(".mainsearch").focusin(function(){
        $(".tip").fadeIn(1500);
    });
    $(".mainsearch").focusout(function(){
        $(".tip").fadeOut(500);
    });
    $("#newThreadButton").click(function(){
        $(".new-thread").fadeIn(1000);
    });
});
if (typeof jQuery == 'undefined') {
    document.write(unescape("%3Cscript src='./js/jquery-3.3.1.js' type='text/javascript'%3E%3C/script%3E"));
}

function renderAds() {
    if (navigator.onLine) {
        console.log("im online");
        return;
    }
    db.transaction(function(tx) {
      tx.executeSql('CREATE TABLE IF NOT EXISTS Ads(brand TEXT, owner TEXT, model TEXT, gear_box TEXT, fuel TEXT, price INTEGER, year INTEGER, pic VARBINARY)', 
        []);
      tx.executeSql('SELECT * FROM Ads', [], function(tx, rs) {
        for(var i = 0; i < rs.rows.length; i++) {
          renderAd(rs.rows[i]);
        }
      });
    });
  }
  
  function insertAd(brand, owner, model, gear_box, fuel, price, year, pic) {
    db.transaction(function(tx) {
      tx.executeSql('INSERT INTO Ads VALUES(?, ?, ?, ?, ?, ?, ?, ?)', [ brand, owner, model, gear_box, fuel, price, year, pic ],
        function(tx, rs) {
        },
        function(tx, error) {
          reportError('sql', error.message);
        });
    });
  }

  function renderAd(row) {
    // add Ad to the database
  }
  function reportError(source, message) {
    console.log(message);
  }