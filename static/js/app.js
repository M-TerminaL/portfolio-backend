/* Start Custom Particles Js */
particlesJS("tsparticles", {
    fps_limit: 60,
    interactivity: {
        detect_on: "canvas",
        events: {
            onclick: { enable: false, mode: "push" },
            onhover: {
                enable: false,
                mode: "attract",
                parallax: { enable: false, force: 60, smooth: 10 }
            },
            resize: true
        },
        modes: {
            push: { quantity: 4 },
            attract: { distance: 200, duration: 0.4, factor: 5 }
        }
    },
    particles: {
        color: { value: "#ffffff" },
        line_linked: {
            color: "#ffffff",
            distance: 150,
            enable: true,
            opacity: 0.4,
            width: 1
        },
        move: {
            attract: { enable: false, rotateX: 600, rotateY: 1200 },
            bounce: false,
            direction: "none",
            enable: true,
            out_mode: "out",
            random: false,
            speed: 2,
            straight: false
        },
        number: { density: { enable: true, value_area: 800 }, value: 80 },
        opacity: {
            anim: { enable: false, opacity_min: 0.1, speed: 1, sync: false },
            random: false,
            value: 0.5
        },
        shape: {
            character: {
                fill: false,
                font: "Verdana",
                style: "",
                value: "*",
                weight: "400"
            },
            image: {
                height: 100,
                replace_color: true,
                src: "images/github.svg",
                width: 100
            },
            polygon: { nb_sides: 5 },
            stroke: { color: "#000000", width: 0 },
            type: "circle"
        },
        size: {
            anim: { enable: false, size_min: 0.1, speed: 40, sync: false },
            random: true,
            value: 5
        }
    },
    polygon: {
        draw: { enable: false, lineColor: "#ffffff", lineWidth: 0.5 },
        move: { radius: 10 },
        scale: 1,
        type: "none",
        url: ""
    },
    retina_detect: true
});

/* End Custom Particles Js */

/* Custom Scrollbar */
const ps = new PerfectScrollbar('.custom-scrollbar-container', {
    wheelSpeed: 0.2,
    wheelPropagation: true,
    minScrollbarLength: 20
});

/* End Custom Scrollbar */

/* Start Page Filling JQuery */

$(document).ready(function() {
	$('#pagepiling').pagepiling({
	    menu: '#nav',
        anchors: ['home', 'about', 'work', 'certificates', 'contactus'],
        direction: 'vertical',
        verticalCentered: true,
        verticalPadding: '2vh',

        sectionsColor: ['#10101a', '#10101a', '#10101a', '#10101a', '#10101a'],
        scrollingSpeed: 700,
        easing: 'swing',
        loopBottom: false,
        loopTop: false,
        css3: true,
        navigation: {
            'textColor': '#2fbf71',
            'bulletsColor': '#fff',
            'position': 'left',
            'tooltips': ['home', 'about', 'work', 'certificates', 'contactus']
        },
       	// normalScrollElements: '.pp-table',
        normalScrollElementTouchThreshold: 5,
        touchSensitivity: 5,
        keyboardScrolling: true,
        sectionSelector: '.section',
        animateAnchor: true,

		//events
		onLeave: function(index, nextIndex, direction){},
		afterLoad: function(anchorLink, index){},
		afterRender: function(){},
	});
});

/* End Page Filling JQuery */

/* Start Magnific Popup JQuery */

$(document).ready(function() {
    $('.image-popup').magnificPopup({
        type: 'image',
        removalDelay: 300,
        mainClass: 'mfp-fade',
        items: {
            src: './images/desktop-wallpaper-software-developer-software-engineering.jpg'
          },
        gallery: {
            enabled: true
        }
    });
});

/* End Magnific Popup JQuery */


/* Start Navbar Toggler Button */

const navbarElement = document.getElementById('navbar-desktop')
const menuBtnElement = document.getElementById('nav-btn')
const navIconElement = document.getElementById('nav-ico')

menuBtnElement.addEventListener('click', () => {
    navbarElement.classList.toggle('toggle')
    navIconElement.classList.toggle('bi-x')
})

/* End Navbar Toggler Button */

/* Start PreLoader */

const preLoader = document.getElementById('pre-loader')

document.addEventListener('DOMContentLoaded', () => {
    preLoader.style.display = 'none'
})

/* End Preloader */




/* Start Auto Write */

let string = "علیرضا بابایی";
let str = document.getElementById("myName");
let split = string.split("");
console.log(split);
(function anim(){
    split.length > 0 ? str.innerHTML += split.shift(): clearTimeout(running);
    let running = setTimeout(anim, 150);
})();

let string1 = "علیرضا بابایی";
let str1 = document.getElementById("myName1");
let split1 = string.split("");
console.log(split1);
(function anim(){
    split1.length > 0 ? str1.innerHTML += split1.shift(): clearTimeout(running);
    let running = setTimeout(anim, 150);
})();

/* End Auto Write */



