let input = document.querySelector("#takeTask");
input.addEventListener("input", () => {
    inputVal = input.value; // Logs real-time input
});
let addBtn = document.querySelector(".addTask");
let taskList = document.querySelector(".showTask");
let markBtn = document.querySelector("#box");
let taskNum = document.querySelector("#number");
let indx = 1;
let taskText = document.querySelector("#task");
let editBtn = document.querySelector("#editButton");
let ol = document.querySelector("#orList");
addBtn.addEventListener("click" , () => {
    let li = document.createElement("li");
    ol.appendChild(li);
    taskText.innerText = inputVal;
    taskNum.innerText = "#" + indx++;
});
markBtn.addEventListener("click",() => {
    markBtn.innerText = "✔️";
});
markBtn.addEventListener("click",() => {
    markBtn.innerText = "";
});
editBtn.addEventListener("click" , () => {
    inputVal = taskText.innerText;
});