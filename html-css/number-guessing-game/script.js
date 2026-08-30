// ACCESSING INPUT VALUE OF USER
let inputLvl1 = document.querySelector("#user-input-l1");
let inputLvl2 = document.querySelector("#user-input-l2");
let inputLvl3 = document.querySelector("#user-input-l3");
// ACCESSING ALL CHECK BUTTONS
let btnLvl1 = document.querySelector("#check-btn-l1");
let btnLvl2 = document.querySelector("#check-btn-l2");
let btnLvl3 = document.querySelector("#check-btn-l3");
// ACCESSING ALL MESSAGES
let msglLvl1 = document.querySelector("#result-l1");
let msglLvl2 = document.querySelector("#result-l2");
let msglLvl3 = document.querySelector("#result-l3");
// ACCESSING ALL RESET BUTTONS
let resetLvl1 = document.querySelector("#reset-btn-l1");
let resetLvl2 = document.querySelector("#reset-btn-l2");
let resetLvl3 = document.querySelector("#reset-btn-l3");
// GENRATING RANDOM NUM FOR ALL LEVELS
let randomNumLvl1 = Math.floor(Math.random() * 10) + 1;
let randomNumLvl2 = Math.floor(Math.random() * 50) + 1;
let randomNumLvl3 = Math.floor(Math.random() * 100) + 1;
// PLAYING GAME LOGIC IN GAME FUNCTION
let game = (compNum,userNum,btn,msg) => {
    if(userNum === compNum){
        msg.innerText = "You Win. 🏆";
        msg.style.backgroundColor = "#A9B5DF";
        btn.disabled = true;
    } else {
        if(userNum > compNum){
            msg.innerText = "Thats Big.";
            msg.style.backgroundColor = "#A9B5DF";
        } else{
            msg.innerText = "Thats Small.";
            msg.style.backgroundColor = "#A9B5DF";
        }
}
};
// SETTING RESET FUNCTION WORKING
const reset = (btn,input,msg) => {
    input.value = "";
    btn.disabled = false;
    msg.innerText = "New Game!";
    msg.style.backgroundColor = "";
};
// ADDING EVENT LISTENER ON CHECK BUTTON OF LEVEL 1
btnLvl1.addEventListener("click", () => {
    game( randomNumLvl1 , Number(inputLvl1.value) , btnLvl1 , msglLvl1 );
});
// ADDING EVENT LISTENER ON CHECK BUTTON OF LEVEL 2
btnLvl2.addEventListener("click", () => {
    game( randomNumLvl2 , Number(inputLvl2.value) , btnLvl2 , msglLvl2 );
});
// ADDING EVENT LISTENER ON CHECK BUTTON OF LEVEL 3
btnLvl3.addEventListener("click", () => {
    game( randomNumLvl3 , Number(inputLvl3.value) , btnLvl3 , msglLvl3 );
});
// ADDING EVENT LISTENER ON RESET BUTTON OF LEVEL 1
resetLvl1.addEventListener("click", () => {
    randomNumLvl1 = Math.floor(Math.random() * 10) + 1;
    reset(btnLvl1,inputLvl1,msglLvl1);
});
// ADDING EVENT LISTENER ON RESET BUTTON OF LEVEL 2
resetLvl2.addEventListener("click", () => {
    randomNumLvl2 = Math.floor(Math.random() *50) + 1;
    reset(btnLvl2,inputLvl2,msglLvl2);
});
// ADDING EVENT LISTENER ON RSEET BUTTON OF LEVEL 3
resetLvl3.addEventListener("click", () => {
    randomNumLvl3 = Math.floor(Math.random() * 100 )+ 1;
    reset(btnLvl3,inputLvl3,msglLvl3);
});