<script language="JavaScript" type="text/javascript">
            function nextPage() {
                id = document.login_form.id.value //ID枠に入力された値（文字列）を定義
                pwd = document.login_form.pass.value; //Password枠に入力された値（文字列）を定義
                location.href = id + pwd + ".html"; //リンク先URLを作成
            }
 </script>