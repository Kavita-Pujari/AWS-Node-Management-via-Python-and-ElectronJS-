//---- Login Functions ----//
async function Login() {
    let log_email = document.getElementById("log_email").value; // Pull out command
    let log_password = document.getElementById("log_password").value;
    eel.ask_login(log_email, log_password)();
    //let output = await eel.ask_login(log_email, log_password)();
}


//---- Update Credentials Functions ----//
async function Update() {
    let log_email = document.getElementById("log_email").value; // Pull out command
    let log_password = document.getElementById("log_password").value;
    eel.ask_update(log_email, log_password)();
}


//---- Remove Credentials Functions ----//
async function Remove() {
    eel.ask_Remove()();
}



eel.expose(relocation);
function relocation(output) {
    window.location = output;
}

eel.expose(error_alert);
function error_alert(output) {
    alert(output);
}

eel.expose(delete_alert);
function delete_alert(output) {
    location.reload();
    alert(output);
}


async function Get_start(){
  eel.start_all()();

}

async function Get_stop(){
  eel.stop_all()();
  
}

async function Get_specific(){
  
}


async function Get_url() {
    let jd_url = document.getElementById("jd_url").value; // Pull out command
    let jd_city = document.getElementById("jd_city").value;
    
    if(jd_city && jd_url) { eel.update_status(jd_url, jd_city)(); }
    else { alert('Please Enter URL And City Name'); }
    
    //let output = await eel.ask_login(log_email, log_password)();
}

async function Sign_Jd() {
    let jd_name = document.getElementById("jd_name").value; // Pull out command
    let jd_number = document.getElementById("jd_number").value;

    if(jd_name && jd_number) { eel.Sign_Jd(jd_name, jd_number)(); }
    else { alert('Please Enter Name And Number'); }

    //let output = await eel.ask_login(log_email, log_password)();
}

eel.expose(AddRow);
function AddRow(Name,Phone,Rating,Rating_Count,Address) {

  var table = $('#datatable1').DataTable();

  table.row.add($(
      '<tr>' +
      '<td>'+Name+'</td>' +
      '<td>'+Address+'</td>' +
      '<td>'+Phone+'</td>' +
      '<td>'+Rating+'</td>' +
      '<td>'+Rating_Count+'</td>' +
      '</tr>' 
  )).draw(false);
  
}


async function GetCred() {
    let output = await eel.get_username()();
    console.log(output);
    document.getElementById("log_email").value = output[0]; // Pull out command
    document.getElementById("log_password").value = output[1];
}

async function GetHistory() {
    let output = await eel.insert_history()();
    console.log(output);
}

