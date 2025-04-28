document.addEventListener('DOMContentLoaded', function () {
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
