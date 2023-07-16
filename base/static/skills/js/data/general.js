const description_text = document.getElementById("Description_text");
description_text.innerHTML += dict_content["Description"];

const article = document.getElementById("Article");
article.innerHTML += dict_content["Article"];

const title_projects = document.querySelectorAll('.Title_projeсts');
title_projects.forEach(element => element.innerHTML+= dict_content["Title_projeсts"]);

const description_skill = document.querySelectorAll('.Description_skill');
description_skill.forEach(element => element.innerHTML+= dict_content["Description_skill"]);

const empty_project = document.querySelectorAll('.Empty_project');
empty_project.forEach(element => element.innerHTML+= dict_content["Empty_project"]);

const info_page = document.getElementById("Info_page");
info_page.innerHTML += dict_content["Info_page"];