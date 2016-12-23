var icon = document.getElementById("icon");

var xmas = [];
for (var i = 23; i < 26; i++){
  xmas.push(new Date(16, 11, i));
}

var cDate = new Date();

var checkDate;
for (i = 0; i < xmas.length; i++){
  checkDate = xmas[i];

  // The current Date
  var cDay = cDate.getDate();
  var cMonth = cDate.getMonth();

  // The Date I'm checking
  var checkDay = checkDate.getDate();
  var checkMonth = checkDate.getMonth();

  if (cDay === checkDay && cMonth === checkMonth) {
    icon.href="res/img/faviconXmas.png"
  }
}
