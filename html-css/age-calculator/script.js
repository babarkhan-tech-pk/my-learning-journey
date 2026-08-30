let inputEl = document.querySelector("#inPut");
let btn = document.querySelector(".ageCalculater");
let months = document.querySelector("#months");
let weeks = document.querySelector("#weeks");
let days = document.querySelector("#days");
let hours = document.querySelector("#hours");
let minutes = document.querySelector("#minutes");
let seconds = document.querySelector("#seconds");
const calculateAge = () =>{
    let input = Number(inputEl.value);;
    let inMonths = input * 12;
    let inWeeks = input * 52;
    let inDays = input * 365;
    let inHours = inDays * 24;
    let inMinutes = inHours * 60;
    let inSeconds = inMinutes * 60;
    // NOW PRINTING
    months.innerText = "Your Age In Months: " + inMonths;
    weeks.innerText = "Your Age In Weeks: " + inWeeks;
    days.innerText = "Your Age In Days: " + inDays;
    hours.innerText = "Your Age In Hours: " + inHours;
    minutes.innerText = "Your Age In Minutes: " + inMinutes;
    seconds.innerText = "Your Age In Seconds: " + inSeconds;   
}
btn.addEventListener("click", calculateAge);