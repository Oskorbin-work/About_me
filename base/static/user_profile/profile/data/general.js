const Button_Save = document.getElementById("Button_Save");
Button_Save.innerHTML = dict_base_content["Button_Save"];

const Groups_Description_True = document.querySelectorAll('.Groups_Description_True');
Groups_Description_True.forEach(element => element.innerHTML= dict_base_content["Groups_Description_True"]+element.innerHTML);

const Groups_Description_False = document.querySelectorAll('.Groups_Description_False');
Groups_Description_False.forEach(element => element.innerHTML= dict_base_content["Groups_Description_False"]+element.innerHTML);