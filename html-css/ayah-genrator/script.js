
const input = document.querySelector(".input");
const getBtn = document.querySelector(".get-btn");
const ayah = document.querySelector(".ayah");


const getAyah = async () => {
    let val = input.value;
    let url = `https://api.alquran.cloud/v1/ayah/${val}/en.asad`;
    let response = await fetch(url);
    let responseData = await response.json();
    let msg = responseData.data.text;
    ayah.style.display = "flex";
    ayah.innerText = msg;
};
getBtn.addEventListener("click",getAyah);