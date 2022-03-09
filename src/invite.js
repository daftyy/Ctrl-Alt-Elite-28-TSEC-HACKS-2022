var acceptInvite = document.getElementById("accept");
var declineInvite = document.getElementById("decline");

declineInvite.onclick = decInc;
acceptInvite.onclick = AccInc;

function decInc() {
	var parent = acceptInvite.parentElement;
	console.log(parent.getAttributeNames);
}

function AccInc() {
	console.log("Accepted Invite");
}

// document.onclick = check;
// function check(e) {
// 	var target = (e && e.target) || (event && event.srcElement);

// 	//Nav Menu
// 	if (!checkParent(target, navMenuDiv)) {
// 		// click NOT on the menu
// 		if (checkParent(target, navMenu)) {
// 			// click on the link
// 			if (navMenuDiv.classList.contains("hidden")) {
// 				navMenuDiv.classList.remove("hidden");
// 			} else {
// 				navMenuDiv.classList.add("hidden");
// 			}
// 		} else {
// 			// click both outside link and outside menu, hide menu
// 			navMenuDiv.classList.add("hidden");
// 		}
// 	}
// }
