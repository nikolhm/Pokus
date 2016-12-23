function pong() {
  var poeng = 0;
  var theGameIsOn = true;

  var canvas = document.getElementById("pongCanvas");
  var ctx = canvas.getContext("2d");

  var bane = {
    bredde: canvas.width,
    hoyde: canvas.height,
    gressFarge: "#5d1f1f",
    linjeFarge: "#101010",
    linjeTykkelse: 4
  };

  var ball = {
    radius: 7,
    farge: "#bbc712",
    xpos: bane.bredde - 100,
    ypos: 100,
    xRetning: 1,
    yRetning: 1,
    xFart: 4,
    yFart: 4
  };

  var motstander = {
    farge: "#101010",
    bredde: 10,
    hoyde: 50,
    xpos: bane.bredde - 25,
    ypos: ball.ypos
  };

  var racket = {
    farge: "#101010",
    bredde: 10,
    hoyde: 50,
    xpos: 15,
    ypos: bane.hoyde / 2,
    yRetning: 0,
    yFart: 5
  };

  function tegnBane() {
    //console.log("Tegner bane");

    ctx.fillStyle = bane.gressFarge;
    ctx.fillRect(0, 0, bane.bredde, bane.hoyde);
    ctx.fillStyle = bane.linjeFarge;
    ctx.fillRect(bane.bredde / 2 - bane.linjeTykkelse / 2, 0, bane.linjeTykkelse, bane.hoyde);
  }

  function tegnBall() {
    //console.log("Tegner balll");

    ctx.beginPath();
    ctx.arc(ball.xpos, ball.ypos, ball.radius, 0, Math.PI * 2);
    ctx.closePath();
    ctx.fillStyle = ball.farge;
    ctx.fill();
    ball.xpos += ball.xFart * ball.xRetning;
    ball.ypos += ball.yFart * ball.yRetning;
  }

  function tegnMotstander() {
    //console.log("Tegner motstander");

    motstander.ypos = ball.ypos - motstander.hoyde / 2;

    ctx.fillStyle = motstander.farge;
    ctx.fillRect(motstander.xpos, motstander.ypos, motstander.bredde, motstander.hoyde);
  }

  function tegnRacket() {
    //console.log("Tegner racket");

    ctx.fillStyle = racket.farge;
    ctx.fillRect(racket.xpos, racket.ypos - racket.hoyde / 2, racket.bredde, racket.hoyde);

    if (racket.yRetning === -1 && racket.ypos - racket.hoyde / 2 <= 0) {
      return;
    }

    if (racket.yRetning === 1 && racket.ypos + racket.hoyde / 2 >= bane.hoyde) {
      return;
    }

    racket.ypos += racket.yFart * racket.yRetning;
  }

  function sjekkOmBallTrefferVegg() {
    //console.log("Sjekker om ballen treffer en vegg");

    // Nedre vegg
    if (ball.ypos + ball.radius >= bane.hoyde) {
      ball.yRetning = -1;
    }

    // Øvre vegg
    if (ball.ypos - ball.radius <= 0) {
      ball.yRetning = 1;
    }
  }

  function sjekkOmBallTrefferMotstander() {
    //console.log("Sjekker om ballen treffer motstanderen");

    if (ball.xpos + ball.radius >= motstander.xpos - motstander.bredde) {
      ball.xRetning = -1;
    }
  }

  function sjekkOmBallTrefferRacket() {
    //console.log("Sjekker om ballen treffer racketen");

    var ballenErTilHoyre = ball.xpos + ball.radius < racket.xpos;
    var ballenErTilVenstre = ball.xpos - ball.radius > racket.xpos + racket.bredde;
    var ballenErOver = ball.ypos + ball.radius < racket.ypos - racket.hoyde / 2;
    var ballenErUnder = ball.ypos - ball.radius > racket.ypos + racket.hoyde / 2;

    if (!ballenErTilHoyre && !ballenErTilVenstre && !ballenErOver && !ballenErUnder) {
      ball.xRetning = 1;
      poeng++;
    }
  }

  function sjekkOmBallErUtenforBanen() {
    //console.log("Sjekker om ballen er utenfor banen");

    if (ball.xpos + ball.radius < 0) {
      theGameIsOn = false;
    }
  }

  document.onkeydown = function(evt) {
    var tast = evt.keyCode;
    if (tast === 87) {
      racket.yRetning = -1;
    }

    if (tast === 83) {
      racket.yRetning = 1;
    }

    if (tast === 13) {
      GameLoop();
    }
  };

  document.onkeyup = function(evt) {
    var tast = evt.keyCode;
    if (tast === 87 && racket.yRetning === -1) {
      racket.yRetning = 0;
    }

    if (tast === 83 && racket.yRetning === 1) {
      racket.yRetning = 0;
    }
  };

  function GameLoop() {
    tegnBane();
    tegnBall();
    tegnRacket();
    tegnMotstander();
    sjekkOmBallTrefferVegg();
    sjekkOmBallTrefferMotstander();
    sjekkOmBallTrefferRacket();
    sjekkOmBallErUtenforBanen();

    if (theGameIsOn) {
      requestAnimationFrame(GameLoop);
    } else {
      document.getElementById("pongPoints").innerHTML = "Du fikk: " + poeng.toString() + " poeng.";
    }
  }
}
