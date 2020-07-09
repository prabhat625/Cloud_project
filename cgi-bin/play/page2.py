#!/usr/bin/python36 
import subprocess as sp
import cgi
print("content-type: text/html\n")
form=cgi.FieldStorage()
port=str(form.getvalue("port"))
portc=str(form.getvalue("portc"))
sp.getoutput("sudo systemctl daemon-reload")

sp.getoutput("sudo systemctl restart vncserver@:"+str(port)+".service")


sp.getoutput("sudo ansible-playbook cron.yml")
string=("http://192.168.43.228:{}".format(portc))

print('''    
<html>
<title>IAAS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body bgcolor="black">

<div class="w3-container">
  <h2 style="color:white">Here We Go:-</h2>

  <div class="w3-light-grey">
    <div id="myBar" class="w3-container w3-green" style="height:24px;width:0%">
    </div>
  </div>
<br>
  <p id="myP"><span id="demo"></span></p>

  <p><button class="w3-button w3-light-grey" onclick="move();this.disabled='true'">Start Service</button></p>
  
  <form action={}>
  <p><button id="my" class="w3-button w3-light-grey" disabled="true" type="submit">Use Now!!!!</button></p>
  </form>
</div>
'''.format(string))
print('''
<script>
function move() {
  var elem = document.getElementById("myBar");   
  var width = 0;
  var id = setInterval(frame, 1000);
  function frame() {
    if (width >= 100) {
      clearInterval(id);
      document.getElementById("myP").className = "w3-text-green w3-animate-opacity";
      document.getElementById("my").disabled=false;
    } else {
      width++; 
      elem.style.width = width + '%'; 
      var num = width * 1 / 100;
      num = num.toFixed(0)
      
    }
  }
}
</script>

</body>
</html>		''')
