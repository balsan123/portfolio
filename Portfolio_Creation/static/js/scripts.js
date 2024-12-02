function showAlert(){

var username=document.getElementById('username').value;
var password=document.getElementById('password').value;
var password1=document.getElementById('password1').value;

if(!username|| !password || !password1){
alert("please fill out the required field")
}
else{
alert("Registration successful. Now you can login")

}


}