const Login_Welcome = document.getElementById("Login_Welcome");
if (Login_Welcome) {
    Login_Welcome.innerHTML = dict_base_content["Login_Welcome"] + Login_Welcome.innerHTML;
}

const Link_Login_Base = document.getElementById("Link_Login_Base");
if (Link_Login_Base) {
    Link_Login_Base.innerHTML = dict_base_content["Link_Login_Base"];
}
const Link_Logout_Base = document.getElementById("Link_Logout_Base");
if (Link_Logout_Base){
    Link_Logout_Base.innerHTML = dict_base_content["Link_Logout_Base"];
}
