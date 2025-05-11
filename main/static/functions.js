document.addEventListener('DOMContentLoaded', function () {
	if (!sessionStorage.getItem('animationPlayed')) {
		setTimeout(() => {
			document.getElementById('navbar')?.classList.remove('expanded');
			document.getElementById('brandLogo')?.classList.remove('expanded');
			document.getElementById('hamburgerMenu')?.classList.remove('hidden');
		}, 1000);

		// Mark animation as played
		sessionStorage.setItem('animationPlayed', 'true');
	} else {
		// Immediately remove classes with no animation if revisiting another page
		document.getElementById('navbar')?.classList.remove('expanded');
		document.getElementById('brandLogo')?.classList.remove('expanded');
		document.getElementById('hamburgerMenu')?.classList.remove('hidden');
	}

	function updateBackgroundImages() {
		const wallPaper = document.getElementById('landingPageBackgroundPhoto');
		const originalUrl = wallPaper.getAttribute('originalUrl');
		const croppedUrl = wallPaper.getAttribute('croppedUrl');

		// Switch based on screen size
		if (window.innerWidth <= 991) {
			wallPaper.style.backgroundImage = `url('${croppedUrl}')`;
		} else {
			wallPaper.style.backgroundImage = `url('${originalUrl}')`;
		}

		console.log('Background image updated to:', wallPaper.style.backgroundImage);
	}

	// Update on load
	updateBackgroundImages();

	// Update on resize
	window.addEventListener('resize', updateBackgroundImages);
});
function setFooterYear() {
	const yearElement = document.getElementById('footer-year');
	const currentYear = new Date().getFullYear();
	yearElement.textContent = currentYear;
}
window.onload = setFooterYear;
