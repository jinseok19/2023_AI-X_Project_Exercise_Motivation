$("#signupBtn").click(function (e) {
  e.preventDefault();
  const id = $("#inputId").val();
  const pwd = $("#inputPwd").val();

  if (id.trim() == "" || pwd.trim() == "") {
    alert("입력되지 않은 항목이 있습니다");
    return false;
  }

  //서버에서 로그인 정보 확인하고 되면은 넘어감
  // 토큰이나 넘겨라
});
