const dashboard = document.getElementById("dashboard");
const schedule = document.getElementById("schedule");

let signinstate = true; //Backend SignIn state
let isinterviewer = true; //Backend Person Type fetch

if (!signinstate) {
  dashboard.classList.add("hidden");
  schedule.classList.add("hidden");
} else {
  if (isinterviewer) dashboard.classList.remove("hidden");
  else schedule.classList.remove("hidden");
}
