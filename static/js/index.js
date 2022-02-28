
const showMenu = (toggleId, navId) => {
	const toggle = document.getElementById(toggleId),
	nav = document.getElementById(navId)

	if (toggle && nav) {
		toggle.addEventListener('click', () => {
			nav.classList.toggle('show')
		})
	}
}



const navLink = document.querySelectorAll('.nav-link')

function linkAction() {
	console.log("link action")
	const navMenu = document.getElementById('navbarSupportedContent')
	navMenu.classList.remove('show')
}

navLink.forEach(n => n.addEventListener('click', linkAction))

const sections = document.querySelectorAll('section[id]')
const nav_toggler = document.querySelector('.navbar-toggler')
const my_navlist_menu = document.getElementById('my_nav_toggle')

const menuToggle = document.querySelector('#navbarSupportedContent')
const bsCollapse = new bootstrap.Collapse(menuToggle, {
  toggle: false
})


function scrollActive() {
	//nav_toggler.style.visibility = 'hidden'
	//my_navlist_menu.style.visibility = 'visible'
	if(bsCollapse._isShown()){
		bsCollapse.hide()
	}
	
	showElement(my_navlist_menu)
	hideElement(nav_toggler)
	const scrollY = window.pageYOffset
	sections.forEach(current =>{
		const sectionHeight = current.offsetHeight
		const sectionTop = current.offsetTop - 50;
		sectionId = current.getAttribute('id')
		nav_menu = document.querySelector('.navbar-collapse a[href*=' + sectionId + ']')
		if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
            document.querySelector('.navbar-collapse a[href*=' + sectionId + ']').classList.add('active')
        }else{
            document.querySelector('.navbar-collapse a[href*=' + sectionId + ']').classList.remove('active')
        }

	})
}

function createScrollStopListener(element, callback, timeout) {
	var handle = null;
	var onScroll = function() {
		if (handle) {
			clearTimeout(handle);
		}
		handle = setTimeout(callback, timeout || 1000); // default 200 ms
	};
	element.addEventListener('scroll', onScroll);
	return function() {
		element.removeEventListener('scroll', onScroll);
	};
}

function showElement (element) {
	//element.style.visibility = 'visible'
	element.classList.remove('hide')
	element.classList.add('show')

}

function hideElement (element) {
	//element.style.visibility = 'hidden'
	element.classList.remove('show')
	element.classList.add('hide')
}

createScrollStopListener(window, function() {
	showElement(nav_toggler)
	hideElement(my_navlist_menu)
});

window.addEventListener('scroll', scrollActive)

function showContactSuccessModal () {
	console.log("show modal")
	contactSuccessModal = new bootstrap.Modal(document.getElementById('contactSuccessModal'))
	contactSuccessModal.show()
}


const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2000,
    delay: 200,

});

sr.reveal('.home_data, .about_img, .skills_category, .project_title, .projects_img, .skills_txt',{}); 
sr.reveal('.home_img, .about_subtitle , .about_career, .about_txt, .skills_img',{delay: 400}); 
sr.reveal('.home_social_icon',{ interval: 200}); 
sr.reveal('.skills_data, .contact_input',{interval: 200});




