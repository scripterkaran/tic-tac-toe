<script>

</script>

<template>
  <div>
    <form class="form-2">
        <h1><span class="log-in">Log in</span> or <span class="sign-up">sign up</span></h1>
        <div class="float">
            <label for="email"><i class="icon-user"></i>Username</label>
            <input type="text" id="email" name="email" placeholder="Username or email">
        </div>
        <div class="float">
            <label for="password"><i class="icon-lock"></i>Password</label>
            <input type="password" id="password" name="password" placeholder="Password">
        </div>
        <div class="clearfix">
            <input type="submit" name="submit" value="Submit">
        </div>
    </form>
  </div>
</template>


<style>
  .form-2 {
    /* Size and position */
    width: 340px;
    margin: 60px auto 30px;
    padding: 15px;
    position: relative;

    /* Styles */
    background: #fffaf6;
    border-radius: 4px;
    color: #7e7975;
    box-shadow:
        0 2px 2px rgba(0,0,0,0.2),
        0 1px 5px rgba(0,0,0,0.2),
        0 0 0 12px rgba(255,255,255,0.4);
}
  .form-2 h1 {
    font-size: 15px;
    font-weight: bold;
    color: #bdb5aa;
    padding-bottom: 8px;
    border-bottom: 1px solid #EBE6E2;
    text-shadow: 0 2px 0 rgba(255,255,255,0.8);
    box-shadow: 0 1px 0 rgba(255,255,255,0.8);
}

.form-2 h1 .log-in,
.form-2 h1 .sign-up {
    display: inline-block;
    text-transform: uppercase;
}

.form-2 h1 .log-in {
    color: #6c6763;
    padding-right: 2px;
}

.form-2 h1 .sign-up {
    color: #ffb347;
    padding-left: 2px;
}
  .form-2 .float {
    width: 100%;
    padding: 10px 0;
    border-top: 1px solid rgba(255,255,255,1);
}

  .form-2 label {
    display: block;
    padding: 0 0 5px 2px;
    cursor: pointer;
    text-transform: uppercase;
    font-weight: 400;
    text-shadow: 0 1px 0 rgba(255,255,255,0.8);
    font-size: 11px;
}

.form-2 label i {
    margin-right: 5px; /* Gap between icon and text */
    display: inline-block;
    width: 10px;
}
  .form-2 input[type=text],
.form-2 input[type=password] {
    font-family: 'Lato', Calibri, Arial, sans-serif;
    font-size: 13px;
    font-weight: 400;
    display: block;
    width: 100%;
    height: 25px;
    margin-bottom: 5px;
    border: 1px solid #ebe6e2;
    border-radius: 5px;
    transition: all 0.3s ease-out;
}
  .form-2 input[type=text]:hover,
.form-2 input[type=password]:hover {
    border-color: #CCC;
}

.form-2 label:hover ~ input {
    border-color: #CCC;
}

.form-2 input[type=text]:focus,
.form-2 input[type=password]:focus {
    border-color: #BBB;
    outline: none; /* Remove Chrome's outline */
}
  .clearfix:after {
	content: "";
	display: table;
	clear: both;
}


.form-2 input[type=submit],
.form-2 .log-twitter {
    /* Size and position */
    width: 100%;
    height: 38px;
    position: relative;

    /* Styles */
    box-shadow: inset 0 1px rgba(255,255,255,0.3);
    border-radius: 3px;
    cursor: pointer;

    /* Font styles */
    font-family: 'Lato', Calibri, Arial, sans-serif;
    font-size: 14px;
    line-height: 38px; /* Same as height */
    text-align: center;
    font-weight: bold;
}

.form-2 input[type=submit] {
    margin-left: 1%;
    background: linear-gradient(#fbd568, #ffb347);
    border: 1px solid #f4ab4c;
    color: #996319;
    text-shadow: 0 1px rgba(255,255,255,0.3);
}

.form-2 .log-twitter {
    margin-right: 1%;
    background: linear-gradient(#34a5cf, #2a8ac4);
    border: 1px solid #2b8bc7;
    color: #ffffff;
    text-shadow: 0 -1px rgba(0,0,0,0.3);
    text-decoration: none;
}
  .no-boxshadow .form-2 input[type=submit]:hover {
    background: #ffb347;
}

.no-boxshadow .form-2 .log-twitter:hover {
    background: #2a8ac4;
}

</style>
