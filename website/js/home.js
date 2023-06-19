var time = 595;
var starFlag = true;
var state = true;
var audio1 = new Audio("../audios/text.mp3");
var befor1 = new Audio("../audios/just start with.._happy_jennifer.wav")
var pro1 = new Audio("../audios/keep going, you got this_happy_Katelyn.wav")
var pro2 = new Audio("../audios/you got this_happy_emily.wav")
var pro3 = new Audio("../audios/push yourself_happy_Katelyn.wav")
$(document).ready(function () {
  $("#modalBox").modal("show");

  buttonEvt();
});

function startMent(){
  setTimeout(()=> {
    $(".modal-body").text("Just start with one exercise, and I promise you’ll feel more energized and motivated to continue.");
    $("#modalBox").modal("show");
    befor1.play()
    setTimeout(() => {
      $("#modalBox").modal("hide");
    },10000  );
  }, 20000);
}

function init() {
  document.querySelector(".stopWatch").innerHTML = "00:00:00";
}

function buttonEvt() {
  var hour = 0;
  var min = 0;
  var sec = 0;
  var timer;
  
  // 모달 안의 okay 버튼에 이벤트를 건다.
  $("#closeModalBtn").on("click", function () {
    $("#modalBox").modal("hide");

  });


  startMent()



  // start btn
  $("#goStopBtn").click(function () {
    if (state) {
      $("#goStopBtn").css("backgroundColor", "red");
      $("#goStopBtn").text("PAUSE");
      state = false;

      if (time == 0) {
        init();
      }

      timer = setInterval(function () {
        time++;

        min = Math.floor(time / 60);
        hour = Math.floor(min / 60);
        sec = time % 60;
        min = min % 60;

        if (time == 600) {
          $(".modal-body").text("Keep going, you got this!");
          $("#modalBox").modal("show");

          // 오디오 재생
          pro1.play();

          setTimeout(() => {
            $("#modalBox").modal("hide");
            // 오디오 중지
            time += 1180;
          }, 6000);


        } else if (time == 1800) {
          $(".modal-body").text("You got this! Don’t give up, keep pushing yourself to reach your goals and remember why you started in the first place!");
          pro2.play();
          $("#modalBox").modal("show");
          setTimeout(() => {
            $("#modalBox").modal("hide");
            time += 1780;
          }, 12000);

        } else if (time == 3600) {
          $(".modal-body").text("Push yourself a little harder, always remember why you started. You got this!");
          pro3.play();
          $("#modalBox").modal("show");
          setTimeout(() => {
            $("#modalBox").modal("hide");
          }, 6000);
        }

        var th = hour;
        var tm = min;
        var ts = sec;
        if (th < 10) {
          th = "0" + hour;
        }
        if (tm < 10) {
          tm = "0" + min;
        }
        if (ts < 10) {
          ts = "0" + sec;
        }

        document.querySelector(".stopWatch").innerHTML =
          th + ":" + tm + ":" + ts;
      }, 1000);
    } else {
      $("#goStopBtn").css("backgroundColor", "blue");
      $("#goStopBtn").text("START");
      clearInterval(timer);
      state = true;
    }
  });

  // stop btn
  $("#stopBtn").click(function () {
    if (time != 0) {
      $(".fa").css("color", "#FAED7D");
      this.style.color = "#4C4C4C";
      clearInterval(timer);
      starFlag = true;
      time = 0;
      init();
    }
  });

  $(".saveBtn").click(function () {
    window.location.href = "https://d487f2f15ffa323319.gradio.live";
  });

  $("#mypageBtn").click(function () {
    window.location.href = "mypage.html";
  });

}
