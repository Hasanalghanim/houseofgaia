document.addEventListener('DOMContentLoaded', function () {
	const alreadyPlayed = sessionStorage.getItem('animationPlayed');
	const splashScreen = document.getElementById('splashScreen');
	const mainContent = document.getElementById('mainContent');
	const splashLogo = document.getElementById('splashLogo');

	if (!alreadyPlayed) {
		// Start the splash screen animation
		setTimeout(() => {
			// Start the logo animation
			splashLogo.style.opacity = 1;
			splashLogo.style.transform = 'scale(1)';

			// Wait for the logo animation to finish (1.5s)
			setTimeout(() => {
				// Now that logo animation is done, start fading out splash screen
				splashScreen.classList.add('fade-out');

				// After splash screen fades out, show the main content
				setTimeout(() => {
					splashScreen.style.visibility = 'hidden'; // Hide splash screen completely
					mainContent.style.visibility = 'visible'; // Make main content visible
					mainContent.classList.add('show'); // Fade in the main content
				}, 50); // Wait until splash screen fades out completely
			}, 1000); // Duration of the logo animation
		}, 500); //  delay splash screen animation

		sessionStorage.setItem('animationPlayed', 'true');
	} else {
		// Skip splash screen on  visits
		splashScreen.style.visibility = 'hidden';
		mainContent.style.visibility = 'visible';
		mainContent.classList.add('show'); // Ensure main content is visible
	}

	// Responsive background image switching
	function updateBackgroundImages() {
		const wallPaper = document.getElementById('landingPageBackgroundPhoto');
		if (!wallPaper) return;

		const originalUrl = wallPaper.getAttribute('originalUrl');
		const croppedUrl = wallPaper.getAttribute('croppedUrl');

		if (!originalUrl || !croppedUrl) return;

		wallPaper.style.backgroundImage = window.innerWidth <= 991 ? `url('${croppedUrl}')` : `url('${originalUrl}')`;

		console.log('Background image updated to:', wallPaper.style.backgroundImage);
	}

	// Initial call + on resize
	updateBackgroundImages();
	window.addEventListener('resize', updateBackgroundImages);

	// Footer year update
	const yearElement = document.getElementById('footer-year');
	if (yearElement) {
		yearElement.textContent = new Date().getFullYear();
	}
});
